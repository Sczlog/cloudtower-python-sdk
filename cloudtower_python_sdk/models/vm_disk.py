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


class VmDisk(object):
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
        'boot': 'int',
        'bus': 'Bus',
        'cloud_init_image_name': 'str',
        'cloud_init_image_path': 'str',
        'device': 'str',
        'disabled': 'bool',
        'elf_image': 'NestedElfImage',
        'id': 'str',
        'key': 'int',
        'max_bandwidth': 'float',
        'max_bandwidth_policy': 'VmDiskIoRestrictType',
        'max_iops': 'int',
        'max_iops_policy': 'VmDiskIoRestrictType',
        'serial': 'str',
        'svt_image': 'NestedSvtImage',
        'type': 'VmDiskType',
        'unsafe_image_path': 'str',
        'unsafe_image_uuid': 'str',
        'unsafe_provision': 'str',
        'vm': 'NestedVm',
        'vm_volume': 'NestedVmVolume'
    }

    attribute_map = {
        'boot': 'boot',
        'bus': 'bus',
        'cloud_init_image_name': 'cloud_init_image_name',
        'cloud_init_image_path': 'cloud_init_image_path',
        'device': 'device',
        'disabled': 'disabled',
        'elf_image': 'elf_image',
        'id': 'id',
        'key': 'key',
        'max_bandwidth': 'max_bandwidth',
        'max_bandwidth_policy': 'max_bandwidth_policy',
        'max_iops': 'max_iops',
        'max_iops_policy': 'max_iops_policy',
        'serial': 'serial',
        'svt_image': 'svt_image',
        'type': 'type',
        'unsafe_image_path': 'unsafe_image_path',
        'unsafe_image_uuid': 'unsafe_image_uuid',
        'unsafe_provision': 'unsafe_provision',
        'vm': 'vm',
        'vm_volume': 'vm_volume'
    }

    def __init__(self, boot=None, bus=None, cloud_init_image_name=None, cloud_init_image_path=None, device=None, disabled=None, elf_image=None, id=None, key=None, max_bandwidth=None, max_bandwidth_policy=None, max_iops=None, max_iops_policy=None, serial=None, svt_image=None, type=None, unsafe_image_path=None, unsafe_image_uuid=None, unsafe_provision=None, vm=None, vm_volume=None, local_vars_configuration=None):  # noqa: E501
        """VmDisk - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._boot = None
        self._bus = None
        self._cloud_init_image_name = None
        self._cloud_init_image_path = None
        self._device = None
        self._disabled = None
        self._elf_image = None
        self._id = None
        self._key = None
        self._max_bandwidth = None
        self._max_bandwidth_policy = None
        self._max_iops = None
        self._max_iops_policy = None
        self._serial = None
        self._svt_image = None
        self._type = None
        self._unsafe_image_path = None
        self._unsafe_image_uuid = None
        self._unsafe_provision = None
        self._vm = None
        self._vm_volume = None
        self.discriminator = None

        self.boot = boot
        self.bus = bus
        self.cloud_init_image_name = cloud_init_image_name
        self.cloud_init_image_path = cloud_init_image_path
        self.device = device
        self.disabled = disabled
        self.elf_image = elf_image
        self.id = id
        self.key = key
        self.max_bandwidth = max_bandwidth
        self.max_bandwidth_policy = max_bandwidth_policy
        self.max_iops = max_iops
        self.max_iops_policy = max_iops_policy
        self.serial = serial
        self.svt_image = svt_image
        self.type = type
        self.unsafe_image_path = unsafe_image_path
        self.unsafe_image_uuid = unsafe_image_uuid
        self.unsafe_provision = unsafe_provision
        self.vm = vm
        self.vm_volume = vm_volume

    @property
    def boot(self):
        """Gets the boot of this VmDisk.  # noqa: E501


        :return: The boot of this VmDisk.  # noqa: E501
        :rtype: int
        """
        return self._boot

    @boot.setter
    def boot(self, boot):
        """Sets the boot of this VmDisk.


        :param boot: The boot of this VmDisk.  # noqa: E501
        :type boot: int
        """
        if self.local_vars_configuration.client_side_validation and boot is None:  # noqa: E501
            raise ValueError("Invalid value for `boot`, must not be `None`")  # noqa: E501

        self._boot = boot

    @property
    def bus(self):
        """Gets the bus of this VmDisk.  # noqa: E501


        :return: The bus of this VmDisk.  # noqa: E501
        :rtype: Bus
        """
        return self._bus

    @bus.setter
    def bus(self, bus):
        """Sets the bus of this VmDisk.


        :param bus: The bus of this VmDisk.  # noqa: E501
        :type bus: Bus
        """
        if self.local_vars_configuration.client_side_validation and bus is None:  # noqa: E501
            raise ValueError("Invalid value for `bus`, must not be `None`")  # noqa: E501

        self._bus = bus

    @property
    def cloud_init_image_name(self):
        """Gets the cloud_init_image_name of this VmDisk.  # noqa: E501


        :return: The cloud_init_image_name of this VmDisk.  # noqa: E501
        :rtype: str
        """
        return self._cloud_init_image_name

    @cloud_init_image_name.setter
    def cloud_init_image_name(self, cloud_init_image_name):
        """Sets the cloud_init_image_name of this VmDisk.


        :param cloud_init_image_name: The cloud_init_image_name of this VmDisk.  # noqa: E501
        :type cloud_init_image_name: str
        """

        self._cloud_init_image_name = cloud_init_image_name

    @property
    def cloud_init_image_path(self):
        """Gets the cloud_init_image_path of this VmDisk.  # noqa: E501


        :return: The cloud_init_image_path of this VmDisk.  # noqa: E501
        :rtype: str
        """
        return self._cloud_init_image_path

    @cloud_init_image_path.setter
    def cloud_init_image_path(self, cloud_init_image_path):
        """Sets the cloud_init_image_path of this VmDisk.


        :param cloud_init_image_path: The cloud_init_image_path of this VmDisk.  # noqa: E501
        :type cloud_init_image_path: str
        """

        self._cloud_init_image_path = cloud_init_image_path

    @property
    def device(self):
        """Gets the device of this VmDisk.  # noqa: E501


        :return: The device of this VmDisk.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this VmDisk.


        :param device: The device of this VmDisk.  # noqa: E501
        :type device: str
        """

        self._device = device

    @property
    def disabled(self):
        """Gets the disabled of this VmDisk.  # noqa: E501


        :return: The disabled of this VmDisk.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this VmDisk.


        :param disabled: The disabled of this VmDisk.  # noqa: E501
        :type disabled: bool
        """

        self._disabled = disabled

    @property
    def elf_image(self):
        """Gets the elf_image of this VmDisk.  # noqa: E501


        :return: The elf_image of this VmDisk.  # noqa: E501
        :rtype: NestedElfImage
        """
        return self._elf_image

    @elf_image.setter
    def elf_image(self, elf_image):
        """Sets the elf_image of this VmDisk.


        :param elf_image: The elf_image of this VmDisk.  # noqa: E501
        :type elf_image: NestedElfImage
        """

        self._elf_image = elf_image

    @property
    def id(self):
        """Gets the id of this VmDisk.  # noqa: E501


        :return: The id of this VmDisk.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VmDisk.


        :param id: The id of this VmDisk.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def key(self):
        """Gets the key of this VmDisk.  # noqa: E501


        :return: The key of this VmDisk.  # noqa: E501
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this VmDisk.


        :param key: The key of this VmDisk.  # noqa: E501
        :type key: int
        """

        self._key = key

    @property
    def max_bandwidth(self):
        """Gets the max_bandwidth of this VmDisk.  # noqa: E501


        :return: The max_bandwidth of this VmDisk.  # noqa: E501
        :rtype: float
        """
        return self._max_bandwidth

    @max_bandwidth.setter
    def max_bandwidth(self, max_bandwidth):
        """Sets the max_bandwidth of this VmDisk.


        :param max_bandwidth: The max_bandwidth of this VmDisk.  # noqa: E501
        :type max_bandwidth: float
        """

        self._max_bandwidth = max_bandwidth

    @property
    def max_bandwidth_policy(self):
        """Gets the max_bandwidth_policy of this VmDisk.  # noqa: E501


        :return: The max_bandwidth_policy of this VmDisk.  # noqa: E501
        :rtype: VmDiskIoRestrictType
        """
        return self._max_bandwidth_policy

    @max_bandwidth_policy.setter
    def max_bandwidth_policy(self, max_bandwidth_policy):
        """Sets the max_bandwidth_policy of this VmDisk.


        :param max_bandwidth_policy: The max_bandwidth_policy of this VmDisk.  # noqa: E501
        :type max_bandwidth_policy: VmDiskIoRestrictType
        """

        self._max_bandwidth_policy = max_bandwidth_policy

    @property
    def max_iops(self):
        """Gets the max_iops of this VmDisk.  # noqa: E501


        :return: The max_iops of this VmDisk.  # noqa: E501
        :rtype: int
        """
        return self._max_iops

    @max_iops.setter
    def max_iops(self, max_iops):
        """Sets the max_iops of this VmDisk.


        :param max_iops: The max_iops of this VmDisk.  # noqa: E501
        :type max_iops: int
        """

        self._max_iops = max_iops

    @property
    def max_iops_policy(self):
        """Gets the max_iops_policy of this VmDisk.  # noqa: E501


        :return: The max_iops_policy of this VmDisk.  # noqa: E501
        :rtype: VmDiskIoRestrictType
        """
        return self._max_iops_policy

    @max_iops_policy.setter
    def max_iops_policy(self, max_iops_policy):
        """Sets the max_iops_policy of this VmDisk.


        :param max_iops_policy: The max_iops_policy of this VmDisk.  # noqa: E501
        :type max_iops_policy: VmDiskIoRestrictType
        """

        self._max_iops_policy = max_iops_policy

    @property
    def serial(self):
        """Gets the serial of this VmDisk.  # noqa: E501


        :return: The serial of this VmDisk.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this VmDisk.


        :param serial: The serial of this VmDisk.  # noqa: E501
        :type serial: str
        """

        self._serial = serial

    @property
    def svt_image(self):
        """Gets the svt_image of this VmDisk.  # noqa: E501


        :return: The svt_image of this VmDisk.  # noqa: E501
        :rtype: NestedSvtImage
        """
        return self._svt_image

    @svt_image.setter
    def svt_image(self, svt_image):
        """Sets the svt_image of this VmDisk.


        :param svt_image: The svt_image of this VmDisk.  # noqa: E501
        :type svt_image: NestedSvtImage
        """

        self._svt_image = svt_image

    @property
    def type(self):
        """Gets the type of this VmDisk.  # noqa: E501


        :return: The type of this VmDisk.  # noqa: E501
        :rtype: VmDiskType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VmDisk.


        :param type: The type of this VmDisk.  # noqa: E501
        :type type: VmDiskType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def unsafe_image_path(self):
        """Gets the unsafe_image_path of this VmDisk.  # noqa: E501


        :return: The unsafe_image_path of this VmDisk.  # noqa: E501
        :rtype: str
        """
        return self._unsafe_image_path

    @unsafe_image_path.setter
    def unsafe_image_path(self, unsafe_image_path):
        """Sets the unsafe_image_path of this VmDisk.


        :param unsafe_image_path: The unsafe_image_path of this VmDisk.  # noqa: E501
        :type unsafe_image_path: str
        """

        self._unsafe_image_path = unsafe_image_path

    @property
    def unsafe_image_uuid(self):
        """Gets the unsafe_image_uuid of this VmDisk.  # noqa: E501


        :return: The unsafe_image_uuid of this VmDisk.  # noqa: E501
        :rtype: str
        """
        return self._unsafe_image_uuid

    @unsafe_image_uuid.setter
    def unsafe_image_uuid(self, unsafe_image_uuid):
        """Sets the unsafe_image_uuid of this VmDisk.


        :param unsafe_image_uuid: The unsafe_image_uuid of this VmDisk.  # noqa: E501
        :type unsafe_image_uuid: str
        """

        self._unsafe_image_uuid = unsafe_image_uuid

    @property
    def unsafe_provision(self):
        """Gets the unsafe_provision of this VmDisk.  # noqa: E501


        :return: The unsafe_provision of this VmDisk.  # noqa: E501
        :rtype: str
        """
        return self._unsafe_provision

    @unsafe_provision.setter
    def unsafe_provision(self, unsafe_provision):
        """Sets the unsafe_provision of this VmDisk.


        :param unsafe_provision: The unsafe_provision of this VmDisk.  # noqa: E501
        :type unsafe_provision: str
        """

        self._unsafe_provision = unsafe_provision

    @property
    def vm(self):
        """Gets the vm of this VmDisk.  # noqa: E501


        :return: The vm of this VmDisk.  # noqa: E501
        :rtype: NestedVm
        """
        return self._vm

    @vm.setter
    def vm(self, vm):
        """Sets the vm of this VmDisk.


        :param vm: The vm of this VmDisk.  # noqa: E501
        :type vm: NestedVm
        """
        if self.local_vars_configuration.client_side_validation and vm is None:  # noqa: E501
            raise ValueError("Invalid value for `vm`, must not be `None`")  # noqa: E501

        self._vm = vm

    @property
    def vm_volume(self):
        """Gets the vm_volume of this VmDisk.  # noqa: E501


        :return: The vm_volume of this VmDisk.  # noqa: E501
        :rtype: NestedVmVolume
        """
        return self._vm_volume

    @vm_volume.setter
    def vm_volume(self, vm_volume):
        """Sets the vm_volume of this VmDisk.


        :param vm_volume: The vm_volume of this VmDisk.  # noqa: E501
        :type vm_volume: NestedVmVolume
        """

        self._vm_volume = vm_volume

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
        if not isinstance(other, VmDisk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmDisk):
            return True

        return self.to_dict() != other.to_dict()
