from enum import Enum

class DriveOperation(str, Enum):
    authenticate = 'authenticate'
    upload_file = 'upload_file'
    fetch_file_list = 'fetch_file_list'
