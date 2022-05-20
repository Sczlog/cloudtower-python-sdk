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


class IscsiLunRollbackParams(object):
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
        'lun_id': 'str',
        'snapshot_id': 'str'
    }

    attribute_map = {
        'lun_id': 'lun_id',
        'snapshot_id': 'snapshot_id'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """IscsiLunRollbackParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._lun_id = None
        self._snapshot_id = None
        self.discriminator = None

        if "lun_id" in kwargs:
            self.lun_id = kwargs["lun_id"]
        if "snapshot_id" in kwargs:
            self.snapshot_id = kwargs["snapshot_id"]

    @property
    def lun_id(self):
        """Gets the lun_id of this IscsiLunRollbackParams.  # noqa: E501


        :return: The lun_id of this IscsiLunRollbackParams.  # noqa: E501
        :rtype: str
        """
        return self._lun_id

    @lun_id.setter
    def lun_id(self, lun_id):
        """Sets the lun_id of this IscsiLunRollbackParams.


        :param lun_id: The lun_id of this IscsiLunRollbackParams.  # noqa: E501
        :type lun_id: str
        """
        if self.local_vars_configuration.client_side_validation and lun_id is None:  # noqa: E501
            raise ValueError("Invalid value for `lun_id`, must not be `None`")  # noqa: E501

        self._lun_id = lun_id

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this IscsiLunRollbackParams.  # noqa: E501


        :return: The snapshot_id of this IscsiLunRollbackParams.  # noqa: E501
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this IscsiLunRollbackParams.


        :param snapshot_id: The snapshot_id of this IscsiLunRollbackParams.  # noqa: E501
        :type snapshot_id: str
        """
        if self.local_vars_configuration.client_side_validation and snapshot_id is None:  # noqa: E501
            raise ValueError("Invalid value for `snapshot_id`, must not be `None`")  # noqa: E501

        self._snapshot_id = snapshot_id

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
        if not isinstance(other, IscsiLunRollbackParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IscsiLunRollbackParams):
            return True

        return self.to_dict() != other.to_dict()
