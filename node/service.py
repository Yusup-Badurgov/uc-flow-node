
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

from node.enums import Parameters


class CustomNodeType():
    properties: List[Property] = [
        Property(
            displayName='Resource',
            name='resource',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            options=[
                OptionValue(
                    name='Customer',
                    value='customer',
                    description='',
                ),
            ],
            displayOptions=DisplayOptions(
                show={
                    'api': [
                        'request_data',
                    ],
                },
            ),
        ),
        Property(
            displayName='auth_result',
            name='auth_result',
            type=Property.Type.JSON,

            displayOptions=DisplayOptions(
                show={
                    'api': [
                        'request_data',
                    ],
                },
            ),
        ),
        Property(
            displayName='Operation',
            name='operation',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            options=[
                OptionValue(
                    name='index',
                    value='index',
                    description='',
                ),
                OptionValue(
                    name='create',
                    value='create',
                    description='',
                ),
                OptionValue(
                    name='update',
                    value='update',
                    description='',
                ),
            ],
            displayOptions=DisplayOptions(
                show={
                    'api': [
                        'request_data',
                    ],
                    'resource': [
                        'customer'
                    ]
                },
            ),
        ),
        Property(
            displayName='Parameters',
            name='parameters',
            type=Property.Type.COLLECTION,
            default={},
            displayOptions=DisplayOptions(
                show={
                    'api': [
                        'request_data'
                    ],
                    'resource': [
                        'customer',
                    ],
                    'operation': [
                        'index',

                    ],
                }
            ),
            options=[
                Property(
                    displayName='id',
                    name=Parameters.id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='id клиента',
                ),
                Property(
                    displayName='id_study',
                    name=Parameters.is_study,
                    type=Property.Type.NUMBER,
                    default='',
                    description='состояние клиента ( 0 - лид, 1 - клиент)',
                ),
                Property(
                    displayName='study_status_id',
                    name=Parameters.study_status_id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='id статуса клиента',
                ),
                Property(
                    displayName='name',
                    name=Parameters.name,
                    type=Property.Type.STRING,
                    default='',
                    description='имя клиента',
                ),
                Property(
                    displayName='gender',
                    name=Parameters.gender,
                    type=Property.Type.STRING,
                    default='',
                    description='пол клиента',
                ),
                Property(
                    displayName='age_from',
                    name=Parameters.age_from,
                    type=Property.Type.NUMBER,
                    default='',
                    description='возраст клиента от',
                ),
                Property(
                    displayName='age_to',
                    name=Parameters.age_to,
                    type=Property.Type.NUMBER,
                    default='',
                    description='возраст клиента до',
                ),
                Property(
                    displayName='phone',
                    name=Parameters.phone,
                    type=Property.Type.STRING,
                    default='',
                    description='контакты клиента',
                ),
                Property(
                    displayName='legal_type',
                    name=Parameters.legal_type,
                    type=Property.Type.NUMBER,
                    default='',
                    description='тип заказчика(1-физ лицо, 2-юр.лицо)',
                ),
                Property(
                    displayName='legal_name',
                    name=Parameters.legal_name,
                    type=Property.Type.STRING,
                    default='',
                    description='имя заказчика',
                ),
                Property(
                    displayName='company_id',
                    name=Parameters.company_id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='id юр лица',
                ),
                Property(
                    displayName='lesson_count_from',
                    name=Parameters.lesson_count_from,
                    type=Property.Type.NUMBER,
                    default='',
                    description='остаток уроков от',
                ),
                Property(
                    displayName='lesson_count_to',
                    name=Parameters.lesson_count_to,
                    type=Property.Type.NUMBER,
                    default='',
                    description='остаток уроков до',
                ),
                Property(
                    displayName='balance_contract_from',
                    name=Parameters.balance_contract_from,
                    type=Property.Type.NUMBER,
                    default='',
                    description='баланс договора от',
                ),
                Property(
                    displayName='balance_contract_to',
                    name=Parameters.balance_contract_to,
                    type=Property.Type.NUMBER,
                    default='',
                    description='баланс договора до',
                ),
                Property(
                    displayName='balance_bonus_from',
                    name=Parameters.balance_bonus_from,
                    type=Property.Type.NUMBER,
                    default='',
                    description='баланс бонусов от',
                ),
                Property(
                    displayName='balance_bonus_to',
                    name=Parameters.balance_bonus_to,
                    type=Property.Type.NUMBER,
                    default='',
                    description='баланс бонусов до',
                ),
                Property(
                    displayName='removed',
                    name=Parameters.removed,
                    type=Property.Type.NUMBER,
                    default='',
                    description='флаг архивности (2 - только архивные, 1 - активные и архивные, 0 – только активные)',
                ),
                Property(
                    displayName='removed_from',
                    name=Parameters.removed_from,
                    type=Property.Type.DATE,
                    default='',
                    description='дата отправки в архив от',
                ),
                Property(
                    displayName='removed_to',
                    name=Parameters.removed,
                    type=Property.Type.DATE,
                    default='',
                    description='дата отправки в архив',
                ),
                Property(
                    displayName='level_id',
                    name=Parameters.level_id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='id уровня знаний',
                ),
                Property(
                    displayName='assigned_id',
                    name=Parameters.assigned_id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='id ответственного менеджера',
                ),
                Property(
                    displayName='employee_id',
                    name=Parameters.employee_id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='id ответственного педагога',
                ),
                Property(
                    displayName='lead_source_id',
                    name=Parameters.lead_source_id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='id источника',
                ),
                Property(
                    displayName='color',
                    name=Parameters.color,
                    type=Property.Type.NUMBER,
                    default='',
                    description='id цвета',
                ),
                Property(
                    displayName='note',
                    name=Parameters.note,
                    type=Property.Type.STRING,
                    default='',
                    description='примечание',
                ),
                Property(
                    displayName='date_from',
                    name=Parameters.date_from,
                    type=Property.Type.DATE,
                    default='',
                    description='дата добавления от',
                ),
                Property(
                    displayName='date_to',
                    name=Parameters.date_to,
                    type=Property.Type.DATE,
                    default='',
                    description='дата добавления до',
                ),
                Property(
                    displayName='next_lesson_date_from',
                    name=Parameters.next_lesson_date_from,
                    type=Property.Type.DATE,
                    default='',
                    description='дата след.посещения от',
                ),
                Property(
                    displayName='next_lesson_date_to',
                    name=Parameters.next_lesson_date_to,
                    type=Property.Type.DATE,
                    default='',
                    description='дата след.посещения до',
                ),
                Property(
                    displayName='tariff_till_from',
                    name=Parameters.tariff_till_from,
                    type=Property.Type.DATE,
                    default='',
                    description='дата действия абонемента от',
                ),
                Property(
                    displayName='tariff_till_to',
                    name=Parameters.tariff_till_to,
                    type=Property.Type.DATE,
                    default='',
                    description='дата действия абонемента до',
                ),
                Property(
                    displayName='customer_reject_id',
                    name=Parameters.customer_reject_id,
                    type=Property.Type.NUMBER,
                    default='',
                    description='id причины отказа',
                ),
                Property(
                    displayName='comment',
                    name=Parameters.comment,
                    type=Property.Type.STRING,
                    default='',
                    description='комментарий',
                ),
                Property(
                    displayName='dob_from',
                    name=Parameters.dob_from,
                    type=Property.Type.DATE,
                    default='',
                    description='дата рождения от',
                ),
                Property(
                    displayName='dob_to',
                    name=Parameters.dob_to,
                    type=Property.Type.DATE,
                    default='',
                    description='дата рождения до',
                ),
                Property(
                    displayName='withGroups:true',
                    name=Parameters.withGroups_true,
                    type=Property.Type.STRING,
                    default='',
                    description='активные группы клиента',
                ),
                Property(
                    displayName='page',
                    name=Parameters.page,
                    type=Property.Type.NUMBER,
                    default='',
                    description='страница для пагинации',
                ),
            ]
        ),
    ]


