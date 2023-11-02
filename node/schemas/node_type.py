from typing import List

from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property, DisplayOptions, OptionValue

from node.schemas.enums import DriveOperation


class NodeType(flow.NodeType):
    id: str = 'd6cd1e39-cb76-4ef3-bb92-423458f408fc'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'ABYusupGoogle Cloud ApiAPP'
    displayName: str = 'ABYusupGoogle Cloud ApiAPP'
    icon: str = '<svg><text x="8" y="50" font-size="50">☁️</text></svg>'
    description: str = 'AYusupGoogle Cloud ApiAPP'
    properties: List[Property] = [
        Property(
            displayName='Выбрать действие',
            name='DriveOperation',
            type=Property.Type.OPTIONS,
            options=[
                OptionValue(
                    name='Авторизация',
                    value=DriveOperation.authenticate,
                    description=''
                ),
                OptionValue(
                    name='Загрузка файла',
                    value=DriveOperation.upload_file,
                    description=''
                ),
                OptionValue(
                    name='Вывести список файлов',
                    value=DriveOperation.fetch_file_list,
                    description=''
                ),
            ]
        ),
        Property(
            displayName='private_key',
            name='private_key',
            type=Property.Type.JSON,
            displayOptions=DisplayOptions(
                show={
                    'DriveOperation': [
                        DriveOperation.authenticate,
                    ],
                },
            ),
        ),
        Property(
            displayName='client_email',
            name='client_email',
            type=Property.Type.JSON,
            displayOptions=DisplayOptions(
                show={
                    'DriveOperation': [
                        DriveOperation.authenticate,
                    ],
                },
            ),
        ),

        Property(
            displayName='data_result',
            name='data_result',
            type=Property.Type.JSON,
            displayOptions=DisplayOptions(
                show={
                    'DriveOperation': [
                        DriveOperation.upload_file,
                    ],
                },
            ),
        ),
        Property(
            displayName='file_data',
            name='file_data',
            type=Property.Type.JSON,
            displayOptions=DisplayOptions(
                show={
                    'DriveOperation': [
                        DriveOperation.authenticate,
                    ],
                },
            ),
        ),
    ]
