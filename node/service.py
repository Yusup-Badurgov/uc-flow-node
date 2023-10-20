from typing import List
from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import info, execute
from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property, RunState
from uc_http_requester.requester import Request


def create_property(display_name: str, name: str, prop_type: Property.Type, description: str) -> Property:
    if prop_type == Property.Type.BOOLEAN:
        placeholder = ''
    elif prop_type == Property.Type.STRING:
        placeholder = f'Введите текст {description}'
    elif prop_type == Property.Type.NUMBER:
        placeholder = f'Введите число {description}'
    else:
        placeholder = f'Введите {description}'

    return Property(
        displayName=display_name,
        name=name,
        type=prop_type,
        placeholder=placeholder,
        description=description,
        required=True
    )


class NodeType(flow.NodeType):
    id: str = '3e4dbc22-c5e8-4e57-8d56-8e862b759480'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'SumTwoNumbers'
    displayName: str = 'Calculate Sum'
    icon: str = '<svg><text x="8" y="50" font-size="50">∑</text></svg>'
    description: str = 'Calculates the sum of two input numbers and returns the result as either a string or a number based on the toggle.'
    properties: List[Property] = [
        create_property('Текстовое поле', 'text_field',
                        Property.Type.STRING, 'Текст'),
        create_property('Числовое поле', 'number_field',
                        Property.Type.NUMBER, 'Число'),
        create_property('Переключатель типа результата', 'toggle', Property.Type.BOOLEAN,
                        'Если включено, результат будет в формате строки. Если выключено, результат будет числом.')
    ]


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            text_value = json.node.data.properties.get('text_field', "0")
            number_value = json.node.data.properties.get('number_field', 0)
            toggle_value = json.node.data.properties.get('toggle', False)

            # Переводим текстовое значение в число и суммируем с числовым значением. Есть возможность работать с числами с зяпятой.
            total = float(text_value) + number_value

            # Если результат является целым числом, преобразуем его в целое число.
            if total.is_integer():
                total = int(total)

            # переключатель строка\число
            result_value = str(total) if toggle_value else total

            await json.save_result({"result": result_value})
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
