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

from retell_ai_python_sdk.type.state import State
from retell_ai_python_sdk.type.tool import Tool

class RequiredRetellLLMBase(TypedDict):
    pass

class OptionalRetellLLMBase(TypedDict, total=False):
    # General prompt that's appended to system prompt no matter what state the agent is in.   - System prompt (with state) = general prompt + state prompt.  - System prompt (no state) = general prompt.
    general_prompt: str

    # A list of tools the model may call (to get external knowledge, call API, etc). You can select from some common predefined tools like end call, transfer call, etc; or you can create your own custom tool (last option) for the LLM to use.   - Tools of LLM (with state) = general tools + state tools + state transitions  - Tools of LLM (no state) = general tools
    general_tools: typing.List[Tool]

    # States of the LLM. This is to help reduce prompt length and tool choices when the call can be broken into distinct states. With shorter prompts and less tools, the LLM can better focus and follow the rules, minimizing hallucination. If this field is not set, the agent would only have general prompt and general tools (essentially one state).
    states: typing.List[State]

    # Name of the starting state. Required if states is not empty.
    starting_state: str

    # First utterance said by the agent in the call. If not set, LLM will dynamically generate a message. If set to \"\", agent will wait for user to speak first.
    begin_message: str

class RetellLLMBase(RequiredRetellLLMBase, OptionalRetellLLMBase):
    pass
