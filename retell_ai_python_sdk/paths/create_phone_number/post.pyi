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
from retell_ai_python_sdk.model.phone_number_response import PhoneNumberResponse as PhoneNumberResponseSchema
from retell_ai_python_sdk.model.call_establish_connection_response import CallEstablishConnectionResponse as CallEstablishConnectionResponseSchema
from retell_ai_python_sdk.model.call_establish_connection401_response import CallEstablishConnection401Response as CallEstablishConnection401ResponseSchema
from retell_ai_python_sdk.model.phone_number_purchase_number_and_bind_agent_request import PhoneNumberPurchaseNumberAndBindAgentRequest as PhoneNumberPurchaseNumberAndBindAgentRequestSchema

from retell_ai_python_sdk.type.phone_number_purchase_number_and_bind_agent_request import PhoneNumberPurchaseNumberAndBindAgentRequest
from retell_ai_python_sdk.type.call_establish_connection401_response import CallEstablishConnection401Response
from retell_ai_python_sdk.type.call_establish_connection_response import CallEstablishConnectionResponse
from retell_ai_python_sdk.type.call_establish_connection500_response import CallEstablishConnection500Response
from retell_ai_python_sdk.type.phone_number_response import PhoneNumberResponse

from ...api_client import Dictionary
from retell_ai_python_sdk.pydantic.call_establish_connection_response import CallEstablishConnectionResponse as CallEstablishConnectionResponsePydantic
from retell_ai_python_sdk.pydantic.call_establish_connection401_response import CallEstablishConnection401Response as CallEstablishConnection401ResponsePydantic
from retell_ai_python_sdk.pydantic.call_establish_connection500_response import CallEstablishConnection500Response as CallEstablishConnection500ResponsePydantic
from retell_ai_python_sdk.pydantic.phone_number_response import PhoneNumberResponse as PhoneNumberResponsePydantic
from retell_ai_python_sdk.pydantic.phone_number_purchase_number_and_bind_agent_request import PhoneNumberPurchaseNumberAndBindAgentRequest as PhoneNumberPurchaseNumberAndBindAgentRequestPydantic

# body param
SchemaForRequestBodyApplicationJson = PhoneNumberPurchaseNumberAndBindAgentRequestSchema


request_body_phone_number_purchase_number_and_bind_agent_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor201ResponseBodyApplicationJson = PhoneNumberResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: PhoneNumberResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: PhoneNumberResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
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

    def _purchase_number_and_bind_agent_mapped_args(
        self,
        agent_id: str,
        area_code: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if agent_id is not None:
            _body["agent_id"] = agent_id
        if area_code is not None:
            _body["area_code"] = area_code
        args.body = _body
        return args

    async def _apurchase_number_and_bind_agent_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
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
            path_template='/create-phone-number',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_phone_number_purchase_number_and_bind_agent_request.serialize(body, content_type)
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


    def _purchase_number_and_bind_agent_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
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
            path_template='/create-phone-number',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_phone_number_purchase_number_and_bind_agent_request.serialize(body, content_type)
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


class PurchaseNumberAndBindAgentRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def apurchase_number_and_bind_agent(
        self,
        agent_id: str,
        area_code: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._purchase_number_and_bind_agent_mapped_args(
            agent_id=agent_id,
            area_code=area_code,
        )
        return await self._apurchase_number_and_bind_agent_oapg(
            body=args.body,
            **kwargs,
        )
    
    def purchase_number_and_bind_agent(
        self,
        agent_id: str,
        area_code: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._purchase_number_and_bind_agent_mapped_args(
            agent_id=agent_id,
            area_code=area_code,
        )
        return self._purchase_number_and_bind_agent_oapg(
            body=args.body,
        )

class PurchaseNumberAndBindAgent(BaseApi):

    async def apurchase_number_and_bind_agent(
        self,
        agent_id: str,
        area_code: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> PhoneNumberResponsePydantic:
        raw_response = await self.raw.apurchase_number_and_bind_agent(
            agent_id=agent_id,
            area_code=area_code,
            **kwargs,
        )
        if validate:
            return PhoneNumberResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PhoneNumberResponsePydantic, raw_response.body)
    
    
    def purchase_number_and_bind_agent(
        self,
        agent_id: str,
        area_code: typing.Optional[int] = None,
        validate: bool = False,
    ) -> PhoneNumberResponsePydantic:
        raw_response = self.raw.purchase_number_and_bind_agent(
            agent_id=agent_id,
            area_code=area_code,
        )
        if validate:
            return PhoneNumberResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PhoneNumberResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        agent_id: str,
        area_code: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._purchase_number_and_bind_agent_mapped_args(
            agent_id=agent_id,
            area_code=area_code,
        )
        return await self._apurchase_number_and_bind_agent_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        agent_id: str,
        area_code: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._purchase_number_and_bind_agent_mapped_args(
            agent_id=agent_id,
            area_code=area_code,
        )
        return self._purchase_number_and_bind_agent_oapg(
            body=args.body,
        )

