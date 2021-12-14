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


class NestedFrozenDisks(object):
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
        'boot': 'float',
        'bus': 'Bus',
        'disabled': 'bool',
        'disk_name': 'str',
        'elf_image_local_id': 'str',
        'image_name': 'str',
        'index': 'int',
        'key': 'int',
        'max_bandwidth': 'float',
        'max_bandwidth_policy': 'VmDiskIoRestrictType',
        'max_iops': 'int',
        'max_iops_policy': 'VmDiskIoRestrictType',
        'path': 'str',
        'size': 'float',
        'snapshot_local_id': 'str',
        'storage_policy_uuid': 'str',
        'svt_image_local_id': 'str',
        'type': 'VmDiskType',
        'vm_volume_local_id': 'str'
    }

    attribute_map = {
        'boot': 'boot',
        'bus': 'bus',
        'disabled': 'disabled',
        'disk_name': 'disk_name',
        'elf_image_local_id': 'elf_image_local_id',
        'image_name': 'image_name',
        'index': 'index',
        'key': 'key',
        'max_bandwidth': 'max_bandwidth',
        'max_bandwidth_policy': 'max_bandwidth_policy',
        'max_iops': 'max_iops',
        'max_iops_policy': 'max_iops_policy',
        'path': 'path',
        'size': 'size',
        'snapshot_local_id': 'snapshot_local_id',
        'storage_policy_uuid': 'storage_policy_uuid',
        'svt_image_local_id': 'svt_image_local_id',
        'type': 'type',
        'vm_volume_local_id': 'vm_volume_local_id'
    }

    def __init__(self, boot=None, bus=None, disabled=None, disk_name=None, elf_image_local_id=None, image_name=None, index=None, key=None, max_bandwidth=None, max_bandwidth_policy=None, max_iops=None, max_iops_policy=None, path=None, size=None, snapshot_local_id=None, storage_policy_uuid=None, svt_image_local_id=None, type=None, vm_volume_local_id=None, local_vars_configuration=None):  # noqa: E501
        """NestedFrozenDisks - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._boot = None
        self._bus = None
        self._disabled = None
        self._disk_name = None
        self._elf_image_local_id = None
        self._image_name = None
        self._index = None
        self._key = None
        self._max_bandwidth = None
        self._max_bandwidth_policy = None
        self._max_iops = None
        self._max_iops_policy = None
        self._path = None
        self._size = None
        self._snapshot_local_id = None
        self._storage_policy_uuid = None
        self._svt_image_local_id = None
        self._type = None
        self._vm_volume_local_id = None
        self.discriminator = None

        self.boot = boot
        self.bus = bus
        self.disabled = disabled
        self.disk_name = disk_name
        self.elf_image_local_id = elf_image_local_id
        self.image_name = image_name
        self.index = index
        self.key = key
        self.max_bandwidth = max_bandwidth
        self.max_bandwidth_policy = max_bandwidth_policy
        self.max_iops = max_iops
        self.max_iops_policy = max_iops_policy
        self.path = path
        self.size = size
        self.snapshot_local_id = snapshot_local_id
        self.storage_policy_uuid = storage_policy_uuid
        self.svt_image_local_id = svt_image_local_id
        self.type = type
        self.vm_volume_local_id = vm_volume_local_id

    @property
    def boot(self):
        """Gets the boot of this NestedFrozenDisks.  # noqa: E501


        :return: The boot of this NestedFrozenDisks.  # noqa: E501
        :rtype: float
        """
        return self._boot

    @boot.setter
    def boot(self, boot):
        """Sets the boot of this NestedFrozenDisks.


        :param boot: The boot of this NestedFrozenDisks.  # noqa: E501
        :type boot: float
        """
        if self.local_vars_configuration.client_side_validation and boot is None:  # noqa: E501
            raise ValueError("Invalid value for `boot`, must not be `None`")  # noqa: E501

        self._boot = boot

    @property
    def bus(self):
        """Gets the bus of this NestedFrozenDisks.  # noqa: E501


        :return: The bus of this NestedFrozenDisks.  # noqa: E501
        :rtype: Bus
        """
        return self._bus

    @bus.setter
    def bus(self, bus):
        """Sets the bus of this NestedFrozenDisks.


        :param bus: The bus of this NestedFrozenDisks.  # noqa: E501
        :type bus: Bus
        """
        if self.local_vars_configuration.client_side_validation and bus is None:  # noqa: E501
            raise ValueError("Invalid value for `bus`, must not be `None`")  # noqa: E501

        self._bus = bus

    @property
    def disabled(self):
        """Gets the disabled of this NestedFrozenDisks.  # noqa: E501


        :return: The disabled of this NestedFrozenDisks.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this NestedFrozenDisks.


        :param disabled: The disabled of this NestedFrozenDisks.  # noqa: E501
        :type disabled: bool
        """

        self._disabled = disabled

    @property
    def disk_name(self):
        """Gets the disk_name of this NestedFrozenDisks.  # noqa: E501


        :return: The disk_name of this NestedFrozenDisks.  # noqa: E501
        :rtype: str
        """
        return self._disk_name

    @disk_name.setter
    def disk_name(self, disk_name):
        """Sets the disk_name of this NestedFrozenDisks.


        :param disk_name: The disk_name of this NestedFrozenDisks.  # noqa: E501
        :type disk_name: str
        """

        self._disk_name = disk_name

    @property
    def elf_image_local_id(self):
        """Gets the elf_image_local_id of this NestedFrozenDisks.  # noqa: E501


        :return: The elf_image_local_id of this NestedFrozenDisks.  # noqa: E501
        :rtype: str
        """
        return self._elf_image_local_id

    @elf_image_local_id.setter
    def elf_image_local_id(self, elf_image_local_id):
        """Sets the elf_image_local_id of this NestedFrozenDisks.


        :param elf_image_local_id: The elf_image_local_id of this NestedFrozenDisks.  # noqa: E501
        :type elf_image_local_id: str
        """
        if self.local_vars_configuration.client_side_validation and elf_image_local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `elf_image_local_id`, must not be `None`")  # noqa: E501

        self._elf_image_local_id = elf_image_local_id

    @property
    def image_name(self):
        """Gets the image_name of this NestedFrozenDisks.  # noqa: E501


        :return: The image_name of this NestedFrozenDisks.  # noqa: E501
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this NestedFrozenDisks.


        :param image_name: The image_name of this NestedFrozenDisks.  # noqa: E501
        :type image_name: str
        """

        self._image_name = image_name

    @property
    def index(self):
        """Gets the index of this NestedFrozenDisks.  # noqa: E501


        :return: The index of this NestedFrozenDisks.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this NestedFrozenDisks.


        :param index: The index of this NestedFrozenDisks.  # noqa: E501
        :type index: int
        """
        if self.local_vars_configuration.client_side_validation and index is None:  # noqa: E501
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def key(self):
        """Gets the key of this NestedFrozenDisks.  # noqa: E501


        :return: The key of this NestedFrozenDisks.  # noqa: E501
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this NestedFrozenDisks.


        :param key: The key of this NestedFrozenDisks.  # noqa: E501
        :type key: int
        """

        self._key = key

    @property
    def max_bandwidth(self):
        """Gets the max_bandwidth of this NestedFrozenDisks.  # noqa: E501


        :return: The max_bandwidth of this NestedFrozenDisks.  # noqa: E501
        :rtype: float
        """
        return self._max_bandwidth

    @max_bandwidth.setter
    def max_bandwidth(self, max_bandwidth):
        """Sets the max_bandwidth of this NestedFrozenDisks.


        :param max_bandwidth: The max_bandwidth of this NestedFrozenDisks.  # noqa: E501
        :type max_bandwidth: float
        """

        self._max_bandwidth = max_bandwidth

    @property
    def max_bandwidth_policy(self):
        """Gets the max_bandwidth_policy of this NestedFrozenDisks.  # noqa: E501


        :return: The max_bandwidth_policy of this NestedFrozenDisks.  # noqa: E501
        :rtype: VmDiskIoRestrictType
        """
        return self._max_bandwidth_policy

    @max_bandwidth_policy.setter
    def max_bandwidth_policy(self, max_bandwidth_policy):
        """Sets the max_bandwidth_policy of this NestedFrozenDisks.


        :param max_bandwidth_policy: The max_bandwidth_policy of this NestedFrozenDisks.  # noqa: E501
        :type max_bandwidth_policy: VmDiskIoRestrictType
        """

        self._max_bandwidth_policy = max_bandwidth_policy

    @property
    def max_iops(self):
        """Gets the max_iops of this NestedFrozenDisks.  # noqa: E501


        :return: The max_iops of this NestedFrozenDisks.  # noqa: E501
        :rtype: int
        """
        return self._max_iops

    @max_iops.setter
    def max_iops(self, max_iops):
        """Sets the max_iops of this NestedFrozenDisks.


        :param max_iops: The max_iops of this NestedFrozenDisks.  # noqa: E501
        :type max_iops: int
        """

        self._max_iops = max_iops

    @property
    def max_iops_policy(self):
        """Gets the max_iops_policy of this NestedFrozenDisks.  # noqa: E501


        :return: The max_iops_policy of this NestedFrozenDisks.  # noqa: E501
        :rtype: VmDiskIoRestrictType
        """
        return self._max_iops_policy

    @max_iops_policy.setter
    def max_iops_policy(self, max_iops_policy):
        """Sets the max_iops_policy of this NestedFrozenDisks.


        :param max_iops_policy: The max_iops_policy of this NestedFrozenDisks.  # noqa: E501
        :type max_iops_policy: VmDiskIoRestrictType
        """

        self._max_iops_policy = max_iops_policy

    @property
    def path(self):
        """Gets the path of this NestedFrozenDisks.  # noqa: E501


        :return: The path of this NestedFrozenDisks.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this NestedFrozenDisks.


        :param path: The path of this NestedFrozenDisks.  # noqa: E501
        :type path: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def size(self):
        """Gets the size of this NestedFrozenDisks.  # noqa: E501


        :return: The size of this NestedFrozenDisks.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this NestedFrozenDisks.


        :param size: The size of this NestedFrozenDisks.  # noqa: E501
        :type size: float
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def snapshot_local_id(self):
        """Gets the snapshot_local_id of this NestedFrozenDisks.  # noqa: E501


        :return: The snapshot_local_id of this NestedFrozenDisks.  # noqa: E501
        :rtype: str
        """
        return self._snapshot_local_id

    @snapshot_local_id.setter
    def snapshot_local_id(self, snapshot_local_id):
        """Sets the snapshot_local_id of this NestedFrozenDisks.


        :param snapshot_local_id: The snapshot_local_id of this NestedFrozenDisks.  # noqa: E501
        :type snapshot_local_id: str
        """

        self._snapshot_local_id = snapshot_local_id

    @property
    def storage_policy_uuid(self):
        """Gets the storage_policy_uuid of this NestedFrozenDisks.  # noqa: E501


        :return: The storage_policy_uuid of this NestedFrozenDisks.  # noqa: E501
        :rtype: str
        """
        return self._storage_policy_uuid

    @storage_policy_uuid.setter
    def storage_policy_uuid(self, storage_policy_uuid):
        """Sets the storage_policy_uuid of this NestedFrozenDisks.


        :param storage_policy_uuid: The storage_policy_uuid of this NestedFrozenDisks.  # noqa: E501
        :type storage_policy_uuid: str
        """
        if self.local_vars_configuration.client_side_validation and storage_policy_uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `storage_policy_uuid`, must not be `None`")  # noqa: E501

        self._storage_policy_uuid = storage_policy_uuid

    @property
    def svt_image_local_id(self):
        """Gets the svt_image_local_id of this NestedFrozenDisks.  # noqa: E501


        :return: The svt_image_local_id of this NestedFrozenDisks.  # noqa: E501
        :rtype: str
        """
        return self._svt_image_local_id

    @svt_image_local_id.setter
    def svt_image_local_id(self, svt_image_local_id):
        """Sets the svt_image_local_id of this NestedFrozenDisks.


        :param svt_image_local_id: The svt_image_local_id of this NestedFrozenDisks.  # noqa: E501
        :type svt_image_local_id: str
        """
        if self.local_vars_configuration.client_side_validation and svt_image_local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `svt_image_local_id`, must not be `None`")  # noqa: E501

        self._svt_image_local_id = svt_image_local_id

    @property
    def type(self):
        """Gets the type of this NestedFrozenDisks.  # noqa: E501


        :return: The type of this NestedFrozenDisks.  # noqa: E501
        :rtype: VmDiskType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NestedFrozenDisks.


        :param type: The type of this NestedFrozenDisks.  # noqa: E501
        :type type: VmDiskType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def vm_volume_local_id(self):
        """Gets the vm_volume_local_id of this NestedFrozenDisks.  # noqa: E501


        :return: The vm_volume_local_id of this NestedFrozenDisks.  # noqa: E501
        :rtype: str
        """
        return self._vm_volume_local_id

    @vm_volume_local_id.setter
    def vm_volume_local_id(self, vm_volume_local_id):
        """Sets the vm_volume_local_id of this NestedFrozenDisks.


        :param vm_volume_local_id: The vm_volume_local_id of this NestedFrozenDisks.  # noqa: E501
        :type vm_volume_local_id: str
        """
        if self.local_vars_configuration.client_side_validation and vm_volume_local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `vm_volume_local_id`, must not be `None`")  # noqa: E501

        self._vm_volume_local_id = vm_volume_local_id

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
        if not isinstance(other, NestedFrozenDisks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedFrozenDisks):
            return True

        return self.to_dict() != other.to_dict()
