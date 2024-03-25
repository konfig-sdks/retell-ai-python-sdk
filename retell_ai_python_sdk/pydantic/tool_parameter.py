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

from retell_ai_python_sdk.pydantic.tool_parameter_properties import ToolParameterProperties
from retell_ai_python_sdk.pydantic.tool_parameter_required import ToolParameterRequired

class ToolParameter(BaseModel):
    # Type must be \"object\" for a JSON Schema object.
    type: Literal["object"] = Field(alias='type')

    properties: ToolParameterProperties = Field(alias='properties')

    required: typing.Optional[ToolParameterRequired] = Field(None, alias='required')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
