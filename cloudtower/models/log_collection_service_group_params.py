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


class LogCollectionServiceGroupParams(object):
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
        'services': 'list[str]',
        'group_name': 'str'
    }

    attribute_map = {
        'services': 'services',
        'group_name': 'group_name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """LogCollectionServiceGroupParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._services = None
        self._group_name = None
        self.discriminator = None

        if "services" in kwargs:
            self.services = kwargs["services"]
        if "group_name" in kwargs:
            self.group_name = kwargs["group_name"]

    @property
    def services(self):
        """Gets the services of this LogCollectionServiceGroupParams.  # noqa: E501


        :return: The services of this LogCollectionServiceGroupParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this LogCollectionServiceGroupParams.


        :param services: The services of this LogCollectionServiceGroupParams.  # noqa: E501
        :type services: list[str]
        """

        self._services = services

    @property
    def group_name(self):
        """Gets the group_name of this LogCollectionServiceGroupParams.  # noqa: E501


        :return: The group_name of this LogCollectionServiceGroupParams.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this LogCollectionServiceGroupParams.


        :param group_name: The group_name of this LogCollectionServiceGroupParams.  # noqa: E501
        :type group_name: str
        """
        if self.local_vars_configuration.client_side_validation and group_name is None:  # noqa: E501
            raise ValueError("Invalid value for `group_name`, must not be `None`")  # noqa: E501

        self._group_name = group_name

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
        if not isinstance(other, LogCollectionServiceGroupParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LogCollectionServiceGroupParams):
            return True

        return self.to_dict() != other.to_dict()
