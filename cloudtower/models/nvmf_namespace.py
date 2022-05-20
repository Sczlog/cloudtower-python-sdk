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


class NvmfNamespace(object):
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
        'assigned_size': 'int',
        'bps': 'int',
        'bps_max': 'int',
        'bps_max_length': 'int',
        'bps_rd': 'int',
        'bps_rd_max': 'int',
        'bps_rd_max_length': 'int',
        'bps_wr': 'int',
        'bps_wr_max': 'int',
        'bps_wr_max_length': 'int',
        'consistency_group': 'NestedConsistencyGroup',
        'entity_async_status': 'EntityAsyncStatus',
        'id': 'str',
        'io_size': 'int',
        'iops': 'int',
        'iops_max': 'int',
        'iops_max_length': 'int',
        'iops_rd': 'int',
        'iops_rd_max': 'int',
        'iops_rd_max_length': 'int',
        'iops_wr': 'int',
        'iops_wr_max': 'int',
        'iops_wr_max_length': 'int',
        'is_shared': 'bool',
        'labels': 'list[NestedLabel]',
        'local_created_at': 'str',
        'local_id': 'str',
        'name': 'str',
        'namespace_group': 'NestedNamespaceGroup',
        'namespace_id': 'int',
        'nqn_whitelist': 'str',
        'nvmf_subsystem': 'NestedNvmfSubsystem',
        'replica_num': 'int',
        'shared_size': 'int',
        'snapshot_num': 'int',
        'stripe_num': 'int',
        'stripe_size': 'int',
        'thin_provision': 'bool',
        'unique_size': 'int',
        'zbs_volume_id': 'str'
    }

    attribute_map = {
        'assigned_size': 'assigned_size',
        'bps': 'bps',
        'bps_max': 'bps_max',
        'bps_max_length': 'bps_max_length',
        'bps_rd': 'bps_rd',
        'bps_rd_max': 'bps_rd_max',
        'bps_rd_max_length': 'bps_rd_max_length',
        'bps_wr': 'bps_wr',
        'bps_wr_max': 'bps_wr_max',
        'bps_wr_max_length': 'bps_wr_max_length',
        'consistency_group': 'consistency_group',
        'entity_async_status': 'entityAsyncStatus',
        'id': 'id',
        'io_size': 'io_size',
        'iops': 'iops',
        'iops_max': 'iops_max',
        'iops_max_length': 'iops_max_length',
        'iops_rd': 'iops_rd',
        'iops_rd_max': 'iops_rd_max',
        'iops_rd_max_length': 'iops_rd_max_length',
        'iops_wr': 'iops_wr',
        'iops_wr_max': 'iops_wr_max',
        'iops_wr_max_length': 'iops_wr_max_length',
        'is_shared': 'is_shared',
        'labels': 'labels',
        'local_created_at': 'local_created_at',
        'local_id': 'local_id',
        'name': 'name',
        'namespace_group': 'namespace_group',
        'namespace_id': 'namespace_id',
        'nqn_whitelist': 'nqn_whitelist',
        'nvmf_subsystem': 'nvmf_subsystem',
        'replica_num': 'replica_num',
        'shared_size': 'shared_size',
        'snapshot_num': 'snapshot_num',
        'stripe_num': 'stripe_num',
        'stripe_size': 'stripe_size',
        'thin_provision': 'thin_provision',
        'unique_size': 'unique_size',
        'zbs_volume_id': 'zbs_volume_id'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NvmfNamespace - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._assigned_size = None
        self._bps = None
        self._bps_max = None
        self._bps_max_length = None
        self._bps_rd = None
        self._bps_rd_max = None
        self._bps_rd_max_length = None
        self._bps_wr = None
        self._bps_wr_max = None
        self._bps_wr_max_length = None
        self._consistency_group = None
        self._entity_async_status = None
        self._id = None
        self._io_size = None
        self._iops = None
        self._iops_max = None
        self._iops_max_length = None
        self._iops_rd = None
        self._iops_rd_max = None
        self._iops_rd_max_length = None
        self._iops_wr = None
        self._iops_wr_max = None
        self._iops_wr_max_length = None
        self._is_shared = None
        self._labels = None
        self._local_created_at = None
        self._local_id = None
        self._name = None
        self._namespace_group = None
        self._namespace_id = None
        self._nqn_whitelist = None
        self._nvmf_subsystem = None
        self._replica_num = None
        self._shared_size = None
        self._snapshot_num = None
        self._stripe_num = None
        self._stripe_size = None
        self._thin_provision = None
        self._unique_size = None
        self._zbs_volume_id = None
        self.discriminator = None

        if "assigned_size" in kwargs:
            self.assigned_size = kwargs["assigned_size"]
        if "bps" in kwargs:
            self.bps = kwargs["bps"]
        if "bps_max" in kwargs:
            self.bps_max = kwargs["bps_max"]
        if "bps_max_length" in kwargs:
            self.bps_max_length = kwargs["bps_max_length"]
        if "bps_rd" in kwargs:
            self.bps_rd = kwargs["bps_rd"]
        if "bps_rd_max" in kwargs:
            self.bps_rd_max = kwargs["bps_rd_max"]
        if "bps_rd_max_length" in kwargs:
            self.bps_rd_max_length = kwargs["bps_rd_max_length"]
        if "bps_wr" in kwargs:
            self.bps_wr = kwargs["bps_wr"]
        if "bps_wr_max" in kwargs:
            self.bps_wr_max = kwargs["bps_wr_max"]
        if "bps_wr_max_length" in kwargs:
            self.bps_wr_max_length = kwargs["bps_wr_max_length"]
        self.consistency_group = kwargs.get("consistency_group", None)
        self.entity_async_status = kwargs.get("entity_async_status", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "io_size" in kwargs:
            self.io_size = kwargs["io_size"]
        if "iops" in kwargs:
            self.iops = kwargs["iops"]
        if "iops_max" in kwargs:
            self.iops_max = kwargs["iops_max"]
        if "iops_max_length" in kwargs:
            self.iops_max_length = kwargs["iops_max_length"]
        if "iops_rd" in kwargs:
            self.iops_rd = kwargs["iops_rd"]
        if "iops_rd_max" in kwargs:
            self.iops_rd_max = kwargs["iops_rd_max"]
        if "iops_rd_max_length" in kwargs:
            self.iops_rd_max_length = kwargs["iops_rd_max_length"]
        if "iops_wr" in kwargs:
            self.iops_wr = kwargs["iops_wr"]
        if "iops_wr_max" in kwargs:
            self.iops_wr_max = kwargs["iops_wr_max"]
        if "iops_wr_max_length" in kwargs:
            self.iops_wr_max_length = kwargs["iops_wr_max_length"]
        if "is_shared" in kwargs:
            self.is_shared = kwargs["is_shared"]
        self.labels = kwargs.get("labels", None)
        if "local_created_at" in kwargs:
            self.local_created_at = kwargs["local_created_at"]
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        self.namespace_group = kwargs.get("namespace_group", None)
        if "namespace_id" in kwargs:
            self.namespace_id = kwargs["namespace_id"]
        if "nqn_whitelist" in kwargs:
            self.nqn_whitelist = kwargs["nqn_whitelist"]
        if "nvmf_subsystem" in kwargs:
            self.nvmf_subsystem = kwargs["nvmf_subsystem"]
        if "replica_num" in kwargs:
            self.replica_num = kwargs["replica_num"]
        if "shared_size" in kwargs:
            self.shared_size = kwargs["shared_size"]
        if "snapshot_num" in kwargs:
            self.snapshot_num = kwargs["snapshot_num"]
        if "stripe_num" in kwargs:
            self.stripe_num = kwargs["stripe_num"]
        if "stripe_size" in kwargs:
            self.stripe_size = kwargs["stripe_size"]
        if "thin_provision" in kwargs:
            self.thin_provision = kwargs["thin_provision"]
        if "unique_size" in kwargs:
            self.unique_size = kwargs["unique_size"]
        if "zbs_volume_id" in kwargs:
            self.zbs_volume_id = kwargs["zbs_volume_id"]

    @property
    def assigned_size(self):
        """Gets the assigned_size of this NvmfNamespace.  # noqa: E501


        :return: The assigned_size of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._assigned_size

    @assigned_size.setter
    def assigned_size(self, assigned_size):
        """Sets the assigned_size of this NvmfNamespace.


        :param assigned_size: The assigned_size of this NvmfNamespace.  # noqa: E501
        :type assigned_size: int
        """
        if self.local_vars_configuration.client_side_validation and assigned_size is None:  # noqa: E501
            raise ValueError("Invalid value for `assigned_size`, must not be `None`")  # noqa: E501

        self._assigned_size = assigned_size

    @property
    def bps(self):
        """Gets the bps of this NvmfNamespace.  # noqa: E501


        :return: The bps of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._bps

    @bps.setter
    def bps(self, bps):
        """Sets the bps of this NvmfNamespace.


        :param bps: The bps of this NvmfNamespace.  # noqa: E501
        :type bps: int
        """
        if self.local_vars_configuration.client_side_validation and bps is None:  # noqa: E501
            raise ValueError("Invalid value for `bps`, must not be `None`")  # noqa: E501

        self._bps = bps

    @property
    def bps_max(self):
        """Gets the bps_max of this NvmfNamespace.  # noqa: E501


        :return: The bps_max of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._bps_max

    @bps_max.setter
    def bps_max(self, bps_max):
        """Sets the bps_max of this NvmfNamespace.


        :param bps_max: The bps_max of this NvmfNamespace.  # noqa: E501
        :type bps_max: int
        """
        if self.local_vars_configuration.client_side_validation and bps_max is None:  # noqa: E501
            raise ValueError("Invalid value for `bps_max`, must not be `None`")  # noqa: E501

        self._bps_max = bps_max

    @property
    def bps_max_length(self):
        """Gets the bps_max_length of this NvmfNamespace.  # noqa: E501


        :return: The bps_max_length of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._bps_max_length

    @bps_max_length.setter
    def bps_max_length(self, bps_max_length):
        """Sets the bps_max_length of this NvmfNamespace.


        :param bps_max_length: The bps_max_length of this NvmfNamespace.  # noqa: E501
        :type bps_max_length: int
        """
        if self.local_vars_configuration.client_side_validation and bps_max_length is None:  # noqa: E501
            raise ValueError("Invalid value for `bps_max_length`, must not be `None`")  # noqa: E501

        self._bps_max_length = bps_max_length

    @property
    def bps_rd(self):
        """Gets the bps_rd of this NvmfNamespace.  # noqa: E501


        :return: The bps_rd of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._bps_rd

    @bps_rd.setter
    def bps_rd(self, bps_rd):
        """Sets the bps_rd of this NvmfNamespace.


        :param bps_rd: The bps_rd of this NvmfNamespace.  # noqa: E501
        :type bps_rd: int
        """
        if self.local_vars_configuration.client_side_validation and bps_rd is None:  # noqa: E501
            raise ValueError("Invalid value for `bps_rd`, must not be `None`")  # noqa: E501

        self._bps_rd = bps_rd

    @property
    def bps_rd_max(self):
        """Gets the bps_rd_max of this NvmfNamespace.  # noqa: E501


        :return: The bps_rd_max of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._bps_rd_max

    @bps_rd_max.setter
    def bps_rd_max(self, bps_rd_max):
        """Sets the bps_rd_max of this NvmfNamespace.


        :param bps_rd_max: The bps_rd_max of this NvmfNamespace.  # noqa: E501
        :type bps_rd_max: int
        """
        if self.local_vars_configuration.client_side_validation and bps_rd_max is None:  # noqa: E501
            raise ValueError("Invalid value for `bps_rd_max`, must not be `None`")  # noqa: E501

        self._bps_rd_max = bps_rd_max

    @property
    def bps_rd_max_length(self):
        """Gets the bps_rd_max_length of this NvmfNamespace.  # noqa: E501


        :return: The bps_rd_max_length of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._bps_rd_max_length

    @bps_rd_max_length.setter
    def bps_rd_max_length(self, bps_rd_max_length):
        """Sets the bps_rd_max_length of this NvmfNamespace.


        :param bps_rd_max_length: The bps_rd_max_length of this NvmfNamespace.  # noqa: E501
        :type bps_rd_max_length: int
        """
        if self.local_vars_configuration.client_side_validation and bps_rd_max_length is None:  # noqa: E501
            raise ValueError("Invalid value for `bps_rd_max_length`, must not be `None`")  # noqa: E501

        self._bps_rd_max_length = bps_rd_max_length

    @property
    def bps_wr(self):
        """Gets the bps_wr of this NvmfNamespace.  # noqa: E501


        :return: The bps_wr of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._bps_wr

    @bps_wr.setter
    def bps_wr(self, bps_wr):
        """Sets the bps_wr of this NvmfNamespace.


        :param bps_wr: The bps_wr of this NvmfNamespace.  # noqa: E501
        :type bps_wr: int
        """
        if self.local_vars_configuration.client_side_validation and bps_wr is None:  # noqa: E501
            raise ValueError("Invalid value for `bps_wr`, must not be `None`")  # noqa: E501

        self._bps_wr = bps_wr

    @property
    def bps_wr_max(self):
        """Gets the bps_wr_max of this NvmfNamespace.  # noqa: E501


        :return: The bps_wr_max of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._bps_wr_max

    @bps_wr_max.setter
    def bps_wr_max(self, bps_wr_max):
        """Sets the bps_wr_max of this NvmfNamespace.


        :param bps_wr_max: The bps_wr_max of this NvmfNamespace.  # noqa: E501
        :type bps_wr_max: int
        """
        if self.local_vars_configuration.client_side_validation and bps_wr_max is None:  # noqa: E501
            raise ValueError("Invalid value for `bps_wr_max`, must not be `None`")  # noqa: E501

        self._bps_wr_max = bps_wr_max

    @property
    def bps_wr_max_length(self):
        """Gets the bps_wr_max_length of this NvmfNamespace.  # noqa: E501


        :return: The bps_wr_max_length of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._bps_wr_max_length

    @bps_wr_max_length.setter
    def bps_wr_max_length(self, bps_wr_max_length):
        """Sets the bps_wr_max_length of this NvmfNamespace.


        :param bps_wr_max_length: The bps_wr_max_length of this NvmfNamespace.  # noqa: E501
        :type bps_wr_max_length: int
        """
        if self.local_vars_configuration.client_side_validation and bps_wr_max_length is None:  # noqa: E501
            raise ValueError("Invalid value for `bps_wr_max_length`, must not be `None`")  # noqa: E501

        self._bps_wr_max_length = bps_wr_max_length

    @property
    def consistency_group(self):
        """Gets the consistency_group of this NvmfNamespace.  # noqa: E501


        :return: The consistency_group of this NvmfNamespace.  # noqa: E501
        :rtype: NestedConsistencyGroup
        """
        return self._consistency_group

    @consistency_group.setter
    def consistency_group(self, consistency_group):
        """Sets the consistency_group of this NvmfNamespace.


        :param consistency_group: The consistency_group of this NvmfNamespace.  # noqa: E501
        :type consistency_group: NestedConsistencyGroup
        """

        self._consistency_group = consistency_group

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this NvmfNamespace.  # noqa: E501


        :return: The entity_async_status of this NvmfNamespace.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this NvmfNamespace.


        :param entity_async_status: The entity_async_status of this NvmfNamespace.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def id(self):
        """Gets the id of this NvmfNamespace.  # noqa: E501


        :return: The id of this NvmfNamespace.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NvmfNamespace.


        :param id: The id of this NvmfNamespace.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def io_size(self):
        """Gets the io_size of this NvmfNamespace.  # noqa: E501


        :return: The io_size of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._io_size

    @io_size.setter
    def io_size(self, io_size):
        """Sets the io_size of this NvmfNamespace.


        :param io_size: The io_size of this NvmfNamespace.  # noqa: E501
        :type io_size: int
        """
        if self.local_vars_configuration.client_side_validation and io_size is None:  # noqa: E501
            raise ValueError("Invalid value for `io_size`, must not be `None`")  # noqa: E501

        self._io_size = io_size

    @property
    def iops(self):
        """Gets the iops of this NvmfNamespace.  # noqa: E501


        :return: The iops of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """Sets the iops of this NvmfNamespace.


        :param iops: The iops of this NvmfNamespace.  # noqa: E501
        :type iops: int
        """
        if self.local_vars_configuration.client_side_validation and iops is None:  # noqa: E501
            raise ValueError("Invalid value for `iops`, must not be `None`")  # noqa: E501

        self._iops = iops

    @property
    def iops_max(self):
        """Gets the iops_max of this NvmfNamespace.  # noqa: E501


        :return: The iops_max of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._iops_max

    @iops_max.setter
    def iops_max(self, iops_max):
        """Sets the iops_max of this NvmfNamespace.


        :param iops_max: The iops_max of this NvmfNamespace.  # noqa: E501
        :type iops_max: int
        """
        if self.local_vars_configuration.client_side_validation and iops_max is None:  # noqa: E501
            raise ValueError("Invalid value for `iops_max`, must not be `None`")  # noqa: E501

        self._iops_max = iops_max

    @property
    def iops_max_length(self):
        """Gets the iops_max_length of this NvmfNamespace.  # noqa: E501


        :return: The iops_max_length of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._iops_max_length

    @iops_max_length.setter
    def iops_max_length(self, iops_max_length):
        """Sets the iops_max_length of this NvmfNamespace.


        :param iops_max_length: The iops_max_length of this NvmfNamespace.  # noqa: E501
        :type iops_max_length: int
        """
        if self.local_vars_configuration.client_side_validation and iops_max_length is None:  # noqa: E501
            raise ValueError("Invalid value for `iops_max_length`, must not be `None`")  # noqa: E501

        self._iops_max_length = iops_max_length

    @property
    def iops_rd(self):
        """Gets the iops_rd of this NvmfNamespace.  # noqa: E501


        :return: The iops_rd of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._iops_rd

    @iops_rd.setter
    def iops_rd(self, iops_rd):
        """Sets the iops_rd of this NvmfNamespace.


        :param iops_rd: The iops_rd of this NvmfNamespace.  # noqa: E501
        :type iops_rd: int
        """
        if self.local_vars_configuration.client_side_validation and iops_rd is None:  # noqa: E501
            raise ValueError("Invalid value for `iops_rd`, must not be `None`")  # noqa: E501

        self._iops_rd = iops_rd

    @property
    def iops_rd_max(self):
        """Gets the iops_rd_max of this NvmfNamespace.  # noqa: E501


        :return: The iops_rd_max of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._iops_rd_max

    @iops_rd_max.setter
    def iops_rd_max(self, iops_rd_max):
        """Sets the iops_rd_max of this NvmfNamespace.


        :param iops_rd_max: The iops_rd_max of this NvmfNamespace.  # noqa: E501
        :type iops_rd_max: int
        """
        if self.local_vars_configuration.client_side_validation and iops_rd_max is None:  # noqa: E501
            raise ValueError("Invalid value for `iops_rd_max`, must not be `None`")  # noqa: E501

        self._iops_rd_max = iops_rd_max

    @property
    def iops_rd_max_length(self):
        """Gets the iops_rd_max_length of this NvmfNamespace.  # noqa: E501


        :return: The iops_rd_max_length of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._iops_rd_max_length

    @iops_rd_max_length.setter
    def iops_rd_max_length(self, iops_rd_max_length):
        """Sets the iops_rd_max_length of this NvmfNamespace.


        :param iops_rd_max_length: The iops_rd_max_length of this NvmfNamespace.  # noqa: E501
        :type iops_rd_max_length: int
        """
        if self.local_vars_configuration.client_side_validation and iops_rd_max_length is None:  # noqa: E501
            raise ValueError("Invalid value for `iops_rd_max_length`, must not be `None`")  # noqa: E501

        self._iops_rd_max_length = iops_rd_max_length

    @property
    def iops_wr(self):
        """Gets the iops_wr of this NvmfNamespace.  # noqa: E501


        :return: The iops_wr of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._iops_wr

    @iops_wr.setter
    def iops_wr(self, iops_wr):
        """Sets the iops_wr of this NvmfNamespace.


        :param iops_wr: The iops_wr of this NvmfNamespace.  # noqa: E501
        :type iops_wr: int
        """
        if self.local_vars_configuration.client_side_validation and iops_wr is None:  # noqa: E501
            raise ValueError("Invalid value for `iops_wr`, must not be `None`")  # noqa: E501

        self._iops_wr = iops_wr

    @property
    def iops_wr_max(self):
        """Gets the iops_wr_max of this NvmfNamespace.  # noqa: E501


        :return: The iops_wr_max of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._iops_wr_max

    @iops_wr_max.setter
    def iops_wr_max(self, iops_wr_max):
        """Sets the iops_wr_max of this NvmfNamespace.


        :param iops_wr_max: The iops_wr_max of this NvmfNamespace.  # noqa: E501
        :type iops_wr_max: int
        """
        if self.local_vars_configuration.client_side_validation and iops_wr_max is None:  # noqa: E501
            raise ValueError("Invalid value for `iops_wr_max`, must not be `None`")  # noqa: E501

        self._iops_wr_max = iops_wr_max

    @property
    def iops_wr_max_length(self):
        """Gets the iops_wr_max_length of this NvmfNamespace.  # noqa: E501


        :return: The iops_wr_max_length of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._iops_wr_max_length

    @iops_wr_max_length.setter
    def iops_wr_max_length(self, iops_wr_max_length):
        """Sets the iops_wr_max_length of this NvmfNamespace.


        :param iops_wr_max_length: The iops_wr_max_length of this NvmfNamespace.  # noqa: E501
        :type iops_wr_max_length: int
        """
        if self.local_vars_configuration.client_side_validation and iops_wr_max_length is None:  # noqa: E501
            raise ValueError("Invalid value for `iops_wr_max_length`, must not be `None`")  # noqa: E501

        self._iops_wr_max_length = iops_wr_max_length

    @property
    def is_shared(self):
        """Gets the is_shared of this NvmfNamespace.  # noqa: E501


        :return: The is_shared of this NvmfNamespace.  # noqa: E501
        :rtype: bool
        """
        return self._is_shared

    @is_shared.setter
    def is_shared(self, is_shared):
        """Sets the is_shared of this NvmfNamespace.


        :param is_shared: The is_shared of this NvmfNamespace.  # noqa: E501
        :type is_shared: bool
        """
        if self.local_vars_configuration.client_side_validation and is_shared is None:  # noqa: E501
            raise ValueError("Invalid value for `is_shared`, must not be `None`")  # noqa: E501

        self._is_shared = is_shared

    @property
    def labels(self):
        """Gets the labels of this NvmfNamespace.  # noqa: E501


        :return: The labels of this NvmfNamespace.  # noqa: E501
        :rtype: list[NestedLabel]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this NvmfNamespace.


        :param labels: The labels of this NvmfNamespace.  # noqa: E501
        :type labels: list[NestedLabel]
        """

        self._labels = labels

    @property
    def local_created_at(self):
        """Gets the local_created_at of this NvmfNamespace.  # noqa: E501


        :return: The local_created_at of this NvmfNamespace.  # noqa: E501
        :rtype: str
        """
        return self._local_created_at

    @local_created_at.setter
    def local_created_at(self, local_created_at):
        """Sets the local_created_at of this NvmfNamespace.


        :param local_created_at: The local_created_at of this NvmfNamespace.  # noqa: E501
        :type local_created_at: str
        """
        if self.local_vars_configuration.client_side_validation and local_created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `local_created_at`, must not be `None`")  # noqa: E501

        self._local_created_at = local_created_at

    @property
    def local_id(self):
        """Gets the local_id of this NvmfNamespace.  # noqa: E501


        :return: The local_id of this NvmfNamespace.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this NvmfNamespace.


        :param local_id: The local_id of this NvmfNamespace.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def name(self):
        """Gets the name of this NvmfNamespace.  # noqa: E501


        :return: The name of this NvmfNamespace.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NvmfNamespace.


        :param name: The name of this NvmfNamespace.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespace_group(self):
        """Gets the namespace_group of this NvmfNamespace.  # noqa: E501


        :return: The namespace_group of this NvmfNamespace.  # noqa: E501
        :rtype: NestedNamespaceGroup
        """
        return self._namespace_group

    @namespace_group.setter
    def namespace_group(self, namespace_group):
        """Sets the namespace_group of this NvmfNamespace.


        :param namespace_group: The namespace_group of this NvmfNamespace.  # noqa: E501
        :type namespace_group: NestedNamespaceGroup
        """

        self._namespace_group = namespace_group

    @property
    def namespace_id(self):
        """Gets the namespace_id of this NvmfNamespace.  # noqa: E501


        :return: The namespace_id of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._namespace_id

    @namespace_id.setter
    def namespace_id(self, namespace_id):
        """Sets the namespace_id of this NvmfNamespace.


        :param namespace_id: The namespace_id of this NvmfNamespace.  # noqa: E501
        :type namespace_id: int
        """
        if self.local_vars_configuration.client_side_validation and namespace_id is None:  # noqa: E501
            raise ValueError("Invalid value for `namespace_id`, must not be `None`")  # noqa: E501

        self._namespace_id = namespace_id

    @property
    def nqn_whitelist(self):
        """Gets the nqn_whitelist of this NvmfNamespace.  # noqa: E501


        :return: The nqn_whitelist of this NvmfNamespace.  # noqa: E501
        :rtype: str
        """
        return self._nqn_whitelist

    @nqn_whitelist.setter
    def nqn_whitelist(self, nqn_whitelist):
        """Sets the nqn_whitelist of this NvmfNamespace.


        :param nqn_whitelist: The nqn_whitelist of this NvmfNamespace.  # noqa: E501
        :type nqn_whitelist: str
        """
        if self.local_vars_configuration.client_side_validation and nqn_whitelist is None:  # noqa: E501
            raise ValueError("Invalid value for `nqn_whitelist`, must not be `None`")  # noqa: E501

        self._nqn_whitelist = nqn_whitelist

    @property
    def nvmf_subsystem(self):
        """Gets the nvmf_subsystem of this NvmfNamespace.  # noqa: E501


        :return: The nvmf_subsystem of this NvmfNamespace.  # noqa: E501
        :rtype: NestedNvmfSubsystem
        """
        return self._nvmf_subsystem

    @nvmf_subsystem.setter
    def nvmf_subsystem(self, nvmf_subsystem):
        """Sets the nvmf_subsystem of this NvmfNamespace.


        :param nvmf_subsystem: The nvmf_subsystem of this NvmfNamespace.  # noqa: E501
        :type nvmf_subsystem: NestedNvmfSubsystem
        """
        if self.local_vars_configuration.client_side_validation and nvmf_subsystem is None:  # noqa: E501
            raise ValueError("Invalid value for `nvmf_subsystem`, must not be `None`")  # noqa: E501

        self._nvmf_subsystem = nvmf_subsystem

    @property
    def replica_num(self):
        """Gets the replica_num of this NvmfNamespace.  # noqa: E501


        :return: The replica_num of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._replica_num

    @replica_num.setter
    def replica_num(self, replica_num):
        """Sets the replica_num of this NvmfNamespace.


        :param replica_num: The replica_num of this NvmfNamespace.  # noqa: E501
        :type replica_num: int
        """
        if self.local_vars_configuration.client_side_validation and replica_num is None:  # noqa: E501
            raise ValueError("Invalid value for `replica_num`, must not be `None`")  # noqa: E501

        self._replica_num = replica_num

    @property
    def shared_size(self):
        """Gets the shared_size of this NvmfNamespace.  # noqa: E501


        :return: The shared_size of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._shared_size

    @shared_size.setter
    def shared_size(self, shared_size):
        """Sets the shared_size of this NvmfNamespace.


        :param shared_size: The shared_size of this NvmfNamespace.  # noqa: E501
        :type shared_size: int
        """
        if self.local_vars_configuration.client_side_validation and shared_size is None:  # noqa: E501
            raise ValueError("Invalid value for `shared_size`, must not be `None`")  # noqa: E501

        self._shared_size = shared_size

    @property
    def snapshot_num(self):
        """Gets the snapshot_num of this NvmfNamespace.  # noqa: E501


        :return: The snapshot_num of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._snapshot_num

    @snapshot_num.setter
    def snapshot_num(self, snapshot_num):
        """Sets the snapshot_num of this NvmfNamespace.


        :param snapshot_num: The snapshot_num of this NvmfNamespace.  # noqa: E501
        :type snapshot_num: int
        """
        if self.local_vars_configuration.client_side_validation and snapshot_num is None:  # noqa: E501
            raise ValueError("Invalid value for `snapshot_num`, must not be `None`")  # noqa: E501

        self._snapshot_num = snapshot_num

    @property
    def stripe_num(self):
        """Gets the stripe_num of this NvmfNamespace.  # noqa: E501


        :return: The stripe_num of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._stripe_num

    @stripe_num.setter
    def stripe_num(self, stripe_num):
        """Sets the stripe_num of this NvmfNamespace.


        :param stripe_num: The stripe_num of this NvmfNamespace.  # noqa: E501
        :type stripe_num: int
        """
        if self.local_vars_configuration.client_side_validation and stripe_num is None:  # noqa: E501
            raise ValueError("Invalid value for `stripe_num`, must not be `None`")  # noqa: E501

        self._stripe_num = stripe_num

    @property
    def stripe_size(self):
        """Gets the stripe_size of this NvmfNamespace.  # noqa: E501


        :return: The stripe_size of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._stripe_size

    @stripe_size.setter
    def stripe_size(self, stripe_size):
        """Sets the stripe_size of this NvmfNamespace.


        :param stripe_size: The stripe_size of this NvmfNamespace.  # noqa: E501
        :type stripe_size: int
        """
        if self.local_vars_configuration.client_side_validation and stripe_size is None:  # noqa: E501
            raise ValueError("Invalid value for `stripe_size`, must not be `None`")  # noqa: E501

        self._stripe_size = stripe_size

    @property
    def thin_provision(self):
        """Gets the thin_provision of this NvmfNamespace.  # noqa: E501


        :return: The thin_provision of this NvmfNamespace.  # noqa: E501
        :rtype: bool
        """
        return self._thin_provision

    @thin_provision.setter
    def thin_provision(self, thin_provision):
        """Sets the thin_provision of this NvmfNamespace.


        :param thin_provision: The thin_provision of this NvmfNamespace.  # noqa: E501
        :type thin_provision: bool
        """
        if self.local_vars_configuration.client_side_validation and thin_provision is None:  # noqa: E501
            raise ValueError("Invalid value for `thin_provision`, must not be `None`")  # noqa: E501

        self._thin_provision = thin_provision

    @property
    def unique_size(self):
        """Gets the unique_size of this NvmfNamespace.  # noqa: E501


        :return: The unique_size of this NvmfNamespace.  # noqa: E501
        :rtype: int
        """
        return self._unique_size

    @unique_size.setter
    def unique_size(self, unique_size):
        """Sets the unique_size of this NvmfNamespace.


        :param unique_size: The unique_size of this NvmfNamespace.  # noqa: E501
        :type unique_size: int
        """
        if self.local_vars_configuration.client_side_validation and unique_size is None:  # noqa: E501
            raise ValueError("Invalid value for `unique_size`, must not be `None`")  # noqa: E501

        self._unique_size = unique_size

    @property
    def zbs_volume_id(self):
        """Gets the zbs_volume_id of this NvmfNamespace.  # noqa: E501


        :return: The zbs_volume_id of this NvmfNamespace.  # noqa: E501
        :rtype: str
        """
        return self._zbs_volume_id

    @zbs_volume_id.setter
    def zbs_volume_id(self, zbs_volume_id):
        """Sets the zbs_volume_id of this NvmfNamespace.


        :param zbs_volume_id: The zbs_volume_id of this NvmfNamespace.  # noqa: E501
        :type zbs_volume_id: str
        """
        if self.local_vars_configuration.client_side_validation and zbs_volume_id is None:  # noqa: E501
            raise ValueError("Invalid value for `zbs_volume_id`, must not be `None`")  # noqa: E501

        self._zbs_volume_id = zbs_volume_id

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
        if not isinstance(other, NvmfNamespace):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NvmfNamespace):
            return True

        return self.to_dict() != other.to_dict()
