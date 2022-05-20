# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 1.10.0
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


class VmCdRomParams(object):
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
        'elf_image_id': 'str',
        'index': 'int',
        'key': 'int',
        'boot': 'int'
    }

    attribute_map = {
        'elf_image_id': 'elf_image_id',
        'index': 'index',
        'key': 'key',
        'boot': 'boot'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VmCdRomParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._elf_image_id = None
        self._index = None
        self._key = None
        self._boot = None
        self.discriminator = None

        if "elf_image_id" in kwargs:
            self.elf_image_id = kwargs["elf_image_id"]
        if "index" in kwargs:
            self.index = kwargs["index"]
        if "key" in kwargs:
            self.key = kwargs["key"]
        if "boot" in kwargs:
            self.boot = kwargs["boot"]

    @property
    def elf_image_id(self):
        """Gets the elf_image_id of this VmCdRomParams.  # noqa: E501


        :return: The elf_image_id of this VmCdRomParams.  # noqa: E501
        :rtype: str
        """
        return self._elf_image_id

    @elf_image_id.setter
    def elf_image_id(self, elf_image_id):
        """Sets the elf_image_id of this VmCdRomParams.


        :param elf_image_id: The elf_image_id of this VmCdRomParams.  # noqa: E501
        :type elf_image_id: str
        """

        self._elf_image_id = elf_image_id

    @property
    def index(self):
        """Gets the index of this VmCdRomParams.  # noqa: E501


        :return: The index of this VmCdRomParams.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this VmCdRomParams.


        :param index: The index of this VmCdRomParams.  # noqa: E501
        :type index: int
        """

        self._index = index

    @property
    def key(self):
        """Gets the key of this VmCdRomParams.  # noqa: E501


        :return: The key of this VmCdRomParams.  # noqa: E501
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this VmCdRomParams.


        :param key: The key of this VmCdRomParams.  # noqa: E501
        :type key: int
        """

        self._key = key

    @property
    def boot(self):
        """Gets the boot of this VmCdRomParams.  # noqa: E501


        :return: The boot of this VmCdRomParams.  # noqa: E501
        :rtype: int
        """
        return self._boot

    @boot.setter
    def boot(self, boot):
        """Sets the boot of this VmCdRomParams.


        :param boot: The boot of this VmCdRomParams.  # noqa: E501
        :type boot: int
        """
        if self.local_vars_configuration.client_side_validation and boot is None:  # noqa: E501
            raise ValueError("Invalid value for `boot`, must not be `None`")  # noqa: E501

        self._boot = boot

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
        if not isinstance(other, VmCdRomParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmCdRomParams):
            return True

        return self.to_dict() != other.to_dict()
