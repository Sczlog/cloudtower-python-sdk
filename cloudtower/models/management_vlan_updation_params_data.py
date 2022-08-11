# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Contact: info@smartx.com
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


class ManagementVlanUpdationParamsData(object):
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
        'extra_ip': 'list[ExtraIp]',
        'subnetmask': 'str',
        'gateway_ip': 'str',
        'vlan_id': 'int'
    }

    attribute_map = {
        'extra_ip': 'extra_ip',
        'subnetmask': 'subnetmask',
        'gateway_ip': 'gateway_ip',
        'vlan_id': 'vlan_id'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ManagementVlanUpdationParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._extra_ip = None
        self._subnetmask = None
        self._gateway_ip = None
        self._vlan_id = None
        self.discriminator = None

        if "extra_ip" in kwargs:
            self.extra_ip = kwargs["extra_ip"]
        if "subnetmask" in kwargs:
            self.subnetmask = kwargs["subnetmask"]
        if "gateway_ip" in kwargs:
            self.gateway_ip = kwargs["gateway_ip"]
        if "vlan_id" in kwargs:
            self.vlan_id = kwargs["vlan_id"]

    @property
    def extra_ip(self):
        """Gets the extra_ip of this ManagementVlanUpdationParamsData.  # noqa: E501


        :return: The extra_ip of this ManagementVlanUpdationParamsData.  # noqa: E501
        :rtype: list[ExtraIp]
        """
        return self._extra_ip

    @extra_ip.setter
    def extra_ip(self, extra_ip):
        """Sets the extra_ip of this ManagementVlanUpdationParamsData.


        :param extra_ip: The extra_ip of this ManagementVlanUpdationParamsData.  # noqa: E501
        :type extra_ip: list[ExtraIp]
        """

        self._extra_ip = extra_ip

    @property
    def subnetmask(self):
        """Gets the subnetmask of this ManagementVlanUpdationParamsData.  # noqa: E501


        :return: The subnetmask of this ManagementVlanUpdationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._subnetmask

    @subnetmask.setter
    def subnetmask(self, subnetmask):
        """Sets the subnetmask of this ManagementVlanUpdationParamsData.


        :param subnetmask: The subnetmask of this ManagementVlanUpdationParamsData.  # noqa: E501
        :type subnetmask: str
        """

        self._subnetmask = subnetmask

    @property
    def gateway_ip(self):
        """Gets the gateway_ip of this ManagementVlanUpdationParamsData.  # noqa: E501


        :return: The gateway_ip of this ManagementVlanUpdationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        """Sets the gateway_ip of this ManagementVlanUpdationParamsData.


        :param gateway_ip: The gateway_ip of this ManagementVlanUpdationParamsData.  # noqa: E501
        :type gateway_ip: str
        """

        self._gateway_ip = gateway_ip

    @property
    def vlan_id(self):
        """Gets the vlan_id of this ManagementVlanUpdationParamsData.  # noqa: E501


        :return: The vlan_id of this ManagementVlanUpdationParamsData.  # noqa: E501
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this ManagementVlanUpdationParamsData.


        :param vlan_id: The vlan_id of this ManagementVlanUpdationParamsData.  # noqa: E501
        :type vlan_id: int
        """

        self._vlan_id = vlan_id

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
        if not isinstance(other, ManagementVlanUpdationParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ManagementVlanUpdationParamsData):
            return True

        return self.to_dict() != other.to_dict()
