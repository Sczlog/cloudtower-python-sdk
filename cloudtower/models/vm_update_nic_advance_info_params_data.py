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


class VmUpdateNicAdvanceInfoParamsData(object):
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
        'mirror': 'bool',
        'enabled': 'bool',
        'mac_address': 'str',
        'nic_id': 'str',
        'connect_vlan_id': 'str'
    }

    attribute_map = {
        'mirror': 'mirror',
        'enabled': 'enabled',
        'mac_address': 'mac_address',
        'nic_id': 'nic_id',
        'connect_vlan_id': 'connect_vlan_id'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VmUpdateNicAdvanceInfoParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._mirror = None
        self._enabled = None
        self._mac_address = None
        self._nic_id = None
        self._connect_vlan_id = None
        self.discriminator = None

        if "mirror" in kwargs:
            self.mirror = kwargs["mirror"]
        if "enabled" in kwargs:
            self.enabled = kwargs["enabled"]
        if "mac_address" in kwargs:
            self.mac_address = kwargs["mac_address"]
        if "nic_id" in kwargs:
            self.nic_id = kwargs["nic_id"]
        if "connect_vlan_id" in kwargs:
            self.connect_vlan_id = kwargs["connect_vlan_id"]

    @property
    def mirror(self):
        """Gets the mirror of this VmUpdateNicAdvanceInfoParamsData.  # noqa: E501


        :return: The mirror of this VmUpdateNicAdvanceInfoParamsData.  # noqa: E501
        :rtype: bool
        """
        return self._mirror

    @mirror.setter
    def mirror(self, mirror):
        """Sets the mirror of this VmUpdateNicAdvanceInfoParamsData.


        :param mirror: The mirror of this VmUpdateNicAdvanceInfoParamsData.  # noqa: E501
        :type mirror: bool
        """

        self._mirror = mirror

    @property
    def enabled(self):
        """Gets the enabled of this VmUpdateNicAdvanceInfoParamsData.  # noqa: E501


        :return: The enabled of this VmUpdateNicAdvanceInfoParamsData.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this VmUpdateNicAdvanceInfoParamsData.


        :param enabled: The enabled of this VmUpdateNicAdvanceInfoParamsData.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def mac_address(self):
        """Gets the mac_address of this VmUpdateNicAdvanceInfoParamsData.  # noqa: E501


        :return: The mac_address of this VmUpdateNicAdvanceInfoParamsData.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this VmUpdateNicAdvanceInfoParamsData.


        :param mac_address: The mac_address of this VmUpdateNicAdvanceInfoParamsData.  # noqa: E501
        :type mac_address: str
        """

        self._mac_address = mac_address

    @property
    def nic_id(self):
        """Gets the nic_id of this VmUpdateNicAdvanceInfoParamsData.  # noqa: E501


        :return: The nic_id of this VmUpdateNicAdvanceInfoParamsData.  # noqa: E501
        :rtype: str
        """
        return self._nic_id

    @nic_id.setter
    def nic_id(self, nic_id):
        """Sets the nic_id of this VmUpdateNicAdvanceInfoParamsData.


        :param nic_id: The nic_id of this VmUpdateNicAdvanceInfoParamsData.  # noqa: E501
        :type nic_id: str
        """

        self._nic_id = nic_id

    @property
    def connect_vlan_id(self):
        """Gets the connect_vlan_id of this VmUpdateNicAdvanceInfoParamsData.  # noqa: E501


        :return: The connect_vlan_id of this VmUpdateNicAdvanceInfoParamsData.  # noqa: E501
        :rtype: str
        """
        return self._connect_vlan_id

    @connect_vlan_id.setter
    def connect_vlan_id(self, connect_vlan_id):
        """Sets the connect_vlan_id of this VmUpdateNicAdvanceInfoParamsData.


        :param connect_vlan_id: The connect_vlan_id of this VmUpdateNicAdvanceInfoParamsData.  # noqa: E501
        :type connect_vlan_id: str
        """

        self._connect_vlan_id = connect_vlan_id

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
        if not isinstance(other, VmUpdateNicAdvanceInfoParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmUpdateNicAdvanceInfoParamsData):
            return True

        return self.to_dict() != other.to_dict()
