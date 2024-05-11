# coding: utf-8
from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cloudtower.api_client import ApiClient
from cloudtower.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SecurityPolicyApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_security_policy(self, security_policy_create_params, **kwargs):  # noqa: E501
        """create_security_policy  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_security_policy(security_policy_create_params, async_req=True)
        >>> result = thread.get()

        :param security_policy_create_params: (required)
        :type security_policy_create_params: SecurityPolicyCreateParams
        :param content_language:
        :type content_language: ContentLanguage
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
        :rtype: WithTaskSecurityPolicy
        """
        kwargs['_return_http_data_only'] = True
        return self.create_security_policy_with_http_info(security_policy_create_params, **kwargs)  # noqa: E501

    def create_security_policy_with_http_info(self, security_policy_create_params, **kwargs):  # noqa: E501
        """create_security_policy  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_security_policy_with_http_info(security_policy_create_params, async_req=True)
        >>> result = thread.get()

        :param security_policy_create_params: (required)
        :type security_policy_create_params: SecurityPolicyCreateParams
        :param content_language:
        :type content_language: ContentLanguage
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
        :rtype: tuple(WithTaskSecurityPolicy, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'security_policy_create_params',
            'content_language'
        ]
        all_params.extend(
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

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_security_policy" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'security_policy_create_params' is set
        if self.api_client.client_side_validation and ('security_policy_create_params' not in local_var_params or  # noqa: E501
                                                        local_var_params['security_policy_create_params'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `security_policy_create_params` when calling `create_security_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'content_language' in local_var_params:
            header_params['content-language'] = local_var_params['content_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'security_policy_create_params' in local_var_params:
            body_params = local_var_params['security_policy_create_params']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json'],
                'POST', body_params))  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        response_types_map = {
            200: "WithTaskSecurityPolicy",
            400: "ErrorBody",
            404: "ErrorBody",
            500: "ErrorBody",
        }

        return self.api_client.call_api(
            '/create-security-policy', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def delete_security_policy(self, security_policy_delete_params, **kwargs):  # noqa: E501
        """delete_security_policy  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_security_policy(security_policy_delete_params, async_req=True)
        >>> result = thread.get()

        :param security_policy_delete_params: (required)
        :type security_policy_delete_params: SecurityPolicyDeleteParams
        :param content_language:
        :type content_language: ContentLanguage
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
        :rtype: list[WithTaskDeleteSecurityPolicy]
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_security_policy_with_http_info(security_policy_delete_params, **kwargs)  # noqa: E501

    def delete_security_policy_with_http_info(self, security_policy_delete_params, **kwargs):  # noqa: E501
        """delete_security_policy  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_security_policy_with_http_info(security_policy_delete_params, async_req=True)
        >>> result = thread.get()

        :param security_policy_delete_params: (required)
        :type security_policy_delete_params: SecurityPolicyDeleteParams
        :param content_language:
        :type content_language: ContentLanguage
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
        :rtype: tuple(list[WithTaskDeleteSecurityPolicy], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'security_policy_delete_params',
            'content_language'
        ]
        all_params.extend(
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

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_security_policy" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'security_policy_delete_params' is set
        if self.api_client.client_side_validation and ('security_policy_delete_params' not in local_var_params or  # noqa: E501
                                                        local_var_params['security_policy_delete_params'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `security_policy_delete_params` when calling `delete_security_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'content_language' in local_var_params:
            header_params['content-language'] = local_var_params['content_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'security_policy_delete_params' in local_var_params:
            body_params = local_var_params['security_policy_delete_params']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json'],
                'POST', body_params))  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        response_types_map = {
            200: "list[WithTaskDeleteSecurityPolicy]",
            400: "ErrorBody",
            404: "ErrorBody",
            500: "ErrorBody",
        }

        return self.api_client.call_api(
            '/delete-security-policy', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_security_policies(self, get_security_policies_request_body, **kwargs):  # noqa: E501
        """get_security_policies  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_security_policies(get_security_policies_request_body, async_req=True)
        >>> result = thread.get()

        :param get_security_policies_request_body: (required)
        :type get_security_policies_request_body: GetSecurityPoliciesRequestBody
        :param content_language:
        :type content_language: str
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
        :rtype: list[SecurityPolicy]
        """
        kwargs['_return_http_data_only'] = True
        return self.get_security_policies_with_http_info(get_security_policies_request_body, **kwargs)  # noqa: E501

    def get_security_policies_with_http_info(self, get_security_policies_request_body, **kwargs):  # noqa: E501
        """get_security_policies  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_security_policies_with_http_info(get_security_policies_request_body, async_req=True)
        >>> result = thread.get()

        :param get_security_policies_request_body: (required)
        :type get_security_policies_request_body: GetSecurityPoliciesRequestBody
        :param content_language:
        :type content_language: str
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
        :rtype: tuple(list[SecurityPolicy], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'get_security_policies_request_body',
            'content_language'
        ]
        all_params.extend(
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

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_security_policies" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'get_security_policies_request_body' is set
        if self.api_client.client_side_validation and ('get_security_policies_request_body' not in local_var_params or  # noqa: E501
                                                        local_var_params['get_security_policies_request_body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `get_security_policies_request_body` when calling `get_security_policies`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'content_language' in local_var_params:
            header_params['content-language'] = local_var_params['content_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'get_security_policies_request_body' in local_var_params:
            body_params = local_var_params['get_security_policies_request_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json'],
                'POST', body_params))  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        response_types_map = {
            200: "list[SecurityPolicy]",
            400: "ErrorBody",
            404: "ErrorBody",
            500: "ErrorBody",
        }

        return self.api_client.call_api(
            '/get-security-policies', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_security_policies_connection(self, get_security_policies_connection_request_body, **kwargs):  # noqa: E501
        """get_security_policies_connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_security_policies_connection(get_security_policies_connection_request_body, async_req=True)
        >>> result = thread.get()

        :param get_security_policies_connection_request_body: (required)
        :type get_security_policies_connection_request_body: GetSecurityPoliciesConnectionRequestBody
        :param content_language:
        :type content_language: str
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
        :rtype: SecurityPolicyConnection
        """
        kwargs['_return_http_data_only'] = True
        return self.get_security_policies_connection_with_http_info(get_security_policies_connection_request_body, **kwargs)  # noqa: E501

    def get_security_policies_connection_with_http_info(self, get_security_policies_connection_request_body, **kwargs):  # noqa: E501
        """get_security_policies_connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_security_policies_connection_with_http_info(get_security_policies_connection_request_body, async_req=True)
        >>> result = thread.get()

        :param get_security_policies_connection_request_body: (required)
        :type get_security_policies_connection_request_body: GetSecurityPoliciesConnectionRequestBody
        :param content_language:
        :type content_language: str
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
        :rtype: tuple(SecurityPolicyConnection, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'get_security_policies_connection_request_body',
            'content_language'
        ]
        all_params.extend(
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

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_security_policies_connection" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'get_security_policies_connection_request_body' is set
        if self.api_client.client_side_validation and ('get_security_policies_connection_request_body' not in local_var_params or  # noqa: E501
                                                        local_var_params['get_security_policies_connection_request_body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `get_security_policies_connection_request_body` when calling `get_security_policies_connection`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'content_language' in local_var_params:
            header_params['content-language'] = local_var_params['content_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'get_security_policies_connection_request_body' in local_var_params:
            body_params = local_var_params['get_security_policies_connection_request_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json'],
                'POST', body_params))  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        response_types_map = {
            200: "SecurityPolicyConnection",
            400: "ErrorBody",
            404: "ErrorBody",
            500: "ErrorBody",
        }

        return self.api_client.call_api(
            '/get-security-policies-connection', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def update_security_policy(self, security_policy_update_body, **kwargs):  # noqa: E501
        """update_security_policy  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_security_policy(security_policy_update_body, async_req=True)
        >>> result = thread.get()

        :param security_policy_update_body: (required)
        :type security_policy_update_body: SecurityPolicyUpdateBody
        :param content_language:
        :type content_language: ContentLanguage
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
        :rtype: list[WithTaskSecurityPolicy]
        """
        kwargs['_return_http_data_only'] = True
        return self.update_security_policy_with_http_info(security_policy_update_body, **kwargs)  # noqa: E501

    def update_security_policy_with_http_info(self, security_policy_update_body, **kwargs):  # noqa: E501
        """update_security_policy  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_security_policy_with_http_info(security_policy_update_body, async_req=True)
        >>> result = thread.get()

        :param security_policy_update_body: (required)
        :type security_policy_update_body: SecurityPolicyUpdateBody
        :param content_language:
        :type content_language: ContentLanguage
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
        :rtype: tuple(list[WithTaskSecurityPolicy], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'security_policy_update_body',
            'content_language'
        ]
        all_params.extend(
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

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_security_policy" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'security_policy_update_body' is set
        if self.api_client.client_side_validation and ('security_policy_update_body' not in local_var_params or  # noqa: E501
                                                        local_var_params['security_policy_update_body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `security_policy_update_body` when calling `update_security_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'content_language' in local_var_params:
            header_params['content-language'] = local_var_params['content_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'security_policy_update_body' in local_var_params:
            body_params = local_var_params['security_policy_update_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json'],
                'POST', body_params))  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        response_types_map = {
            200: "list[WithTaskSecurityPolicy]",
            400: "ErrorBody",
            404: "ErrorBody",
            500: "ErrorBody",
        }

        return self.api_client.call_api(
            '/update-security-policy', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
