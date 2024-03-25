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


class RequiredCheckAvailabilityCalTool(TypedDict):
    type: str

    # Name of the tool. Must be unique within all tools available to LLM at any given time (general tools + state tools + state transitions).
    name: str

    # Cal.com Api key that have access to the cal.com event you want to check availability for.
    cal_api_key: str

    # Cal.com event type id number for the cal.com event you want to check availability for.
    event_type_id: typing.Union[int, float]

class OptionalCheckAvailabilityCalTool(TypedDict, total=False):
    # Describes when to check availability.
    description: str

    # Timezone to be used when checking availability, must be in [IANA timezone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If not specified, will check if user specified timezone in call, and if not, will use the timezone of the Retell servers.
    timezone: str

class CheckAvailabilityCalTool(RequiredCheckAvailabilityCalTool, OptionalCheckAvailabilityCalTool):
    pass
