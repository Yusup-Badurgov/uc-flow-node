from uc_flow_nodes.views import execute

from uc_flow_schemas.flow import RunState
from uc_flow_nodes.schemas import NodeRunContext

from node.schemas.enums import DriveOperation
from node.views.essence import GoogleDriveAuthenticator, GoogleDriveLister, GoogleDriveUploader


class ExecuteView(execute.Execute):

    async def post(self, json: NodeRunContext) -> NodeRunContext:

        drive_operation = json.node.data.properties['DriveOperation']

        if drive_operation == DriveOperation.authenticate:
            private_key = json.node.data.properties['private_key']
            client_email = json.node.data.properties['client_email']

            service_account_data = {
                "private_key": private_key,
                "client_email": client_email,
            }
            authenticator = GoogleDriveAuthenticator(service_account_data)
            access_token = await authenticator.get_access_token()

            file_data = json.node.data.properties['file_data']

            await json.save_result({
                "access_token": access_token,
                'file_data': file_data[0],
            })

        elif drive_operation == DriveOperation.upload_file:
            data_result = json.node.data.properties['data_result']
            access_token = data_result['access_token']
            file_data = data_result['file_data']

            uploader = GoogleDriveUploader(access_token)
            file_name = file_data['name']
            file_url = file_data['path']
            await uploader.upload_file(file_url, file_name)
            await json.save_result({"status": f'Файл {file_name} успешно загружен на Google диск'})

        elif drive_operation == DriveOperation.fetch_file_list:
            data_result = json.node.data.properties['data_result']
            access_token = data_result['access_token']

            lister = GoogleDriveLister(access_token)
            files = await lister.list_files()
            await json.save_result({"files": files})

        json.state = RunState.complete
        return json
