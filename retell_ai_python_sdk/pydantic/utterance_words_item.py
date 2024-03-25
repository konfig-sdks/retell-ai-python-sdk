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


class UtteranceWordsItem(BaseModel):
    # Word transcript (with punctuation if applicable).
    word: typing.Optional[str] = Field(None, alias='word')

    # Start time of the word in the call in second. This is relative audio time, not wall time.
    start: typing.Optional[typing.Union[int, float]] = Field(None, alias='start')

    # End time of the word in the call in second. This is relative audio time, not wall time.
    end: typing.Optional[typing.Union[int, float]] = Field(None, alias='end')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
