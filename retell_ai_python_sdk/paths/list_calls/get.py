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
from retell_ai_python_sdk.model.call_get_details_response import CallGetDetailsResponse as CallGetDetailsResponseSchema
from retell_ai_python_sdk.model.call_establish_connection_response import CallEstablishConnectionResponse as CallEstablishConnectionResponseSchema
from retell_ai_python_sdk.model.call_establish_connection401_response import CallEstablishConnection401Response as CallEstablishConnection401ResponseSchema

from retell_ai_python_sdk.type.call_get_details_response import CallGetDetailsResponse
from retell_ai_python_sdk.type.call_establish_connection401_response import CallEstablishConnection401Response
from retell_ai_python_sdk.type.call_establish_connection_response import CallEstablishConnectionResponse
from retell_ai_python_sdk.type.call_establish_connection500_response import CallEstablishConnection500Response

from ...api_client import Dictionary
from retell_ai_python_sdk.pydantic.call_establish_connection_response import CallEstablishConnectionResponse as CallEstablishConnectionResponsePydantic
from retell_ai_python_sdk.pydantic.call_establish_connection401_response import CallEstablishConnection401Response as CallEstablishConnection401ResponsePydantic
from retell_ai_python_sdk.pydantic.call_get_details_response import CallGetDetailsResponse as CallGetDetailsResponsePydantic
from retell_ai_python_sdk.pydantic.call_establish_connection500_response import CallEstablishConnection500Response as CallEstablishConnection500ResponsePydantic

from . import path

# Query params


class FilterCriteriaSchema(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            
            
            class agent_id(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'agent_id':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            before_start_timestamp = schemas.IntSchema
            after_start_timestamp = schemas.IntSchema
            before_end_timestamp = schemas.IntSchema
            after_end_timestamp = schemas.IntSchema
            __annotations__ = {
                "agent_id": agent_id,
                "before_start_timestamp": before_start_timestamp,
                "after_start_timestamp": after_start_timestamp,
                "before_end_timestamp": before_end_timestamp,
                "after_end_timestamp": after_end_timestamp,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agent_id"]) -> MetaOapg.properties.agent_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["before_start_timestamp"]) -> MetaOapg.properties.before_start_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["after_start_timestamp"]) -> MetaOapg.properties.after_start_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["before_end_timestamp"]) -> MetaOapg.properties.before_end_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["after_end_timestamp"]) -> MetaOapg.properties.after_end_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["agent_id", "before_start_timestamp", "after_start_timestamp", "before_end_timestamp", "after_end_timestamp", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agent_id"]) -> typing.Union[MetaOapg.properties.agent_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["before_start_timestamp"]) -> typing.Union[MetaOapg.properties.before_start_timestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["after_start_timestamp"]) -> typing.Union[MetaOapg.properties.after_start_timestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["before_end_timestamp"]) -> typing.Union[MetaOapg.properties.before_end_timestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["after_end_timestamp"]) -> typing.Union[MetaOapg.properties.after_end_timestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["agent_id", "before_start_timestamp", "after_start_timestamp", "before_end_timestamp", "after_end_timestamp", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        agent_id: typing.Union[MetaOapg.properties.agent_id, list, tuple, schemas.Unset] = schemas.unset,
        before_start_timestamp: typing.Union[MetaOapg.properties.before_start_timestamp, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        after_start_timestamp: typing.Union[MetaOapg.properties.after_start_timestamp, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        before_end_timestamp: typing.Union[MetaOapg.properties.before_end_timestamp, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        after_end_timestamp: typing.Union[MetaOapg.properties.after_end_timestamp, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FilterCriteriaSchema':
        return super().__new__(
            cls,
            *args,
            agent_id=agent_id,
            before_start_timestamp=before_start_timestamp,
            after_start_timestamp=after_start_timestamp,
            before_end_timestamp=before_end_timestamp,
            after_end_timestamp=after_end_timestamp,
            _configuration=_configuration,
            **kwargs,
        )


class SortOrderSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "ascending": "ASCENDING",
            "descending": "DESCENDING",
        }
    
    @schemas.classproperty
    def ASCENDING(cls):
        return cls("ascending")
    
    @schemas.classproperty
    def DESCENDING(cls):
        return cls("descending")
LimitSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'filter_criteria': typing.Union[FilterCriteriaSchema, dict, frozendict.frozendict, ],
        'sort_order': typing.Union[SortOrderSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_filter_criteria = api_client.QueryParameter(
    name="filter_criteria",
    style=api_client.ParameterStyle.FORM,
    schema=FilterCriteriaSchema,
    explode=True,
)
request_query_sort_order = api_client.QueryParameter(
    name="sort_order",
    style=api_client.ParameterStyle.FORM,
    schema=SortOrderSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
_auth = [
    'api_key',
]
SchemaFor200ResponseBodyApplicationJson = CallGetDetailsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CallGetDetailsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CallGetDetailsResponse


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
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_details_0_mapped_args(
        self,
        filter_criteria: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        sort_order: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if filter_criteria is not None:
            _query_params["filter_criteria"] = filter_criteria
        if sort_order is not None:
            _query_params["sort_order"] = sort_order
        if limit is not None:
            _query_params["limit"] = limit
        args.query = _query_params
        return args

    async def _aget_details_0_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_filter_criteria,
            request_query_sort_order,
            request_query_limit,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
            path_template='/list-calls',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _get_details_0_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_filter_criteria,
            request_query_sort_order,
            request_query_limit,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
            path_template='/list-calls',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


class GetDetails0Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_details_0(
        self,
        filter_criteria: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        sort_order: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_details_0_mapped_args(
            filter_criteria=filter_criteria,
            sort_order=sort_order,
            limit=limit,
        )
        return await self._aget_details_0_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_details_0(
        self,
        filter_criteria: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        sort_order: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_details_0_mapped_args(
            filter_criteria=filter_criteria,
            sort_order=sort_order,
            limit=limit,
        )
        return self._get_details_0_oapg(
            query_params=args.query,
        )

class GetDetails0(BaseApi):

    async def aget_details_0(
        self,
        filter_criteria: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        sort_order: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> CallGetDetailsResponsePydantic:
        raw_response = await self.raw.aget_details_0(
            filter_criteria=filter_criteria,
            sort_order=sort_order,
            limit=limit,
            **kwargs,
        )
        if validate:
            return RootModel[CallGetDetailsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(CallGetDetailsResponsePydantic, raw_response.body)
    
    
    def get_details_0(
        self,
        filter_criteria: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        sort_order: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
    ) -> CallGetDetailsResponsePydantic:
        raw_response = self.raw.get_details_0(
            filter_criteria=filter_criteria,
            sort_order=sort_order,
            limit=limit,
        )
        if validate:
            return RootModel[CallGetDetailsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(CallGetDetailsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        filter_criteria: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        sort_order: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_details_0_mapped_args(
            filter_criteria=filter_criteria,
            sort_order=sort_order,
            limit=limit,
        )
        return await self._aget_details_0_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        filter_criteria: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        sort_order: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_details_0_mapped_args(
            filter_criteria=filter_criteria,
            sort_order=sort_order,
            limit=limit,
        )
        return self._get_details_0_oapg(
            query_params=args.query,
        )

