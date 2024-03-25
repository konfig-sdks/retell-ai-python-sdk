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

from retell_ai_python_sdk.type.state_edge import StateEdge
from retell_ai_python_sdk.type.tool import Tool

class RequiredState(TypedDict):
    # Name of the state, must be unique for each state.
    name: str

class OptionalState(TypedDict, total=False):
    # Prompt of the state, will be appended to the system prompt of LLM.    - System prompt = general prompt + state prompt.
    state_prompt: str

    # Edges of the state define how and what state can be reached from this state.
    edges: typing.List[StateEdge]

    # A list of tools specific to this state the model may call (to get external knowledge, call API, etc). You can select from some common predefined tools like end call, transfer call, etc; or you can create your own custom tool (last option) for the LLM to use.   - Tools of LLM = general tools + state tools + state transitions
    tools: typing.List[Tool]

class State(RequiredState, OptionalState):
    pass
