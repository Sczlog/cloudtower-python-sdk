# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 1.10.0
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


class Zone(object):
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
        'cluster': 'NestedCluster',
        'datacenter': 'NestedDatacenter',
        'failure_data_space': 'int',
        'host_num': 'int',
        'hosts': 'list[NestedHost]',
        'id': 'str',
        'is_preferred': 'bool',
        'local_id': 'str',
        'provisioned_cpu_cores': 'int',
        'provisioned_cpu_cores_for_active_vm': 'int',
        'provisioned_data_space': 'int',
        'provisioned_memory_bytes': 'int',
        'running_vm_num': 'int',
        'stopped_vm_num': 'int',
        'suspended_vm_num': 'int',
        'total_cache_capacity': 'int',
        'total_cpu_cores': 'int',
        'total_cpu_hz': 'int',
        'total_data_capacity': 'int',
        'total_memory_bytes': 'int',
        'used_data_space': 'int',
        'valid_data_space': 'int',
        'vm_num': 'int'
    }

    attribute_map = {
        'cluster': 'cluster',
        'datacenter': 'datacenter',
        'failure_data_space': 'failure_data_space',
        'host_num': 'host_num',
        'hosts': 'hosts',
        'id': 'id',
        'is_preferred': 'is_preferred',
        'local_id': 'local_id',
        'provisioned_cpu_cores': 'provisioned_cpu_cores',
        'provisioned_cpu_cores_for_active_vm': 'provisioned_cpu_cores_for_active_vm',
        'provisioned_data_space': 'provisioned_data_space',
        'provisioned_memory_bytes': 'provisioned_memory_bytes',
        'running_vm_num': 'running_vm_num',
        'stopped_vm_num': 'stopped_vm_num',
        'suspended_vm_num': 'suspended_vm_num',
        'total_cache_capacity': 'total_cache_capacity',
        'total_cpu_cores': 'total_cpu_cores',
        'total_cpu_hz': 'total_cpu_hz',
        'total_data_capacity': 'total_data_capacity',
        'total_memory_bytes': 'total_memory_bytes',
        'used_data_space': 'used_data_space',
        'valid_data_space': 'valid_data_space',
        'vm_num': 'vm_num'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """Zone - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._cluster = None
        self._datacenter = None
        self._failure_data_space = None
        self._host_num = None
        self._hosts = None
        self._id = None
        self._is_preferred = None
        self._local_id = None
        self._provisioned_cpu_cores = None
        self._provisioned_cpu_cores_for_active_vm = None
        self._provisioned_data_space = None
        self._provisioned_memory_bytes = None
        self._running_vm_num = None
        self._stopped_vm_num = None
        self._suspended_vm_num = None
        self._total_cache_capacity = None
        self._total_cpu_cores = None
        self._total_cpu_hz = None
        self._total_data_capacity = None
        self._total_memory_bytes = None
        self._used_data_space = None
        self._valid_data_space = None
        self._vm_num = None
        self.discriminator = None

        if "cluster" in kwargs:
            self.cluster = kwargs["cluster"]
        if "datacenter" in kwargs:
            self.datacenter = kwargs["datacenter"]
        self.failure_data_space = kwargs.get("failure_data_space", None)
        self.host_num = kwargs.get("host_num", None)
        self.hosts = kwargs.get("hosts", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "is_preferred" in kwargs:
            self.is_preferred = kwargs["is_preferred"]
        self.local_id = kwargs.get("local_id", None)
        self.provisioned_cpu_cores = kwargs.get("provisioned_cpu_cores", None)
        self.provisioned_cpu_cores_for_active_vm = kwargs.get("provisioned_cpu_cores_for_active_vm", None)
        self.provisioned_data_space = kwargs.get("provisioned_data_space", None)
        self.provisioned_memory_bytes = kwargs.get("provisioned_memory_bytes", None)
        self.running_vm_num = kwargs.get("running_vm_num", None)
        self.stopped_vm_num = kwargs.get("stopped_vm_num", None)
        self.suspended_vm_num = kwargs.get("suspended_vm_num", None)
        self.total_cache_capacity = kwargs.get("total_cache_capacity", None)
        self.total_cpu_cores = kwargs.get("total_cpu_cores", None)
        self.total_cpu_hz = kwargs.get("total_cpu_hz", None)
        self.total_data_capacity = kwargs.get("total_data_capacity", None)
        self.total_memory_bytes = kwargs.get("total_memory_bytes", None)
        self.used_data_space = kwargs.get("used_data_space", None)
        self.valid_data_space = kwargs.get("valid_data_space", None)
        self.vm_num = kwargs.get("vm_num", None)

    @property
    def cluster(self):
        """Gets the cluster of this Zone.  # noqa: E501


        :return: The cluster of this Zone.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this Zone.


        :param cluster: The cluster of this Zone.  # noqa: E501
        :type cluster: NestedCluster
        """
        if self.local_vars_configuration.client_side_validation and cluster is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster`, must not be `None`")  # noqa: E501

        self._cluster = cluster

    @property
    def datacenter(self):
        """Gets the datacenter of this Zone.  # noqa: E501


        :return: The datacenter of this Zone.  # noqa: E501
        :rtype: NestedDatacenter
        """
        return self._datacenter

    @datacenter.setter
    def datacenter(self, datacenter):
        """Sets the datacenter of this Zone.


        :param datacenter: The datacenter of this Zone.  # noqa: E501
        :type datacenter: NestedDatacenter
        """
        if self.local_vars_configuration.client_side_validation and datacenter is None:  # noqa: E501
            raise ValueError("Invalid value for `datacenter`, must not be `None`")  # noqa: E501

        self._datacenter = datacenter

    @property
    def failure_data_space(self):
        """Gets the failure_data_space of this Zone.  # noqa: E501


        :return: The failure_data_space of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._failure_data_space

    @failure_data_space.setter
    def failure_data_space(self, failure_data_space):
        """Sets the failure_data_space of this Zone.


        :param failure_data_space: The failure_data_space of this Zone.  # noqa: E501
        :type failure_data_space: int
        """

        self._failure_data_space = failure_data_space

    @property
    def host_num(self):
        """Gets the host_num of this Zone.  # noqa: E501


        :return: The host_num of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        """Sets the host_num of this Zone.


        :param host_num: The host_num of this Zone.  # noqa: E501
        :type host_num: int
        """

        self._host_num = host_num

    @property
    def hosts(self):
        """Gets the hosts of this Zone.  # noqa: E501


        :return: The hosts of this Zone.  # noqa: E501
        :rtype: list[NestedHost]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this Zone.


        :param hosts: The hosts of this Zone.  # noqa: E501
        :type hosts: list[NestedHost]
        """

        self._hosts = hosts

    @property
    def id(self):
        """Gets the id of this Zone.  # noqa: E501


        :return: The id of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Zone.


        :param id: The id of this Zone.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_preferred(self):
        """Gets the is_preferred of this Zone.  # noqa: E501


        :return: The is_preferred of this Zone.  # noqa: E501
        :rtype: bool
        """
        return self._is_preferred

    @is_preferred.setter
    def is_preferred(self, is_preferred):
        """Sets the is_preferred of this Zone.


        :param is_preferred: The is_preferred of this Zone.  # noqa: E501
        :type is_preferred: bool
        """
        if self.local_vars_configuration.client_side_validation and is_preferred is None:  # noqa: E501
            raise ValueError("Invalid value for `is_preferred`, must not be `None`")  # noqa: E501

        self._is_preferred = is_preferred

    @property
    def local_id(self):
        """Gets the local_id of this Zone.  # noqa: E501


        :return: The local_id of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this Zone.


        :param local_id: The local_id of this Zone.  # noqa: E501
        :type local_id: str
        """

        self._local_id = local_id

    @property
    def provisioned_cpu_cores(self):
        """Gets the provisioned_cpu_cores of this Zone.  # noqa: E501


        :return: The provisioned_cpu_cores of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._provisioned_cpu_cores

    @provisioned_cpu_cores.setter
    def provisioned_cpu_cores(self, provisioned_cpu_cores):
        """Sets the provisioned_cpu_cores of this Zone.


        :param provisioned_cpu_cores: The provisioned_cpu_cores of this Zone.  # noqa: E501
        :type provisioned_cpu_cores: int
        """

        self._provisioned_cpu_cores = provisioned_cpu_cores

    @property
    def provisioned_cpu_cores_for_active_vm(self):
        """Gets the provisioned_cpu_cores_for_active_vm of this Zone.  # noqa: E501


        :return: The provisioned_cpu_cores_for_active_vm of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._provisioned_cpu_cores_for_active_vm

    @provisioned_cpu_cores_for_active_vm.setter
    def provisioned_cpu_cores_for_active_vm(self, provisioned_cpu_cores_for_active_vm):
        """Sets the provisioned_cpu_cores_for_active_vm of this Zone.


        :param provisioned_cpu_cores_for_active_vm: The provisioned_cpu_cores_for_active_vm of this Zone.  # noqa: E501
        :type provisioned_cpu_cores_for_active_vm: int
        """

        self._provisioned_cpu_cores_for_active_vm = provisioned_cpu_cores_for_active_vm

    @property
    def provisioned_data_space(self):
        """Gets the provisioned_data_space of this Zone.  # noqa: E501


        :return: The provisioned_data_space of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._provisioned_data_space

    @provisioned_data_space.setter
    def provisioned_data_space(self, provisioned_data_space):
        """Sets the provisioned_data_space of this Zone.


        :param provisioned_data_space: The provisioned_data_space of this Zone.  # noqa: E501
        :type provisioned_data_space: int
        """

        self._provisioned_data_space = provisioned_data_space

    @property
    def provisioned_memory_bytes(self):
        """Gets the provisioned_memory_bytes of this Zone.  # noqa: E501


        :return: The provisioned_memory_bytes of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._provisioned_memory_bytes

    @provisioned_memory_bytes.setter
    def provisioned_memory_bytes(self, provisioned_memory_bytes):
        """Sets the provisioned_memory_bytes of this Zone.


        :param provisioned_memory_bytes: The provisioned_memory_bytes of this Zone.  # noqa: E501
        :type provisioned_memory_bytes: int
        """

        self._provisioned_memory_bytes = provisioned_memory_bytes

    @property
    def running_vm_num(self):
        """Gets the running_vm_num of this Zone.  # noqa: E501


        :return: The running_vm_num of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._running_vm_num

    @running_vm_num.setter
    def running_vm_num(self, running_vm_num):
        """Sets the running_vm_num of this Zone.


        :param running_vm_num: The running_vm_num of this Zone.  # noqa: E501
        :type running_vm_num: int
        """

        self._running_vm_num = running_vm_num

    @property
    def stopped_vm_num(self):
        """Gets the stopped_vm_num of this Zone.  # noqa: E501


        :return: The stopped_vm_num of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._stopped_vm_num

    @stopped_vm_num.setter
    def stopped_vm_num(self, stopped_vm_num):
        """Sets the stopped_vm_num of this Zone.


        :param stopped_vm_num: The stopped_vm_num of this Zone.  # noqa: E501
        :type stopped_vm_num: int
        """

        self._stopped_vm_num = stopped_vm_num

    @property
    def suspended_vm_num(self):
        """Gets the suspended_vm_num of this Zone.  # noqa: E501


        :return: The suspended_vm_num of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._suspended_vm_num

    @suspended_vm_num.setter
    def suspended_vm_num(self, suspended_vm_num):
        """Sets the suspended_vm_num of this Zone.


        :param suspended_vm_num: The suspended_vm_num of this Zone.  # noqa: E501
        :type suspended_vm_num: int
        """

        self._suspended_vm_num = suspended_vm_num

    @property
    def total_cache_capacity(self):
        """Gets the total_cache_capacity of this Zone.  # noqa: E501


        :return: The total_cache_capacity of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._total_cache_capacity

    @total_cache_capacity.setter
    def total_cache_capacity(self, total_cache_capacity):
        """Sets the total_cache_capacity of this Zone.


        :param total_cache_capacity: The total_cache_capacity of this Zone.  # noqa: E501
        :type total_cache_capacity: int
        """

        self._total_cache_capacity = total_cache_capacity

    @property
    def total_cpu_cores(self):
        """Gets the total_cpu_cores of this Zone.  # noqa: E501


        :return: The total_cpu_cores of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._total_cpu_cores

    @total_cpu_cores.setter
    def total_cpu_cores(self, total_cpu_cores):
        """Sets the total_cpu_cores of this Zone.


        :param total_cpu_cores: The total_cpu_cores of this Zone.  # noqa: E501
        :type total_cpu_cores: int
        """

        self._total_cpu_cores = total_cpu_cores

    @property
    def total_cpu_hz(self):
        """Gets the total_cpu_hz of this Zone.  # noqa: E501


        :return: The total_cpu_hz of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._total_cpu_hz

    @total_cpu_hz.setter
    def total_cpu_hz(self, total_cpu_hz):
        """Sets the total_cpu_hz of this Zone.


        :param total_cpu_hz: The total_cpu_hz of this Zone.  # noqa: E501
        :type total_cpu_hz: int
        """

        self._total_cpu_hz = total_cpu_hz

    @property
    def total_data_capacity(self):
        """Gets the total_data_capacity of this Zone.  # noqa: E501


        :return: The total_data_capacity of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._total_data_capacity

    @total_data_capacity.setter
    def total_data_capacity(self, total_data_capacity):
        """Sets the total_data_capacity of this Zone.


        :param total_data_capacity: The total_data_capacity of this Zone.  # noqa: E501
        :type total_data_capacity: int
        """

        self._total_data_capacity = total_data_capacity

    @property
    def total_memory_bytes(self):
        """Gets the total_memory_bytes of this Zone.  # noqa: E501


        :return: The total_memory_bytes of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._total_memory_bytes

    @total_memory_bytes.setter
    def total_memory_bytes(self, total_memory_bytes):
        """Sets the total_memory_bytes of this Zone.


        :param total_memory_bytes: The total_memory_bytes of this Zone.  # noqa: E501
        :type total_memory_bytes: int
        """

        self._total_memory_bytes = total_memory_bytes

    @property
    def used_data_space(self):
        """Gets the used_data_space of this Zone.  # noqa: E501


        :return: The used_data_space of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._used_data_space

    @used_data_space.setter
    def used_data_space(self, used_data_space):
        """Sets the used_data_space of this Zone.


        :param used_data_space: The used_data_space of this Zone.  # noqa: E501
        :type used_data_space: int
        """

        self._used_data_space = used_data_space

    @property
    def valid_data_space(self):
        """Gets the valid_data_space of this Zone.  # noqa: E501


        :return: The valid_data_space of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._valid_data_space

    @valid_data_space.setter
    def valid_data_space(self, valid_data_space):
        """Sets the valid_data_space of this Zone.


        :param valid_data_space: The valid_data_space of this Zone.  # noqa: E501
        :type valid_data_space: int
        """

        self._valid_data_space = valid_data_space

    @property
    def vm_num(self):
        """Gets the vm_num of this Zone.  # noqa: E501


        :return: The vm_num of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._vm_num

    @vm_num.setter
    def vm_num(self, vm_num):
        """Sets the vm_num of this Zone.


        :param vm_num: The vm_num of this Zone.  # noqa: E501
        :type vm_num: int
        """

        self._vm_num = vm_num

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
        if not isinstance(other, Zone):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Zone):
            return True

        return self.to_dict() != other.to_dict()
