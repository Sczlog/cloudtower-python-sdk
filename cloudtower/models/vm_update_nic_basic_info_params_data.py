# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VmUpdateNicBasicInfoParamsData(object):
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
        'subnet_mask': 'str',
        'gateway': 'str',
        'ip_address': 'str'
    }

    attribute_map = {
        'subnet_mask': 'subnet_mask',
        'gateway': 'gateway',
        'ip_address': 'ip_address'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VmUpdateNicBasicInfoParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._subnet_mask = None
        self._gateway = None
        self._ip_address = None
        self.discriminator = None

        if "subnet_mask" in kwargs:
            self.subnet_mask = kwargs["subnet_mask"]
        if "gateway" in kwargs:
            self.gateway = kwargs["gateway"]
        if "ip_address" in kwargs:
            self.ip_address = kwargs["ip_address"]

    @property
    def subnet_mask(self):
        """Gets the subnet_mask of this VmUpdateNicBasicInfoParamsData.  # noqa: E501


        :return: The subnet_mask of this VmUpdateNicBasicInfoParamsData.  # noqa: E501
        :rtype: str
        """
        return self._subnet_mask

    @subnet_mask.setter
    def subnet_mask(self, subnet_mask):
        """Sets the subnet_mask of this VmUpdateNicBasicInfoParamsData.


        :param subnet_mask: The subnet_mask of this VmUpdateNicBasicInfoParamsData.  # noqa: E501
        :type subnet_mask: str
        """

        self._subnet_mask = subnet_mask

    @property
    def gateway(self):
        """Gets the gateway of this VmUpdateNicBasicInfoParamsData.  # noqa: E501


        :return: The gateway of this VmUpdateNicBasicInfoParamsData.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this VmUpdateNicBasicInfoParamsData.


        :param gateway: The gateway of this VmUpdateNicBasicInfoParamsData.  # noqa: E501
        :type gateway: str
        """

        self._gateway = gateway

    @property
    def ip_address(self):
        """Gets the ip_address of this VmUpdateNicBasicInfoParamsData.  # noqa: E501


        :return: The ip_address of this VmUpdateNicBasicInfoParamsData.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this VmUpdateNicBasicInfoParamsData.


        :param ip_address: The ip_address of this VmUpdateNicBasicInfoParamsData.  # noqa: E501
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
        if not isinstance(other, VmUpdateNicBasicInfoParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmUpdateNicBasicInfoParamsData):
            return True

        return self.to_dict() != other.to_dict()
