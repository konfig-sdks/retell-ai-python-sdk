# coding: utf-8
"""
    Retell SDK

    API for voice AI. Effortlessly integrate human-like Voice AI into your product. | We are building an API that enables your product to provide an intuitive and engaging way for user interaction - through voice.

    The version of the OpenAPI document: 1.0.0
    Contact: founders@retellai.com
    Created by: https://www.retellai.com/
"""

import typing
import inspect
from datetime import date, datetime
from retell_ai_python_sdk.client_custom import ClientCustom
from retell_ai_python_sdk.configuration import Configuration
from retell_ai_python_sdk.api_client import ApiClient
from retell_ai_python_sdk.type_util import copy_signature
from retell_ai_python_sdk.apis.tags.agent_api import AgentApi
from retell_ai_python_sdk.apis.tags.call_api import CallApi
from retell_ai_python_sdk.apis.tags.phone_number_api import PhoneNumberApi
from retell_ai_python_sdk.apis.tags.retell_api import RetellApi
from retell_ai_python_sdk.apis.tags.retell_llm_api import RetellLLMApi



class RetellAi(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.agent: AgentApi = AgentApi(api_client)
        self.call: CallApi = CallApi(api_client)
        self.phone_number: PhoneNumberApi = PhoneNumberApi(api_client)
        self.retell: RetellApi = RetellApi(api_client)
        self.retell_llm: RetellLLMApi = RetellLLMApi(api_client)
