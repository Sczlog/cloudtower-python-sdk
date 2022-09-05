# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class ZoneTopoWhereInput(object):
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
        '_and': 'list[ZoneTopoWhereInput]',
        'cluster': 'ClusterWhereInput',
        'cluster_topo': 'ClusterTopoWhereInput',
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
        'local_id': 'str',
        'local_id_contains': 'str',
        'local_id_ends_with': 'str',
        'local_id_gt': 'str',
        'local_id_gte': 'str',
        'local_id_in': 'list[str]',
        'local_id_lt': 'str',
        'local_id_lte': 'str',
        'local_id_not': 'str',
        'local_id_not_contains': 'str',
        'local_id_not_ends_with': 'str',
        'local_id_not_in': 'list[str]',
        'local_id_not_starts_with': 'str',
        'local_id_starts_with': 'str',
        '_not': 'list[ZoneTopoWhereInput]',
        '_or': 'list[ZoneTopoWhereInput]',
        'rack_topoes_every': 'RackTopoWhereInput',
        'rack_topoes_none': 'RackTopoWhereInput',
        'rack_topoes_some': 'RackTopoWhereInput'
    }

    attribute_map = {
        '_and': 'AND',
        'cluster': 'cluster',
        'cluster_topo': 'cluster_topo',
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
        'local_id': 'local_id',
        'local_id_contains': 'local_id_contains',
        'local_id_ends_with': 'local_id_ends_with',
        'local_id_gt': 'local_id_gt',
        'local_id_gte': 'local_id_gte',
        'local_id_in': 'local_id_in',
        'local_id_lt': 'local_id_lt',
        'local_id_lte': 'local_id_lte',
        'local_id_not': 'local_id_not',
        'local_id_not_contains': 'local_id_not_contains',
        'local_id_not_ends_with': 'local_id_not_ends_with',
        'local_id_not_in': 'local_id_not_in',
        'local_id_not_starts_with': 'local_id_not_starts_with',
        'local_id_starts_with': 'local_id_starts_with',
        '_not': 'NOT',
        '_or': 'OR',
        'rack_topoes_every': 'rack_topoes_every',
        'rack_topoes_none': 'rack_topoes_none',
        'rack_topoes_some': 'rack_topoes_some'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ZoneTopoWhereInput - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self.__and = None
        self._cluster = None
        self._cluster_topo = None
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
        self._local_id = None
        self._local_id_contains = None
        self._local_id_ends_with = None
        self._local_id_gt = None
        self._local_id_gte = None
        self._local_id_in = None
        self._local_id_lt = None
        self._local_id_lte = None
        self._local_id_not = None
        self._local_id_not_contains = None
        self._local_id_not_ends_with = None
        self._local_id_not_in = None
        self._local_id_not_starts_with = None
        self._local_id_starts_with = None
        self.__not = None
        self.__or = None
        self._rack_topoes_every = None
        self._rack_topoes_none = None
        self._rack_topoes_some = None
        self.discriminator = None

        self._and = kwargs.get("_and", None)
        self.cluster = kwargs.get("cluster", None)
        self.cluster_topo = kwargs.get("cluster_topo", None)
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
        self.local_id = kwargs.get("local_id", None)
        self.local_id_contains = kwargs.get("local_id_contains", None)
        self.local_id_ends_with = kwargs.get("local_id_ends_with", None)
        self.local_id_gt = kwargs.get("local_id_gt", None)
        self.local_id_gte = kwargs.get("local_id_gte", None)
        self.local_id_in = kwargs.get("local_id_in", None)
        self.local_id_lt = kwargs.get("local_id_lt", None)
        self.local_id_lte = kwargs.get("local_id_lte", None)
        self.local_id_not = kwargs.get("local_id_not", None)
        self.local_id_not_contains = kwargs.get("local_id_not_contains", None)
        self.local_id_not_ends_with = kwargs.get("local_id_not_ends_with", None)
        self.local_id_not_in = kwargs.get("local_id_not_in", None)
        self.local_id_not_starts_with = kwargs.get("local_id_not_starts_with", None)
        self.local_id_starts_with = kwargs.get("local_id_starts_with", None)
        self._not = kwargs.get("_not", None)
        self._or = kwargs.get("_or", None)
        self.rack_topoes_every = kwargs.get("rack_topoes_every", None)
        self.rack_topoes_none = kwargs.get("rack_topoes_none", None)
        self.rack_topoes_some = kwargs.get("rack_topoes_some", None)

    @property
    def _and(self):
        """Gets the _and of this ZoneTopoWhereInput.  # noqa: E501


        :return: The _and of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: list[ZoneTopoWhereInput]
        """
        return self.__and

    @_and.setter
    def _and(self, _and):
        """Sets the _and of this ZoneTopoWhereInput.


        :param _and: The _and of this ZoneTopoWhereInput.  # noqa: E501
        :type _and: list[ZoneTopoWhereInput]
        """

        self.__and = _and

    @property
    def cluster(self):
        """Gets the cluster of this ZoneTopoWhereInput.  # noqa: E501


        :return: The cluster of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: ClusterWhereInput
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this ZoneTopoWhereInput.


        :param cluster: The cluster of this ZoneTopoWhereInput.  # noqa: E501
        :type cluster: ClusterWhereInput
        """

        self._cluster = cluster

    @property
    def cluster_topo(self):
        """Gets the cluster_topo of this ZoneTopoWhereInput.  # noqa: E501


        :return: The cluster_topo of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: ClusterTopoWhereInput
        """
        return self._cluster_topo

    @cluster_topo.setter
    def cluster_topo(self, cluster_topo):
        """Sets the cluster_topo of this ZoneTopoWhereInput.


        :param cluster_topo: The cluster_topo of this ZoneTopoWhereInput.  # noqa: E501
        :type cluster_topo: ClusterTopoWhereInput
        """

        self._cluster_topo = cluster_topo

    @property
    def id(self):
        """Gets the id of this ZoneTopoWhereInput.  # noqa: E501


        :return: The id of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ZoneTopoWhereInput.


        :param id: The id of this ZoneTopoWhereInput.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def id_contains(self):
        """Gets the id_contains of this ZoneTopoWhereInput.  # noqa: E501


        :return: The id_contains of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_contains

    @id_contains.setter
    def id_contains(self, id_contains):
        """Sets the id_contains of this ZoneTopoWhereInput.


        :param id_contains: The id_contains of this ZoneTopoWhereInput.  # noqa: E501
        :type id_contains: str
        """

        self._id_contains = id_contains

    @property
    def id_ends_with(self):
        """Gets the id_ends_with of this ZoneTopoWhereInput.  # noqa: E501


        :return: The id_ends_with of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_ends_with

    @id_ends_with.setter
    def id_ends_with(self, id_ends_with):
        """Sets the id_ends_with of this ZoneTopoWhereInput.


        :param id_ends_with: The id_ends_with of this ZoneTopoWhereInput.  # noqa: E501
        :type id_ends_with: str
        """

        self._id_ends_with = id_ends_with

    @property
    def id_gt(self):
        """Gets the id_gt of this ZoneTopoWhereInput.  # noqa: E501


        :return: The id_gt of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_gt

    @id_gt.setter
    def id_gt(self, id_gt):
        """Sets the id_gt of this ZoneTopoWhereInput.


        :param id_gt: The id_gt of this ZoneTopoWhereInput.  # noqa: E501
        :type id_gt: str
        """

        self._id_gt = id_gt

    @property
    def id_gte(self):
        """Gets the id_gte of this ZoneTopoWhereInput.  # noqa: E501


        :return: The id_gte of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_gte

    @id_gte.setter
    def id_gte(self, id_gte):
        """Sets the id_gte of this ZoneTopoWhereInput.


        :param id_gte: The id_gte of this ZoneTopoWhereInput.  # noqa: E501
        :type id_gte: str
        """

        self._id_gte = id_gte

    @property
    def id_in(self):
        """Gets the id_in of this ZoneTopoWhereInput.  # noqa: E501


        :return: The id_in of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._id_in

    @id_in.setter
    def id_in(self, id_in):
        """Sets the id_in of this ZoneTopoWhereInput.


        :param id_in: The id_in of this ZoneTopoWhereInput.  # noqa: E501
        :type id_in: list[str]
        """

        self._id_in = id_in

    @property
    def id_lt(self):
        """Gets the id_lt of this ZoneTopoWhereInput.  # noqa: E501


        :return: The id_lt of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_lt

    @id_lt.setter
    def id_lt(self, id_lt):
        """Sets the id_lt of this ZoneTopoWhereInput.


        :param id_lt: The id_lt of this ZoneTopoWhereInput.  # noqa: E501
        :type id_lt: str
        """

        self._id_lt = id_lt

    @property
    def id_lte(self):
        """Gets the id_lte of this ZoneTopoWhereInput.  # noqa: E501


        :return: The id_lte of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_lte

    @id_lte.setter
    def id_lte(self, id_lte):
        """Sets the id_lte of this ZoneTopoWhereInput.


        :param id_lte: The id_lte of this ZoneTopoWhereInput.  # noqa: E501
        :type id_lte: str
        """

        self._id_lte = id_lte

    @property
    def id_not(self):
        """Gets the id_not of this ZoneTopoWhereInput.  # noqa: E501


        :return: The id_not of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not

    @id_not.setter
    def id_not(self, id_not):
        """Sets the id_not of this ZoneTopoWhereInput.


        :param id_not: The id_not of this ZoneTopoWhereInput.  # noqa: E501
        :type id_not: str
        """

        self._id_not = id_not

    @property
    def id_not_contains(self):
        """Gets the id_not_contains of this ZoneTopoWhereInput.  # noqa: E501


        :return: The id_not_contains of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not_contains

    @id_not_contains.setter
    def id_not_contains(self, id_not_contains):
        """Sets the id_not_contains of this ZoneTopoWhereInput.


        :param id_not_contains: The id_not_contains of this ZoneTopoWhereInput.  # noqa: E501
        :type id_not_contains: str
        """

        self._id_not_contains = id_not_contains

    @property
    def id_not_ends_with(self):
        """Gets the id_not_ends_with of this ZoneTopoWhereInput.  # noqa: E501


        :return: The id_not_ends_with of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not_ends_with

    @id_not_ends_with.setter
    def id_not_ends_with(self, id_not_ends_with):
        """Sets the id_not_ends_with of this ZoneTopoWhereInput.


        :param id_not_ends_with: The id_not_ends_with of this ZoneTopoWhereInput.  # noqa: E501
        :type id_not_ends_with: str
        """

        self._id_not_ends_with = id_not_ends_with

    @property
    def id_not_in(self):
        """Gets the id_not_in of this ZoneTopoWhereInput.  # noqa: E501


        :return: The id_not_in of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._id_not_in

    @id_not_in.setter
    def id_not_in(self, id_not_in):
        """Sets the id_not_in of this ZoneTopoWhereInput.


        :param id_not_in: The id_not_in of this ZoneTopoWhereInput.  # noqa: E501
        :type id_not_in: list[str]
        """

        self._id_not_in = id_not_in

    @property
    def id_not_starts_with(self):
        """Gets the id_not_starts_with of this ZoneTopoWhereInput.  # noqa: E501


        :return: The id_not_starts_with of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not_starts_with

    @id_not_starts_with.setter
    def id_not_starts_with(self, id_not_starts_with):
        """Sets the id_not_starts_with of this ZoneTopoWhereInput.


        :param id_not_starts_with: The id_not_starts_with of this ZoneTopoWhereInput.  # noqa: E501
        :type id_not_starts_with: str
        """

        self._id_not_starts_with = id_not_starts_with

    @property
    def id_starts_with(self):
        """Gets the id_starts_with of this ZoneTopoWhereInput.  # noqa: E501


        :return: The id_starts_with of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_starts_with

    @id_starts_with.setter
    def id_starts_with(self, id_starts_with):
        """Sets the id_starts_with of this ZoneTopoWhereInput.


        :param id_starts_with: The id_starts_with of this ZoneTopoWhereInput.  # noqa: E501
        :type id_starts_with: str
        """

        self._id_starts_with = id_starts_with

    @property
    def local_id(self):
        """Gets the local_id of this ZoneTopoWhereInput.  # noqa: E501


        :return: The local_id of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this ZoneTopoWhereInput.


        :param local_id: The local_id of this ZoneTopoWhereInput.  # noqa: E501
        :type local_id: str
        """

        self._local_id = local_id

    @property
    def local_id_contains(self):
        """Gets the local_id_contains of this ZoneTopoWhereInput.  # noqa: E501


        :return: The local_id_contains of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._local_id_contains

    @local_id_contains.setter
    def local_id_contains(self, local_id_contains):
        """Sets the local_id_contains of this ZoneTopoWhereInput.


        :param local_id_contains: The local_id_contains of this ZoneTopoWhereInput.  # noqa: E501
        :type local_id_contains: str
        """

        self._local_id_contains = local_id_contains

    @property
    def local_id_ends_with(self):
        """Gets the local_id_ends_with of this ZoneTopoWhereInput.  # noqa: E501


        :return: The local_id_ends_with of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._local_id_ends_with

    @local_id_ends_with.setter
    def local_id_ends_with(self, local_id_ends_with):
        """Sets the local_id_ends_with of this ZoneTopoWhereInput.


        :param local_id_ends_with: The local_id_ends_with of this ZoneTopoWhereInput.  # noqa: E501
        :type local_id_ends_with: str
        """

        self._local_id_ends_with = local_id_ends_with

    @property
    def local_id_gt(self):
        """Gets the local_id_gt of this ZoneTopoWhereInput.  # noqa: E501


        :return: The local_id_gt of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._local_id_gt

    @local_id_gt.setter
    def local_id_gt(self, local_id_gt):
        """Sets the local_id_gt of this ZoneTopoWhereInput.


        :param local_id_gt: The local_id_gt of this ZoneTopoWhereInput.  # noqa: E501
        :type local_id_gt: str
        """

        self._local_id_gt = local_id_gt

    @property
    def local_id_gte(self):
        """Gets the local_id_gte of this ZoneTopoWhereInput.  # noqa: E501


        :return: The local_id_gte of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._local_id_gte

    @local_id_gte.setter
    def local_id_gte(self, local_id_gte):
        """Sets the local_id_gte of this ZoneTopoWhereInput.


        :param local_id_gte: The local_id_gte of this ZoneTopoWhereInput.  # noqa: E501
        :type local_id_gte: str
        """

        self._local_id_gte = local_id_gte

    @property
    def local_id_in(self):
        """Gets the local_id_in of this ZoneTopoWhereInput.  # noqa: E501


        :return: The local_id_in of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._local_id_in

    @local_id_in.setter
    def local_id_in(self, local_id_in):
        """Sets the local_id_in of this ZoneTopoWhereInput.


        :param local_id_in: The local_id_in of this ZoneTopoWhereInput.  # noqa: E501
        :type local_id_in: list[str]
        """

        self._local_id_in = local_id_in

    @property
    def local_id_lt(self):
        """Gets the local_id_lt of this ZoneTopoWhereInput.  # noqa: E501


        :return: The local_id_lt of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._local_id_lt

    @local_id_lt.setter
    def local_id_lt(self, local_id_lt):
        """Sets the local_id_lt of this ZoneTopoWhereInput.


        :param local_id_lt: The local_id_lt of this ZoneTopoWhereInput.  # noqa: E501
        :type local_id_lt: str
        """

        self._local_id_lt = local_id_lt

    @property
    def local_id_lte(self):
        """Gets the local_id_lte of this ZoneTopoWhereInput.  # noqa: E501


        :return: The local_id_lte of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._local_id_lte

    @local_id_lte.setter
    def local_id_lte(self, local_id_lte):
        """Sets the local_id_lte of this ZoneTopoWhereInput.


        :param local_id_lte: The local_id_lte of this ZoneTopoWhereInput.  # noqa: E501
        :type local_id_lte: str
        """

        self._local_id_lte = local_id_lte

    @property
    def local_id_not(self):
        """Gets the local_id_not of this ZoneTopoWhereInput.  # noqa: E501


        :return: The local_id_not of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._local_id_not

    @local_id_not.setter
    def local_id_not(self, local_id_not):
        """Sets the local_id_not of this ZoneTopoWhereInput.


        :param local_id_not: The local_id_not of this ZoneTopoWhereInput.  # noqa: E501
        :type local_id_not: str
        """

        self._local_id_not = local_id_not

    @property
    def local_id_not_contains(self):
        """Gets the local_id_not_contains of this ZoneTopoWhereInput.  # noqa: E501


        :return: The local_id_not_contains of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._local_id_not_contains

    @local_id_not_contains.setter
    def local_id_not_contains(self, local_id_not_contains):
        """Sets the local_id_not_contains of this ZoneTopoWhereInput.


        :param local_id_not_contains: The local_id_not_contains of this ZoneTopoWhereInput.  # noqa: E501
        :type local_id_not_contains: str
        """

        self._local_id_not_contains = local_id_not_contains

    @property
    def local_id_not_ends_with(self):
        """Gets the local_id_not_ends_with of this ZoneTopoWhereInput.  # noqa: E501


        :return: The local_id_not_ends_with of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._local_id_not_ends_with

    @local_id_not_ends_with.setter
    def local_id_not_ends_with(self, local_id_not_ends_with):
        """Sets the local_id_not_ends_with of this ZoneTopoWhereInput.


        :param local_id_not_ends_with: The local_id_not_ends_with of this ZoneTopoWhereInput.  # noqa: E501
        :type local_id_not_ends_with: str
        """

        self._local_id_not_ends_with = local_id_not_ends_with

    @property
    def local_id_not_in(self):
        """Gets the local_id_not_in of this ZoneTopoWhereInput.  # noqa: E501


        :return: The local_id_not_in of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._local_id_not_in

    @local_id_not_in.setter
    def local_id_not_in(self, local_id_not_in):
        """Sets the local_id_not_in of this ZoneTopoWhereInput.


        :param local_id_not_in: The local_id_not_in of this ZoneTopoWhereInput.  # noqa: E501
        :type local_id_not_in: list[str]
        """

        self._local_id_not_in = local_id_not_in

    @property
    def local_id_not_starts_with(self):
        """Gets the local_id_not_starts_with of this ZoneTopoWhereInput.  # noqa: E501


        :return: The local_id_not_starts_with of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._local_id_not_starts_with

    @local_id_not_starts_with.setter
    def local_id_not_starts_with(self, local_id_not_starts_with):
        """Sets the local_id_not_starts_with of this ZoneTopoWhereInput.


        :param local_id_not_starts_with: The local_id_not_starts_with of this ZoneTopoWhereInput.  # noqa: E501
        :type local_id_not_starts_with: str
        """

        self._local_id_not_starts_with = local_id_not_starts_with

    @property
    def local_id_starts_with(self):
        """Gets the local_id_starts_with of this ZoneTopoWhereInput.  # noqa: E501


        :return: The local_id_starts_with of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._local_id_starts_with

    @local_id_starts_with.setter
    def local_id_starts_with(self, local_id_starts_with):
        """Sets the local_id_starts_with of this ZoneTopoWhereInput.


        :param local_id_starts_with: The local_id_starts_with of this ZoneTopoWhereInput.  # noqa: E501
        :type local_id_starts_with: str
        """

        self._local_id_starts_with = local_id_starts_with

    @property
    def _not(self):
        """Gets the _not of this ZoneTopoWhereInput.  # noqa: E501


        :return: The _not of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: list[ZoneTopoWhereInput]
        """
        return self.__not

    @_not.setter
    def _not(self, _not):
        """Sets the _not of this ZoneTopoWhereInput.


        :param _not: The _not of this ZoneTopoWhereInput.  # noqa: E501
        :type _not: list[ZoneTopoWhereInput]
        """

        self.__not = _not

    @property
    def _or(self):
        """Gets the _or of this ZoneTopoWhereInput.  # noqa: E501


        :return: The _or of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: list[ZoneTopoWhereInput]
        """
        return self.__or

    @_or.setter
    def _or(self, _or):
        """Sets the _or of this ZoneTopoWhereInput.


        :param _or: The _or of this ZoneTopoWhereInput.  # noqa: E501
        :type _or: list[ZoneTopoWhereInput]
        """

        self.__or = _or

    @property
    def rack_topoes_every(self):
        """Gets the rack_topoes_every of this ZoneTopoWhereInput.  # noqa: E501


        :return: The rack_topoes_every of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: RackTopoWhereInput
        """
        return self._rack_topoes_every

    @rack_topoes_every.setter
    def rack_topoes_every(self, rack_topoes_every):
        """Sets the rack_topoes_every of this ZoneTopoWhereInput.


        :param rack_topoes_every: The rack_topoes_every of this ZoneTopoWhereInput.  # noqa: E501
        :type rack_topoes_every: RackTopoWhereInput
        """

        self._rack_topoes_every = rack_topoes_every

    @property
    def rack_topoes_none(self):
        """Gets the rack_topoes_none of this ZoneTopoWhereInput.  # noqa: E501


        :return: The rack_topoes_none of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: RackTopoWhereInput
        """
        return self._rack_topoes_none

    @rack_topoes_none.setter
    def rack_topoes_none(self, rack_topoes_none):
        """Sets the rack_topoes_none of this ZoneTopoWhereInput.


        :param rack_topoes_none: The rack_topoes_none of this ZoneTopoWhereInput.  # noqa: E501
        :type rack_topoes_none: RackTopoWhereInput
        """

        self._rack_topoes_none = rack_topoes_none

    @property
    def rack_topoes_some(self):
        """Gets the rack_topoes_some of this ZoneTopoWhereInput.  # noqa: E501


        :return: The rack_topoes_some of this ZoneTopoWhereInput.  # noqa: E501
        :rtype: RackTopoWhereInput
        """
        return self._rack_topoes_some

    @rack_topoes_some.setter
    def rack_topoes_some(self, rack_topoes_some):
        """Sets the rack_topoes_some of this ZoneTopoWhereInput.


        :param rack_topoes_some: The rack_topoes_some of this ZoneTopoWhereInput.  # noqa: E501
        :type rack_topoes_some: RackTopoWhereInput
        """

        self._rack_topoes_some = rack_topoes_some

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
        if not isinstance(other, ZoneTopoWhereInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ZoneTopoWhereInput):
            return True

        return self.to_dict() != other.to_dict()
