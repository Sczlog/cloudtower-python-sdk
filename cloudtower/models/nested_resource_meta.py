# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 1.10.0
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


class NestedResourceMeta(object):
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
        'fields': 'list[str]',
        'filter': 'object',
        'name': 'str',
        'type': 'ReportResourceInputEnum'
    }

    attribute_map = {
        'fields': 'fields',
        'filter': 'filter',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedResourceMeta - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._fields = None
        self._filter = None
        self._name = None
        self._type = None
        self.discriminator = None

        if "fields" in kwargs:
            self.fields = kwargs["fields"]
        if "filter" in kwargs:
            self.filter = kwargs["filter"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "type" in kwargs:
            self.type = kwargs["type"]

    @property
    def fields(self):
        """Gets the fields of this NestedResourceMeta.  # noqa: E501


        :return: The fields of this NestedResourceMeta.  # noqa: E501
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this NestedResourceMeta.


        :param fields: The fields of this NestedResourceMeta.  # noqa: E501
        :type fields: list[str]
        """
        if self.local_vars_configuration.client_side_validation and fields is None:  # noqa: E501
            raise ValueError("Invalid value for `fields`, must not be `None`")  # noqa: E501

        self._fields = fields

    @property
    def filter(self):
        """Gets the filter of this NestedResourceMeta.  # noqa: E501


        :return: The filter of this NestedResourceMeta.  # noqa: E501
        :rtype: object
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this NestedResourceMeta.


        :param filter: The filter of this NestedResourceMeta.  # noqa: E501
        :type filter: object
        """
        if self.local_vars_configuration.client_side_validation and filter is None:  # noqa: E501
            raise ValueError("Invalid value for `filter`, must not be `None`")  # noqa: E501

        self._filter = filter

    @property
    def name(self):
        """Gets the name of this NestedResourceMeta.  # noqa: E501


        :return: The name of this NestedResourceMeta.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NestedResourceMeta.


        :param name: The name of this NestedResourceMeta.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this NestedResourceMeta.  # noqa: E501


        :return: The type of this NestedResourceMeta.  # noqa: E501
        :rtype: ReportResourceInputEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NestedResourceMeta.


        :param type: The type of this NestedResourceMeta.  # noqa: E501
        :type type: ReportResourceInputEnum
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, NestedResourceMeta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedResourceMeta):
            return True

        return self.to_dict() != other.to_dict()
