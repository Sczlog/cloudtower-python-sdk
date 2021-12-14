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


class NvmfNamespaceCreationParams(object):
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
        'namespace_id': 'int',
        'group_id': 'str',
        'is_shared': 'bool',
        'assigned_size': 'float',
        'replica_num': 'int',
        'nvmf_subsystem_id': 'str',
        'name': 'str',
        'bps_wr_max_length': 'float',
        'bps_wr_max': 'float',
        'bps_rd_max_length': 'float',
        'bps_rd_max': 'float',
        'bps_max_length': 'float',
        'bps_max': 'float',
        'iops_wr_max_length': 'float',
        'iops_wr_max': 'float',
        'iops_rd_max_length': 'float',
        'iops_rd_max': 'float',
        'iops_max_length': 'float',
        'iops_max': 'float',
        'bps_wr': 'float',
        'bps_rd': 'float',
        'bps': 'float',
        'iops_wr': 'float',
        'iops_rd': 'float',
        'iops': 'float',
        'nqn_whitelist': 'str'
    }

    attribute_map = {
        'namespace_id': 'namespace_id',
        'group_id': 'group_id',
        'is_shared': 'is_shared',
        'assigned_size': 'assigned_size',
        'replica_num': 'replica_num',
        'nvmf_subsystem_id': 'nvmf_subsystem_id',
        'name': 'name',
        'bps_wr_max_length': 'bps_wr_max_length',
        'bps_wr_max': 'bps_wr_max',
        'bps_rd_max_length': 'bps_rd_max_length',
        'bps_rd_max': 'bps_rd_max',
        'bps_max_length': 'bps_max_length',
        'bps_max': 'bps_max',
        'iops_wr_max_length': 'iops_wr_max_length',
        'iops_wr_max': 'iops_wr_max',
        'iops_rd_max_length': 'iops_rd_max_length',
        'iops_rd_max': 'iops_rd_max',
        'iops_max_length': 'iops_max_length',
        'iops_max': 'iops_max',
        'bps_wr': 'bps_wr',
        'bps_rd': 'bps_rd',
        'bps': 'bps',
        'iops_wr': 'iops_wr',
        'iops_rd': 'iops_rd',
        'iops': 'iops',
        'nqn_whitelist': 'nqn_whitelist'
    }

    def __init__(self, namespace_id=None, group_id=None, is_shared=None, assigned_size=None, replica_num=None, nvmf_subsystem_id=None, name=None, bps_wr_max_length=None, bps_wr_max=None, bps_rd_max_length=None, bps_rd_max=None, bps_max_length=None, bps_max=None, iops_wr_max_length=None, iops_wr_max=None, iops_rd_max_length=None, iops_rd_max=None, iops_max_length=None, iops_max=None, bps_wr=None, bps_rd=None, bps=None, iops_wr=None, iops_rd=None, iops=None, nqn_whitelist=None, local_vars_configuration=None):  # noqa: E501
        """NvmfNamespaceCreationParams - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._namespace_id = None
        self._group_id = None
        self._is_shared = None
        self._assigned_size = None
        self._replica_num = None
        self._nvmf_subsystem_id = None
        self._name = None
        self._bps_wr_max_length = None
        self._bps_wr_max = None
        self._bps_rd_max_length = None
        self._bps_rd_max = None
        self._bps_max_length = None
        self._bps_max = None
        self._iops_wr_max_length = None
        self._iops_wr_max = None
        self._iops_rd_max_length = None
        self._iops_rd_max = None
        self._iops_max_length = None
        self._iops_max = None
        self._bps_wr = None
        self._bps_rd = None
        self._bps = None
        self._iops_wr = None
        self._iops_rd = None
        self._iops = None
        self._nqn_whitelist = None
        self.discriminator = None

        if namespace_id is not None:
            self.namespace_id = namespace_id
        if group_id is not None:
            self.group_id = group_id
        if is_shared is not None:
            self.is_shared = is_shared
        self.assigned_size = assigned_size
        self.replica_num = replica_num
        self.nvmf_subsystem_id = nvmf_subsystem_id
        self.name = name
        if bps_wr_max_length is not None:
            self.bps_wr_max_length = bps_wr_max_length
        if bps_wr_max is not None:
            self.bps_wr_max = bps_wr_max
        if bps_rd_max_length is not None:
            self.bps_rd_max_length = bps_rd_max_length
        if bps_rd_max is not None:
            self.bps_rd_max = bps_rd_max
        if bps_max_length is not None:
            self.bps_max_length = bps_max_length
        if bps_max is not None:
            self.bps_max = bps_max
        if iops_wr_max_length is not None:
            self.iops_wr_max_length = iops_wr_max_length
        if iops_wr_max is not None:
            self.iops_wr_max = iops_wr_max
        if iops_rd_max_length is not None:
            self.iops_rd_max_length = iops_rd_max_length
        if iops_rd_max is not None:
            self.iops_rd_max = iops_rd_max
        if iops_max_length is not None:
            self.iops_max_length = iops_max_length
        if iops_max is not None:
            self.iops_max = iops_max
        if bps_wr is not None:
            self.bps_wr = bps_wr
        if bps_rd is not None:
            self.bps_rd = bps_rd
        if bps is not None:
            self.bps = bps
        if iops_wr is not None:
            self.iops_wr = iops_wr
        if iops_rd is not None:
            self.iops_rd = iops_rd
        if iops is not None:
            self.iops = iops
        if nqn_whitelist is not None:
            self.nqn_whitelist = nqn_whitelist

    @property
    def namespace_id(self):
        """Gets the namespace_id of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The namespace_id of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: int
        """
        return self._namespace_id

    @namespace_id.setter
    def namespace_id(self, namespace_id):
        """Sets the namespace_id of this NvmfNamespaceCreationParams.


        :param namespace_id: The namespace_id of this NvmfNamespaceCreationParams.  # noqa: E501
        :type namespace_id: int
        """

        self._namespace_id = namespace_id

    @property
    def group_id(self):
        """Gets the group_id of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The group_id of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this NvmfNamespaceCreationParams.


        :param group_id: The group_id of this NvmfNamespaceCreationParams.  # noqa: E501
        :type group_id: str
        """

        self._group_id = group_id

    @property
    def is_shared(self):
        """Gets the is_shared of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The is_shared of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_shared

    @is_shared.setter
    def is_shared(self, is_shared):
        """Sets the is_shared of this NvmfNamespaceCreationParams.


        :param is_shared: The is_shared of this NvmfNamespaceCreationParams.  # noqa: E501
        :type is_shared: bool
        """

        self._is_shared = is_shared

    @property
    def assigned_size(self):
        """Gets the assigned_size of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The assigned_size of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: float
        """
        return self._assigned_size

    @assigned_size.setter
    def assigned_size(self, assigned_size):
        """Sets the assigned_size of this NvmfNamespaceCreationParams.


        :param assigned_size: The assigned_size of this NvmfNamespaceCreationParams.  # noqa: E501
        :type assigned_size: float
        """
        if self.local_vars_configuration.client_side_validation and assigned_size is None:  # noqa: E501
            raise ValueError("Invalid value for `assigned_size`, must not be `None`")  # noqa: E501

        self._assigned_size = assigned_size

    @property
    def replica_num(self):
        """Gets the replica_num of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The replica_num of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: int
        """
        return self._replica_num

    @replica_num.setter
    def replica_num(self, replica_num):
        """Sets the replica_num of this NvmfNamespaceCreationParams.


        :param replica_num: The replica_num of this NvmfNamespaceCreationParams.  # noqa: E501
        :type replica_num: int
        """
        if self.local_vars_configuration.client_side_validation and replica_num is None:  # noqa: E501
            raise ValueError("Invalid value for `replica_num`, must not be `None`")  # noqa: E501

        self._replica_num = replica_num

    @property
    def nvmf_subsystem_id(self):
        """Gets the nvmf_subsystem_id of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The nvmf_subsystem_id of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._nvmf_subsystem_id

    @nvmf_subsystem_id.setter
    def nvmf_subsystem_id(self, nvmf_subsystem_id):
        """Sets the nvmf_subsystem_id of this NvmfNamespaceCreationParams.


        :param nvmf_subsystem_id: The nvmf_subsystem_id of this NvmfNamespaceCreationParams.  # noqa: E501
        :type nvmf_subsystem_id: str
        """
        if self.local_vars_configuration.client_side_validation and nvmf_subsystem_id is None:  # noqa: E501
            raise ValueError("Invalid value for `nvmf_subsystem_id`, must not be `None`")  # noqa: E501

        self._nvmf_subsystem_id = nvmf_subsystem_id

    @property
    def name(self):
        """Gets the name of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The name of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NvmfNamespaceCreationParams.


        :param name: The name of this NvmfNamespaceCreationParams.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def bps_wr_max_length(self):
        """Gets the bps_wr_max_length of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The bps_wr_max_length of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: float
        """
        return self._bps_wr_max_length

    @bps_wr_max_length.setter
    def bps_wr_max_length(self, bps_wr_max_length):
        """Sets the bps_wr_max_length of this NvmfNamespaceCreationParams.


        :param bps_wr_max_length: The bps_wr_max_length of this NvmfNamespaceCreationParams.  # noqa: E501
        :type bps_wr_max_length: float
        """

        self._bps_wr_max_length = bps_wr_max_length

    @property
    def bps_wr_max(self):
        """Gets the bps_wr_max of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The bps_wr_max of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: float
        """
        return self._bps_wr_max

    @bps_wr_max.setter
    def bps_wr_max(self, bps_wr_max):
        """Sets the bps_wr_max of this NvmfNamespaceCreationParams.


        :param bps_wr_max: The bps_wr_max of this NvmfNamespaceCreationParams.  # noqa: E501
        :type bps_wr_max: float
        """

        self._bps_wr_max = bps_wr_max

    @property
    def bps_rd_max_length(self):
        """Gets the bps_rd_max_length of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The bps_rd_max_length of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: float
        """
        return self._bps_rd_max_length

    @bps_rd_max_length.setter
    def bps_rd_max_length(self, bps_rd_max_length):
        """Sets the bps_rd_max_length of this NvmfNamespaceCreationParams.


        :param bps_rd_max_length: The bps_rd_max_length of this NvmfNamespaceCreationParams.  # noqa: E501
        :type bps_rd_max_length: float
        """

        self._bps_rd_max_length = bps_rd_max_length

    @property
    def bps_rd_max(self):
        """Gets the bps_rd_max of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The bps_rd_max of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: float
        """
        return self._bps_rd_max

    @bps_rd_max.setter
    def bps_rd_max(self, bps_rd_max):
        """Sets the bps_rd_max of this NvmfNamespaceCreationParams.


        :param bps_rd_max: The bps_rd_max of this NvmfNamespaceCreationParams.  # noqa: E501
        :type bps_rd_max: float
        """

        self._bps_rd_max = bps_rd_max

    @property
    def bps_max_length(self):
        """Gets the bps_max_length of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The bps_max_length of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: float
        """
        return self._bps_max_length

    @bps_max_length.setter
    def bps_max_length(self, bps_max_length):
        """Sets the bps_max_length of this NvmfNamespaceCreationParams.


        :param bps_max_length: The bps_max_length of this NvmfNamespaceCreationParams.  # noqa: E501
        :type bps_max_length: float
        """

        self._bps_max_length = bps_max_length

    @property
    def bps_max(self):
        """Gets the bps_max of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The bps_max of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: float
        """
        return self._bps_max

    @bps_max.setter
    def bps_max(self, bps_max):
        """Sets the bps_max of this NvmfNamespaceCreationParams.


        :param bps_max: The bps_max of this NvmfNamespaceCreationParams.  # noqa: E501
        :type bps_max: float
        """

        self._bps_max = bps_max

    @property
    def iops_wr_max_length(self):
        """Gets the iops_wr_max_length of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The iops_wr_max_length of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: float
        """
        return self._iops_wr_max_length

    @iops_wr_max_length.setter
    def iops_wr_max_length(self, iops_wr_max_length):
        """Sets the iops_wr_max_length of this NvmfNamespaceCreationParams.


        :param iops_wr_max_length: The iops_wr_max_length of this NvmfNamespaceCreationParams.  # noqa: E501
        :type iops_wr_max_length: float
        """

        self._iops_wr_max_length = iops_wr_max_length

    @property
    def iops_wr_max(self):
        """Gets the iops_wr_max of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The iops_wr_max of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: float
        """
        return self._iops_wr_max

    @iops_wr_max.setter
    def iops_wr_max(self, iops_wr_max):
        """Sets the iops_wr_max of this NvmfNamespaceCreationParams.


        :param iops_wr_max: The iops_wr_max of this NvmfNamespaceCreationParams.  # noqa: E501
        :type iops_wr_max: float
        """

        self._iops_wr_max = iops_wr_max

    @property
    def iops_rd_max_length(self):
        """Gets the iops_rd_max_length of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The iops_rd_max_length of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: float
        """
        return self._iops_rd_max_length

    @iops_rd_max_length.setter
    def iops_rd_max_length(self, iops_rd_max_length):
        """Sets the iops_rd_max_length of this NvmfNamespaceCreationParams.


        :param iops_rd_max_length: The iops_rd_max_length of this NvmfNamespaceCreationParams.  # noqa: E501
        :type iops_rd_max_length: float
        """

        self._iops_rd_max_length = iops_rd_max_length

    @property
    def iops_rd_max(self):
        """Gets the iops_rd_max of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The iops_rd_max of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: float
        """
        return self._iops_rd_max

    @iops_rd_max.setter
    def iops_rd_max(self, iops_rd_max):
        """Sets the iops_rd_max of this NvmfNamespaceCreationParams.


        :param iops_rd_max: The iops_rd_max of this NvmfNamespaceCreationParams.  # noqa: E501
        :type iops_rd_max: float
        """

        self._iops_rd_max = iops_rd_max

    @property
    def iops_max_length(self):
        """Gets the iops_max_length of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The iops_max_length of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: float
        """
        return self._iops_max_length

    @iops_max_length.setter
    def iops_max_length(self, iops_max_length):
        """Sets the iops_max_length of this NvmfNamespaceCreationParams.


        :param iops_max_length: The iops_max_length of this NvmfNamespaceCreationParams.  # noqa: E501
        :type iops_max_length: float
        """

        self._iops_max_length = iops_max_length

    @property
    def iops_max(self):
        """Gets the iops_max of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The iops_max of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: float
        """
        return self._iops_max

    @iops_max.setter
    def iops_max(self, iops_max):
        """Sets the iops_max of this NvmfNamespaceCreationParams.


        :param iops_max: The iops_max of this NvmfNamespaceCreationParams.  # noqa: E501
        :type iops_max: float
        """

        self._iops_max = iops_max

    @property
    def bps_wr(self):
        """Gets the bps_wr of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The bps_wr of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: float
        """
        return self._bps_wr

    @bps_wr.setter
    def bps_wr(self, bps_wr):
        """Sets the bps_wr of this NvmfNamespaceCreationParams.


        :param bps_wr: The bps_wr of this NvmfNamespaceCreationParams.  # noqa: E501
        :type bps_wr: float
        """

        self._bps_wr = bps_wr

    @property
    def bps_rd(self):
        """Gets the bps_rd of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The bps_rd of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: float
        """
        return self._bps_rd

    @bps_rd.setter
    def bps_rd(self, bps_rd):
        """Sets the bps_rd of this NvmfNamespaceCreationParams.


        :param bps_rd: The bps_rd of this NvmfNamespaceCreationParams.  # noqa: E501
        :type bps_rd: float
        """

        self._bps_rd = bps_rd

    @property
    def bps(self):
        """Gets the bps of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The bps of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: float
        """
        return self._bps

    @bps.setter
    def bps(self, bps):
        """Sets the bps of this NvmfNamespaceCreationParams.


        :param bps: The bps of this NvmfNamespaceCreationParams.  # noqa: E501
        :type bps: float
        """

        self._bps = bps

    @property
    def iops_wr(self):
        """Gets the iops_wr of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The iops_wr of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: float
        """
        return self._iops_wr

    @iops_wr.setter
    def iops_wr(self, iops_wr):
        """Sets the iops_wr of this NvmfNamespaceCreationParams.


        :param iops_wr: The iops_wr of this NvmfNamespaceCreationParams.  # noqa: E501
        :type iops_wr: float
        """

        self._iops_wr = iops_wr

    @property
    def iops_rd(self):
        """Gets the iops_rd of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The iops_rd of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: float
        """
        return self._iops_rd

    @iops_rd.setter
    def iops_rd(self, iops_rd):
        """Sets the iops_rd of this NvmfNamespaceCreationParams.


        :param iops_rd: The iops_rd of this NvmfNamespaceCreationParams.  # noqa: E501
        :type iops_rd: float
        """

        self._iops_rd = iops_rd

    @property
    def iops(self):
        """Gets the iops of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The iops of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: float
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """Sets the iops of this NvmfNamespaceCreationParams.


        :param iops: The iops of this NvmfNamespaceCreationParams.  # noqa: E501
        :type iops: float
        """

        self._iops = iops

    @property
    def nqn_whitelist(self):
        """Gets the nqn_whitelist of this NvmfNamespaceCreationParams.  # noqa: E501


        :return: The nqn_whitelist of this NvmfNamespaceCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._nqn_whitelist

    @nqn_whitelist.setter
    def nqn_whitelist(self, nqn_whitelist):
        """Sets the nqn_whitelist of this NvmfNamespaceCreationParams.


        :param nqn_whitelist: The nqn_whitelist of this NvmfNamespaceCreationParams.  # noqa: E501
        :type nqn_whitelist: str
        """

        self._nqn_whitelist = nqn_whitelist

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
        if not isinstance(other, NvmfNamespaceCreationParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NvmfNamespaceCreationParams):
            return True

        return self.to_dict() != other.to_dict()
