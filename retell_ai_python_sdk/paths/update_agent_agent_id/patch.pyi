# coding: utf-8

"""
    Retell SDK

    API for voice AI. Effortlessly integrate human-like Voice AI into your product. | We are building an API that enables your product to provide an intuitive and engaging way for user interaction - through voice.

    The version of the OpenAPI document: 1.0.0
    Contact: founders@retellai.com
    Created by: https://www.retellai.com/
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from retell_ai_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from retell_ai_python_sdk.api_response import AsyncGeneratorResponse
from retell_ai_python_sdk import api_client, exceptions
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

from retell_ai_python_sdk.model.call_establish_connection500_response import CallEstablishConnection500Response as CallEstablishConnection500ResponseSchema
from retell_ai_python_sdk.model.base_agent_boosted_keywords import BaseAgentBoostedKeywords as BaseAgentBoostedKeywordsSchema
from retell_ai_python_sdk.model.agent_response import AgentResponse as AgentResponseSchema
from retell_ai_python_sdk.model.base_agent import BaseAgent as BaseAgentSchema
from retell_ai_python_sdk.model.call_establish_connection_response import CallEstablishConnectionResponse as CallEstablishConnectionResponseSchema
from retell_ai_python_sdk.model.call_establish_connection401_response import CallEstablishConnection401Response as CallEstablishConnection401ResponseSchema
from retell_ai_python_sdk.model.call_establish_connection422_response import CallEstablishConnection422Response as CallEstablishConnection422ResponseSchema

from retell_ai_python_sdk.type.agent_response import AgentResponse
from retell_ai_python_sdk.type.call_establish_connection401_response import CallEstablishConnection401Response
from retell_ai_python_sdk.type.base_agent_boosted_keywords import BaseAgentBoostedKeywords
from retell_ai_python_sdk.type.call_establish_connection_response import CallEstablishConnectionResponse
from retell_ai_python_sdk.type.call_establish_connection500_response import CallEstablishConnection500Response
from retell_ai_python_sdk.type.base_agent import BaseAgent
from retell_ai_python_sdk.type.call_establish_connection422_response import CallEstablishConnection422Response

from ...api_client import Dictionary
from retell_ai_python_sdk.pydantic.call_establish_connection_response import CallEstablishConnectionResponse as CallEstablishConnectionResponsePydantic
from retell_ai_python_sdk.pydantic.call_establish_connection422_response import CallEstablishConnection422Response as CallEstablishConnection422ResponsePydantic
from retell_ai_python_sdk.pydantic.call_establish_connection401_response import CallEstablishConnection401Response as CallEstablishConnection401ResponsePydantic
from retell_ai_python_sdk.pydantic.call_establish_connection500_response import CallEstablishConnection500Response as CallEstablishConnection500ResponsePydantic
from retell_ai_python_sdk.pydantic.agent_response import AgentResponse as AgentResponsePydantic
from retell_ai_python_sdk.pydantic.base_agent_boosted_keywords import BaseAgentBoostedKeywords as BaseAgentBoostedKeywordsPydantic
from retell_ai_python_sdk.pydantic.base_agent import BaseAgent as BaseAgentPydantic

# Path params
AgentIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'agent_id': typing.Union[AgentIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_agent_id = api_client.PathParameter(
    name="agent_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AgentIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = BaseAgentSchema


request_body_base_agent = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = AgentResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AgentResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AgentResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = CallEstablishConnectionResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: CallEstablishConnectionResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: CallEstablishConnectionResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = CallEstablishConnection401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: CallEstablishConnection401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: CallEstablishConnection401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = CallEstablishConnection422ResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: CallEstablishConnection422Response


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: CallEstablishConnection422Response


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = CallEstablishConnection500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: CallEstablishConnection500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: CallEstablishConnection500Response


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_existing_agent_mapped_args(
        self,
        agent_id: str,
        llm_websocket_url: typing.Optional[str] = None,
        voice_id: typing.Optional[str] = None,
        voice_temperature: typing.Optional[typing.Union[int, float]] = None,
        voice_speed: typing.Optional[typing.Union[int, float]] = None,
        responsiveness: typing.Optional[typing.Union[int, float]] = None,
        enable_backchannel: typing.Optional[bool] = None,
        ambient_sound: typing.Optional[str] = None,
        agent_name: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        webhook_url: typing.Optional[str] = None,
        boosted_keywords: typing.Optional[BaseAgentBoostedKeywords] = None,
        format_text: typing.Optional[bool] = None,
        opt_out_sensitive_data_storage: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if llm_websocket_url is not None:
            _body["llm_websocket_url"] = llm_websocket_url
        if voice_id is not None:
            _body["voice_id"] = voice_id
        if voice_temperature is not None:
            _body["voice_temperature"] = voice_temperature
        if voice_speed is not None:
            _body["voice_speed"] = voice_speed
        if responsiveness is not None:
            _body["responsiveness"] = responsiveness
        if enable_backchannel is not None:
            _body["enable_backchannel"] = enable_backchannel
        if ambient_sound is not None:
            _body["ambient_sound"] = ambient_sound
        if agent_name is not None:
            _body["agent_name"] = agent_name
        if language is not None:
            _body["language"] = language
        if webhook_url is not None:
            _body["webhook_url"] = webhook_url
        if boosted_keywords is not None:
            _body["boosted_keywords"] = boosted_keywords
        if format_text is not None:
            _body["format_text"] = format_text
        if opt_out_sensitive_data_storage is not None:
            _body["optOutSensitiveDataStorage"] = opt_out_sensitive_data_storage
        args.body = _body
        if agent_id is not None:
            _path_params["agent_id"] = agent_id
        args.path = _path_params
        return args

    async def _aupdate_existing_agent_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_agent_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/update-agent/{agent_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_base_agent.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _update_existing_agent_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_agent_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/update-agent/{agent_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_base_agent.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class UpdateExistingAgentRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_existing_agent(
        self,
        agent_id: str,
        llm_websocket_url: typing.Optional[str] = None,
        voice_id: typing.Optional[str] = None,
        voice_temperature: typing.Optional[typing.Union[int, float]] = None,
        voice_speed: typing.Optional[typing.Union[int, float]] = None,
        responsiveness: typing.Optional[typing.Union[int, float]] = None,
        enable_backchannel: typing.Optional[bool] = None,
        ambient_sound: typing.Optional[str] = None,
        agent_name: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        webhook_url: typing.Optional[str] = None,
        boosted_keywords: typing.Optional[BaseAgentBoostedKeywords] = None,
        format_text: typing.Optional[bool] = None,
        opt_out_sensitive_data_storage: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_existing_agent_mapped_args(
            agent_id=agent_id,
            llm_websocket_url=llm_websocket_url,
            voice_id=voice_id,
            voice_temperature=voice_temperature,
            voice_speed=voice_speed,
            responsiveness=responsiveness,
            enable_backchannel=enable_backchannel,
            ambient_sound=ambient_sound,
            agent_name=agent_name,
            language=language,
            webhook_url=webhook_url,
            boosted_keywords=boosted_keywords,
            format_text=format_text,
            opt_out_sensitive_data_storage=opt_out_sensitive_data_storage,
        )
        return await self._aupdate_existing_agent_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_existing_agent(
        self,
        agent_id: str,
        llm_websocket_url: typing.Optional[str] = None,
        voice_id: typing.Optional[str] = None,
        voice_temperature: typing.Optional[typing.Union[int, float]] = None,
        voice_speed: typing.Optional[typing.Union[int, float]] = None,
        responsiveness: typing.Optional[typing.Union[int, float]] = None,
        enable_backchannel: typing.Optional[bool] = None,
        ambient_sound: typing.Optional[str] = None,
        agent_name: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        webhook_url: typing.Optional[str] = None,
        boosted_keywords: typing.Optional[BaseAgentBoostedKeywords] = None,
        format_text: typing.Optional[bool] = None,
        opt_out_sensitive_data_storage: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_existing_agent_mapped_args(
            agent_id=agent_id,
            llm_websocket_url=llm_websocket_url,
            voice_id=voice_id,
            voice_temperature=voice_temperature,
            voice_speed=voice_speed,
            responsiveness=responsiveness,
            enable_backchannel=enable_backchannel,
            ambient_sound=ambient_sound,
            agent_name=agent_name,
            language=language,
            webhook_url=webhook_url,
            boosted_keywords=boosted_keywords,
            format_text=format_text,
            opt_out_sensitive_data_storage=opt_out_sensitive_data_storage,
        )
        return self._update_existing_agent_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateExistingAgent(BaseApi):

    async def aupdate_existing_agent(
        self,
        agent_id: str,
        llm_websocket_url: typing.Optional[str] = None,
        voice_id: typing.Optional[str] = None,
        voice_temperature: typing.Optional[typing.Union[int, float]] = None,
        voice_speed: typing.Optional[typing.Union[int, float]] = None,
        responsiveness: typing.Optional[typing.Union[int, float]] = None,
        enable_backchannel: typing.Optional[bool] = None,
        ambient_sound: typing.Optional[str] = None,
        agent_name: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        webhook_url: typing.Optional[str] = None,
        boosted_keywords: typing.Optional[BaseAgentBoostedKeywords] = None,
        format_text: typing.Optional[bool] = None,
        opt_out_sensitive_data_storage: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> AgentResponsePydantic:
        raw_response = await self.raw.aupdate_existing_agent(
            agent_id=agent_id,
            llm_websocket_url=llm_websocket_url,
            voice_id=voice_id,
            voice_temperature=voice_temperature,
            voice_speed=voice_speed,
            responsiveness=responsiveness,
            enable_backchannel=enable_backchannel,
            ambient_sound=ambient_sound,
            agent_name=agent_name,
            language=language,
            webhook_url=webhook_url,
            boosted_keywords=boosted_keywords,
            format_text=format_text,
            opt_out_sensitive_data_storage=opt_out_sensitive_data_storage,
            **kwargs,
        )
        if validate:
            return RootModel[AgentResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(AgentResponsePydantic, raw_response.body)
    
    
    def update_existing_agent(
        self,
        agent_id: str,
        llm_websocket_url: typing.Optional[str] = None,
        voice_id: typing.Optional[str] = None,
        voice_temperature: typing.Optional[typing.Union[int, float]] = None,
        voice_speed: typing.Optional[typing.Union[int, float]] = None,
        responsiveness: typing.Optional[typing.Union[int, float]] = None,
        enable_backchannel: typing.Optional[bool] = None,
        ambient_sound: typing.Optional[str] = None,
        agent_name: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        webhook_url: typing.Optional[str] = None,
        boosted_keywords: typing.Optional[BaseAgentBoostedKeywords] = None,
        format_text: typing.Optional[bool] = None,
        opt_out_sensitive_data_storage: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> AgentResponsePydantic:
        raw_response = self.raw.update_existing_agent(
            agent_id=agent_id,
            llm_websocket_url=llm_websocket_url,
            voice_id=voice_id,
            voice_temperature=voice_temperature,
            voice_speed=voice_speed,
            responsiveness=responsiveness,
            enable_backchannel=enable_backchannel,
            ambient_sound=ambient_sound,
            agent_name=agent_name,
            language=language,
            webhook_url=webhook_url,
            boosted_keywords=boosted_keywords,
            format_text=format_text,
            opt_out_sensitive_data_storage=opt_out_sensitive_data_storage,
        )
        if validate:
            return RootModel[AgentResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(AgentResponsePydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        agent_id: str,
        llm_websocket_url: typing.Optional[str] = None,
        voice_id: typing.Optional[str] = None,
        voice_temperature: typing.Optional[typing.Union[int, float]] = None,
        voice_speed: typing.Optional[typing.Union[int, float]] = None,
        responsiveness: typing.Optional[typing.Union[int, float]] = None,
        enable_backchannel: typing.Optional[bool] = None,
        ambient_sound: typing.Optional[str] = None,
        agent_name: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        webhook_url: typing.Optional[str] = None,
        boosted_keywords: typing.Optional[BaseAgentBoostedKeywords] = None,
        format_text: typing.Optional[bool] = None,
        opt_out_sensitive_data_storage: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_existing_agent_mapped_args(
            agent_id=agent_id,
            llm_websocket_url=llm_websocket_url,
            voice_id=voice_id,
            voice_temperature=voice_temperature,
            voice_speed=voice_speed,
            responsiveness=responsiveness,
            enable_backchannel=enable_backchannel,
            ambient_sound=ambient_sound,
            agent_name=agent_name,
            language=language,
            webhook_url=webhook_url,
            boosted_keywords=boosted_keywords,
            format_text=format_text,
            opt_out_sensitive_data_storage=opt_out_sensitive_data_storage,
        )
        return await self._aupdate_existing_agent_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        agent_id: str,
        llm_websocket_url: typing.Optional[str] = None,
        voice_id: typing.Optional[str] = None,
        voice_temperature: typing.Optional[typing.Union[int, float]] = None,
        voice_speed: typing.Optional[typing.Union[int, float]] = None,
        responsiveness: typing.Optional[typing.Union[int, float]] = None,
        enable_backchannel: typing.Optional[bool] = None,
        ambient_sound: typing.Optional[str] = None,
        agent_name: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        webhook_url: typing.Optional[str] = None,
        boosted_keywords: typing.Optional[BaseAgentBoostedKeywords] = None,
        format_text: typing.Optional[bool] = None,
        opt_out_sensitive_data_storage: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_existing_agent_mapped_args(
            agent_id=agent_id,
            llm_websocket_url=llm_websocket_url,
            voice_id=voice_id,
            voice_temperature=voice_temperature,
            voice_speed=voice_speed,
            responsiveness=responsiveness,
            enable_backchannel=enable_backchannel,
            ambient_sound=ambient_sound,
            agent_name=agent_name,
            language=language,
            webhook_url=webhook_url,
            boosted_keywords=boosted_keywords,
            format_text=format_text,
            opt_out_sensitive_data_storage=opt_out_sensitive_data_storage,
        )
        return self._update_existing_agent_oapg(
            body=args.body,
            path_params=args.path,
        )

