# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import StrictInt, StrictStr

from typing import List, Optional

from onelogin.models.create_scope200_response import CreateScope200Response
from onelogin.models.create_scope_request import CreateScopeRequest
from onelogin.models.get_scopes200_response_inner import GetScopes200ResponseInner

from onelogin.api_client import ApiClient
from onelogin.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class APIAuthScopesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_scope(self, api_auth_id : StrictStr, content_type : Optional[StrictStr] = None, create_scope_request : Optional[CreateScopeRequest] = None, **kwargs) -> CreateScope200Response:  # noqa: E501
        """Create Api Auth Server Scope  # noqa: E501

        Create API Auth Server Scope  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_scope(api_auth_id, content_type, create_scope_request, async_req=True)
        >>> result = thread.get()

        :param api_auth_id: (required)
        :type api_auth_id: str
        :param content_type:
        :type content_type: str
        :param create_scope_request:
        :type create_scope_request: CreateScopeRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateScope200Response
        """
        kwargs['_return_http_data_only'] = True
        return self.create_scope_with_http_info(api_auth_id, content_type, create_scope_request, **kwargs)  # noqa: E501

    @validate_arguments
    def create_scope_with_http_info(self, api_auth_id : StrictStr, content_type : Optional[StrictStr] = None, create_scope_request : Optional[CreateScopeRequest] = None, **kwargs):  # noqa: E501
        """Create Api Auth Server Scope  # noqa: E501

        Create API Auth Server Scope  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_scope_with_http_info(api_auth_id, content_type, create_scope_request, async_req=True)
        >>> result = thread.get()

        :param api_auth_id: (required)
        :type api_auth_id: str
        :param content_type:
        :type content_type: str
        :param create_scope_request:
        :type create_scope_request: CreateScopeRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CreateScope200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'api_auth_id',
            'content_type',
            'create_scope_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_scope" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['api_auth_id']:
            _path_params['api_auth_id'] = _params['api_auth_id']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['content_type']:
            _header_params['Content-Type'] = _params['content_type']

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None
        if _params['create_scope_request']:
            _body_params = _params['create_scope_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {
            '200': "CreateScope200Response",
            '401': "GetScopes401Response",
            '404': "GetScopes401Response",
            '422': "GetScopes401Response",
        }

        return self.api_client.call_api(
            '/api/2/api_authorizations/{api_auth_id}/scopes', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def delete_scope(self, api_auth_id : StrictStr, scope_id : StrictInt, content_type : Optional[StrictStr] = None, **kwargs) -> None:  # noqa: E501
        """Delete Api Auth Server Scope  # noqa: E501

        Delete Scope  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_scope(api_auth_id, scope_id, content_type, async_req=True)
        >>> result = thread.get()

        :param api_auth_id: (required)
        :type api_auth_id: str
        :param scope_id: (required)
        :type scope_id: int
        :param content_type:
        :type content_type: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_scope_with_http_info(api_auth_id, scope_id, content_type, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_scope_with_http_info(self, api_auth_id : StrictStr, scope_id : StrictInt, content_type : Optional[StrictStr] = None, **kwargs):  # noqa: E501
        """Delete Api Auth Server Scope  # noqa: E501

        Delete Scope  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_scope_with_http_info(api_auth_id, scope_id, content_type, async_req=True)
        >>> result = thread.get()

        :param api_auth_id: (required)
        :type api_auth_id: str
        :param scope_id: (required)
        :type scope_id: int
        :param content_type:
        :type content_type: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'api_auth_id',
            'scope_id',
            'content_type'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_scope" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['api_auth_id']:
            _path_params['api_auth_id'] = _params['api_auth_id']
        if _params['scope_id']:
            _path_params['scope_id'] = _params['scope_id']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['content_type']:
            _header_params['Content-Type'] = _params['content_type']

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/2/api_authorizations/{api_auth_id}/scopes/{scope_id}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_scopes(self, api_auth_id : StrictStr, content_type : Optional[StrictStr] = None, **kwargs) -> List[GetScopes200ResponseInner]:  # noqa: E501
        """Get Api Auth Server Scopes  # noqa: E501

        List Authorization Scopes  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_scopes(api_auth_id, content_type, async_req=True)
        >>> result = thread.get()

        :param api_auth_id: (required)
        :type api_auth_id: str
        :param content_type:
        :type content_type: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[GetScopes200ResponseInner]
        """
        kwargs['_return_http_data_only'] = True
        return self.get_scopes_with_http_info(api_auth_id, content_type, **kwargs)  # noqa: E501

    @validate_arguments
    def get_scopes_with_http_info(self, api_auth_id : StrictStr, content_type : Optional[StrictStr] = None, **kwargs):  # noqa: E501
        """Get Api Auth Server Scopes  # noqa: E501

        List Authorization Scopes  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_scopes_with_http_info(api_auth_id, content_type, async_req=True)
        >>> result = thread.get()

        :param api_auth_id: (required)
        :type api_auth_id: str
        :param content_type:
        :type content_type: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[GetScopes200ResponseInner], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'api_auth_id',
            'content_type'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scopes" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['api_auth_id']:
            _path_params['api_auth_id'] = _params['api_auth_id']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['content_type']:
            _header_params['Content-Type'] = _params['content_type']

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {
            '200': "List[GetScopes200ResponseInner]",
            '401': "GetScopes401Response",
        }

        return self.api_client.call_api(
            '/api/2/api_authorizations/{api_auth_id}/scopes', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def update_scope(self, api_auth_id : StrictStr, scope_id : StrictInt, content_type : Optional[StrictStr] = None, create_scope_request : Optional[CreateScopeRequest] = None, **kwargs) -> CreateScope200Response:  # noqa: E501
        """Update Api Auth Server Scope  # noqa: E501

        Update Scope  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_scope(api_auth_id, scope_id, content_type, create_scope_request, async_req=True)
        >>> result = thread.get()

        :param api_auth_id: (required)
        :type api_auth_id: str
        :param scope_id: (required)
        :type scope_id: int
        :param content_type:
        :type content_type: str
        :param create_scope_request:
        :type create_scope_request: CreateScopeRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateScope200Response
        """
        kwargs['_return_http_data_only'] = True
        return self.update_scope_with_http_info(api_auth_id, scope_id, content_type, create_scope_request, **kwargs)  # noqa: E501

    @validate_arguments
    def update_scope_with_http_info(self, api_auth_id : StrictStr, scope_id : StrictInt, content_type : Optional[StrictStr] = None, create_scope_request : Optional[CreateScopeRequest] = None, **kwargs):  # noqa: E501
        """Update Api Auth Server Scope  # noqa: E501

        Update Scope  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_scope_with_http_info(api_auth_id, scope_id, content_type, create_scope_request, async_req=True)
        >>> result = thread.get()

        :param api_auth_id: (required)
        :type api_auth_id: str
        :param scope_id: (required)
        :type scope_id: int
        :param content_type:
        :type content_type: str
        :param create_scope_request:
        :type create_scope_request: CreateScopeRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CreateScope200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'api_auth_id',
            'scope_id',
            'content_type',
            'create_scope_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_scope" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['api_auth_id']:
            _path_params['api_auth_id'] = _params['api_auth_id']
        if _params['scope_id']:
            _path_params['scope_id'] = _params['scope_id']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['content_type']:
            _header_params['Content-Type'] = _params['content_type']

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None
        if _params['create_scope_request']:
            _body_params = _params['create_scope_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {
            '200': "CreateScope200Response",
            '401': "GetScopes401Response",
            '404': "GetScopes401Response",
            '422': "GetScopes401Response",
        }

        return self.api_client.call_api(
            '/api/2/api_authorizations/{api_auth_id}/scopes/{scope_id}', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))