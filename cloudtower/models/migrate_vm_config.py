# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class MigrateVmConfig(object):
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
        'remove_unmovable_devices': 'bool',
        'new_name': 'str',
        'network_mapping': 'list[VlanMapping]',
        'migrate_type': 'MigrateType',
        'elf_storage_policy': 'VmVolumeElfStoragePolicyType',
        'delete_src_vm': 'bool'
    }

    attribute_map = {
        'remove_unmovable_devices': 'remove_unmovable_devices',
        'new_name': 'new_name',
        'network_mapping': 'network_mapping',
        'migrate_type': 'migrate_type',
        'elf_storage_policy': 'elf_storage_policy',
        'delete_src_vm': 'delete_src_vm'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """MigrateVmConfig - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._remove_unmovable_devices = None
        self._new_name = None
        self._network_mapping = None
        self._migrate_type = None
        self._elf_storage_policy = None
        self._delete_src_vm = None
        self.discriminator = None

        if "remove_unmovable_devices" in kwargs:
            self.remove_unmovable_devices = kwargs["remove_unmovable_devices"]
        if "new_name" in kwargs:
            self.new_name = kwargs["new_name"]
        if "network_mapping" in kwargs:
            self.network_mapping = kwargs["network_mapping"]
        if "migrate_type" in kwargs:
            self.migrate_type = kwargs["migrate_type"]
        if "elf_storage_policy" in kwargs:
            self.elf_storage_policy = kwargs["elf_storage_policy"]
        if "delete_src_vm" in kwargs:
            self.delete_src_vm = kwargs["delete_src_vm"]

    @property
    def remove_unmovable_devices(self):
        """Gets the remove_unmovable_devices of this MigrateVmConfig.  # noqa: E501


        :return: The remove_unmovable_devices of this MigrateVmConfig.  # noqa: E501
        :rtype: bool
        """
        return self._remove_unmovable_devices

    @remove_unmovable_devices.setter
    def remove_unmovable_devices(self, remove_unmovable_devices):
        """Sets the remove_unmovable_devices of this MigrateVmConfig.


        :param remove_unmovable_devices: The remove_unmovable_devices of this MigrateVmConfig.  # noqa: E501
        :type remove_unmovable_devices: bool
        """

        self._remove_unmovable_devices = remove_unmovable_devices

    @property
    def new_name(self):
        """Gets the new_name of this MigrateVmConfig.  # noqa: E501


        :return: The new_name of this MigrateVmConfig.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this MigrateVmConfig.


        :param new_name: The new_name of this MigrateVmConfig.  # noqa: E501
        :type new_name: str
        """

        self._new_name = new_name

    @property
    def network_mapping(self):
        """Gets the network_mapping of this MigrateVmConfig.  # noqa: E501


        :return: The network_mapping of this MigrateVmConfig.  # noqa: E501
        :rtype: list[VlanMapping]
        """
        return self._network_mapping

    @network_mapping.setter
    def network_mapping(self, network_mapping):
        """Sets the network_mapping of this MigrateVmConfig.


        :param network_mapping: The network_mapping of this MigrateVmConfig.  # noqa: E501
        :type network_mapping: list[VlanMapping]
        """
        if self.local_vars_configuration.client_side_validation and network_mapping is None:  # noqa: E501
            raise ValueError("Invalid value for `network_mapping`, must not be `None`")  # noqa: E501

        self._network_mapping = network_mapping

    @property
    def migrate_type(self):
        """Gets the migrate_type of this MigrateVmConfig.  # noqa: E501


        :return: The migrate_type of this MigrateVmConfig.  # noqa: E501
        :rtype: MigrateType
        """
        return self._migrate_type

    @migrate_type.setter
    def migrate_type(self, migrate_type):
        """Sets the migrate_type of this MigrateVmConfig.


        :param migrate_type: The migrate_type of this MigrateVmConfig.  # noqa: E501
        :type migrate_type: MigrateType
        """
        if self.local_vars_configuration.client_side_validation and migrate_type is None:  # noqa: E501
            raise ValueError("Invalid value for `migrate_type`, must not be `None`")  # noqa: E501

        self._migrate_type = migrate_type

    @property
    def elf_storage_policy(self):
        """Gets the elf_storage_policy of this MigrateVmConfig.  # noqa: E501


        :return: The elf_storage_policy of this MigrateVmConfig.  # noqa: E501
        :rtype: VmVolumeElfStoragePolicyType
        """
        return self._elf_storage_policy

    @elf_storage_policy.setter
    def elf_storage_policy(self, elf_storage_policy):
        """Sets the elf_storage_policy of this MigrateVmConfig.


        :param elf_storage_policy: The elf_storage_policy of this MigrateVmConfig.  # noqa: E501
        :type elf_storage_policy: VmVolumeElfStoragePolicyType
        """
        if self.local_vars_configuration.client_side_validation and elf_storage_policy is None:  # noqa: E501
            raise ValueError("Invalid value for `elf_storage_policy`, must not be `None`")  # noqa: E501

        self._elf_storage_policy = elf_storage_policy

    @property
    def delete_src_vm(self):
        """Gets the delete_src_vm of this MigrateVmConfig.  # noqa: E501


        :return: The delete_src_vm of this MigrateVmConfig.  # noqa: E501
        :rtype: bool
        """
        return self._delete_src_vm

    @delete_src_vm.setter
    def delete_src_vm(self, delete_src_vm):
        """Sets the delete_src_vm of this MigrateVmConfig.


        :param delete_src_vm: The delete_src_vm of this MigrateVmConfig.  # noqa: E501
        :type delete_src_vm: bool
        """

        self._delete_src_vm = delete_src_vm

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
        if not isinstance(other, MigrateVmConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MigrateVmConfig):
            return True

        return self.to_dict() != other.to_dict()
