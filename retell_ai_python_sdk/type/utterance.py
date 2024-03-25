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

from retell_ai_python_sdk.type.utterance_words import UtteranceWords

class RequiredUtterance(TypedDict):
    # Documents whether this utterance is spoken by agent or user.
    role: str

    # Transcript of the utterances.
    content: str

    words: UtteranceWords

class OptionalUtterance(TypedDict, total=False):
    pass

class Utterance(RequiredUtterance, OptionalUtterance):
    pass
