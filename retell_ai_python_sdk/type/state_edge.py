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

from retell_ai_python_sdk.type.tool_parameter import ToolParameter

class RequiredStateEdge(TypedDict):
    # Describes what's the transition and at what time / criteria should this transition happen.
    description: str

    # The destination state name when going through transition of state via this edge. State transition internally is implemented as a tool call of LLM, and a tool call with name \"transition_to_{destination_state_name}\" will get created. Feel free to reference it inside the prompt.
    destination_state_name: str

    # After the state transitions, the agent would speak based on the new prompt and tools in the new state. This bit here controls whether to speak a transition sentence during the transition (so agent would say sentences like \"Let's move on to the next section to help you set up an acount.\", and state transitions, and agent continue to speak.). Usually this is not necessary, and is recommended to set to false to avoid LLM repeating itself during and after transition.
    speak_during_transition: bool

class OptionalStateEdge(TypedDict, total=False):
    parameters: ToolParameter

class StateEdge(RequiredStateEdge, OptionalStateEdge):
    pass
