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


class RequiredPhoneNumberResponse(TypedDict):
    # BCP 47 format of the number (+country code, then number with no space, no special characters), used as the unique identifier for phone number APIs.
    phone_number: str

    # Pretty printed phone number, provided for your reference.
    phone_number_pretty: str

    # Unique id of agent to bind to newly obtained number. The number will automatically use the agent when doing inbound / outbound calls.
    agent_id: str

    # Area code of the number to obtain. Format is a 3 digit integer. Currently only supports US area code.
    area_code: int

    # Last modification timestamp (milliseconds since epoch). Either the time of last update or creation if no updates available.
    last_modification_timestamp: int

class OptionalPhoneNumberResponse(TypedDict, total=False):
    pass

class PhoneNumberResponse(RequiredPhoneNumberResponse, OptionalPhoneNumberResponse):
    pass
