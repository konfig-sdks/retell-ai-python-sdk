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

from retell_ai_python_sdk.type.book_appointment_cal_tool import BookAppointmentCalTool
from retell_ai_python_sdk.type.check_availability_cal_tool import CheckAvailabilityCalTool
from retell_ai_python_sdk.type.custom_tool import CustomTool
from retell_ai_python_sdk.type.end_call_tool import EndCallTool
from retell_ai_python_sdk.type.transfer_call_tool import TransferCallTool

Tool = typing.Union[EndCallTool,TransferCallTool,CheckAvailabilityCalTool,BookAppointmentCalTool,CustomTool]
