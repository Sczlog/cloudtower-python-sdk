# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class DataPoint(object):
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
        'v': 'float',
        't': 'int',
        'typename': 'str'
    }

    attribute_map = {
        'v': 'v',
        't': 't',
        'typename': '__typename'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """DataPoint - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._v = None
        self._t = None
        self._typename = None
        self.discriminator = None

        self.v = kwargs.get("v", None)
        if "t" in kwargs:
            self.t = kwargs["t"]
        if "typename" in kwargs:
            self.typename = kwargs["typename"]

    @property
    def v(self):
        """Gets the v of this DataPoint.  # noqa: E501


        :return: The v of this DataPoint.  # noqa: E501
        :rtype: float
        """
        return self._v

    @v.setter
    def v(self, v):
        """Sets the v of this DataPoint.


        :param v: The v of this DataPoint.  # noqa: E501
        :type v: float
        """

        self._v = v

    @property
    def t(self):
        """Gets the t of this DataPoint.  # noqa: E501


        :return: The t of this DataPoint.  # noqa: E501
        :rtype: int
        """
        return self._t

    @t.setter
    def t(self, t):
        """Sets the t of this DataPoint.


        :param t: The t of this DataPoint.  # noqa: E501
        :type t: int
        """
        if self.local_vars_configuration.client_side_validation and t is None:  # noqa: E501
            raise ValueError("Invalid value for `t`, must not be `None`")  # noqa: E501

        self._t = t

    @property
    def typename(self):
        """Gets the typename of this DataPoint.  # noqa: E501


        :return: The typename of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._typename

    @typename.setter
    def typename(self, typename):
        """Sets the typename of this DataPoint.


        :param typename: The typename of this DataPoint.  # noqa: E501
        :type typename: str
        """
        allowed_values = ["DataPoint"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and typename not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `typename` ({0}), must be one of {1}"  # noqa: E501
                .format(typename, allowed_values)
            )

        self._typename = typename

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
        if not isinstance(other, DataPoint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataPoint):
            return True

        return self.to_dict() != other.to_dict()
