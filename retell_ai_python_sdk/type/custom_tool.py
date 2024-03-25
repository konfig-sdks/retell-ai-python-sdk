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

class RequiredCustomTool(TypedDict):
    # Describes what this tool does and when to call this tool.
    description: str

    type: str

    # Name of the tool. Must be unique within all tools available to LLM at any given time (general tools + state tools + state edges).
    name: str

    # The URL we will post the function name and arguments to get a result for the function. Usually this is your server.
    url: str

    # Determines whether the agent would say sentence like \"One moment, let me check that.\" when executing the function. Recommend to turn on if your function call takes over 1s (including network) to complete, so that your agent remains responsive.
    speak_during_execution: bool

    # Determines whether the agent would call LLM another time and speak when the result of function is obtained. Usually this needs to get turned on so user can get update for the function call.
    speak_after_execution: bool

class OptionalCustomTool(TypedDict, total=False):
    parameters: ToolParameter

    # The description for the sentence agent say during execution. Only applicable when speak_during_execution is true. Can write what to say or even provide examples. The default is \"The message you will say to callee when calling this tool. Make sure it fits into the conversation smoothly.\".
    execution_message_description: str

class CustomTool(RequiredCustomTool, OptionalCustomTool):
    pass
