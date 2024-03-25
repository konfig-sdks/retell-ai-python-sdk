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


class ToolParameter(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The parameters the functions accepts, described as a JSON Schema object. See [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. Omitting parameters defines a function with an empty parameter list.
    """


    class MetaOapg:
        required = {
            "type",
            "properties",
        }
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def OBJECT(cls):
                    return cls("object")
        
            @staticmethod
            def properties() -> typing.Type['ToolParameterProperties']:
                return ToolParameterProperties
        
            @staticmethod
            def required() -> typing.Type['ToolParameterRequired']:
                return ToolParameterRequired
            __annotations__ = {
                "type": type,
                "properties": properties,
                "required": required,
            }
    
    type: MetaOapg.properties.type
    properties: 'ToolParameterProperties'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["properties"]) -> 'ToolParameterProperties': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["required"]) -> 'ToolParameterRequired': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "properties", "required", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["properties"]) -> 'ToolParameterProperties': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["required"]) -> typing.Union['ToolParameterRequired', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "properties", "required", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        properties: 'ToolParameterProperties',
        required: typing.Union['ToolParameterRequired', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ToolParameter':
        return super().__new__(
            cls,
            *args,
            type=type,
            properties=properties,
            required=required,
            _configuration=_configuration,
            **kwargs,
        )

from retell_ai_python_sdk.model.tool_parameter_properties import ToolParameterProperties
from retell_ai_python_sdk.model.tool_parameter_required import ToolParameterRequired
