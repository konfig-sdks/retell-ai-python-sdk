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


class PhoneNumberPurchaseNumberAndBindAgentRequest(BaseModel):
    # Unique id of agent to bind to newly obtained number. The number will automatically use the agent when doing inbound / outbound calls.
    agent_id: str = Field(alias='agent_id')

    # Area code of the number to obtain. Format is a 3 digit integer. Currently only supports US area code.
    area_code: typing.Optional[int] = Field(None, alias='area_code')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
