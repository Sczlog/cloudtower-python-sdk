# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class CloudInitNetWork(object):
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
        'routes': 'list[CloudInitNetWorkRoute]',
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

    def __init__(self, **kwargs):  # noqa: E501
        """CloudInitNetWork - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._routes = None
        self._type = None
        self._nic_index = None
        self._netmask = None
        self._ip_address = None
        self.discriminator = None

        if "routes" in kwargs:
            self.routes = kwargs["routes"]
        if "type" in kwargs:
            self.type = kwargs["type"]
        if "nic_index" in kwargs:
            self.nic_index = kwargs["nic_index"]
        if "netmask" in kwargs:
            self.netmask = kwargs["netmask"]
        if "ip_address" in kwargs:
            self.ip_address = kwargs["ip_address"]

    @property
    def routes(self):
        """Gets the routes of this CloudInitNetWork.  # noqa: E501


        :return: The routes of this CloudInitNetWork.  # noqa: E501
        :rtype: list[CloudInitNetWorkRoute]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this CloudInitNetWork.


        :param routes: The routes of this CloudInitNetWork.  # noqa: E501
        :type routes: list[CloudInitNetWorkRoute]
        """

        self._routes = routes

    @property
    def type(self):
        """Gets the type of this CloudInitNetWork.  # noqa: E501


        :return: The type of this CloudInitNetWork.  # noqa: E501
        :rtype: CloudInitNetworkTypeEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CloudInitNetWork.


        :param type: The type of this CloudInitNetWork.  # noqa: E501
        :type type: CloudInitNetworkTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def nic_index(self):
        """Gets the nic_index of this CloudInitNetWork.  # noqa: E501


        :return: The nic_index of this CloudInitNetWork.  # noqa: E501
        :rtype: int
        """
        return self._nic_index

    @nic_index.setter
    def nic_index(self, nic_index):
        """Sets the nic_index of this CloudInitNetWork.


        :param nic_index: The nic_index of this CloudInitNetWork.  # noqa: E501
        :type nic_index: int
        """
        if self.local_vars_configuration.client_side_validation and nic_index is None:  # noqa: E501
            raise ValueError("Invalid value for `nic_index`, must not be `None`")  # noqa: E501

        self._nic_index = nic_index

    @property
    def netmask(self):
        """Gets the netmask of this CloudInitNetWork.  # noqa: E501


        :return: The netmask of this CloudInitNetWork.  # noqa: E501
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this CloudInitNetWork.


        :param netmask: The netmask of this CloudInitNetWork.  # noqa: E501
        :type netmask: str
        """

        self._netmask = netmask

    @property
    def ip_address(self):
        """Gets the ip_address of this CloudInitNetWork.  # noqa: E501


        :return: The ip_address of this CloudInitNetWork.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this CloudInitNetWork.


        :param ip_address: The ip_address of this CloudInitNetWork.  # noqa: E501
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
        if not isinstance(other, CloudInitNetWork):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudInitNetWork):
            return True

        return self.to_dict() != other.to_dict()
