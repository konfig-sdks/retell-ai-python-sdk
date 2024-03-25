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

from retell_ai_python_sdk.pydantic.state_edge import StateEdge
from retell_ai_python_sdk.pydantic.tool import Tool

class State(BaseModel):
    # Name of the state, must be unique for each state.
    name: str = Field(alias='name')

    # Prompt of the state, will be appended to the system prompt of LLM.    - System prompt = general prompt + state prompt.
    state_prompt: typing.Optional[str] = Field(None, alias='state_prompt')

    # Edges of the state define how and what state can be reached from this state.
    edges: typing.Optional[typing.List[StateEdge]] = Field(None, alias='edges')

    # A list of tools specific to this state the model may call (to get external knowledge, call API, etc). You can select from some common predefined tools like end call, transfer call, etc; or you can create your own custom tool (last option) for the LLM to use.   - Tools of LLM = general tools + state tools + state transitions
    tools: typing.Optional[typing.List[Tool]] = Field(None, alias='tools')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
