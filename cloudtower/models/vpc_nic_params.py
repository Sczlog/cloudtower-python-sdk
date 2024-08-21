# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VpcNicParams(object):
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
        'ip_addresses': 'list[str]',
        'floating_ip_id': 'str',
        'vpc_subnet_id': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'ip_addresses': 'ip_addresses',
        'floating_ip_id': 'floating_ip_id',
        'vpc_subnet_id': 'vpc_subnet_id',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VpcNicParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._ip_addresses = None
        self._floating_ip_id = None
        self._vpc_subnet_id = None
        self._vpc_id = None
        self.discriminator = None

        if "ip_addresses" in kwargs:
            self.ip_addresses = kwargs["ip_addresses"]
        if "floating_ip_id" in kwargs:
            self.floating_ip_id = kwargs["floating_ip_id"]
        if "vpc_subnet_id" in kwargs:
            self.vpc_subnet_id = kwargs["vpc_subnet_id"]
        if "vpc_id" in kwargs:
            self.vpc_id = kwargs["vpc_id"]

    @property
    def ip_addresses(self):
        """Gets the ip_addresses of this VpcNicParams.  # noqa: E501


        :return: The ip_addresses of this VpcNicParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """Sets the ip_addresses of this VpcNicParams.


        :param ip_addresses: The ip_addresses of this VpcNicParams.  # noqa: E501
        :type ip_addresses: list[str]
        """

        self._ip_addresses = ip_addresses

    @property
    def floating_ip_id(self):
        """Gets the floating_ip_id of this VpcNicParams.  # noqa: E501


        :return: The floating_ip_id of this VpcNicParams.  # noqa: E501
        :rtype: str
        """
        return self._floating_ip_id

    @floating_ip_id.setter
    def floating_ip_id(self, floating_ip_id):
        """Sets the floating_ip_id of this VpcNicParams.


        :param floating_ip_id: The floating_ip_id of this VpcNicParams.  # noqa: E501
        :type floating_ip_id: str
        """

        self._floating_ip_id = floating_ip_id

    @property
    def vpc_subnet_id(self):
        """Gets the vpc_subnet_id of this VpcNicParams.  # noqa: E501


        :return: The vpc_subnet_id of this VpcNicParams.  # noqa: E501
        :rtype: str
        """
        return self._vpc_subnet_id

    @vpc_subnet_id.setter
    def vpc_subnet_id(self, vpc_subnet_id):
        """Sets the vpc_subnet_id of this VpcNicParams.


        :param vpc_subnet_id: The vpc_subnet_id of this VpcNicParams.  # noqa: E501
        :type vpc_subnet_id: str
        """
        if self.local_vars_configuration.client_side_validation and vpc_subnet_id is None:  # noqa: E501
            raise ValueError("Invalid value for `vpc_subnet_id`, must not be `None`")  # noqa: E501

        self._vpc_subnet_id = vpc_subnet_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this VpcNicParams.  # noqa: E501


        :return: The vpc_id of this VpcNicParams.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this VpcNicParams.


        :param vpc_id: The vpc_id of this VpcNicParams.  # noqa: E501
        :type vpc_id: str
        """
        if self.local_vars_configuration.client_side_validation and vpc_id is None:  # noqa: E501
            raise ValueError("Invalid value for `vpc_id`, must not be `None`")  # noqa: E501

        self._vpc_id = vpc_id

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
        if not isinstance(other, VpcNicParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VpcNicParams):
            return True

        return self.to_dict() != other.to_dict()
