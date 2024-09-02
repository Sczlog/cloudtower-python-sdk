# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class HostBatchCreateDiskInput(object):
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
        'type': 'DiskType',
        'size': 'float',
        'function': 'DiskFunction',
        'drive': 'str'
    }

    attribute_map = {
        'type': 'type',
        'size': 'size',
        'function': 'function',
        'drive': 'drive'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """HostBatchCreateDiskInput - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._type = None
        self._size = None
        self._function = None
        self._drive = None
        self.discriminator = None

        self.type = kwargs.get("type", None)
        self.size = kwargs.get("size", None)
        self.function = kwargs.get("function", None)
        if "drive" in kwargs:
            self.drive = kwargs["drive"]

    @property
    def type(self):
        """Gets the type of this HostBatchCreateDiskInput.  # noqa: E501


        :return: The type of this HostBatchCreateDiskInput.  # noqa: E501
        :rtype: DiskType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HostBatchCreateDiskInput.


        :param type: The type of this HostBatchCreateDiskInput.  # noqa: E501
        :type type: DiskType
        """

        self._type = type

    @property
    def size(self):
        """Gets the size of this HostBatchCreateDiskInput.  # noqa: E501


        :return: The size of this HostBatchCreateDiskInput.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this HostBatchCreateDiskInput.


        :param size: The size of this HostBatchCreateDiskInput.  # noqa: E501
        :type size: float
        """

        self._size = size

    @property
    def function(self):
        """Gets the function of this HostBatchCreateDiskInput.  # noqa: E501


        :return: The function of this HostBatchCreateDiskInput.  # noqa: E501
        :rtype: DiskFunction
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this HostBatchCreateDiskInput.


        :param function: The function of this HostBatchCreateDiskInput.  # noqa: E501
        :type function: DiskFunction
        """

        self._function = function

    @property
    def drive(self):
        """Gets the drive of this HostBatchCreateDiskInput.  # noqa: E501


        :return: The drive of this HostBatchCreateDiskInput.  # noqa: E501
        :rtype: str
        """
        return self._drive

    @drive.setter
    def drive(self, drive):
        """Sets the drive of this HostBatchCreateDiskInput.


        :param drive: The drive of this HostBatchCreateDiskInput.  # noqa: E501
        :type drive: str
        """
        if self.local_vars_configuration.client_side_validation and drive is None:  # noqa: E501
            raise ValueError("Invalid value for `drive`, must not be `None`")  # noqa: E501

        self._drive = drive

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
        if not isinstance(other, HostBatchCreateDiskInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HostBatchCreateDiskInput):
            return True

        return self.to_dict() != other.to_dict()
