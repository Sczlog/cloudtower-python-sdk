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


class VcenterAccountWhereUniqueInput(object):
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
        'id': 'str',
        'local_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'local_id': 'local_id'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VcenterAccountWhereUniqueInput - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._id = None
        self._local_id = None
        self.discriminator = None

        self.id = kwargs.get("id", None)
        self.local_id = kwargs.get("local_id", None)

    @property
    def id(self):
        """Gets the id of this VcenterAccountWhereUniqueInput.  # noqa: E501


        :return: The id of this VcenterAccountWhereUniqueInput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VcenterAccountWhereUniqueInput.


        :param id: The id of this VcenterAccountWhereUniqueInput.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def local_id(self):
        """Gets the local_id of this VcenterAccountWhereUniqueInput.  # noqa: E501


        :return: The local_id of this VcenterAccountWhereUniqueInput.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this VcenterAccountWhereUniqueInput.


        :param local_id: The local_id of this VcenterAccountWhereUniqueInput.  # noqa: E501
        :type local_id: str
        """

        self._local_id = local_id

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
        if not isinstance(other, VcenterAccountWhereUniqueInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VcenterAccountWhereUniqueInput):
            return True

        return self.to_dict() != other.to_dict()
