# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class NicUpdationParamsData(object):
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
        'total_vf_num': 'int',
        'mtu': 'int'
    }

    attribute_map = {
        'total_vf_num': 'total_vf_num',
        'mtu': 'mtu'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NicUpdationParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._total_vf_num = None
        self._mtu = None
        self.discriminator = None

        if "total_vf_num" in kwargs:
            self.total_vf_num = kwargs["total_vf_num"]
        if "mtu" in kwargs:
            self.mtu = kwargs["mtu"]

    @property
    def total_vf_num(self):
        """Gets the total_vf_num of this NicUpdationParamsData.  # noqa: E501


        :return: The total_vf_num of this NicUpdationParamsData.  # noqa: E501
        :rtype: int
        """
        return self._total_vf_num

    @total_vf_num.setter
    def total_vf_num(self, total_vf_num):
        """Sets the total_vf_num of this NicUpdationParamsData.


        :param total_vf_num: The total_vf_num of this NicUpdationParamsData.  # noqa: E501
        :type total_vf_num: int
        """

        self._total_vf_num = total_vf_num

    @property
    def mtu(self):
        """Gets the mtu of this NicUpdationParamsData.  # noqa: E501


        :return: The mtu of this NicUpdationParamsData.  # noqa: E501
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this NicUpdationParamsData.


        :param mtu: The mtu of this NicUpdationParamsData.  # noqa: E501
        :type mtu: int
        """

        self._mtu = mtu

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
        if not isinstance(other, NicUpdationParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NicUpdationParamsData):
            return True

        return self.to_dict() != other.to_dict()
