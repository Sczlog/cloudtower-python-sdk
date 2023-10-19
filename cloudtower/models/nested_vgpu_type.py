# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class NestedVgpuType(object):
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
        'framebuffer': 'float',
        'max_instance': 'int',
        'max_resolution': 'str',
        'name': 'str',
        'vgpu_type_id': 'str'
    }

    attribute_map = {
        'framebuffer': 'framebuffer',
        'max_instance': 'max_instance',
        'max_resolution': 'max_resolution',
        'name': 'name',
        'vgpu_type_id': 'vgpu_type_id'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedVgpuType - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._framebuffer = None
        self._max_instance = None
        self._max_resolution = None
        self._name = None
        self._vgpu_type_id = None
        self.discriminator = None

        self.framebuffer = kwargs.get("framebuffer", None)
        self.max_instance = kwargs.get("max_instance", None)
        self.max_resolution = kwargs.get("max_resolution", None)
        self.name = kwargs.get("name", None)
        self.vgpu_type_id = kwargs.get("vgpu_type_id", None)

    @property
    def framebuffer(self):
        """Gets the framebuffer of this NestedVgpuType.  # noqa: E501


        :return: The framebuffer of this NestedVgpuType.  # noqa: E501
        :rtype: float
        """
        return self._framebuffer

    @framebuffer.setter
    def framebuffer(self, framebuffer):
        """Sets the framebuffer of this NestedVgpuType.


        :param framebuffer: The framebuffer of this NestedVgpuType.  # noqa: E501
        :type framebuffer: float
        """

        self._framebuffer = framebuffer

    @property
    def max_instance(self):
        """Gets the max_instance of this NestedVgpuType.  # noqa: E501


        :return: The max_instance of this NestedVgpuType.  # noqa: E501
        :rtype: int
        """
        return self._max_instance

    @max_instance.setter
    def max_instance(self, max_instance):
        """Sets the max_instance of this NestedVgpuType.


        :param max_instance: The max_instance of this NestedVgpuType.  # noqa: E501
        :type max_instance: int
        """

        self._max_instance = max_instance

    @property
    def max_resolution(self):
        """Gets the max_resolution of this NestedVgpuType.  # noqa: E501


        :return: The max_resolution of this NestedVgpuType.  # noqa: E501
        :rtype: str
        """
        return self._max_resolution

    @max_resolution.setter
    def max_resolution(self, max_resolution):
        """Sets the max_resolution of this NestedVgpuType.


        :param max_resolution: The max_resolution of this NestedVgpuType.  # noqa: E501
        :type max_resolution: str
        """

        self._max_resolution = max_resolution

    @property
    def name(self):
        """Gets the name of this NestedVgpuType.  # noqa: E501


        :return: The name of this NestedVgpuType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NestedVgpuType.


        :param name: The name of this NestedVgpuType.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def vgpu_type_id(self):
        """Gets the vgpu_type_id of this NestedVgpuType.  # noqa: E501


        :return: The vgpu_type_id of this NestedVgpuType.  # noqa: E501
        :rtype: str
        """
        return self._vgpu_type_id

    @vgpu_type_id.setter
    def vgpu_type_id(self, vgpu_type_id):
        """Sets the vgpu_type_id of this NestedVgpuType.


        :param vgpu_type_id: The vgpu_type_id of this NestedVgpuType.  # noqa: E501
        :type vgpu_type_id: str
        """

        self._vgpu_type_id = vgpu_type_id

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
        if not isinstance(other, NestedVgpuType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedVgpuType):
            return True

        return self.to_dict() != other.to_dict()
