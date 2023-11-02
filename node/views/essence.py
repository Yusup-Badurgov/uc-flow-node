
from uc_http_requester.requester import Request


import json
import jwt
import time


class GoogleDriveAuthenticator:

    SCOPES = ["https://www.googleapis.com/auth/drive"]

    def __init__(self, service_account):
        self.service_account = service_account
        self.token_uri = "https://oauth2.googleapis.com/token"

    async def get_access_token(self):

        assertion = {
            "iss": self.service_account["client_email"],
            "scope": " ".join(self.SCOPES),
            "aud": self.token_uri,
            "exp": int(time.time()) + 3600,
            "iat": int(time.time())
        }

        # Создаем JWT
        signed_jwt = jwt.encode(
            assertion, self.service_account["private_key"], algorithm="RS256")

        payload = {
            "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
            "assertion": signed_jwt
        }

        # Отправляем запрос для получения токена
        request = Request(
            method=Request.Method.post,
            url=self.token_uri,
            data=payload
        )
        response = await request.execute()
        return json.loads(response.content)["access_token"]


class GoogleDriveUploader:

    API_ENDPOINT = "https://www.googleapis.com/upload/drive/v3/files"

    def __init__(self, access_token):
        self.access_token = access_token

    async def upload_file(self, file_url, file_name):
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/octet-stream"
        }

        file_content_request = Request(
            method=Request.Method.get,
            url=file_url
        )
        file_content_response = await file_content_request.execute()
        file_content = file_content_response.content

        metadata = {
            'name': file_name
        }
        multipart_boundary = "boundary_string"
        multipart_data = f"--{multipart_boundary}\n"
        multipart_data += "Content-Type: application/json; charset=UTF-8\n\n"
        multipart_data += json.dumps(metadata) + "\n"
        multipart_data += f"--{multipart_boundary}\n"
        multipart_data += "Content-Type: application/octet-stream\n\n"
        multipart_data += file_content.decode('utf-8') + "\n"
        multipart_data += f"--{multipart_boundary}--"

        upload_request = Request(
            method=Request.Method.post,
            url=self.API_ENDPOINT,
            headers={
                **headers,
                "Content-Type": f"multipart/related; boundary={multipart_boundary}"
            },
            data=multipart_data,
            params={"uploadType": "multipart"}
        )

        response = await upload_request.execute()

        if response.status_code == 200:
            response_data = json.loads(response.content)
            return {"success": True, "file_id": response_data.get("id"), "file_name": response_data.get("name")}
        else:
            response_data = json.loads(response.content)
            return {"success": False, "error": response_data.get("error")}


class GoogleDriveLister:

    API_ENDPOINT = "https://www.googleapis.com/drive/v3/files"

    def __init__(self, access_token):
        self.access_token = access_token

    async def list_files(self):
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        request = Request(
            method=Request.Method.get,
            url=self.API_ENDPOINT,
            headers=headers
        )

        response = await request.execute()
        return json.loads(response.content)["files"]
