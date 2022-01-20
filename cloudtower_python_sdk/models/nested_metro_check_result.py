# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 1.9.0
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


class NestedMetroCheckResult(object):
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
        'critical': 'int',
        'info': 'int',
        'items': 'list[NestedMetroCheckItem]',
        'notice': 'int',
        'status': 'MetroCheckStatusEnum'
    }

    attribute_map = {
        'critical': 'critical',
        'info': 'info',
        'items': 'items',
        'notice': 'notice',
        'status': 'status'
    }

    def __init__(self, critical=None, info=None, items=None, notice=None, status=None, local_vars_configuration=None):  # noqa: E501
        """NestedMetroCheckResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._critical = None
        self._info = None
        self._items = None
        self._notice = None
        self._status = None
        self.discriminator = None

        self.critical = critical
        self.info = info
        self.items = items
        self.notice = notice
        self.status = status

    @property
    def critical(self):
        """Gets the critical of this NestedMetroCheckResult.  # noqa: E501


        :return: The critical of this NestedMetroCheckResult.  # noqa: E501
        :rtype: int
        """
        return self._critical

    @critical.setter
    def critical(self, critical):
        """Sets the critical of this NestedMetroCheckResult.


        :param critical: The critical of this NestedMetroCheckResult.  # noqa: E501
        :type critical: int
        """
        if self.local_vars_configuration.client_side_validation and critical is None:  # noqa: E501
            raise ValueError("Invalid value for `critical`, must not be `None`")  # noqa: E501

        self._critical = critical

    @property
    def info(self):
        """Gets the info of this NestedMetroCheckResult.  # noqa: E501


        :return: The info of this NestedMetroCheckResult.  # noqa: E501
        :rtype: int
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this NestedMetroCheckResult.


        :param info: The info of this NestedMetroCheckResult.  # noqa: E501
        :type info: int
        """
        if self.local_vars_configuration.client_side_validation and info is None:  # noqa: E501
            raise ValueError("Invalid value for `info`, must not be `None`")  # noqa: E501

        self._info = info

    @property
    def items(self):
        """Gets the items of this NestedMetroCheckResult.  # noqa: E501


        :return: The items of this NestedMetroCheckResult.  # noqa: E501
        :rtype: list[NestedMetroCheckItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this NestedMetroCheckResult.


        :param items: The items of this NestedMetroCheckResult.  # noqa: E501
        :type items: list[NestedMetroCheckItem]
        """
        if self.local_vars_configuration.client_side_validation and items is None:  # noqa: E501
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

    @property
    def notice(self):
        """Gets the notice of this NestedMetroCheckResult.  # noqa: E501


        :return: The notice of this NestedMetroCheckResult.  # noqa: E501
        :rtype: int
        """
        return self._notice

    @notice.setter
    def notice(self, notice):
        """Sets the notice of this NestedMetroCheckResult.


        :param notice: The notice of this NestedMetroCheckResult.  # noqa: E501
        :type notice: int
        """
        if self.local_vars_configuration.client_side_validation and notice is None:  # noqa: E501
            raise ValueError("Invalid value for `notice`, must not be `None`")  # noqa: E501

        self._notice = notice

    @property
    def status(self):
        """Gets the status of this NestedMetroCheckResult.  # noqa: E501


        :return: The status of this NestedMetroCheckResult.  # noqa: E501
        :rtype: MetroCheckStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NestedMetroCheckResult.


        :param status: The status of this NestedMetroCheckResult.  # noqa: E501
        :type status: MetroCheckStatusEnum
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if not isinstance(other, NestedMetroCheckResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedMetroCheckResult):
            return True

        return self.to_dict() != other.to_dict()
