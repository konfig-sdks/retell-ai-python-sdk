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


class CallEstablishConnectionRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "agent_id",
            "sample_rate",
            "audio_encoding",
            "audio_websocket_protocol",
        }
        
        class properties:
            agent_id = schemas.StrSchema
            
            
            class audio_websocket_protocol(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def WEB(cls):
                    return cls("web")
                
                @schemas.classproperty
                def TWILIO(cls):
                    return cls("twilio")
            
            
            class audio_encoding(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def S16LE(cls):
                    return cls("s16le")
                
                @schemas.classproperty
                def MULAW(cls):
                    return cls("mulaw")
            sample_rate = schemas.IntSchema
            end_call_after_silence_ms = schemas.IntSchema
            from_number = schemas.StrSchema
            to_number = schemas.StrSchema
            metadata = schemas.DictSchema
        
            @staticmethod
            def retell_llm_dynamic_variables() -> typing.Type['CallEstablishConnectionRequestRetellLlmDynamicVariables']:
                return CallEstablishConnectionRequestRetellLlmDynamicVariables
            __annotations__ = {
                "agent_id": agent_id,
                "audio_websocket_protocol": audio_websocket_protocol,
                "audio_encoding": audio_encoding,
                "sample_rate": sample_rate,
                "end_call_after_silence_ms": end_call_after_silence_ms,
                "from_number": from_number,
                "to_number": to_number,
                "metadata": metadata,
                "retell_llm_dynamic_variables": retell_llm_dynamic_variables,
            }
    
    agent_id: MetaOapg.properties.agent_id
    sample_rate: MetaOapg.properties.sample_rate
    audio_encoding: MetaOapg.properties.audio_encoding
    audio_websocket_protocol: MetaOapg.properties.audio_websocket_protocol
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agent_id"]) -> MetaOapg.properties.agent_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["audio_websocket_protocol"]) -> MetaOapg.properties.audio_websocket_protocol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["audio_encoding"]) -> MetaOapg.properties.audio_encoding: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sample_rate"]) -> MetaOapg.properties.sample_rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_call_after_silence_ms"]) -> MetaOapg.properties.end_call_after_silence_ms: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_number"]) -> MetaOapg.properties.from_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_number"]) -> MetaOapg.properties.to_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["retell_llm_dynamic_variables"]) -> 'CallEstablishConnectionRequestRetellLlmDynamicVariables': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["agent_id", "audio_websocket_protocol", "audio_encoding", "sample_rate", "end_call_after_silence_ms", "from_number", "to_number", "metadata", "retell_llm_dynamic_variables", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agent_id"]) -> MetaOapg.properties.agent_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["audio_websocket_protocol"]) -> MetaOapg.properties.audio_websocket_protocol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["audio_encoding"]) -> MetaOapg.properties.audio_encoding: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sample_rate"]) -> MetaOapg.properties.sample_rate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_call_after_silence_ms"]) -> typing.Union[MetaOapg.properties.end_call_after_silence_ms, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_number"]) -> typing.Union[MetaOapg.properties.from_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_number"]) -> typing.Union[MetaOapg.properties.to_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["retell_llm_dynamic_variables"]) -> typing.Union['CallEstablishConnectionRequestRetellLlmDynamicVariables', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["agent_id", "audio_websocket_protocol", "audio_encoding", "sample_rate", "end_call_after_silence_ms", "from_number", "to_number", "metadata", "retell_llm_dynamic_variables", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        agent_id: typing.Union[MetaOapg.properties.agent_id, str, ],
        sample_rate: typing.Union[MetaOapg.properties.sample_rate, decimal.Decimal, int, ],
        audio_encoding: typing.Union[MetaOapg.properties.audio_encoding, str, ],
        audio_websocket_protocol: typing.Union[MetaOapg.properties.audio_websocket_protocol, str, ],
        end_call_after_silence_ms: typing.Union[MetaOapg.properties.end_call_after_silence_ms, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        from_number: typing.Union[MetaOapg.properties.from_number, str, schemas.Unset] = schemas.unset,
        to_number: typing.Union[MetaOapg.properties.to_number, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        retell_llm_dynamic_variables: typing.Union['CallEstablishConnectionRequestRetellLlmDynamicVariables', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CallEstablishConnectionRequest':
        return super().__new__(
            cls,
            *args,
            agent_id=agent_id,
            sample_rate=sample_rate,
            audio_encoding=audio_encoding,
            audio_websocket_protocol=audio_websocket_protocol,
            end_call_after_silence_ms=end_call_after_silence_ms,
            from_number=from_number,
            to_number=to_number,
            metadata=metadata,
            retell_llm_dynamic_variables=retell_llm_dynamic_variables,
            _configuration=_configuration,
            **kwargs,
        )

from retell_ai_python_sdk.model.call_establish_connection_request_retell_llm_dynamic_variables import CallEstablishConnectionRequestRetellLlmDynamicVariables
