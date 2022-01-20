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


class SnapshotGroupCloneParamsClone(object):
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
        'from_source_vm_id': 'str',
        'to_cloned_vm_name': 'str'
    }

    attribute_map = {
        'from_source_vm_id': 'from_source_vm_id',
        'to_cloned_vm_name': 'to_cloned_vm_name'
    }

    def __init__(self, from_source_vm_id=None, to_cloned_vm_name=None, local_vars_configuration=None):  # noqa: E501
        """SnapshotGroupCloneParamsClone - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._from_source_vm_id = None
        self._to_cloned_vm_name = None
        self.discriminator = None

        self.from_source_vm_id = from_source_vm_id
        self.to_cloned_vm_name = to_cloned_vm_name

    @property
    def from_source_vm_id(self):
        """Gets the from_source_vm_id of this SnapshotGroupCloneParamsClone.  # noqa: E501


        :return: The from_source_vm_id of this SnapshotGroupCloneParamsClone.  # noqa: E501
        :rtype: str
        """
        return self._from_source_vm_id

    @from_source_vm_id.setter
    def from_source_vm_id(self, from_source_vm_id):
        """Sets the from_source_vm_id of this SnapshotGroupCloneParamsClone.


        :param from_source_vm_id: The from_source_vm_id of this SnapshotGroupCloneParamsClone.  # noqa: E501
        :type from_source_vm_id: str
        """
        if self.local_vars_configuration.client_side_validation and from_source_vm_id is None:  # noqa: E501
            raise ValueError("Invalid value for `from_source_vm_id`, must not be `None`")  # noqa: E501

        self._from_source_vm_id = from_source_vm_id

    @property
    def to_cloned_vm_name(self):
        """Gets the to_cloned_vm_name of this SnapshotGroupCloneParamsClone.  # noqa: E501


        :return: The to_cloned_vm_name of this SnapshotGroupCloneParamsClone.  # noqa: E501
        :rtype: str
        """
        return self._to_cloned_vm_name

    @to_cloned_vm_name.setter
    def to_cloned_vm_name(self, to_cloned_vm_name):
        """Sets the to_cloned_vm_name of this SnapshotGroupCloneParamsClone.


        :param to_cloned_vm_name: The to_cloned_vm_name of this SnapshotGroupCloneParamsClone.  # noqa: E501
        :type to_cloned_vm_name: str
        """
        if self.local_vars_configuration.client_side_validation and to_cloned_vm_name is None:  # noqa: E501
            raise ValueError("Invalid value for `to_cloned_vm_name`, must not be `None`")  # noqa: E501

        self._to_cloned_vm_name = to_cloned_vm_name

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
        if not isinstance(other, SnapshotGroupCloneParamsClone):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnapshotGroupCloneParamsClone):
            return True

        return self.to_dict() != other.to_dict()
