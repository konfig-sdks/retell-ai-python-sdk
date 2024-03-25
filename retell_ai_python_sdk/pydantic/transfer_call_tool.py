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


class TransferCallTool(BaseModel):
    type: Literal["transfer_call"] = Field(alias='type')

    # Name of the tool. Must be unique within all tools available to LLM at any given time (general tools + state tools + state edges).
    name: str = Field(alias='name')

    # The number to transfer to in E.164 format (a + and country code, then the phone number with no space or other special characters). For example, +16175551212.
    number: str = Field(alias='number')

    # Describes when to transfer the call.
    description: typing.Optional[str] = Field(None, alias='description')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
