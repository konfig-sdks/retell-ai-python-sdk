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


class BookAppointmentCalTool(BaseModel):
    type: Literal["book_appointment_cal"] = Field(alias='type')

    # Name of the tool. Must be unique within all tools available to LLM at any given time (general tools + state tools + state transitions).
    name: str = Field(alias='name')

    # Cal.com Api key that have access to the cal.com event you want to book appointment.
    cal_api_key: str = Field(alias='cal_api_key')

    # Cal.com event type id number for the cal.com event you want to book appointment.
    event_type_id: typing.Union[int, float] = Field(alias='event_type_id')

    # Describes when to book the appointment.
    description: typing.Optional[str] = Field(None, alias='description')

    # Timezone to be used when booking appointment, must be in [IANA timezone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If not specified, will check if user specified timezone in call, and if not, will use the timezone of the Retell servers.
    timezone: typing.Optional[str] = Field(None, alias='timezone')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
