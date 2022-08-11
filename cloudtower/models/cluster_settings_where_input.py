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


class ClusterSettingsWhereInput(object):
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
        '_and': 'list[ClusterSettingsWhereInput]',
        'cluster': 'ClusterWhereInput',
        'default_ha': 'bool',
        'default_ha_not': 'bool',
        'enabled_iscsi': 'bool',
        'enabled_iscsi_not': 'bool',
        'id': 'str',
        'id_contains': 'str',
        'id_ends_with': 'str',
        'id_gt': 'str',
        'id_gte': 'str',
        'id_in': 'list[str]',
        'id_lt': 'str',
        'id_lte': 'str',
        'id_not': 'str',
        'id_not_contains': 'str',
        'id_not_ends_with': 'str',
        'id_not_in': 'list[str]',
        'id_not_starts_with': 'str',
        'id_starts_with': 'str',
        '_not': 'list[ClusterSettingsWhereInput]',
        '_or': 'list[ClusterSettingsWhereInput]'
    }

    attribute_map = {
        '_and': 'AND',
        'cluster': 'cluster',
        'default_ha': 'default_ha',
        'default_ha_not': 'default_ha_not',
        'enabled_iscsi': 'enabled_iscsi',
        'enabled_iscsi_not': 'enabled_iscsi_not',
        'id': 'id',
        'id_contains': 'id_contains',
        'id_ends_with': 'id_ends_with',
        'id_gt': 'id_gt',
        'id_gte': 'id_gte',
        'id_in': 'id_in',
        'id_lt': 'id_lt',
        'id_lte': 'id_lte',
        'id_not': 'id_not',
        'id_not_contains': 'id_not_contains',
        'id_not_ends_with': 'id_not_ends_with',
        'id_not_in': 'id_not_in',
        'id_not_starts_with': 'id_not_starts_with',
        'id_starts_with': 'id_starts_with',
        '_not': 'NOT',
        '_or': 'OR'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ClusterSettingsWhereInput - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self.__and = None
        self._cluster = None
        self._default_ha = None
        self._default_ha_not = None
        self._enabled_iscsi = None
        self._enabled_iscsi_not = None
        self._id = None
        self._id_contains = None
        self._id_ends_with = None
        self._id_gt = None
        self._id_gte = None
        self._id_in = None
        self._id_lt = None
        self._id_lte = None
        self._id_not = None
        self._id_not_contains = None
        self._id_not_ends_with = None
        self._id_not_in = None
        self._id_not_starts_with = None
        self._id_starts_with = None
        self.__not = None
        self.__or = None
        self.discriminator = None

        self._and = kwargs.get("_and", None)
        self.cluster = kwargs.get("cluster", None)
        self.default_ha = kwargs.get("default_ha", None)
        self.default_ha_not = kwargs.get("default_ha_not", None)
        self.enabled_iscsi = kwargs.get("enabled_iscsi", None)
        self.enabled_iscsi_not = kwargs.get("enabled_iscsi_not", None)
        self.id = kwargs.get("id", None)
        self.id_contains = kwargs.get("id_contains", None)
        self.id_ends_with = kwargs.get("id_ends_with", None)
        self.id_gt = kwargs.get("id_gt", None)
        self.id_gte = kwargs.get("id_gte", None)
        self.id_in = kwargs.get("id_in", None)
        self.id_lt = kwargs.get("id_lt", None)
        self.id_lte = kwargs.get("id_lte", None)
        self.id_not = kwargs.get("id_not", None)
        self.id_not_contains = kwargs.get("id_not_contains", None)
        self.id_not_ends_with = kwargs.get("id_not_ends_with", None)
        self.id_not_in = kwargs.get("id_not_in", None)
        self.id_not_starts_with = kwargs.get("id_not_starts_with", None)
        self.id_starts_with = kwargs.get("id_starts_with", None)
        self._not = kwargs.get("_not", None)
        self._or = kwargs.get("_or", None)

    @property
    def _and(self):
        """Gets the _and of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The _and of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: list[ClusterSettingsWhereInput]
        """
        return self.__and

    @_and.setter
    def _and(self, _and):
        """Sets the _and of this ClusterSettingsWhereInput.


        :param _and: The _and of this ClusterSettingsWhereInput.  # noqa: E501
        :type _and: list[ClusterSettingsWhereInput]
        """

        self.__and = _and

    @property
    def cluster(self):
        """Gets the cluster of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The cluster of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: ClusterWhereInput
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this ClusterSettingsWhereInput.


        :param cluster: The cluster of this ClusterSettingsWhereInput.  # noqa: E501
        :type cluster: ClusterWhereInput
        """

        self._cluster = cluster

    @property
    def default_ha(self):
        """Gets the default_ha of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The default_ha of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: bool
        """
        return self._default_ha

    @default_ha.setter
    def default_ha(self, default_ha):
        """Sets the default_ha of this ClusterSettingsWhereInput.


        :param default_ha: The default_ha of this ClusterSettingsWhereInput.  # noqa: E501
        :type default_ha: bool
        """

        self._default_ha = default_ha

    @property
    def default_ha_not(self):
        """Gets the default_ha_not of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The default_ha_not of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: bool
        """
        return self._default_ha_not

    @default_ha_not.setter
    def default_ha_not(self, default_ha_not):
        """Sets the default_ha_not of this ClusterSettingsWhereInput.


        :param default_ha_not: The default_ha_not of this ClusterSettingsWhereInput.  # noqa: E501
        :type default_ha_not: bool
        """

        self._default_ha_not = default_ha_not

    @property
    def enabled_iscsi(self):
        """Gets the enabled_iscsi of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The enabled_iscsi of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: bool
        """
        return self._enabled_iscsi

    @enabled_iscsi.setter
    def enabled_iscsi(self, enabled_iscsi):
        """Sets the enabled_iscsi of this ClusterSettingsWhereInput.


        :param enabled_iscsi: The enabled_iscsi of this ClusterSettingsWhereInput.  # noqa: E501
        :type enabled_iscsi: bool
        """

        self._enabled_iscsi = enabled_iscsi

    @property
    def enabled_iscsi_not(self):
        """Gets the enabled_iscsi_not of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The enabled_iscsi_not of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: bool
        """
        return self._enabled_iscsi_not

    @enabled_iscsi_not.setter
    def enabled_iscsi_not(self, enabled_iscsi_not):
        """Sets the enabled_iscsi_not of this ClusterSettingsWhereInput.


        :param enabled_iscsi_not: The enabled_iscsi_not of this ClusterSettingsWhereInput.  # noqa: E501
        :type enabled_iscsi_not: bool
        """

        self._enabled_iscsi_not = enabled_iscsi_not

    @property
    def id(self):
        """Gets the id of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The id of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterSettingsWhereInput.


        :param id: The id of this ClusterSettingsWhereInput.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def id_contains(self):
        """Gets the id_contains of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The id_contains of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_contains

    @id_contains.setter
    def id_contains(self, id_contains):
        """Sets the id_contains of this ClusterSettingsWhereInput.


        :param id_contains: The id_contains of this ClusterSettingsWhereInput.  # noqa: E501
        :type id_contains: str
        """

        self._id_contains = id_contains

    @property
    def id_ends_with(self):
        """Gets the id_ends_with of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The id_ends_with of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_ends_with

    @id_ends_with.setter
    def id_ends_with(self, id_ends_with):
        """Sets the id_ends_with of this ClusterSettingsWhereInput.


        :param id_ends_with: The id_ends_with of this ClusterSettingsWhereInput.  # noqa: E501
        :type id_ends_with: str
        """

        self._id_ends_with = id_ends_with

    @property
    def id_gt(self):
        """Gets the id_gt of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The id_gt of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_gt

    @id_gt.setter
    def id_gt(self, id_gt):
        """Sets the id_gt of this ClusterSettingsWhereInput.


        :param id_gt: The id_gt of this ClusterSettingsWhereInput.  # noqa: E501
        :type id_gt: str
        """

        self._id_gt = id_gt

    @property
    def id_gte(self):
        """Gets the id_gte of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The id_gte of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_gte

    @id_gte.setter
    def id_gte(self, id_gte):
        """Sets the id_gte of this ClusterSettingsWhereInput.


        :param id_gte: The id_gte of this ClusterSettingsWhereInput.  # noqa: E501
        :type id_gte: str
        """

        self._id_gte = id_gte

    @property
    def id_in(self):
        """Gets the id_in of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The id_in of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._id_in

    @id_in.setter
    def id_in(self, id_in):
        """Sets the id_in of this ClusterSettingsWhereInput.


        :param id_in: The id_in of this ClusterSettingsWhereInput.  # noqa: E501
        :type id_in: list[str]
        """

        self._id_in = id_in

    @property
    def id_lt(self):
        """Gets the id_lt of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The id_lt of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_lt

    @id_lt.setter
    def id_lt(self, id_lt):
        """Sets the id_lt of this ClusterSettingsWhereInput.


        :param id_lt: The id_lt of this ClusterSettingsWhereInput.  # noqa: E501
        :type id_lt: str
        """

        self._id_lt = id_lt

    @property
    def id_lte(self):
        """Gets the id_lte of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The id_lte of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_lte

    @id_lte.setter
    def id_lte(self, id_lte):
        """Sets the id_lte of this ClusterSettingsWhereInput.


        :param id_lte: The id_lte of this ClusterSettingsWhereInput.  # noqa: E501
        :type id_lte: str
        """

        self._id_lte = id_lte

    @property
    def id_not(self):
        """Gets the id_not of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The id_not of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not

    @id_not.setter
    def id_not(self, id_not):
        """Sets the id_not of this ClusterSettingsWhereInput.


        :param id_not: The id_not of this ClusterSettingsWhereInput.  # noqa: E501
        :type id_not: str
        """

        self._id_not = id_not

    @property
    def id_not_contains(self):
        """Gets the id_not_contains of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The id_not_contains of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not_contains

    @id_not_contains.setter
    def id_not_contains(self, id_not_contains):
        """Sets the id_not_contains of this ClusterSettingsWhereInput.


        :param id_not_contains: The id_not_contains of this ClusterSettingsWhereInput.  # noqa: E501
        :type id_not_contains: str
        """

        self._id_not_contains = id_not_contains

    @property
    def id_not_ends_with(self):
        """Gets the id_not_ends_with of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The id_not_ends_with of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not_ends_with

    @id_not_ends_with.setter
    def id_not_ends_with(self, id_not_ends_with):
        """Sets the id_not_ends_with of this ClusterSettingsWhereInput.


        :param id_not_ends_with: The id_not_ends_with of this ClusterSettingsWhereInput.  # noqa: E501
        :type id_not_ends_with: str
        """

        self._id_not_ends_with = id_not_ends_with

    @property
    def id_not_in(self):
        """Gets the id_not_in of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The id_not_in of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._id_not_in

    @id_not_in.setter
    def id_not_in(self, id_not_in):
        """Sets the id_not_in of this ClusterSettingsWhereInput.


        :param id_not_in: The id_not_in of this ClusterSettingsWhereInput.  # noqa: E501
        :type id_not_in: list[str]
        """

        self._id_not_in = id_not_in

    @property
    def id_not_starts_with(self):
        """Gets the id_not_starts_with of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The id_not_starts_with of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not_starts_with

    @id_not_starts_with.setter
    def id_not_starts_with(self, id_not_starts_with):
        """Sets the id_not_starts_with of this ClusterSettingsWhereInput.


        :param id_not_starts_with: The id_not_starts_with of this ClusterSettingsWhereInput.  # noqa: E501
        :type id_not_starts_with: str
        """

        self._id_not_starts_with = id_not_starts_with

    @property
    def id_starts_with(self):
        """Gets the id_starts_with of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The id_starts_with of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_starts_with

    @id_starts_with.setter
    def id_starts_with(self, id_starts_with):
        """Sets the id_starts_with of this ClusterSettingsWhereInput.


        :param id_starts_with: The id_starts_with of this ClusterSettingsWhereInput.  # noqa: E501
        :type id_starts_with: str
        """

        self._id_starts_with = id_starts_with

    @property
    def _not(self):
        """Gets the _not of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The _not of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: list[ClusterSettingsWhereInput]
        """
        return self.__not

    @_not.setter
    def _not(self, _not):
        """Sets the _not of this ClusterSettingsWhereInput.


        :param _not: The _not of this ClusterSettingsWhereInput.  # noqa: E501
        :type _not: list[ClusterSettingsWhereInput]
        """

        self.__not = _not

    @property
    def _or(self):
        """Gets the _or of this ClusterSettingsWhereInput.  # noqa: E501


        :return: The _or of this ClusterSettingsWhereInput.  # noqa: E501
        :rtype: list[ClusterSettingsWhereInput]
        """
        return self.__or

    @_or.setter
    def _or(self, _or):
        """Sets the _or of this ClusterSettingsWhereInput.


        :param _or: The _or of this ClusterSettingsWhereInput.  # noqa: E501
        :type _or: list[ClusterSettingsWhereInput]
        """

        self.__or = _or

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
        if not isinstance(other, ClusterSettingsWhereInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterSettingsWhereInput):
            return True

        return self.to_dict() != other.to_dict()