class AuthorizationNodeType():
    properties: List[Property] = [
        Property(
            displayName='url',
            name='url_field',
            type=Property.Type.STRING,
            noDataExpression=True,

            displayOptions=DisplayOptions(
                show={
                    'api': [
                        'auth_data',
                    ],
                },
            ),
        ),
        Property(
            displayName='id филиала',
            name='branch_field',
            type=Property.Type.NUMBER,
            noDataExpression=True,

            displayOptions=DisplayOptions(
                show={
                    'api': [
                        'auth_data',
                    ],
                },
            ),
        ),
        Property(
            displayName='E-mail',
            name='email_field',
            type=Property.Type.STRING,
            noDataExpression=True,

            displayOptions=DisplayOptions(
                show={
                    'api': [
                        'auth_data',
                    ],
                },
            ),
        ),
        Property(
            displayName='Ключ API',
            name='api_field',
            type=Property.Type.STRING,
            noDataExpression=True,

            displayOptions=DisplayOptions(
                show={
                    'api': [
                        'auth_data',
                    ],
                },
            ),
        ),
    ]


class NodeType(BaseNodeType):
    id: str = '0e2a5fd7-1bbe-453f-8cbd-2e34377013bc'
    secret: SecretStr = '777'
    type: BaseNodeType.Type = BaseNodeType.Type.action
    displayName: str = 'ABYusupAlfaCRM'
    icon: str = '<svg><text x="8" y="50" font-size="50">YusupAlfaCRM</text></svg>'
    group: List[str] = ["custom"]
    version: int = 1
    description: str = 'Custom action node'
    defaults: Defaults = Defaults(name='custom-action', color='#00FF00')
    inputs: List[str] = ['main']
    outputs: List[str] = ['main']
    properties: List[Property] = [
        Property(
            displayName='Выберите действие',
            name='api',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            options=[
                OptionValue(
                    name='Авторизация',
                    value='auth_data',
                    description='Авторизация',
                ),
                OptionValue(
                    name='Получение данных',
                    value='request_data',
                    description='Получение данных',
                ),
            ]
        ),
    ]
    properties: List[Property] = properties + AuthorizationNodeType.properties
    properties: List[Property] = properties + CustomNodeType.properties


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            api_choice = json.node.data.properties.get('api')

            if api_choice == 'auth_data':

                url = json.node.data.properties.get('url_field')
                branch = json.node.data.properties.get('branch_field')
                email = json.node.data.properties.get('email_field')
                api_key = json.node.data.properties.get('api_field')

                headers = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                }

                req = Request(
                    url=f'https://{url}/v2api/auth/login',
                    method=Request.Method.post,
                    json={"email": email, "api_key": api_key},
                    headers=headers
                )

                response = await req.execute()
                json_content = response.json()

                data = {
                    "branch": branch,
                    "url": url
                }
                data.update({"token": json_content.get('token', 'нет токена')})

                await json.save_result(data)
                json.state = RunState.complete

            if api_choice == 'request_data':
                def extract_parameters(parameters: dict) -> dict:
                    return {key: value[0] for key, value in parameters.items() if value and len(value) > 0}

                parameters = extract_parameters(json.node.data.properties.get('parameters', {}))

                auth_result = json.node.data.properties.get('auth_result', {})
                token = auth_result.get('token')
                branch = auth_result.get('branch')
                base_url = auth_result.get('url')

                headers = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'X-ALFACRM-TOKEN': token
                }

                operation_endpoints = {
                    'index': f'/v2api/{branch}/customer/index',
                    'create': f'/v2api/{branch}/customer/create',
                    'update': f'/v2api/{branch}/customer/update'
                }

                endpoint = operation_endpoints.get(
                    json.node.data.properties.get('operation'), '')

                if json.node.data.properties.get('operation') == 'create':
                    parameters["branch_ids"] = [branch]

                elif json.node.data.properties.get('operation') == 'update' and 'id' in parameters:
                    endpoint += f'?id={parameters.pop("id")}'

                full_url = f'https://{base_url}{endpoint}'

                data = Request(
                    url=full_url,
                    method=Request.Method.post,
                    json=parameters,
                    headers=headers
                )


                result = await data.execute()

                await json.save_result({
                    "result": result.json()
                })

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
