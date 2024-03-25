# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from retell_ai_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    REGISTERCALL = "/register-call"
    GETCALL_CALL_ID = "/get-call/{call_id}"
    LISTCALLS = "/list-calls"
    CREATEAGENT = "/create-agent"
    GETAGENT_AGENT_ID = "/get-agent/{agent_id}"
    LISTAGENTS = "/list-agents"
    UPDATEAGENT_AGENT_ID = "/update-agent/{agent_id}"
    DELETEAGENT_AGENT_ID = "/delete-agent/{agent_id}"
    CREATERETELLLLM = "/create-retell-llm"
    GETRETELLLLM_LLM_ID = "/get-retell-llm/{llm_id}"
    LISTRETELLLLMS = "/list-retell-llms"
    UPDATERETELLLLM_LLM_ID = "/update-retell-llm/{llm_id}"
    DELETERETELLLLM_LLM_ID = "/delete-retell-llm/{llm_id}"
    CREATEPHONENUMBER = "/create-phone-number"
    GETPHONENUMBER_PHONE_NUMBER = "/get-phone-number/{phone_number}"
    LISTPHONENUMBERS = "/list-phone-numbers"
    UPDATEPHONENUMBER_PHONE_NUMBER = "/update-phone-number/{phone_number}"
    DELETEPHONENUMBER_PHONE_NUMBER = "/delete-phone-number/{phone_number}"
    CREATEPHONECALL = "/create-phone-call"
