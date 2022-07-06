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


class IscsiLunSnapshot(object):
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
        'consistency_group_snapshot': 'NestedConsistencyGroupSnapshot',
        'entity_async_status': 'EntityAsyncStatus',
        'id': 'str',
        'iscsi_lun': 'NestedIscsiLun',
        'iscsi_target': 'NestedIscsiTarget',
        'labels': 'list[NestedLabel]',
        'local_created_at': 'str',
        'local_id': 'str',
        'name': 'str',
        'unique_size': 'int'
    }

    attribute_map = {
        'consistency_group_snapshot': 'consistency_group_snapshot',
        'entity_async_status': 'entityAsyncStatus',
        'id': 'id',
        'iscsi_lun': 'iscsi_lun',
        'iscsi_target': 'iscsi_target',
        'labels': 'labels',
        'local_created_at': 'local_created_at',
        'local_id': 'local_id',
        'name': 'name',
        'unique_size': 'unique_size'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """IscsiLunSnapshot - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._consistency_group_snapshot = None
        self._entity_async_status = None
        self._id = None
        self._iscsi_lun = None
        self._iscsi_target = None
        self._labels = None
        self._local_created_at = None
        self._local_id = None
        self._name = None
        self._unique_size = None
        self.discriminator = None

        self.consistency_group_snapshot = kwargs.get("consistency_group_snapshot", None)
        self.entity_async_status = kwargs.get("entity_async_status", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        self.iscsi_lun = kwargs.get("iscsi_lun", None)
        if "iscsi_target" in kwargs:
            self.iscsi_target = kwargs["iscsi_target"]
        self.labels = kwargs.get("labels", None)
        if "local_created_at" in kwargs:
            self.local_created_at = kwargs["local_created_at"]
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "unique_size" in kwargs:
            self.unique_size = kwargs["unique_size"]

    @property
    def consistency_group_snapshot(self):
        """Gets the consistency_group_snapshot of this IscsiLunSnapshot.  # noqa: E501


        :return: The consistency_group_snapshot of this IscsiLunSnapshot.  # noqa: E501
        :rtype: NestedConsistencyGroupSnapshot
        """
        return self._consistency_group_snapshot

    @consistency_group_snapshot.setter
    def consistency_group_snapshot(self, consistency_group_snapshot):
        """Sets the consistency_group_snapshot of this IscsiLunSnapshot.


        :param consistency_group_snapshot: The consistency_group_snapshot of this IscsiLunSnapshot.  # noqa: E501
        :type consistency_group_snapshot: NestedConsistencyGroupSnapshot
        """

        self._consistency_group_snapshot = consistency_group_snapshot

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this IscsiLunSnapshot.  # noqa: E501


        :return: The entity_async_status of this IscsiLunSnapshot.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this IscsiLunSnapshot.


        :param entity_async_status: The entity_async_status of this IscsiLunSnapshot.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def id(self):
        """Gets the id of this IscsiLunSnapshot.  # noqa: E501


        :return: The id of this IscsiLunSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IscsiLunSnapshot.


        :param id: The id of this IscsiLunSnapshot.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def iscsi_lun(self):
        """Gets the iscsi_lun of this IscsiLunSnapshot.  # noqa: E501


        :return: The iscsi_lun of this IscsiLunSnapshot.  # noqa: E501
        :rtype: NestedIscsiLun
        """
        return self._iscsi_lun

    @iscsi_lun.setter
    def iscsi_lun(self, iscsi_lun):
        """Sets the iscsi_lun of this IscsiLunSnapshot.


        :param iscsi_lun: The iscsi_lun of this IscsiLunSnapshot.  # noqa: E501
        :type iscsi_lun: NestedIscsiLun
        """

        self._iscsi_lun = iscsi_lun

    @property
    def iscsi_target(self):
        """Gets the iscsi_target of this IscsiLunSnapshot.  # noqa: E501


        :return: The iscsi_target of this IscsiLunSnapshot.  # noqa: E501
        :rtype: NestedIscsiTarget
        """
        return self._iscsi_target

    @iscsi_target.setter
    def iscsi_target(self, iscsi_target):
        """Sets the iscsi_target of this IscsiLunSnapshot.


        :param iscsi_target: The iscsi_target of this IscsiLunSnapshot.  # noqa: E501
        :type iscsi_target: NestedIscsiTarget
        """
        if self.local_vars_configuration.client_side_validation and iscsi_target is None:  # noqa: E501
            raise ValueError("Invalid value for `iscsi_target`, must not be `None`")  # noqa: E501

        self._iscsi_target = iscsi_target

    @property
    def labels(self):
        """Gets the labels of this IscsiLunSnapshot.  # noqa: E501


        :return: The labels of this IscsiLunSnapshot.  # noqa: E501
        :rtype: list[NestedLabel]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this IscsiLunSnapshot.


        :param labels: The labels of this IscsiLunSnapshot.  # noqa: E501
        :type labels: list[NestedLabel]
        """

        self._labels = labels

    @property
    def local_created_at(self):
        """Gets the local_created_at of this IscsiLunSnapshot.  # noqa: E501


        :return: The local_created_at of this IscsiLunSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._local_created_at

    @local_created_at.setter
    def local_created_at(self, local_created_at):
        """Sets the local_created_at of this IscsiLunSnapshot.


        :param local_created_at: The local_created_at of this IscsiLunSnapshot.  # noqa: E501
        :type local_created_at: str
        """
        if self.local_vars_configuration.client_side_validation and local_created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `local_created_at`, must not be `None`")  # noqa: E501

        self._local_created_at = local_created_at

    @property
    def local_id(self):
        """Gets the local_id of this IscsiLunSnapshot.  # noqa: E501


        :return: The local_id of this IscsiLunSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this IscsiLunSnapshot.


        :param local_id: The local_id of this IscsiLunSnapshot.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def name(self):
        """Gets the name of this IscsiLunSnapshot.  # noqa: E501


        :return: The name of this IscsiLunSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IscsiLunSnapshot.


        :param name: The name of this IscsiLunSnapshot.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def unique_size(self):
        """Gets the unique_size of this IscsiLunSnapshot.  # noqa: E501


        :return: The unique_size of this IscsiLunSnapshot.  # noqa: E501
        :rtype: int
        """
        return self._unique_size

    @unique_size.setter
    def unique_size(self, unique_size):
        """Sets the unique_size of this IscsiLunSnapshot.


        :param unique_size: The unique_size of this IscsiLunSnapshot.  # noqa: E501
        :type unique_size: int
        """
        if self.local_vars_configuration.client_side_validation and unique_size is None:  # noqa: E501
            raise ValueError("Invalid value for `unique_size`, must not be `None`")  # noqa: E501

        self._unique_size = unique_size

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
        if not isinstance(other, IscsiLunSnapshot):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IscsiLunSnapshot):
            return True

        return self.to_dict() != other.to_dict()
