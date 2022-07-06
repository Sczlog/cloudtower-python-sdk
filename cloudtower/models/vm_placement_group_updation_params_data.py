# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.1.0
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


class VmPlacementGroupUpdationParamsData(object):
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
        'vm_vm_policy': 'VmVmPolicy',
        'vms': 'VmWhereInput',
        'prefer_hosts': 'HostWhereInput',
        'must_hosts': 'HostWhereInput',
        'vm_host_prefer_enabled': 'bool',
        'vm_host_must_policy': 'bool',
        'vm_host_must_enabled': 'bool',
        'vm_host_prefer_policy': 'bool',
        'vm_vm_policy_enabled': 'bool',
        'name': 'str',
        'description': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'vm_vm_policy': 'vm_vm_policy',
        'vms': 'vms',
        'prefer_hosts': 'prefer_hosts',
        'must_hosts': 'must_hosts',
        'vm_host_prefer_enabled': 'vm_host_prefer_enabled',
        'vm_host_must_policy': 'vm_host_must_policy',
        'vm_host_must_enabled': 'vm_host_must_enabled',
        'vm_host_prefer_policy': 'vm_host_prefer_policy',
        'vm_vm_policy_enabled': 'vm_vm_policy_enabled',
        'name': 'name',
        'description': 'description',
        'enabled': 'enabled'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VmPlacementGroupUpdationParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._vm_vm_policy = None
        self._vms = None
        self._prefer_hosts = None
        self._must_hosts = None
        self._vm_host_prefer_enabled = None
        self._vm_host_must_policy = None
        self._vm_host_must_enabled = None
        self._vm_host_prefer_policy = None
        self._vm_vm_policy_enabled = None
        self._name = None
        self._description = None
        self._enabled = None
        self.discriminator = None

        if "vm_vm_policy" in kwargs:
            self.vm_vm_policy = kwargs["vm_vm_policy"]
        if "vms" in kwargs:
            self.vms = kwargs["vms"]
        if "prefer_hosts" in kwargs:
            self.prefer_hosts = kwargs["prefer_hosts"]
        if "must_hosts" in kwargs:
            self.must_hosts = kwargs["must_hosts"]
        if "vm_host_prefer_enabled" in kwargs:
            self.vm_host_prefer_enabled = kwargs["vm_host_prefer_enabled"]
        if "vm_host_must_policy" in kwargs:
            self.vm_host_must_policy = kwargs["vm_host_must_policy"]
        if "vm_host_must_enabled" in kwargs:
            self.vm_host_must_enabled = kwargs["vm_host_must_enabled"]
        if "vm_host_prefer_policy" in kwargs:
            self.vm_host_prefer_policy = kwargs["vm_host_prefer_policy"]
        if "vm_vm_policy_enabled" in kwargs:
            self.vm_vm_policy_enabled = kwargs["vm_vm_policy_enabled"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "description" in kwargs:
            self.description = kwargs["description"]
        if "enabled" in kwargs:
            self.enabled = kwargs["enabled"]

    @property
    def vm_vm_policy(self):
        """Gets the vm_vm_policy of this VmPlacementGroupUpdationParamsData.  # noqa: E501


        :return: The vm_vm_policy of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :rtype: VmVmPolicy
        """
        return self._vm_vm_policy

    @vm_vm_policy.setter
    def vm_vm_policy(self, vm_vm_policy):
        """Sets the vm_vm_policy of this VmPlacementGroupUpdationParamsData.


        :param vm_vm_policy: The vm_vm_policy of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :type vm_vm_policy: VmVmPolicy
        """

        self._vm_vm_policy = vm_vm_policy

    @property
    def vms(self):
        """Gets the vms of this VmPlacementGroupUpdationParamsData.  # noqa: E501


        :return: The vms of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :rtype: VmWhereInput
        """
        return self._vms

    @vms.setter
    def vms(self, vms):
        """Sets the vms of this VmPlacementGroupUpdationParamsData.


        :param vms: The vms of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :type vms: VmWhereInput
        """

        self._vms = vms

    @property
    def prefer_hosts(self):
        """Gets the prefer_hosts of this VmPlacementGroupUpdationParamsData.  # noqa: E501


        :return: The prefer_hosts of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :rtype: HostWhereInput
        """
        return self._prefer_hosts

    @prefer_hosts.setter
    def prefer_hosts(self, prefer_hosts):
        """Sets the prefer_hosts of this VmPlacementGroupUpdationParamsData.


        :param prefer_hosts: The prefer_hosts of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :type prefer_hosts: HostWhereInput
        """

        self._prefer_hosts = prefer_hosts

    @property
    def must_hosts(self):
        """Gets the must_hosts of this VmPlacementGroupUpdationParamsData.  # noqa: E501


        :return: The must_hosts of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :rtype: HostWhereInput
        """
        return self._must_hosts

    @must_hosts.setter
    def must_hosts(self, must_hosts):
        """Sets the must_hosts of this VmPlacementGroupUpdationParamsData.


        :param must_hosts: The must_hosts of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :type must_hosts: HostWhereInput
        """

        self._must_hosts = must_hosts

    @property
    def vm_host_prefer_enabled(self):
        """Gets the vm_host_prefer_enabled of this VmPlacementGroupUpdationParamsData.  # noqa: E501


        :return: The vm_host_prefer_enabled of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :rtype: bool
        """
        return self._vm_host_prefer_enabled

    @vm_host_prefer_enabled.setter
    def vm_host_prefer_enabled(self, vm_host_prefer_enabled):
        """Sets the vm_host_prefer_enabled of this VmPlacementGroupUpdationParamsData.


        :param vm_host_prefer_enabled: The vm_host_prefer_enabled of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :type vm_host_prefer_enabled: bool
        """

        self._vm_host_prefer_enabled = vm_host_prefer_enabled

    @property
    def vm_host_must_policy(self):
        """Gets the vm_host_must_policy of this VmPlacementGroupUpdationParamsData.  # noqa: E501


        :return: The vm_host_must_policy of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :rtype: bool
        """
        return self._vm_host_must_policy

    @vm_host_must_policy.setter
    def vm_host_must_policy(self, vm_host_must_policy):
        """Sets the vm_host_must_policy of this VmPlacementGroupUpdationParamsData.


        :param vm_host_must_policy: The vm_host_must_policy of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :type vm_host_must_policy: bool
        """

        self._vm_host_must_policy = vm_host_must_policy

    @property
    def vm_host_must_enabled(self):
        """Gets the vm_host_must_enabled of this VmPlacementGroupUpdationParamsData.  # noqa: E501


        :return: The vm_host_must_enabled of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :rtype: bool
        """
        return self._vm_host_must_enabled

    @vm_host_must_enabled.setter
    def vm_host_must_enabled(self, vm_host_must_enabled):
        """Sets the vm_host_must_enabled of this VmPlacementGroupUpdationParamsData.


        :param vm_host_must_enabled: The vm_host_must_enabled of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :type vm_host_must_enabled: bool
        """

        self._vm_host_must_enabled = vm_host_must_enabled

    @property
    def vm_host_prefer_policy(self):
        """Gets the vm_host_prefer_policy of this VmPlacementGroupUpdationParamsData.  # noqa: E501


        :return: The vm_host_prefer_policy of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :rtype: bool
        """
        return self._vm_host_prefer_policy

    @vm_host_prefer_policy.setter
    def vm_host_prefer_policy(self, vm_host_prefer_policy):
        """Sets the vm_host_prefer_policy of this VmPlacementGroupUpdationParamsData.


        :param vm_host_prefer_policy: The vm_host_prefer_policy of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :type vm_host_prefer_policy: bool
        """

        self._vm_host_prefer_policy = vm_host_prefer_policy

    @property
    def vm_vm_policy_enabled(self):
        """Gets the vm_vm_policy_enabled of this VmPlacementGroupUpdationParamsData.  # noqa: E501


        :return: The vm_vm_policy_enabled of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :rtype: bool
        """
        return self._vm_vm_policy_enabled

    @vm_vm_policy_enabled.setter
    def vm_vm_policy_enabled(self, vm_vm_policy_enabled):
        """Sets the vm_vm_policy_enabled of this VmPlacementGroupUpdationParamsData.


        :param vm_vm_policy_enabled: The vm_vm_policy_enabled of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :type vm_vm_policy_enabled: bool
        """

        self._vm_vm_policy_enabled = vm_vm_policy_enabled

    @property
    def name(self):
        """Gets the name of this VmPlacementGroupUpdationParamsData.  # noqa: E501


        :return: The name of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VmPlacementGroupUpdationParamsData.


        :param name: The name of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this VmPlacementGroupUpdationParamsData.  # noqa: E501


        :return: The description of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VmPlacementGroupUpdationParamsData.


        :param description: The description of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this VmPlacementGroupUpdationParamsData.  # noqa: E501


        :return: The enabled of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this VmPlacementGroupUpdationParamsData.


        :param enabled: The enabled of this VmPlacementGroupUpdationParamsData.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

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
        if not isinstance(other, VmPlacementGroupUpdationParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmPlacementGroupUpdationParamsData):
            return True

        return self.to_dict() != other.to_dict()
