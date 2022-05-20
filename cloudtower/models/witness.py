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


class Witness(object):
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
        'cpu_hz_per_core': 'int',
        'data_ip': 'str',
        'id': 'str',
        'local_id': 'str',
        'name': 'str',
        'system_data_capacity': 'int',
        'system_used_data_space': 'int',
        'total_cpu_cores': 'int',
        'total_cpu_hz': 'int',
        'total_memory_bytes': 'int'
    }

    attribute_map = {
        'cluster': 'cluster',
        'cpu_hz_per_core': 'cpu_hz_per_core',
        'data_ip': 'data_ip',
        'id': 'id',
        'local_id': 'local_id',
        'name': 'name',
        'system_data_capacity': 'system_data_capacity',
        'system_used_data_space': 'system_used_data_space',
        'total_cpu_cores': 'total_cpu_cores',
        'total_cpu_hz': 'total_cpu_hz',
        'total_memory_bytes': 'total_memory_bytes'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """Witness - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._cluster = None
        self._cpu_hz_per_core = None
        self._data_ip = None
        self._id = None
        self._local_id = None
        self._name = None
        self._system_data_capacity = None
        self._system_used_data_space = None
        self._total_cpu_cores = None
        self._total_cpu_hz = None
        self._total_memory_bytes = None
        self.discriminator = None

        if "cluster" in kwargs:
            self.cluster = kwargs["cluster"]
        if "cpu_hz_per_core" in kwargs:
            self.cpu_hz_per_core = kwargs["cpu_hz_per_core"]
        if "data_ip" in kwargs:
            self.data_ip = kwargs["data_ip"]
        if "id" in kwargs:
            self.id = kwargs["id"]
        self.local_id = kwargs.get("local_id", None)
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "system_data_capacity" in kwargs:
            self.system_data_capacity = kwargs["system_data_capacity"]
        if "system_used_data_space" in kwargs:
            self.system_used_data_space = kwargs["system_used_data_space"]
        if "total_cpu_cores" in kwargs:
            self.total_cpu_cores = kwargs["total_cpu_cores"]
        if "total_cpu_hz" in kwargs:
            self.total_cpu_hz = kwargs["total_cpu_hz"]
        if "total_memory_bytes" in kwargs:
            self.total_memory_bytes = kwargs["total_memory_bytes"]

    @property
    def cluster(self):
        """Gets the cluster of this Witness.  # noqa: E501


        :return: The cluster of this Witness.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this Witness.


        :param cluster: The cluster of this Witness.  # noqa: E501
        :type cluster: NestedCluster
        """
        if self.local_vars_configuration.client_side_validation and cluster is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster`, must not be `None`")  # noqa: E501

        self._cluster = cluster

    @property
    def cpu_hz_per_core(self):
        """Gets the cpu_hz_per_core of this Witness.  # noqa: E501


        :return: The cpu_hz_per_core of this Witness.  # noqa: E501
        :rtype: int
        """
        return self._cpu_hz_per_core

    @cpu_hz_per_core.setter
    def cpu_hz_per_core(self, cpu_hz_per_core):
        """Sets the cpu_hz_per_core of this Witness.


        :param cpu_hz_per_core: The cpu_hz_per_core of this Witness.  # noqa: E501
        :type cpu_hz_per_core: int
        """
        if self.local_vars_configuration.client_side_validation and cpu_hz_per_core is None:  # noqa: E501
            raise ValueError("Invalid value for `cpu_hz_per_core`, must not be `None`")  # noqa: E501

        self._cpu_hz_per_core = cpu_hz_per_core

    @property
    def data_ip(self):
        """Gets the data_ip of this Witness.  # noqa: E501


        :return: The data_ip of this Witness.  # noqa: E501
        :rtype: str
        """
        return self._data_ip

    @data_ip.setter
    def data_ip(self, data_ip):
        """Sets the data_ip of this Witness.


        :param data_ip: The data_ip of this Witness.  # noqa: E501
        :type data_ip: str
        """
        if self.local_vars_configuration.client_side_validation and data_ip is None:  # noqa: E501
            raise ValueError("Invalid value for `data_ip`, must not be `None`")  # noqa: E501

        self._data_ip = data_ip

    @property
    def id(self):
        """Gets the id of this Witness.  # noqa: E501


        :return: The id of this Witness.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Witness.


        :param id: The id of this Witness.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def local_id(self):
        """Gets the local_id of this Witness.  # noqa: E501


        :return: The local_id of this Witness.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this Witness.


        :param local_id: The local_id of this Witness.  # noqa: E501
        :type local_id: str
        """

        self._local_id = local_id

    @property
    def name(self):
        """Gets the name of this Witness.  # noqa: E501


        :return: The name of this Witness.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Witness.


        :param name: The name of this Witness.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def system_data_capacity(self):
        """Gets the system_data_capacity of this Witness.  # noqa: E501


        :return: The system_data_capacity of this Witness.  # noqa: E501
        :rtype: int
        """
        return self._system_data_capacity

    @system_data_capacity.setter
    def system_data_capacity(self, system_data_capacity):
        """Sets the system_data_capacity of this Witness.


        :param system_data_capacity: The system_data_capacity of this Witness.  # noqa: E501
        :type system_data_capacity: int
        """
        if self.local_vars_configuration.client_side_validation and system_data_capacity is None:  # noqa: E501
            raise ValueError("Invalid value for `system_data_capacity`, must not be `None`")  # noqa: E501

        self._system_data_capacity = system_data_capacity

    @property
    def system_used_data_space(self):
        """Gets the system_used_data_space of this Witness.  # noqa: E501


        :return: The system_used_data_space of this Witness.  # noqa: E501
        :rtype: int
        """
        return self._system_used_data_space

    @system_used_data_space.setter
    def system_used_data_space(self, system_used_data_space):
        """Sets the system_used_data_space of this Witness.


        :param system_used_data_space: The system_used_data_space of this Witness.  # noqa: E501
        :type system_used_data_space: int
        """
        if self.local_vars_configuration.client_side_validation and system_used_data_space is None:  # noqa: E501
            raise ValueError("Invalid value for `system_used_data_space`, must not be `None`")  # noqa: E501

        self._system_used_data_space = system_used_data_space

    @property
    def total_cpu_cores(self):
        """Gets the total_cpu_cores of this Witness.  # noqa: E501


        :return: The total_cpu_cores of this Witness.  # noqa: E501
        :rtype: int
        """
        return self._total_cpu_cores

    @total_cpu_cores.setter
    def total_cpu_cores(self, total_cpu_cores):
        """Sets the total_cpu_cores of this Witness.


        :param total_cpu_cores: The total_cpu_cores of this Witness.  # noqa: E501
        :type total_cpu_cores: int
        """
        if self.local_vars_configuration.client_side_validation and total_cpu_cores is None:  # noqa: E501
            raise ValueError("Invalid value for `total_cpu_cores`, must not be `None`")  # noqa: E501

        self._total_cpu_cores = total_cpu_cores

    @property
    def total_cpu_hz(self):
        """Gets the total_cpu_hz of this Witness.  # noqa: E501


        :return: The total_cpu_hz of this Witness.  # noqa: E501
        :rtype: int
        """
        return self._total_cpu_hz

    @total_cpu_hz.setter
    def total_cpu_hz(self, total_cpu_hz):
        """Sets the total_cpu_hz of this Witness.


        :param total_cpu_hz: The total_cpu_hz of this Witness.  # noqa: E501
        :type total_cpu_hz: int
        """
        if self.local_vars_configuration.client_side_validation and total_cpu_hz is None:  # noqa: E501
            raise ValueError("Invalid value for `total_cpu_hz`, must not be `None`")  # noqa: E501

        self._total_cpu_hz = total_cpu_hz

    @property
    def total_memory_bytes(self):
        """Gets the total_memory_bytes of this Witness.  # noqa: E501


        :return: The total_memory_bytes of this Witness.  # noqa: E501
        :rtype: int
        """
        return self._total_memory_bytes

    @total_memory_bytes.setter
    def total_memory_bytes(self, total_memory_bytes):
        """Sets the total_memory_bytes of this Witness.


        :param total_memory_bytes: The total_memory_bytes of this Witness.  # noqa: E501
        :type total_memory_bytes: int
        """
        if self.local_vars_configuration.client_side_validation and total_memory_bytes is None:  # noqa: E501
            raise ValueError("Invalid value for `total_memory_bytes`, must not be `None`")  # noqa: E501

        self._total_memory_bytes = total_memory_bytes

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
        if not isinstance(other, Witness):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Witness):
            return True

        return self.to_dict() != other.to_dict()
