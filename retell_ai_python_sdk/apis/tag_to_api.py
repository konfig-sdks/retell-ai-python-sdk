import typing_extensions

from retell_ai_python_sdk.apis.tags import TagValues
from retell_ai_python_sdk.apis.tags.phone_number_api import PhoneNumberApi
from retell_ai_python_sdk.apis.tags.agent_api import AgentApi
from retell_ai_python_sdk.apis.tags.retell_api import RetellApi
from retell_ai_python_sdk.apis.tags.call_api import CallApi
from retell_ai_python_sdk.apis.tags.retell_llm_api import RetellLLMApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PHONE_NUMBER: PhoneNumberApi,
        TagValues.AGENT: AgentApi,
        TagValues.RETELL: RetellApi,
        TagValues.CALL: CallApi,
        TagValues.RETELL_LLM: RetellLLMApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PHONE_NUMBER: PhoneNumberApi,
        TagValues.AGENT: AgentApi,
        TagValues.RETELL: RetellApi,
        TagValues.CALL: CallApi,
        TagValues.RETELL_LLM: RetellLLMApi,
    }
)
