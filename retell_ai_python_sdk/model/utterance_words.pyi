# coding: utf-8

"""
    Retell SDK

    API for voice AI. Effortlessly integrate human-like Voice AI into your product. | We are building an API that enables your product to provide an intuitive and engaging way for user interaction - through voice.

    The version of the OpenAPI document: 1.0.0
    Contact: founders@retellai.com
    Created by: https://www.retellai.com/
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from retell_ai_python_sdk import schemas  # noqa: F401


class UtteranceWords(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Array of words in the utternace with the word timestamp. Useful for understanding what word was spoken at what time. Note that the word timestamp is not guranteed to be accurate, it's more like an approximation.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['UtteranceWordsItem']:
            return UtteranceWordsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['UtteranceWordsItem'], typing.List['UtteranceWordsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'UtteranceWords':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'UtteranceWordsItem':
        return super().__getitem__(i)

from retell_ai_python_sdk.model.utterance_words_item import UtteranceWordsItem
