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


class VirtualPrivateCloudNatGatewayApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_virtual_private_cloud_nat_gateway(self, virtual_private_cloud_nat_gateway_creation_params, **kwargs):  # noqa: E501
        """create_virtual_private_cloud_nat_gateway  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_virtual_private_cloud_nat_gateway(virtual_private_cloud_nat_gateway_creation_params, async_req=True)
        >>> result = thread.get()

        :param virtual_private_cloud_nat_gateway_creation_params: (required)
        :type virtual_private_cloud_nat_gateway_creation_params: list[VirtualPrivateCloudNatGatewayCreationParams]
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
        :rtype: list[WithTaskVirtualPrivateCloudNatGateway]
        """
        kwargs['_return_http_data_only'] = True
        return self.create_virtual_private_cloud_nat_gateway_with_http_info(virtual_private_cloud_nat_gateway_creation_params, **kwargs)  # noqa: E501

    def create_virtual_private_cloud_nat_gateway_with_http_info(self, virtual_private_cloud_nat_gateway_creation_params, **kwargs):  # noqa: E501
        """create_virtual_private_cloud_nat_gateway  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_virtual_private_cloud_nat_gateway_with_http_info(virtual_private_cloud_nat_gateway_creation_params, async_req=True)
        >>> result = thread.get()

        :param virtual_private_cloud_nat_gateway_creation_params: (required)
        :type virtual_private_cloud_nat_gateway_creation_params: list[VirtualPrivateCloudNatGatewayCreationParams]
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
        :rtype: tuple(list[WithTaskVirtualPrivateCloudNatGateway], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'virtual_private_cloud_nat_gateway_creation_params',
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
                    " to method create_virtual_private_cloud_nat_gateway" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'virtual_private_cloud_nat_gateway_creation_params' is set
        if self.api_client.client_side_validation and ('virtual_private_cloud_nat_gateway_creation_params' not in local_var_params or  # noqa: E501
                                                        local_var_params['virtual_private_cloud_nat_gateway_creation_params'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `virtual_private_cloud_nat_gateway_creation_params` when calling `create_virtual_private_cloud_nat_gateway`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'content_language' in local_var_params:
            header_params['content-language'] = local_var_params['content_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'virtual_private_cloud_nat_gateway_creation_params' in local_var_params:
            body_params = local_var_params['virtual_private_cloud_nat_gateway_creation_params']
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
            200: "list[WithTaskVirtualPrivateCloudNatGateway]",
            400: "ErrorBody",
            404: "ErrorBody",
            500: "ErrorBody",
        }

        return self.api_client.call_api(
            '/create-virtual-private-cloud-nat-gateway', 'POST',
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

    def delete_virtual_private_cloud_nat_gateway(self, virtual_private_cloud_nat_gateway_deletion_params, **kwargs):  # noqa: E501
        """delete_virtual_private_cloud_nat_gateway  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_virtual_private_cloud_nat_gateway(virtual_private_cloud_nat_gateway_deletion_params, async_req=True)
        >>> result = thread.get()

        :param virtual_private_cloud_nat_gateway_deletion_params: (required)
        :type virtual_private_cloud_nat_gateway_deletion_params: VirtualPrivateCloudNatGatewayDeletionParams
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
        :rtype: list[WithTaskDeleteVirtualPrivateCloudNatGateway]
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_virtual_private_cloud_nat_gateway_with_http_info(virtual_private_cloud_nat_gateway_deletion_params, **kwargs)  # noqa: E501

    def delete_virtual_private_cloud_nat_gateway_with_http_info(self, virtual_private_cloud_nat_gateway_deletion_params, **kwargs):  # noqa: E501
        """delete_virtual_private_cloud_nat_gateway  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_virtual_private_cloud_nat_gateway_with_http_info(virtual_private_cloud_nat_gateway_deletion_params, async_req=True)
        >>> result = thread.get()

        :param virtual_private_cloud_nat_gateway_deletion_params: (required)
        :type virtual_private_cloud_nat_gateway_deletion_params: VirtualPrivateCloudNatGatewayDeletionParams
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
        :rtype: tuple(list[WithTaskDeleteVirtualPrivateCloudNatGateway], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'virtual_private_cloud_nat_gateway_deletion_params',
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
                    " to method delete_virtual_private_cloud_nat_gateway" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'virtual_private_cloud_nat_gateway_deletion_params' is set
        if self.api_client.client_side_validation and ('virtual_private_cloud_nat_gateway_deletion_params' not in local_var_params or  # noqa: E501
                                                        local_var_params['virtual_private_cloud_nat_gateway_deletion_params'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `virtual_private_cloud_nat_gateway_deletion_params` when calling `delete_virtual_private_cloud_nat_gateway`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'content_language' in local_var_params:
            header_params['content-language'] = local_var_params['content_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'virtual_private_cloud_nat_gateway_deletion_params' in local_var_params:
            body_params = local_var_params['virtual_private_cloud_nat_gateway_deletion_params']
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
            200: "list[WithTaskDeleteVirtualPrivateCloudNatGateway]",
            400: "ErrorBody",
            404: "ErrorBody",
            500: "ErrorBody",
        }

        return self.api_client.call_api(
            '/delete-virtual-private-cloud-nat-gateway', 'POST',
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

    def get_virtual_private_cloud_nat_gateways(self, get_virtual_private_cloud_nat_gateways_request_body, **kwargs):  # noqa: E501
        """get_virtual_private_cloud_nat_gateways  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_virtual_private_cloud_nat_gateways(get_virtual_private_cloud_nat_gateways_request_body, async_req=True)
        >>> result = thread.get()

        :param get_virtual_private_cloud_nat_gateways_request_body: (required)
        :type get_virtual_private_cloud_nat_gateways_request_body: GetVirtualPrivateCloudNatGatewaysRequestBody
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
        :rtype: list[VirtualPrivateCloudNatGateway]
        """
        kwargs['_return_http_data_only'] = True
        return self.get_virtual_private_cloud_nat_gateways_with_http_info(get_virtual_private_cloud_nat_gateways_request_body, **kwargs)  # noqa: E501

    def get_virtual_private_cloud_nat_gateways_with_http_info(self, get_virtual_private_cloud_nat_gateways_request_body, **kwargs):  # noqa: E501
        """get_virtual_private_cloud_nat_gateways  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_virtual_private_cloud_nat_gateways_with_http_info(get_virtual_private_cloud_nat_gateways_request_body, async_req=True)
        >>> result = thread.get()

        :param get_virtual_private_cloud_nat_gateways_request_body: (required)
        :type get_virtual_private_cloud_nat_gateways_request_body: GetVirtualPrivateCloudNatGatewaysRequestBody
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
        :rtype: tuple(list[VirtualPrivateCloudNatGateway], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'get_virtual_private_cloud_nat_gateways_request_body',
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
                    " to method get_virtual_private_cloud_nat_gateways" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'get_virtual_private_cloud_nat_gateways_request_body' is set
        if self.api_client.client_side_validation and ('get_virtual_private_cloud_nat_gateways_request_body' not in local_var_params or  # noqa: E501
                                                        local_var_params['get_virtual_private_cloud_nat_gateways_request_body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `get_virtual_private_cloud_nat_gateways_request_body` when calling `get_virtual_private_cloud_nat_gateways`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'content_language' in local_var_params:
            header_params['content-language'] = local_var_params['content_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'get_virtual_private_cloud_nat_gateways_request_body' in local_var_params:
            body_params = local_var_params['get_virtual_private_cloud_nat_gateways_request_body']
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
            200: "list[VirtualPrivateCloudNatGateway]",
            400: "ErrorBody",
            404: "ErrorBody",
            500: "ErrorBody",
        }

        return self.api_client.call_api(
            '/get-virtual-private-cloud-nat-gateways', 'POST',
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

    def get_virtual_private_cloud_nat_gateways_connection(self, get_virtual_private_cloud_nat_gateways_connection_request_body, **kwargs):  # noqa: E501
        """get_virtual_private_cloud_nat_gateways_connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_virtual_private_cloud_nat_gateways_connection(get_virtual_private_cloud_nat_gateways_connection_request_body, async_req=True)
        >>> result = thread.get()

        :param get_virtual_private_cloud_nat_gateways_connection_request_body: (required)
        :type get_virtual_private_cloud_nat_gateways_connection_request_body: GetVirtualPrivateCloudNatGatewaysConnectionRequestBody
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
        :rtype: VirtualPrivateCloudNatGatewayConnection
        """
        kwargs['_return_http_data_only'] = True
        return self.get_virtual_private_cloud_nat_gateways_connection_with_http_info(get_virtual_private_cloud_nat_gateways_connection_request_body, **kwargs)  # noqa: E501

    def get_virtual_private_cloud_nat_gateways_connection_with_http_info(self, get_virtual_private_cloud_nat_gateways_connection_request_body, **kwargs):  # noqa: E501
        """get_virtual_private_cloud_nat_gateways_connection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_virtual_private_cloud_nat_gateways_connection_with_http_info(get_virtual_private_cloud_nat_gateways_connection_request_body, async_req=True)
        >>> result = thread.get()

        :param get_virtual_private_cloud_nat_gateways_connection_request_body: (required)
        :type get_virtual_private_cloud_nat_gateways_connection_request_body: GetVirtualPrivateCloudNatGatewaysConnectionRequestBody
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
        :rtype: tuple(VirtualPrivateCloudNatGatewayConnection, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'get_virtual_private_cloud_nat_gateways_connection_request_body',
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
                    " to method get_virtual_private_cloud_nat_gateways_connection" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'get_virtual_private_cloud_nat_gateways_connection_request_body' is set
        if self.api_client.client_side_validation and ('get_virtual_private_cloud_nat_gateways_connection_request_body' not in local_var_params or  # noqa: E501
                                                        local_var_params['get_virtual_private_cloud_nat_gateways_connection_request_body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `get_virtual_private_cloud_nat_gateways_connection_request_body` when calling `get_virtual_private_cloud_nat_gateways_connection`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'content_language' in local_var_params:
            header_params['content-language'] = local_var_params['content_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'get_virtual_private_cloud_nat_gateways_connection_request_body' in local_var_params:
            body_params = local_var_params['get_virtual_private_cloud_nat_gateways_connection_request_body']
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
            200: "VirtualPrivateCloudNatGatewayConnection",
            400: "ErrorBody",
            404: "ErrorBody",
            500: "ErrorBody",
        }

        return self.api_client.call_api(
            '/get-virtual-private-cloud-nat-gateways-connection', 'POST',
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

    def update_virtual_private_cloud_nat_gateway(self, virtual_private_cloud_nat_gateway_updation_params, **kwargs):  # noqa: E501
        """update_virtual_private_cloud_nat_gateway  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_virtual_private_cloud_nat_gateway(virtual_private_cloud_nat_gateway_updation_params, async_req=True)
        >>> result = thread.get()

        :param virtual_private_cloud_nat_gateway_updation_params: (required)
        :type virtual_private_cloud_nat_gateway_updation_params: VirtualPrivateCloudNatGatewayUpdationParams
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
        :rtype: list[WithTaskVirtualPrivateCloudNatGateway]
        """
        kwargs['_return_http_data_only'] = True
        return self.update_virtual_private_cloud_nat_gateway_with_http_info(virtual_private_cloud_nat_gateway_updation_params, **kwargs)  # noqa: E501

    def update_virtual_private_cloud_nat_gateway_with_http_info(self, virtual_private_cloud_nat_gateway_updation_params, **kwargs):  # noqa: E501
        """update_virtual_private_cloud_nat_gateway  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_virtual_private_cloud_nat_gateway_with_http_info(virtual_private_cloud_nat_gateway_updation_params, async_req=True)
        >>> result = thread.get()

        :param virtual_private_cloud_nat_gateway_updation_params: (required)
        :type virtual_private_cloud_nat_gateway_updation_params: VirtualPrivateCloudNatGatewayUpdationParams
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
        :rtype: tuple(list[WithTaskVirtualPrivateCloudNatGateway], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'virtual_private_cloud_nat_gateway_updation_params',
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
                    " to method update_virtual_private_cloud_nat_gateway" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'virtual_private_cloud_nat_gateway_updation_params' is set
        if self.api_client.client_side_validation and ('virtual_private_cloud_nat_gateway_updation_params' not in local_var_params or  # noqa: E501
                                                        local_var_params['virtual_private_cloud_nat_gateway_updation_params'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `virtual_private_cloud_nat_gateway_updation_params` when calling `update_virtual_private_cloud_nat_gateway`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))
        if 'content_language' in local_var_params:
            header_params['content-language'] = local_var_params['content_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'virtual_private_cloud_nat_gateway_updation_params' in local_var_params:
            body_params = local_var_params['virtual_private_cloud_nat_gateway_updation_params']
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
            200: "list[WithTaskVirtualPrivateCloudNatGateway]",
            400: "ErrorBody",
            404: "ErrorBody",
            500: "ErrorBody",
        }

        return self.api_client.call_api(
            '/update-virtual-private-cloud-nat-gateway', 'POST',
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
