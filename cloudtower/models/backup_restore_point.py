# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class BackupRestorePoint(object):
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
        'backup_plan': 'NestedBackupPlan',
        'backup_restore_executions': 'list[NestedBackupRestoreExecution]',
        'backup_target_execution': 'NestedBackupTargetExecution',
        'cluster_local_id': 'str',
        'compressed': 'bool',
        'compression_ratio': 'float',
        'creation': 'BackupRestorePointCreation',
        'entity_async_status': 'EntityAsyncStatus',
        'id': 'str',
        'local_created_at': 'str',
        'local_id': 'str',
        'logical_size': 'int',
        'parent_restore_point': 'str',
        'physical_size': 'int',
        'size': 'int',
        'slice': 'str',
        'snapshot_consistent_type': 'ConsistentType',
        'type': 'BackupRestorePointType',
        'valid_capacity': 'int',
        'valid_size': 'int',
        'vm': 'NestedVm',
        'vm_local_id': 'str',
        'vm_name': 'str'
    }

    attribute_map = {
        'backup_plan': 'backup_plan',
        'backup_restore_executions': 'backup_restore_executions',
        'backup_target_execution': 'backup_target_execution',
        'cluster_local_id': 'cluster_local_id',
        'compressed': 'compressed',
        'compression_ratio': 'compression_ratio',
        'creation': 'creation',
        'entity_async_status': 'entityAsyncStatus',
        'id': 'id',
        'local_created_at': 'local_created_at',
        'local_id': 'local_id',
        'logical_size': 'logical_size',
        'parent_restore_point': 'parent_restore_point',
        'physical_size': 'physical_size',
        'size': 'size',
        'slice': 'slice',
        'snapshot_consistent_type': 'snapshot_consistent_type',
        'type': 'type',
        'valid_capacity': 'valid_capacity',
        'valid_size': 'valid_size',
        'vm': 'vm',
        'vm_local_id': 'vm_local_id',
        'vm_name': 'vm_name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """BackupRestorePoint - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._backup_plan = None
        self._backup_restore_executions = None
        self._backup_target_execution = None
        self._cluster_local_id = None
        self._compressed = None
        self._compression_ratio = None
        self._creation = None
        self._entity_async_status = None
        self._id = None
        self._local_created_at = None
        self._local_id = None
        self._logical_size = None
        self._parent_restore_point = None
        self._physical_size = None
        self._size = None
        self._slice = None
        self._snapshot_consistent_type = None
        self._type = None
        self._valid_capacity = None
        self._valid_size = None
        self._vm = None
        self._vm_local_id = None
        self._vm_name = None
        self.discriminator = None

        if "backup_plan" in kwargs:
            self.backup_plan = kwargs["backup_plan"]
        self.backup_restore_executions = kwargs.get("backup_restore_executions", None)
        if "backup_target_execution" in kwargs:
            self.backup_target_execution = kwargs["backup_target_execution"]
        self.cluster_local_id = kwargs.get("cluster_local_id", None)
        self.compressed = kwargs.get("compressed", None)
        self.compression_ratio = kwargs.get("compression_ratio", None)
        self.creation = kwargs.get("creation", None)
        self.entity_async_status = kwargs.get("entity_async_status", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        self.local_created_at = kwargs.get("local_created_at", None)
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        self.logical_size = kwargs.get("logical_size", None)
        self.parent_restore_point = kwargs.get("parent_restore_point", None)
        self.physical_size = kwargs.get("physical_size", None)
        self.size = kwargs.get("size", None)
        if "slice" in kwargs:
            self.slice = kwargs["slice"]
        self.snapshot_consistent_type = kwargs.get("snapshot_consistent_type", None)
        self.type = kwargs.get("type", None)
        self.valid_capacity = kwargs.get("valid_capacity", None)
        self.valid_size = kwargs.get("valid_size", None)
        self.vm = kwargs.get("vm", None)
        self.vm_local_id = kwargs.get("vm_local_id", None)
        self.vm_name = kwargs.get("vm_name", None)

    @property
    def backup_plan(self):
        """Gets the backup_plan of this BackupRestorePoint.  # noqa: E501


        :return: The backup_plan of this BackupRestorePoint.  # noqa: E501
        :rtype: NestedBackupPlan
        """
        return self._backup_plan

    @backup_plan.setter
    def backup_plan(self, backup_plan):
        """Sets the backup_plan of this BackupRestorePoint.


        :param backup_plan: The backup_plan of this BackupRestorePoint.  # noqa: E501
        :type backup_plan: NestedBackupPlan
        """
        if self.local_vars_configuration.client_side_validation and backup_plan is None:  # noqa: E501
            raise ValueError("Invalid value for `backup_plan`, must not be `None`")  # noqa: E501

        self._backup_plan = backup_plan

    @property
    def backup_restore_executions(self):
        """Gets the backup_restore_executions of this BackupRestorePoint.  # noqa: E501


        :return: The backup_restore_executions of this BackupRestorePoint.  # noqa: E501
        :rtype: list[NestedBackupRestoreExecution]
        """
        return self._backup_restore_executions

    @backup_restore_executions.setter
    def backup_restore_executions(self, backup_restore_executions):
        """Sets the backup_restore_executions of this BackupRestorePoint.


        :param backup_restore_executions: The backup_restore_executions of this BackupRestorePoint.  # noqa: E501
        :type backup_restore_executions: list[NestedBackupRestoreExecution]
        """

        self._backup_restore_executions = backup_restore_executions

    @property
    def backup_target_execution(self):
        """Gets the backup_target_execution of this BackupRestorePoint.  # noqa: E501


        :return: The backup_target_execution of this BackupRestorePoint.  # noqa: E501
        :rtype: NestedBackupTargetExecution
        """
        return self._backup_target_execution

    @backup_target_execution.setter
    def backup_target_execution(self, backup_target_execution):
        """Sets the backup_target_execution of this BackupRestorePoint.


        :param backup_target_execution: The backup_target_execution of this BackupRestorePoint.  # noqa: E501
        :type backup_target_execution: NestedBackupTargetExecution
        """
        if self.local_vars_configuration.client_side_validation and backup_target_execution is None:  # noqa: E501
            raise ValueError("Invalid value for `backup_target_execution`, must not be `None`")  # noqa: E501

        self._backup_target_execution = backup_target_execution

    @property
    def cluster_local_id(self):
        """Gets the cluster_local_id of this BackupRestorePoint.  # noqa: E501


        :return: The cluster_local_id of this BackupRestorePoint.  # noqa: E501
        :rtype: str
        """
        return self._cluster_local_id

    @cluster_local_id.setter
    def cluster_local_id(self, cluster_local_id):
        """Sets the cluster_local_id of this BackupRestorePoint.


        :param cluster_local_id: The cluster_local_id of this BackupRestorePoint.  # noqa: E501
        :type cluster_local_id: str
        """

        self._cluster_local_id = cluster_local_id

    @property
    def compressed(self):
        """Gets the compressed of this BackupRestorePoint.  # noqa: E501


        :return: The compressed of this BackupRestorePoint.  # noqa: E501
        :rtype: bool
        """
        return self._compressed

    @compressed.setter
    def compressed(self, compressed):
        """Sets the compressed of this BackupRestorePoint.


        :param compressed: The compressed of this BackupRestorePoint.  # noqa: E501
        :type compressed: bool
        """

        self._compressed = compressed

    @property
    def compression_ratio(self):
        """Gets the compression_ratio of this BackupRestorePoint.  # noqa: E501


        :return: The compression_ratio of this BackupRestorePoint.  # noqa: E501
        :rtype: float
        """
        return self._compression_ratio

    @compression_ratio.setter
    def compression_ratio(self, compression_ratio):
        """Sets the compression_ratio of this BackupRestorePoint.


        :param compression_ratio: The compression_ratio of this BackupRestorePoint.  # noqa: E501
        :type compression_ratio: float
        """

        self._compression_ratio = compression_ratio

    @property
    def creation(self):
        """Gets the creation of this BackupRestorePoint.  # noqa: E501


        :return: The creation of this BackupRestorePoint.  # noqa: E501
        :rtype: BackupRestorePointCreation
        """
        return self._creation

    @creation.setter
    def creation(self, creation):
        """Sets the creation of this BackupRestorePoint.


        :param creation: The creation of this BackupRestorePoint.  # noqa: E501
        :type creation: BackupRestorePointCreation
        """

        self._creation = creation

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this BackupRestorePoint.  # noqa: E501


        :return: The entity_async_status of this BackupRestorePoint.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this BackupRestorePoint.


        :param entity_async_status: The entity_async_status of this BackupRestorePoint.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def id(self):
        """Gets the id of this BackupRestorePoint.  # noqa: E501


        :return: The id of this BackupRestorePoint.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BackupRestorePoint.


        :param id: The id of this BackupRestorePoint.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def local_created_at(self):
        """Gets the local_created_at of this BackupRestorePoint.  # noqa: E501


        :return: The local_created_at of this BackupRestorePoint.  # noqa: E501
        :rtype: str
        """
        return self._local_created_at

    @local_created_at.setter
    def local_created_at(self, local_created_at):
        """Sets the local_created_at of this BackupRestorePoint.


        :param local_created_at: The local_created_at of this BackupRestorePoint.  # noqa: E501
        :type local_created_at: str
        """

        self._local_created_at = local_created_at

    @property
    def local_id(self):
        """Gets the local_id of this BackupRestorePoint.  # noqa: E501


        :return: The local_id of this BackupRestorePoint.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this BackupRestorePoint.


        :param local_id: The local_id of this BackupRestorePoint.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def logical_size(self):
        """Gets the logical_size of this BackupRestorePoint.  # noqa: E501


        :return: The logical_size of this BackupRestorePoint.  # noqa: E501
        :rtype: int
        """
        return self._logical_size

    @logical_size.setter
    def logical_size(self, logical_size):
        """Sets the logical_size of this BackupRestorePoint.


        :param logical_size: The logical_size of this BackupRestorePoint.  # noqa: E501
        :type logical_size: int
        """

        self._logical_size = logical_size

    @property
    def parent_restore_point(self):
        """Gets the parent_restore_point of this BackupRestorePoint.  # noqa: E501


        :return: The parent_restore_point of this BackupRestorePoint.  # noqa: E501
        :rtype: str
        """
        return self._parent_restore_point

    @parent_restore_point.setter
    def parent_restore_point(self, parent_restore_point):
        """Sets the parent_restore_point of this BackupRestorePoint.


        :param parent_restore_point: The parent_restore_point of this BackupRestorePoint.  # noqa: E501
        :type parent_restore_point: str
        """

        self._parent_restore_point = parent_restore_point

    @property
    def physical_size(self):
        """Gets the physical_size of this BackupRestorePoint.  # noqa: E501


        :return: The physical_size of this BackupRestorePoint.  # noqa: E501
        :rtype: int
        """
        return self._physical_size

    @physical_size.setter
    def physical_size(self, physical_size):
        """Sets the physical_size of this BackupRestorePoint.


        :param physical_size: The physical_size of this BackupRestorePoint.  # noqa: E501
        :type physical_size: int
        """

        self._physical_size = physical_size

    @property
    def size(self):
        """Gets the size of this BackupRestorePoint.  # noqa: E501


        :return: The size of this BackupRestorePoint.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BackupRestorePoint.


        :param size: The size of this BackupRestorePoint.  # noqa: E501
        :type size: int
        """

        self._size = size

    @property
    def slice(self):
        """Gets the slice of this BackupRestorePoint.  # noqa: E501


        :return: The slice of this BackupRestorePoint.  # noqa: E501
        :rtype: str
        """
        return self._slice

    @slice.setter
    def slice(self, slice):
        """Sets the slice of this BackupRestorePoint.


        :param slice: The slice of this BackupRestorePoint.  # noqa: E501
        :type slice: str
        """
        if self.local_vars_configuration.client_side_validation and slice is None:  # noqa: E501
            raise ValueError("Invalid value for `slice`, must not be `None`")  # noqa: E501

        self._slice = slice

    @property
    def snapshot_consistent_type(self):
        """Gets the snapshot_consistent_type of this BackupRestorePoint.  # noqa: E501


        :return: The snapshot_consistent_type of this BackupRestorePoint.  # noqa: E501
        :rtype: ConsistentType
        """
        return self._snapshot_consistent_type

    @snapshot_consistent_type.setter
    def snapshot_consistent_type(self, snapshot_consistent_type):
        """Sets the snapshot_consistent_type of this BackupRestorePoint.


        :param snapshot_consistent_type: The snapshot_consistent_type of this BackupRestorePoint.  # noqa: E501
        :type snapshot_consistent_type: ConsistentType
        """

        self._snapshot_consistent_type = snapshot_consistent_type

    @property
    def type(self):
        """Gets the type of this BackupRestorePoint.  # noqa: E501


        :return: The type of this BackupRestorePoint.  # noqa: E501
        :rtype: BackupRestorePointType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BackupRestorePoint.


        :param type: The type of this BackupRestorePoint.  # noqa: E501
        :type type: BackupRestorePointType
        """

        self._type = type

    @property
    def valid_capacity(self):
        """Gets the valid_capacity of this BackupRestorePoint.  # noqa: E501


        :return: The valid_capacity of this BackupRestorePoint.  # noqa: E501
        :rtype: int
        """
        return self._valid_capacity

    @valid_capacity.setter
    def valid_capacity(self, valid_capacity):
        """Sets the valid_capacity of this BackupRestorePoint.


        :param valid_capacity: The valid_capacity of this BackupRestorePoint.  # noqa: E501
        :type valid_capacity: int
        """

        self._valid_capacity = valid_capacity

    @property
    def valid_size(self):
        """Gets the valid_size of this BackupRestorePoint.  # noqa: E501


        :return: The valid_size of this BackupRestorePoint.  # noqa: E501
        :rtype: int
        """
        return self._valid_size

    @valid_size.setter
    def valid_size(self, valid_size):
        """Sets the valid_size of this BackupRestorePoint.


        :param valid_size: The valid_size of this BackupRestorePoint.  # noqa: E501
        :type valid_size: int
        """

        self._valid_size = valid_size

    @property
    def vm(self):
        """Gets the vm of this BackupRestorePoint.  # noqa: E501


        :return: The vm of this BackupRestorePoint.  # noqa: E501
        :rtype: NestedVm
        """
        return self._vm

    @vm.setter
    def vm(self, vm):
        """Sets the vm of this BackupRestorePoint.


        :param vm: The vm of this BackupRestorePoint.  # noqa: E501
        :type vm: NestedVm
        """

        self._vm = vm

    @property
    def vm_local_id(self):
        """Gets the vm_local_id of this BackupRestorePoint.  # noqa: E501


        :return: The vm_local_id of this BackupRestorePoint.  # noqa: E501
        :rtype: str
        """
        return self._vm_local_id

    @vm_local_id.setter
    def vm_local_id(self, vm_local_id):
        """Sets the vm_local_id of this BackupRestorePoint.


        :param vm_local_id: The vm_local_id of this BackupRestorePoint.  # noqa: E501
        :type vm_local_id: str
        """

        self._vm_local_id = vm_local_id

    @property
    def vm_name(self):
        """Gets the vm_name of this BackupRestorePoint.  # noqa: E501


        :return: The vm_name of this BackupRestorePoint.  # noqa: E501
        :rtype: str
        """
        return self._vm_name

    @vm_name.setter
    def vm_name(self, vm_name):
        """Sets the vm_name of this BackupRestorePoint.


        :param vm_name: The vm_name of this BackupRestorePoint.  # noqa: E501
        :type vm_name: str
        """

        self._vm_name = vm_name

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
        if not isinstance(other, BackupRestorePoint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BackupRestorePoint):
            return True

        return self.to_dict() != other.to_dict()
