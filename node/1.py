# from typing import List
# from uc_flow_nodes.schemas import NodeRunContext
# from uc_flow_nodes.service import NodeService
# from uc_flow_nodes.views import info, execute
# from uc_flow_schemas import flow
# from uc_flow_schemas.flow import Property, RunState
# from uc_http_requester.requester import Request
# from typing import List
# from pydantic import SecretStr
# from uc_flow_schemas import flow
# from uc_flow_schemas.flow import (
#     Defaults,
#     Property,
#     NodeType as BaseNodeType,
#     DisplayOptions,
#     OptionValue,
# )

# from node.enums import first_dropdown, second_dropdown


# class NodeType(BaseNodeType):
#     id: str = ''
#     secret: SecretStr = '777'
#     type: BaseNodeType.Type = BaseNodeType.Type.action
#     displayName: str = 'YusupAlfaCRM'
#     icon: str = '<svg><text x="8" y="50" font-size="50">YusupAlfaCRM</text></svg>'
#     group: List[str] = ["custom"]
#     version: int = 1
#     description: str = 'Custom action node'
#     defaults: Defaults = Defaults(name='custom-action', color='#00FF00')
#     inputs: List[str] = ['main']
#     outputs: List[str] = ['main']
#     properties: List[Property] = [
#         Property(
#             displayName='Выберите действие',
#             name='api',
#             type=Property.Type.OPTIONS,
#             noDataExpression=True,
#             options=[
#                 OptionValue(
#                     name='Авторизация',
#                     value='auth_data',
#                     description='Авторизация',
#                 ),
#                 OptionValue(
#                     name='Получение данных',
#                     value='request_data',
#                     description='Получение данных',
#                 ),
#             ]
#         ),
    #     Property(
    #         displayName='Resource',
    #         name='resource',
    #         type=Property.Type.OPTIONS,
    #         noDataExpression=True,
    #         options=[
    #             OptionValue(
    #                 name='Customer',
    #                 value='customer',
    #                 description='',
    #             ),
    #         ],
    #         displayOptions=DisplayOptions(
    #             show={
    #                 'api': [
    #                     'auth_data',
    #                 ],
    #             },
    #         ),
    #     ),
    #     Property(
    #         displayName='Operation',
    #         name='operation',
    #         type=Property.Type.OPTIONS,
    #         noDataExpression=True,
    #         options=[
    #             OptionValue(
    #                 name='index',
    #                 value='index',
    #                 description='',
    #             ),
    #             OptionValue(
    #                 name='create',
    #                 value='create',
    #                 description='',
    #             ),
    #             OptionValue(
    #                 name='update',
    #                 value='update',
    #                 description='',
    #             ),
    #         ],
    #         displayOptions=DisplayOptions(
    #             show={
    #                 'api': [
    #                     'auth_data',
    #                 ],
    #                 'resource': [
    #                     'customer'
    #                 ]
    #             },
    #         ),
    #     ),

    # ]


# class InfoView(info.Info):
#     class Response(info.Info.Response):
#         node_type: NodeType


# class ExecuteView(execute.Execute):
#     async def post(self, json: NodeRunContext) -> NodeRunContext:
#         try:
#             toggle_value = json.node.data.properties.get('toggle', False)
#             first_dropdown_value = json.node.data.properties.get('first_dropdown')
#             second_dropdown_value = json.node.data.properties.get('second_dropdown')

#             # Проверка для "Значение 1"
#             if toggle_value and first_dropdown_value == first_dropdown.VALUE_1 and second_dropdown_value == second_dropdown.VALUE_1:
#                 email_value = json.node.data.properties.get('email_field')
#                 await json.save_result({"email": email_value})
            
#             # Проверка для "Значение 2"
#             elif toggle_value and first_dropdown_value == first_dropdown.VALUE_2 and second_dropdown_value == second_dropdown.VALUE_2:
#                 datetime_value = json.node.data.properties.get('datetime_field')
#                 await json.save_result({"datetime": datetime_value})
            
#             else:
#                 await json.save_error("Тумблер выключен или выбраны разные значения в списках.")

#             json.state = RunState.complete
#         except Exception as e:
#             self.log.warning(f'Error {e}')
#             await json.save_error(str(e))
#             json.state = RunState.error
#         return json



# class Service(NodeService):
#     class Routes(NodeService.Routes):
#         Info = InfoView
#         Execute = ExecuteView
