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


class ClusterTopo(object):
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
        'brick_topoes': 'list[NestedBrickTopo]',
        'cluster': 'NestedCluster',
        'id': 'str',
        'local_id': 'str',
        'name': 'str',
        'node_topoes': 'list[NestedNodeTopo]',
        'zone_topoes': 'list[NestedZoneTopo]'
    }

    attribute_map = {
        'brick_topoes': 'brick_topoes',
        'cluster': 'cluster',
        'id': 'id',
        'local_id': 'local_id',
        'name': 'name',
        'node_topoes': 'node_topoes',
        'zone_topoes': 'zone_topoes'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ClusterTopo - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._brick_topoes = None
        self._cluster = None
        self._id = None
        self._local_id = None
        self._name = None
        self._node_topoes = None
        self._zone_topoes = None
        self.discriminator = None

        self.brick_topoes = kwargs.get("brick_topoes", None)
        if "cluster" in kwargs:
            self.cluster = kwargs["cluster"]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        self.node_topoes = kwargs.get("node_topoes", None)
        self.zone_topoes = kwargs.get("zone_topoes", None)

    @property
    def brick_topoes(self):
        """Gets the brick_topoes of this ClusterTopo.  # noqa: E501


        :return: The brick_topoes of this ClusterTopo.  # noqa: E501
        :rtype: list[NestedBrickTopo]
        """
        return self._brick_topoes

    @brick_topoes.setter
    def brick_topoes(self, brick_topoes):
        """Sets the brick_topoes of this ClusterTopo.


        :param brick_topoes: The brick_topoes of this ClusterTopo.  # noqa: E501
        :type brick_topoes: list[NestedBrickTopo]
        """

        self._brick_topoes = brick_topoes

    @property
    def cluster(self):
        """Gets the cluster of this ClusterTopo.  # noqa: E501


        :return: The cluster of this ClusterTopo.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this ClusterTopo.


        :param cluster: The cluster of this ClusterTopo.  # noqa: E501
        :type cluster: NestedCluster
        """
        if self.local_vars_configuration.client_side_validation and cluster is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster`, must not be `None`")  # noqa: E501

        self._cluster = cluster

    @property
    def id(self):
        """Gets the id of this ClusterTopo.  # noqa: E501


        :return: The id of this ClusterTopo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterTopo.


        :param id: The id of this ClusterTopo.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def local_id(self):
        """Gets the local_id of this ClusterTopo.  # noqa: E501


        :return: The local_id of this ClusterTopo.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this ClusterTopo.


        :param local_id: The local_id of this ClusterTopo.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def name(self):
        """Gets the name of this ClusterTopo.  # noqa: E501


        :return: The name of this ClusterTopo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterTopo.


        :param name: The name of this ClusterTopo.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def node_topoes(self):
        """Gets the node_topoes of this ClusterTopo.  # noqa: E501


        :return: The node_topoes of this ClusterTopo.  # noqa: E501
        :rtype: list[NestedNodeTopo]
        """
        return self._node_topoes

    @node_topoes.setter
    def node_topoes(self, node_topoes):
        """Sets the node_topoes of this ClusterTopo.


        :param node_topoes: The node_topoes of this ClusterTopo.  # noqa: E501
        :type node_topoes: list[NestedNodeTopo]
        """

        self._node_topoes = node_topoes

    @property
    def zone_topoes(self):
        """Gets the zone_topoes of this ClusterTopo.  # noqa: E501


        :return: The zone_topoes of this ClusterTopo.  # noqa: E501
        :rtype: list[NestedZoneTopo]
        """
        return self._zone_topoes

    @zone_topoes.setter
    def zone_topoes(self, zone_topoes):
        """Sets the zone_topoes of this ClusterTopo.


        :param zone_topoes: The zone_topoes of this ClusterTopo.  # noqa: E501
        :type zone_topoes: list[NestedZoneTopo]
        """

        self._zone_topoes = zone_topoes

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
        if not isinstance(other, ClusterTopo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterTopo):
            return True

        return self.to_dict() != other.to_dict()
