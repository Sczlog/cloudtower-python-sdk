# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class LogServiceConfig(object):
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
        'group_name': 'str',
        'service_list': 'list[str]'
    }

    attribute_map = {
        'group_name': 'group_name',
        'service_list': 'service_list'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """LogServiceConfig - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._group_name = None
        self._service_list = None
        self.discriminator = None

        if "group_name" in kwargs:
            self.group_name = kwargs["group_name"]
        if "service_list" in kwargs:
            self.service_list = kwargs["service_list"]

    @property
    def group_name(self):
        """Gets the group_name of this LogServiceConfig.  # noqa: E501


        :return: The group_name of this LogServiceConfig.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this LogServiceConfig.


        :param group_name: The group_name of this LogServiceConfig.  # noqa: E501
        :type group_name: str
        """
        if self.local_vars_configuration.client_side_validation and group_name is None:  # noqa: E501
            raise ValueError("Invalid value for `group_name`, must not be `None`")  # noqa: E501

        self._group_name = group_name

    @property
    def service_list(self):
        """Gets the service_list of this LogServiceConfig.  # noqa: E501


        :return: The service_list of this LogServiceConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._service_list

    @service_list.setter
    def service_list(self, service_list):
        """Sets the service_list of this LogServiceConfig.


        :param service_list: The service_list of this LogServiceConfig.  # noqa: E501
        :type service_list: list[str]
        """
        if self.local_vars_configuration.client_side_validation and service_list is None:  # noqa: E501
            raise ValueError("Invalid value for `service_list`, must not be `None`")  # noqa: E501

        self._service_list = service_list

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
        if not isinstance(other, LogServiceConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LogServiceConfig):
            return True

        return self.to_dict() != other.to_dict()
