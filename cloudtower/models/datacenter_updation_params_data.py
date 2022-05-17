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


class DatacenterUpdationParamsData(object):
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
        'clusters': 'ClusterWhereInput',
        'name': 'str'
    }

    attribute_map = {
        'clusters': 'clusters',
        'name': 'name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """DatacenterUpdationParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._clusters = None
        self._name = None
        self.discriminator = None

        if "clusters" in kwargs:
            self.clusters = kwargs["clusters"]
        if "name" in kwargs:
            self.name = kwargs["name"]

    @property
    def clusters(self):
        """Gets the clusters of this DatacenterUpdationParamsData.  # noqa: E501


        :return: The clusters of this DatacenterUpdationParamsData.  # noqa: E501
        :rtype: ClusterWhereInput
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this DatacenterUpdationParamsData.


        :param clusters: The clusters of this DatacenterUpdationParamsData.  # noqa: E501
        :type clusters: ClusterWhereInput
        """

        self._clusters = clusters

    @property
    def name(self):
        """Gets the name of this DatacenterUpdationParamsData.  # noqa: E501


        :return: The name of this DatacenterUpdationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatacenterUpdationParamsData.


        :param name: The name of this DatacenterUpdationParamsData.  # noqa: E501
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
        if not isinstance(other, DatacenterUpdationParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatacenterUpdationParamsData):
            return True

        return self.to_dict() != other.to_dict()
