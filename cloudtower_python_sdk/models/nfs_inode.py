# coding: utf-8

"""
    Tower SDK API

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 1.8.0
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


class NfsInode(object):
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
        'assigned_size': 'float',
        'entity_async_status': 'EntityAsyncStatus',
        'file': 'bool',
        'id': 'str',
        'labels': 'list[NestedLabel]',
        'local_id': 'str',
        'local_updated_at': 'str',
        'name': 'str',
        'nfs_export': 'NestedNfsExport',
        'parent_id': 'str',
        'shared_size': 'float',
        'snapshot_num': 'int',
        'unique_size': 'float'
    }

    attribute_map = {
        'assigned_size': 'assigned_size',
        'entity_async_status': 'entityAsyncStatus',
        'file': 'file',
        'id': 'id',
        'labels': 'labels',
        'local_id': 'local_id',
        'local_updated_at': 'local_updated_at',
        'name': 'name',
        'nfs_export': 'nfs_export',
        'parent_id': 'parent_id',
        'shared_size': 'shared_size',
        'snapshot_num': 'snapshot_num',
        'unique_size': 'unique_size'
    }

    def __init__(self, assigned_size=None, entity_async_status=None, file=None, id=None, labels=None, local_id=None, local_updated_at=None, name=None, nfs_export=None, parent_id=None, shared_size=None, snapshot_num=None, unique_size=None, local_vars_configuration=None):  # noqa: E501
        """NfsInode - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._assigned_size = None
        self._entity_async_status = None
        self._file = None
        self._id = None
        self._labels = None
        self._local_id = None
        self._local_updated_at = None
        self._name = None
        self._nfs_export = None
        self._parent_id = None
        self._shared_size = None
        self._snapshot_num = None
        self._unique_size = None
        self.discriminator = None

        self.assigned_size = assigned_size
        self.entity_async_status = entity_async_status
        self.file = file
        self.id = id
        self.labels = labels
        self.local_id = local_id
        self.local_updated_at = local_updated_at
        self.name = name
        self.nfs_export = nfs_export
        self.parent_id = parent_id
        self.shared_size = shared_size
        self.snapshot_num = snapshot_num
        self.unique_size = unique_size

    @property
    def assigned_size(self):
        """Gets the assigned_size of this NfsInode.  # noqa: E501


        :return: The assigned_size of this NfsInode.  # noqa: E501
        :rtype: float
        """
        return self._assigned_size

    @assigned_size.setter
    def assigned_size(self, assigned_size):
        """Sets the assigned_size of this NfsInode.


        :param assigned_size: The assigned_size of this NfsInode.  # noqa: E501
        :type assigned_size: float
        """
        if self.local_vars_configuration.client_side_validation and assigned_size is None:  # noqa: E501
            raise ValueError("Invalid value for `assigned_size`, must not be `None`")  # noqa: E501

        self._assigned_size = assigned_size

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this NfsInode.  # noqa: E501


        :return: The entity_async_status of this NfsInode.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this NfsInode.


        :param entity_async_status: The entity_async_status of this NfsInode.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def file(self):
        """Gets the file of this NfsInode.  # noqa: E501


        :return: The file of this NfsInode.  # noqa: E501
        :rtype: bool
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this NfsInode.


        :param file: The file of this NfsInode.  # noqa: E501
        :type file: bool
        """
        if self.local_vars_configuration.client_side_validation and file is None:  # noqa: E501
            raise ValueError("Invalid value for `file`, must not be `None`")  # noqa: E501

        self._file = file

    @property
    def id(self):
        """Gets the id of this NfsInode.  # noqa: E501


        :return: The id of this NfsInode.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NfsInode.


        :param id: The id of this NfsInode.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def labels(self):
        """Gets the labels of this NfsInode.  # noqa: E501


        :return: The labels of this NfsInode.  # noqa: E501
        :rtype: list[NestedLabel]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this NfsInode.


        :param labels: The labels of this NfsInode.  # noqa: E501
        :type labels: list[NestedLabel]
        """

        self._labels = labels

    @property
    def local_id(self):
        """Gets the local_id of this NfsInode.  # noqa: E501


        :return: The local_id of this NfsInode.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this NfsInode.


        :param local_id: The local_id of this NfsInode.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def local_updated_at(self):
        """Gets the local_updated_at of this NfsInode.  # noqa: E501


        :return: The local_updated_at of this NfsInode.  # noqa: E501
        :rtype: str
        """
        return self._local_updated_at

    @local_updated_at.setter
    def local_updated_at(self, local_updated_at):
        """Sets the local_updated_at of this NfsInode.


        :param local_updated_at: The local_updated_at of this NfsInode.  # noqa: E501
        :type local_updated_at: str
        """
        if self.local_vars_configuration.client_side_validation and local_updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `local_updated_at`, must not be `None`")  # noqa: E501

        self._local_updated_at = local_updated_at

    @property
    def name(self):
        """Gets the name of this NfsInode.  # noqa: E501


        :return: The name of this NfsInode.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NfsInode.


        :param name: The name of this NfsInode.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def nfs_export(self):
        """Gets the nfs_export of this NfsInode.  # noqa: E501


        :return: The nfs_export of this NfsInode.  # noqa: E501
        :rtype: NestedNfsExport
        """
        return self._nfs_export

    @nfs_export.setter
    def nfs_export(self, nfs_export):
        """Sets the nfs_export of this NfsInode.


        :param nfs_export: The nfs_export of this NfsInode.  # noqa: E501
        :type nfs_export: NestedNfsExport
        """
        if self.local_vars_configuration.client_side_validation and nfs_export is None:  # noqa: E501
            raise ValueError("Invalid value for `nfs_export`, must not be `None`")  # noqa: E501

        self._nfs_export = nfs_export

    @property
    def parent_id(self):
        """Gets the parent_id of this NfsInode.  # noqa: E501


        :return: The parent_id of this NfsInode.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this NfsInode.


        :param parent_id: The parent_id of this NfsInode.  # noqa: E501
        :type parent_id: str
        """
        if self.local_vars_configuration.client_side_validation and parent_id is None:  # noqa: E501
            raise ValueError("Invalid value for `parent_id`, must not be `None`")  # noqa: E501

        self._parent_id = parent_id

    @property
    def shared_size(self):
        """Gets the shared_size of this NfsInode.  # noqa: E501


        :return: The shared_size of this NfsInode.  # noqa: E501
        :rtype: float
        """
        return self._shared_size

    @shared_size.setter
    def shared_size(self, shared_size):
        """Sets the shared_size of this NfsInode.


        :param shared_size: The shared_size of this NfsInode.  # noqa: E501
        :type shared_size: float
        """
        if self.local_vars_configuration.client_side_validation and shared_size is None:  # noqa: E501
            raise ValueError("Invalid value for `shared_size`, must not be `None`")  # noqa: E501

        self._shared_size = shared_size

    @property
    def snapshot_num(self):
        """Gets the snapshot_num of this NfsInode.  # noqa: E501


        :return: The snapshot_num of this NfsInode.  # noqa: E501
        :rtype: int
        """
        return self._snapshot_num

    @snapshot_num.setter
    def snapshot_num(self, snapshot_num):
        """Sets the snapshot_num of this NfsInode.


        :param snapshot_num: The snapshot_num of this NfsInode.  # noqa: E501
        :type snapshot_num: int
        """
        if self.local_vars_configuration.client_side_validation and snapshot_num is None:  # noqa: E501
            raise ValueError("Invalid value for `snapshot_num`, must not be `None`")  # noqa: E501

        self._snapshot_num = snapshot_num

    @property
    def unique_size(self):
        """Gets the unique_size of this NfsInode.  # noqa: E501


        :return: The unique_size of this NfsInode.  # noqa: E501
        :rtype: float
        """
        return self._unique_size

    @unique_size.setter
    def unique_size(self, unique_size):
        """Sets the unique_size of this NfsInode.


        :param unique_size: The unique_size of this NfsInode.  # noqa: E501
        :type unique_size: float
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
        if not isinstance(other, NfsInode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NfsInode):
            return True

        return self.to_dict() != other.to_dict()
