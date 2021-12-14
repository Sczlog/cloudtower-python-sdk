# coding: utf-8

"""
    Tower SDK API

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 1.8.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower_python_sdk.configuration import Configuration


class VmCreateVmFromTemplateParamsCloudInitNetworks(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'routes': 'list[VmCreateVmFromTemplateParamsCloudInitRoutes]',
        'type': 'CloudInitNetworkTypeEnum',
        'nic_index': 'int',
        'netmask': 'str',
        'ip_address': 'str'
    }

    attribute_map = {
        'routes': 'routes',
        'type': 'type',
        'nic_index': 'nic_index',
        'netmask': 'netmask',
        'ip_address': 'ip_address'
    }

    def __init__(self, routes=None, type=None, nic_index=None, netmask=None, ip_address=None, local_vars_configuration=None):  # noqa: E501
        """VmCreateVmFromTemplateParamsCloudInitNetworks - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._routes = None
        self._type = None
        self._nic_index = None
        self._netmask = None
        self._ip_address = None
        self.discriminator = None

        if routes is not None:
            self.routes = routes
        self.type = type
        self.nic_index = nic_index
        if netmask is not None:
            self.netmask = netmask
        if ip_address is not None:
            self.ip_address = ip_address

    @property
    def routes(self):
        """Gets the routes of this VmCreateVmFromTemplateParamsCloudInitNetworks.  # noqa: E501


        :return: The routes of this VmCreateVmFromTemplateParamsCloudInitNetworks.  # noqa: E501
        :rtype: list[VmCreateVmFromTemplateParamsCloudInitRoutes]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this VmCreateVmFromTemplateParamsCloudInitNetworks.


        :param routes: The routes of this VmCreateVmFromTemplateParamsCloudInitNetworks.  # noqa: E501
        :type routes: list[VmCreateVmFromTemplateParamsCloudInitRoutes]
        """

        self._routes = routes

    @property
    def type(self):
        """Gets the type of this VmCreateVmFromTemplateParamsCloudInitNetworks.  # noqa: E501


        :return: The type of this VmCreateVmFromTemplateParamsCloudInitNetworks.  # noqa: E501
        :rtype: CloudInitNetworkTypeEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VmCreateVmFromTemplateParamsCloudInitNetworks.


        :param type: The type of this VmCreateVmFromTemplateParamsCloudInitNetworks.  # noqa: E501
        :type type: CloudInitNetworkTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def nic_index(self):
        """Gets the nic_index of this VmCreateVmFromTemplateParamsCloudInitNetworks.  # noqa: E501


        :return: The nic_index of this VmCreateVmFromTemplateParamsCloudInitNetworks.  # noqa: E501
        :rtype: int
        """
        return self._nic_index

    @nic_index.setter
    def nic_index(self, nic_index):
        """Sets the nic_index of this VmCreateVmFromTemplateParamsCloudInitNetworks.


        :param nic_index: The nic_index of this VmCreateVmFromTemplateParamsCloudInitNetworks.  # noqa: E501
        :type nic_index: int
        """
        if self.local_vars_configuration.client_side_validation and nic_index is None:  # noqa: E501
            raise ValueError("Invalid value for `nic_index`, must not be `None`")  # noqa: E501

        self._nic_index = nic_index

    @property
    def netmask(self):
        """Gets the netmask of this VmCreateVmFromTemplateParamsCloudInitNetworks.  # noqa: E501


        :return: The netmask of this VmCreateVmFromTemplateParamsCloudInitNetworks.  # noqa: E501
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this VmCreateVmFromTemplateParamsCloudInitNetworks.


        :param netmask: The netmask of this VmCreateVmFromTemplateParamsCloudInitNetworks.  # noqa: E501
        :type netmask: str
        """

        self._netmask = netmask

    @property
    def ip_address(self):
        """Gets the ip_address of this VmCreateVmFromTemplateParamsCloudInitNetworks.  # noqa: E501


        :return: The ip_address of this VmCreateVmFromTemplateParamsCloudInitNetworks.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this VmCreateVmFromTemplateParamsCloudInitNetworks.


        :param ip_address: The ip_address of this VmCreateVmFromTemplateParamsCloudInitNetworks.  # noqa: E501
        :type ip_address: str
        """

        self._ip_address = ip_address

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VmCreateVmFromTemplateParamsCloudInitNetworks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmCreateVmFromTemplateParamsCloudInitNetworks):
            return True

        return self.to_dict() != other.to_dict()
