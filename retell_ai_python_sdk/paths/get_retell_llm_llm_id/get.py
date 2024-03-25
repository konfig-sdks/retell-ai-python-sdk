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

from retell_ai_python_sdk.model.retell_llm_response import RetellLLMResponse as RetellLLMResponseSchema
from retell_ai_python_sdk.model.call_establish_connection500_response import CallEstablishConnection500Response as CallEstablishConnection500ResponseSchema
from retell_ai_python_sdk.model.call_establish_connection_response import CallEstablishConnectionResponse as CallEstablishConnectionResponseSchema
from retell_ai_python_sdk.model.call_establish_connection401_response import CallEstablishConnection401Response as CallEstablishConnection401ResponseSchema
from retell_ai_python_sdk.model.call_establish_connection422_response import CallEstablishConnection422Response as CallEstablishConnection422ResponseSchema

from retell_ai_python_sdk.type.call_establish_connection401_response import CallEstablishConnection401Response
from retell_ai_python_sdk.type.call_establish_connection_response import CallEstablishConnectionResponse
from retell_ai_python_sdk.type.call_establish_connection500_response import CallEstablishConnection500Response
from retell_ai_python_sdk.type.call_establish_connection422_response import CallEstablishConnection422Response
from retell_ai_python_sdk.type.retell_llm_response import RetellLLMResponse

from ...api_client import Dictionary
from retell_ai_python_sdk.pydantic.call_establish_connection_response import CallEstablishConnectionResponse as CallEstablishConnectionResponsePydantic
from retell_ai_python_sdk.pydantic.call_establish_connection422_response import CallEstablishConnection422Response as CallEstablishConnection422ResponsePydantic
from retell_ai_python_sdk.pydantic.call_establish_connection401_response import CallEstablishConnection401Response as CallEstablishConnection401ResponsePydantic
from retell_ai_python_sdk.pydantic.call_establish_connection500_response import CallEstablishConnection500Response as CallEstablishConnection500ResponsePydantic
from retell_ai_python_sdk.pydantic.retell_llm_response import RetellLLMResponse as RetellLLMResponsePydantic

from . import path

# Path params
LlmIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'llm_id': typing.Union[LlmIdSchema, str, ],
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


request_path_llm_id = api_client.PathParameter(
    name="llm_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=LlmIdSchema,
    required=True,
)
_auth = [
    'api_key',
]
SchemaFor200ResponseBodyApplicationJson = RetellLLMResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: RetellLLMResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: RetellLLMResponse


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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '422': _response_for_422,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_llm_details_mapped_args(
        self,
        llm_id: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if llm_id is not None:
            _path_params["llm_id"] = llm_id
        args.path = _path_params
        return args

    async def _aget_llm_details_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
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
            request_path_llm_id,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/get-retell-llm/{llm_id}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _get_llm_details_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
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
            request_path_llm_id,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/get-retell-llm/{llm_id}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class GetLlmDetailsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_llm_details(
        self,
        llm_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_llm_details_mapped_args(
            llm_id=llm_id,
        )
        return await self._aget_llm_details_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get_llm_details(
        self,
        llm_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_llm_details_mapped_args(
            llm_id=llm_id,
        )
        return self._get_llm_details_oapg(
            path_params=args.path,
        )

class GetLlmDetails(BaseApi):

    async def aget_llm_details(
        self,
        llm_id: str,
        validate: bool = False,
        **kwargs,
    ) -> RetellLLMResponsePydantic:
        raw_response = await self.raw.aget_llm_details(
            llm_id=llm_id,
            **kwargs,
        )
        if validate:
            return RootModel[RetellLLMResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(RetellLLMResponsePydantic, raw_response.body)
    
    
    def get_llm_details(
        self,
        llm_id: str,
        validate: bool = False,
    ) -> RetellLLMResponsePydantic:
        raw_response = self.raw.get_llm_details(
            llm_id=llm_id,
        )
        if validate:
            return RootModel[RetellLLMResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(RetellLLMResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        llm_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_llm_details_mapped_args(
            llm_id=llm_id,
        )
        return await self._aget_llm_details_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        llm_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_llm_details_mapped_args(
            llm_id=llm_id,
        )
        return self._get_llm_details_oapg(
            path_params=args.path,
        )

