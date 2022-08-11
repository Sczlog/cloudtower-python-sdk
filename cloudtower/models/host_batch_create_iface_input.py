# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Contact: info@smartx.com
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


class HostBatchCreateIfaceInput(object):
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
        'netmask': 'str',
        'name': 'list[str]',
        'ip': 'str',
        'function': 'HostBatchCreateIfaceFunction'
    }

    attribute_map = {
        'netmask': 'netmask',
        'name': 'name',
        'ip': 'ip',
        'function': 'function'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """HostBatchCreateIfaceInput - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._netmask = None
        self._name = None
        self._ip = None
        self._function = None
        self.discriminator = None

        if "netmask" in kwargs:
            self.netmask = kwargs["netmask"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "ip" in kwargs:
            self.ip = kwargs["ip"]
        if "function" in kwargs:
            self.function = kwargs["function"]

    @property
    def netmask(self):
        """Gets the netmask of this HostBatchCreateIfaceInput.  # noqa: E501


        :return: The netmask of this HostBatchCreateIfaceInput.  # noqa: E501
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this HostBatchCreateIfaceInput.


        :param netmask: The netmask of this HostBatchCreateIfaceInput.  # noqa: E501
        :type netmask: str
        """
        if self.local_vars_configuration.client_side_validation and netmask is None:  # noqa: E501
            raise ValueError("Invalid value for `netmask`, must not be `None`")  # noqa: E501

        self._netmask = netmask

    @property
    def name(self):
        """Gets the name of this HostBatchCreateIfaceInput.  # noqa: E501


        :return: The name of this HostBatchCreateIfaceInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HostBatchCreateIfaceInput.


        :param name: The name of this HostBatchCreateIfaceInput.  # noqa: E501
        :type name: list[str]
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def ip(self):
        """Gets the ip of this HostBatchCreateIfaceInput.  # noqa: E501


        :return: The ip of this HostBatchCreateIfaceInput.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this HostBatchCreateIfaceInput.


        :param ip: The ip of this HostBatchCreateIfaceInput.  # noqa: E501
        :type ip: str
        """
        if self.local_vars_configuration.client_side_validation and ip is None:  # noqa: E501
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def function(self):
        """Gets the function of this HostBatchCreateIfaceInput.  # noqa: E501


        :return: The function of this HostBatchCreateIfaceInput.  # noqa: E501
        :rtype: HostBatchCreateIfaceFunction
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this HostBatchCreateIfaceInput.


        :param function: The function of this HostBatchCreateIfaceInput.  # noqa: E501
        :type function: HostBatchCreateIfaceFunction
        """
        if self.local_vars_configuration.client_side_validation and function is None:  # noqa: E501
            raise ValueError("Invalid value for `function`, must not be `None`")  # noqa: E501

        self._function = function

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
        if not isinstance(other, HostBatchCreateIfaceInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HostBatchCreateIfaceInput):
            return True

        return self.to_dict() != other.to_dict()
