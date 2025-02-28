# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class NestedVirtualPrivateCloudServiceTepIpPool(object):
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
        'display_name': 'str',
        'gateway': 'str',
        'ip_end': 'str',
        'ip_start': 'str',
        'netmask': 'str'
    }

    attribute_map = {
        'display_name': 'display_name',
        'gateway': 'gateway',
        'ip_end': 'ip_end',
        'ip_start': 'ip_start',
        'netmask': 'netmask'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedVirtualPrivateCloudServiceTepIpPool - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._display_name = None
        self._gateway = None
        self._ip_end = None
        self._ip_start = None
        self._netmask = None
        self.discriminator = None

        if "display_name" in kwargs:
            self.display_name = kwargs["display_name"]
        if "gateway" in kwargs:
            self.gateway = kwargs["gateway"]
        if "ip_end" in kwargs:
            self.ip_end = kwargs["ip_end"]
        if "ip_start" in kwargs:
            self.ip_start = kwargs["ip_start"]
        if "netmask" in kwargs:
            self.netmask = kwargs["netmask"]

    @property
    def display_name(self):
        """Gets the display_name of this NestedVirtualPrivateCloudServiceTepIpPool.  # noqa: E501


        :return: The display_name of this NestedVirtualPrivateCloudServiceTepIpPool.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this NestedVirtualPrivateCloudServiceTepIpPool.


        :param display_name: The display_name of this NestedVirtualPrivateCloudServiceTepIpPool.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def gateway(self):
        """Gets the gateway of this NestedVirtualPrivateCloudServiceTepIpPool.  # noqa: E501


        :return: The gateway of this NestedVirtualPrivateCloudServiceTepIpPool.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this NestedVirtualPrivateCloudServiceTepIpPool.


        :param gateway: The gateway of this NestedVirtualPrivateCloudServiceTepIpPool.  # noqa: E501
        :type gateway: str
        """
        if self.local_vars_configuration.client_side_validation and gateway is None:  # noqa: E501
            raise ValueError("Invalid value for `gateway`, must not be `None`")  # noqa: E501

        self._gateway = gateway

    @property
    def ip_end(self):
        """Gets the ip_end of this NestedVirtualPrivateCloudServiceTepIpPool.  # noqa: E501


        :return: The ip_end of this NestedVirtualPrivateCloudServiceTepIpPool.  # noqa: E501
        :rtype: str
        """
        return self._ip_end

    @ip_end.setter
    def ip_end(self, ip_end):
        """Sets the ip_end of this NestedVirtualPrivateCloudServiceTepIpPool.


        :param ip_end: The ip_end of this NestedVirtualPrivateCloudServiceTepIpPool.  # noqa: E501
        :type ip_end: str
        """
        if self.local_vars_configuration.client_side_validation and ip_end is None:  # noqa: E501
            raise ValueError("Invalid value for `ip_end`, must not be `None`")  # noqa: E501

        self._ip_end = ip_end

    @property
    def ip_start(self):
        """Gets the ip_start of this NestedVirtualPrivateCloudServiceTepIpPool.  # noqa: E501


        :return: The ip_start of this NestedVirtualPrivateCloudServiceTepIpPool.  # noqa: E501
        :rtype: str
        """
        return self._ip_start

    @ip_start.setter
    def ip_start(self, ip_start):
        """Sets the ip_start of this NestedVirtualPrivateCloudServiceTepIpPool.


        :param ip_start: The ip_start of this NestedVirtualPrivateCloudServiceTepIpPool.  # noqa: E501
        :type ip_start: str
        """
        if self.local_vars_configuration.client_side_validation and ip_start is None:  # noqa: E501
            raise ValueError("Invalid value for `ip_start`, must not be `None`")  # noqa: E501

        self._ip_start = ip_start

    @property
    def netmask(self):
        """Gets the netmask of this NestedVirtualPrivateCloudServiceTepIpPool.  # noqa: E501


        :return: The netmask of this NestedVirtualPrivateCloudServiceTepIpPool.  # noqa: E501
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this NestedVirtualPrivateCloudServiceTepIpPool.


        :param netmask: The netmask of this NestedVirtualPrivateCloudServiceTepIpPool.  # noqa: E501
        :type netmask: str
        """
        if self.local_vars_configuration.client_side_validation and netmask is None:  # noqa: E501
            raise ValueError("Invalid value for `netmask`, must not be `None`")  # noqa: E501

        self._netmask = netmask

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
        if not isinstance(other, NestedVirtualPrivateCloudServiceTepIpPool):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedVirtualPrivateCloudServiceTepIpPool):
            return True

        return self.to_dict() != other.to_dict()
