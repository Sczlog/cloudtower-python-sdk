# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VmVolumeCreationParams(object):
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
        'elf_storage_policy': 'VmVolumeElfStoragePolicyType',
        'size': 'int',
        'sharing': 'bool',
        'cluster_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'elf_storage_policy': 'elf_storage_policy',
        'size': 'size',
        'sharing': 'sharing',
        'cluster_id': 'cluster_id',
        'name': 'name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VmVolumeCreationParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._elf_storage_policy = None
        self._size = None
        self._sharing = None
        self._cluster_id = None
        self._name = None
        self.discriminator = None

        if "elf_storage_policy" in kwargs:
            self.elf_storage_policy = kwargs["elf_storage_policy"]
        if "size" in kwargs:
            self.size = kwargs["size"]
        if "sharing" in kwargs:
            self.sharing = kwargs["sharing"]
        if "cluster_id" in kwargs:
            self.cluster_id = kwargs["cluster_id"]
        if "name" in kwargs:
            self.name = kwargs["name"]

    @property
    def elf_storage_policy(self):
        """Gets the elf_storage_policy of this VmVolumeCreationParams.  # noqa: E501


        :return: The elf_storage_policy of this VmVolumeCreationParams.  # noqa: E501
        :rtype: VmVolumeElfStoragePolicyType
        """
        return self._elf_storage_policy

    @elf_storage_policy.setter
    def elf_storage_policy(self, elf_storage_policy):
        """Sets the elf_storage_policy of this VmVolumeCreationParams.


        :param elf_storage_policy: The elf_storage_policy of this VmVolumeCreationParams.  # noqa: E501
        :type elf_storage_policy: VmVolumeElfStoragePolicyType
        """
        if self.local_vars_configuration.client_side_validation and elf_storage_policy is None:  # noqa: E501
            raise ValueError("Invalid value for `elf_storage_policy`, must not be `None`")  # noqa: E501

        self._elf_storage_policy = elf_storage_policy

    @property
    def size(self):
        """Gets the size of this VmVolumeCreationParams.  # noqa: E501


        :return: The size of this VmVolumeCreationParams.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this VmVolumeCreationParams.


        :param size: The size of this VmVolumeCreationParams.  # noqa: E501
        :type size: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def sharing(self):
        """Gets the sharing of this VmVolumeCreationParams.  # noqa: E501


        :return: The sharing of this VmVolumeCreationParams.  # noqa: E501
        :rtype: bool
        """
        return self._sharing

    @sharing.setter
    def sharing(self, sharing):
        """Sets the sharing of this VmVolumeCreationParams.


        :param sharing: The sharing of this VmVolumeCreationParams.  # noqa: E501
        :type sharing: bool
        """
        if self.local_vars_configuration.client_side_validation and sharing is None:  # noqa: E501
            raise ValueError("Invalid value for `sharing`, must not be `None`")  # noqa: E501

        self._sharing = sharing

    @property
    def cluster_id(self):
        """Gets the cluster_id of this VmVolumeCreationParams.  # noqa: E501


        :return: The cluster_id of this VmVolumeCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this VmVolumeCreationParams.


        :param cluster_id: The cluster_id of this VmVolumeCreationParams.  # noqa: E501
        :type cluster_id: str
        """
        if self.local_vars_configuration.client_side_validation and cluster_id is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def name(self):
        """Gets the name of this VmVolumeCreationParams.  # noqa: E501


        :return: The name of this VmVolumeCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VmVolumeCreationParams.


        :param name: The name of this VmVolumeCreationParams.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, VmVolumeCreationParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmVolumeCreationParams):
            return True

        return self.to_dict() != other.to_dict()
