from typing import List
from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import info, execute
from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property, RunState
from uc_http_requester.requester import Request
from typing import List
from pydantic import SecretStr
from uc_flow_schemas import flow
from uc_flow_schemas.flow import (
    Defaults,
    Property,
    NodeType as BaseNodeType,
    DisplayOptions,
    OptionValue,
)

from node.enums import first_dropdown, second_dropdown


class NodeType(BaseNodeType):
    id: str = 'b4dd759a-c74e-4be3-ae79-fc44f0205a4c'
    secret: SecretStr = '999'
    type: BaseNodeType.Type = BaseNodeType.Type.action
    displayName: str = 'YusupHollihop'
    icon: str = '<svg><text x="8" y="50" font-size="50">YusupHOP</text></svg>'
    group: List[str] = ["custom"]
    version: int = 1
    description: str = 'Custom action node'
    defaults: Defaults = Defaults(name='custom-action', color='#00FF00')
    inputs: List[str] = ['main']
    outputs: List[str] = ['main']
    properties: List[Property] = [
        Property(
            displayName='Переключатель',
            name='toggle',
            type=Property.Type.BOOLEAN,
            required=True
        ),
        Property(
            displayName='Первый список',
            name='first_dropdown',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            options=[
                OptionValue(
                    name='Значение 1',
                    value=first_dropdown.VALUE_1,
                    description='Значение 1',
                ),
                OptionValue(
                    name='Значение 2',
                    value=first_dropdown.VALUE_2,
                    description='Значение 2',
                ),
            ],
            displayOptions=DisplayOptions(
                show={
                    'toggle': [True],
                },
            ),
        ),
        Property(
            displayName='Второй список',
            name='second_dropdown',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            options=[
                OptionValue(
                    name='Значение 1',
                    value=second_dropdown.VALUE_1,
                    description='Значение 1',
                ),
                OptionValue(
                    name='Значение 2',
                    value=second_dropdown.VALUE_2,
                    description='Значение 2',
                ),
            ],
            displayOptions=DisplayOptions(
                show={
                    'toggle': [True],
                },
            ),
        ),
        Property(
            displayName='Поле для ввода почты',
            name='email_field',
            type=Property.Type.STRING,
            placeholder='Введите ваш email',
            displayOptions=DisplayOptions(
                show={
                    'first_dropdown': [
                        first_dropdown.VALUE_1,
                    ],
                    'second_dropdown': [
                        second_dropdown.VALUE_1,
                    ]
                },
            ),
        ),
        Property(
            displayName='Поле для ввода даты и времени',
            name='datetime_field',
            type=Property.Type.DATETIME,
            placeholder='Выберите дату и время',
            displayOptions=DisplayOptions(
                show={
                    'first_dropdown': [
                        first_dropdown.VALUE_2,
                    ],
                    'second_dropdown': [
                        second_dropdown.VALUE_2,
                    ]
                },
            ),
        ),

    ]


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            toggle_value = json.node.data.properties.get('toggle', False)
            first_dropdown_value = json.node.data.properties.get('first_dropdown')
            second_dropdown_value = json.node.data.properties.get('second_dropdown')

            # Проверка для "Значение 1"
            if toggle_value and first_dropdown_value == first_dropdown.VALUE_1 and second_dropdown_value == second_dropdown.VALUE_1:
                email_value = json.node.data.properties.get('email_field')
                await json.save_result({"email": email_value})
            
            # Проверка для "Значение 2"
            elif toggle_value and first_dropdown_value == first_dropdown.VALUE_2 and second_dropdown_value == second_dropdown.VALUE_2:
                datetime_value = json.node.data.properties.get('datetime_field')
                await json.save_result({"datetime": datetime_value})
            
            else:
                await json.save_error("Тумблер выключен или выбраны разные значения в списках.")

            json.state = RunState.complete
        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error
        return json



class Service(NodeService):
    class Routes(NodeService.Routes):
        Info = InfoView
        Execute = ExecuteView
