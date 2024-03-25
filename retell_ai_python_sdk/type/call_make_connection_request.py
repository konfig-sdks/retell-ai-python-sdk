# coding: utf-8

"""
    Retell SDK

    API for voice AI. Effortlessly integrate human-like Voice AI into your product. | We are building an API that enables your product to provide an intuitive and engaging way for user interaction - through voice.

    The version of the OpenAPI document: 1.0.0
    Contact: founders@retellai.com
    Created by: https://www.retellai.com/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from retell_ai_python_sdk.type.call_make_connection_request_phone_number import CallMakeConnectionRequestPhoneNumber
from retell_ai_python_sdk.type.call_make_connection_request_retell_llm_dynamic_variables import CallMakeConnectionRequestRetellLlmDynamicVariables

class RequiredCallMakeConnectionRequest(TypedDict):
    phone_number: CallMakeConnectionRequestPhoneNumber

class OptionalCallMakeConnectionRequest(TypedDict, total=False):
    # For this particular call, override the agent used with this agent id. This does not bind the agent to this number, this is for one time override.
    override_agent_id: str

    retell_llm_dynamic_variables: CallMakeConnectionRequestRetellLlmDynamicVariables

class CallMakeConnectionRequest(RequiredCallMakeConnectionRequest, OptionalCallMakeConnectionRequest):
    pass
