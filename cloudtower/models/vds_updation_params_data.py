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


class VdsUpdationParamsData(object):
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
        'nic_ids': 'list[str]',
        'work_mode': 'str',
        'bond_mode': 'str',
        'name': 'str'
    }

    attribute_map = {
        'nic_ids': 'nicIds',
        'work_mode': 'work_mode',
        'bond_mode': 'bond_mode',
        'name': 'name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VdsUpdationParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._nic_ids = None
        self._work_mode = None
        self._bond_mode = None
        self._name = None
        self.discriminator = None

        if "nic_ids" in kwargs:
            self.nic_ids = kwargs["nic_ids"]
        if "work_mode" in kwargs:
            self.work_mode = kwargs["work_mode"]
        if "bond_mode" in kwargs:
            self.bond_mode = kwargs["bond_mode"]
        if "name" in kwargs:
            self.name = kwargs["name"]

    @property
    def nic_ids(self):
        """Gets the nic_ids of this VdsUpdationParamsData.  # noqa: E501


        :return: The nic_ids of this VdsUpdationParamsData.  # noqa: E501
        :rtype: list[str]
        """
        return self._nic_ids

    @nic_ids.setter
    def nic_ids(self, nic_ids):
        """Sets the nic_ids of this VdsUpdationParamsData.


        :param nic_ids: The nic_ids of this VdsUpdationParamsData.  # noqa: E501
        :type nic_ids: list[str]
        """

        self._nic_ids = nic_ids

    @property
    def work_mode(self):
        """Gets the work_mode of this VdsUpdationParamsData.  # noqa: E501


        :return: The work_mode of this VdsUpdationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._work_mode

    @work_mode.setter
    def work_mode(self, work_mode):
        """Sets the work_mode of this VdsUpdationParamsData.


        :param work_mode: The work_mode of this VdsUpdationParamsData.  # noqa: E501
        :type work_mode: str
        """

        self._work_mode = work_mode

    @property
    def bond_mode(self):
        """Gets the bond_mode of this VdsUpdationParamsData.  # noqa: E501


        :return: The bond_mode of this VdsUpdationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._bond_mode

    @bond_mode.setter
    def bond_mode(self, bond_mode):
        """Sets the bond_mode of this VdsUpdationParamsData.


        :param bond_mode: The bond_mode of this VdsUpdationParamsData.  # noqa: E501
        :type bond_mode: str
        """

        self._bond_mode = bond_mode

    @property
    def name(self):
        """Gets the name of this VdsUpdationParamsData.  # noqa: E501


        :return: The name of this VdsUpdationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VdsUpdationParamsData.


        :param name: The name of this VdsUpdationParamsData.  # noqa: E501
        :type name: str
        """

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
        if not isinstance(other, VdsUpdationParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VdsUpdationParamsData):
            return True

        return self.to_dict() != other.to_dict()
