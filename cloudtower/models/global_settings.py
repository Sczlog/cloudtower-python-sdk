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


class GlobalSettings(object):
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
        'auth': 'NestedAuthSettings',
        'id': 'str',
        'vm_recycle_bin': 'NestedVmRecycleBin'
    }

    attribute_map = {
        'auth': 'auth',
        'id': 'id',
        'vm_recycle_bin': 'vm_recycle_bin'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """GlobalSettings - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._auth = None
        self._id = None
        self._vm_recycle_bin = None
        self.discriminator = None

        self.auth = kwargs.get("auth", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "vm_recycle_bin" in kwargs:
            self.vm_recycle_bin = kwargs["vm_recycle_bin"]

    @property
    def auth(self):
        """Gets the auth of this GlobalSettings.  # noqa: E501


        :return: The auth of this GlobalSettings.  # noqa: E501
        :rtype: NestedAuthSettings
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this GlobalSettings.


        :param auth: The auth of this GlobalSettings.  # noqa: E501
        :type auth: NestedAuthSettings
        """

        self._auth = auth

    @property
    def id(self):
        """Gets the id of this GlobalSettings.  # noqa: E501


        :return: The id of this GlobalSettings.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GlobalSettings.


        :param id: The id of this GlobalSettings.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def vm_recycle_bin(self):
        """Gets the vm_recycle_bin of this GlobalSettings.  # noqa: E501


        :return: The vm_recycle_bin of this GlobalSettings.  # noqa: E501
        :rtype: NestedVmRecycleBin
        """
        return self._vm_recycle_bin

    @vm_recycle_bin.setter
    def vm_recycle_bin(self, vm_recycle_bin):
        """Sets the vm_recycle_bin of this GlobalSettings.


        :param vm_recycle_bin: The vm_recycle_bin of this GlobalSettings.  # noqa: E501
        :type vm_recycle_bin: NestedVmRecycleBin
        """
        if self.local_vars_configuration.client_side_validation and vm_recycle_bin is None:  # noqa: E501
            raise ValueError("Invalid value for `vm_recycle_bin`, must not be `None`")  # noqa: E501

        self._vm_recycle_bin = vm_recycle_bin

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
        if not isinstance(other, GlobalSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GlobalSettings):
            return True

        return self.to_dict() != other.to_dict()
