import typing_extensions

from retell_ai_python_sdk.paths import PathValues
from retell_ai_python_sdk.apis.paths.register_call import RegisterCall
from retell_ai_python_sdk.apis.paths.get_call_call_id import GetCallCallId
from retell_ai_python_sdk.apis.paths.list_calls import ListCalls
from retell_ai_python_sdk.apis.paths.create_agent import CreateAgent
from retell_ai_python_sdk.apis.paths.get_agent_agent_id import GetAgentAgentId
from retell_ai_python_sdk.apis.paths.list_agents import ListAgents
from retell_ai_python_sdk.apis.paths.update_agent_agent_id import UpdateAgentAgentId
from retell_ai_python_sdk.apis.paths.delete_agent_agent_id import DeleteAgentAgentId
from retell_ai_python_sdk.apis.paths.create_retell_llm import CreateRetellLlm
from retell_ai_python_sdk.apis.paths.get_retell_llm_llm_id import GetRetellLlmLlmId
from retell_ai_python_sdk.apis.paths.list_retell_llms import ListRetellLlms
from retell_ai_python_sdk.apis.paths.update_retell_llm_llm_id import UpdateRetellLlmLlmId
from retell_ai_python_sdk.apis.paths.delete_retell_llm_llm_id import DeleteRetellLlmLlmId
from retell_ai_python_sdk.apis.paths.create_phone_number import CreatePhoneNumber
from retell_ai_python_sdk.apis.paths.get_phone_number_phone_number import GetPhoneNumberPhoneNumber
from retell_ai_python_sdk.apis.paths.list_phone_numbers import ListPhoneNumbers
from retell_ai_python_sdk.apis.paths.update_phone_number_phone_number import UpdatePhoneNumberPhoneNumber
from retell_ai_python_sdk.apis.paths.delete_phone_number_phone_number import DeletePhoneNumberPhoneNumber
from retell_ai_python_sdk.apis.paths.create_phone_call import CreatePhoneCall

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.REGISTERCALL: RegisterCall,
        PathValues.GETCALL_CALL_ID: GetCallCallId,
        PathValues.LISTCALLS: ListCalls,
        PathValues.CREATEAGENT: CreateAgent,
        PathValues.GETAGENT_AGENT_ID: GetAgentAgentId,
        PathValues.LISTAGENTS: ListAgents,
        PathValues.UPDATEAGENT_AGENT_ID: UpdateAgentAgentId,
        PathValues.DELETEAGENT_AGENT_ID: DeleteAgentAgentId,
        PathValues.CREATERETELLLLM: CreateRetellLlm,
        PathValues.GETRETELLLLM_LLM_ID: GetRetellLlmLlmId,
        PathValues.LISTRETELLLLMS: ListRetellLlms,
        PathValues.UPDATERETELLLLM_LLM_ID: UpdateRetellLlmLlmId,
        PathValues.DELETERETELLLLM_LLM_ID: DeleteRetellLlmLlmId,
        PathValues.CREATEPHONENUMBER: CreatePhoneNumber,
        PathValues.GETPHONENUMBER_PHONE_NUMBER: GetPhoneNumberPhoneNumber,
        PathValues.LISTPHONENUMBERS: ListPhoneNumbers,
        PathValues.UPDATEPHONENUMBER_PHONE_NUMBER: UpdatePhoneNumberPhoneNumber,
        PathValues.DELETEPHONENUMBER_PHONE_NUMBER: DeletePhoneNumberPhoneNumber,
        PathValues.CREATEPHONECALL: CreatePhoneCall,
    }
)

path_to_api = PathToApi(
    {
        PathValues.REGISTERCALL: RegisterCall,
        PathValues.GETCALL_CALL_ID: GetCallCallId,
        PathValues.LISTCALLS: ListCalls,
        PathValues.CREATEAGENT: CreateAgent,
        PathValues.GETAGENT_AGENT_ID: GetAgentAgentId,
        PathValues.LISTAGENTS: ListAgents,
        PathValues.UPDATEAGENT_AGENT_ID: UpdateAgentAgentId,
        PathValues.DELETEAGENT_AGENT_ID: DeleteAgentAgentId,
        PathValues.CREATERETELLLLM: CreateRetellLlm,
        PathValues.GETRETELLLLM_LLM_ID: GetRetellLlmLlmId,
        PathValues.LISTRETELLLLMS: ListRetellLlms,
        PathValues.UPDATERETELLLLM_LLM_ID: UpdateRetellLlmLlmId,
        PathValues.DELETERETELLLLM_LLM_ID: DeleteRetellLlmLlmId,
        PathValues.CREATEPHONENUMBER: CreatePhoneNumber,
        PathValues.GETPHONENUMBER_PHONE_NUMBER: GetPhoneNumberPhoneNumber,
        PathValues.LISTPHONENUMBERS: ListPhoneNumbers,
        PathValues.UPDATEPHONENUMBER_PHONE_NUMBER: UpdatePhoneNumberPhoneNumber,
        PathValues.DELETEPHONENUMBER_PHONE_NUMBER: DeletePhoneNumberPhoneNumber,
        PathValues.CREATEPHONECALL: CreatePhoneCall,
    }
)
