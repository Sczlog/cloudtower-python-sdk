# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.1.0
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


class NestedTagPosition(object):
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
        'column': 'int',
        'row': 'int',
        'tag': 'str'
    }

    attribute_map = {
        'column': 'column',
        'row': 'row',
        'tag': 'tag'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedTagPosition - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._column = None
        self._row = None
        self._tag = None
        self.discriminator = None

        if "column" in kwargs:
            self.column = kwargs["column"]
        if "row" in kwargs:
            self.row = kwargs["row"]
        if "tag" in kwargs:
            self.tag = kwargs["tag"]

    @property
    def column(self):
        """Gets the column of this NestedTagPosition.  # noqa: E501


        :return: The column of this NestedTagPosition.  # noqa: E501
        :rtype: int
        """
        return self._column

    @column.setter
    def column(self, column):
        """Sets the column of this NestedTagPosition.


        :param column: The column of this NestedTagPosition.  # noqa: E501
        :type column: int
        """
        if self.local_vars_configuration.client_side_validation and column is None:  # noqa: E501
            raise ValueError("Invalid value for `column`, must not be `None`")  # noqa: E501

        self._column = column

    @property
    def row(self):
        """Gets the row of this NestedTagPosition.  # noqa: E501


        :return: The row of this NestedTagPosition.  # noqa: E501
        :rtype: int
        """
        return self._row

    @row.setter
    def row(self, row):
        """Sets the row of this NestedTagPosition.


        :param row: The row of this NestedTagPosition.  # noqa: E501
        :type row: int
        """
        if self.local_vars_configuration.client_side_validation and row is None:  # noqa: E501
            raise ValueError("Invalid value for `row`, must not be `None`")  # noqa: E501

        self._row = row

    @property
    def tag(self):
        """Gets the tag of this NestedTagPosition.  # noqa: E501


        :return: The tag of this NestedTagPosition.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this NestedTagPosition.


        :param tag: The tag of this NestedTagPosition.  # noqa: E501
        :type tag: str
        """
        if self.local_vars_configuration.client_side_validation and tag is None:  # noqa: E501
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

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
        if not isinstance(other, NestedTagPosition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedTagPosition):
            return True

        return self.to_dict() != other.to_dict()
