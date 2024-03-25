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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from retell_ai_python_sdk.pydantic.call_make_connection_request_phone_number import CallMakeConnectionRequestPhoneNumber
from retell_ai_python_sdk.pydantic.call_make_connection_request_retell_llm_dynamic_variables import CallMakeConnectionRequestRetellLlmDynamicVariables

class CallMakeConnectionRequest(BaseModel):
    phone_number: CallMakeConnectionRequestPhoneNumber = Field(alias='phone_number')

    # For this particular call, override the agent used with this agent id. This does not bind the agent to this number, this is for one time override.
    override_agent_id: typing.Optional[str] = Field(None, alias='override_agent_id')

    retell_llm_dynamic_variables: typing.Optional[CallMakeConnectionRequestRetellLlmDynamicVariables] = Field(None, alias='retell_llm_dynamic_variables')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
