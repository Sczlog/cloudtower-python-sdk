# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class IscsiLunDeletionParamsData(object):
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
        'remove_snapshot': 'bool'
    }

    attribute_map = {
        'remove_snapshot': 'remove_snapshot'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """IscsiLunDeletionParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._remove_snapshot = None
        self.discriminator = None

        if "remove_snapshot" in kwargs:
            self.remove_snapshot = kwargs["remove_snapshot"]

    @property
    def remove_snapshot(self):
        """Gets the remove_snapshot of this IscsiLunDeletionParamsData.  # noqa: E501


        :return: The remove_snapshot of this IscsiLunDeletionParamsData.  # noqa: E501
        :rtype: bool
        """
        return self._remove_snapshot

    @remove_snapshot.setter
    def remove_snapshot(self, remove_snapshot):
        """Sets the remove_snapshot of this IscsiLunDeletionParamsData.


        :param remove_snapshot: The remove_snapshot of this IscsiLunDeletionParamsData.  # noqa: E501
        :type remove_snapshot: bool
        """
        if self.local_vars_configuration.client_side_validation and remove_snapshot is None:  # noqa: E501
            raise ValueError("Invalid value for `remove_snapshot`, must not be `None`")  # noqa: E501

        self._remove_snapshot = remove_snapshot

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
        if not isinstance(other, IscsiLunDeletionParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IscsiLunDeletionParamsData):
            return True

        return self.to_dict() != other.to_dict()
