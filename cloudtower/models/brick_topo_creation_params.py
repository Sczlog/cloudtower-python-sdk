# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.0.0
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


class BrickTopoCreationParams(object):
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
        'tag_position_in_brick': 'list[NestedTagPosition]',
        'node_topoes': 'NodeTopoWhereInput',
        'rack_topo_id': 'str',
        'capacity': 'NestedCapacity',
        'cluster_id': 'str',
        'height': 'int',
        'name': 'str',
        'position': 'int'
    }

    attribute_map = {
        'tag_position_in_brick': 'tag_position_in_brick',
        'node_topoes': 'node_topoes',
        'rack_topo_id': 'rack_topo_id',
        'capacity': 'capacity',
        'cluster_id': 'cluster_id',
        'height': 'height',
        'name': 'name',
        'position': 'position'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """BrickTopoCreationParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._tag_position_in_brick = None
        self._node_topoes = None
        self._rack_topo_id = None
        self._capacity = None
        self._cluster_id = None
        self._height = None
        self._name = None
        self._position = None
        self.discriminator = None

        self.tag_position_in_brick = kwargs.get("tag_position_in_brick", None)
        if "node_topoes" in kwargs:
            self.node_topoes = kwargs["node_topoes"]
        if "rack_topo_id" in kwargs:
            self.rack_topo_id = kwargs["rack_topo_id"]
        if "capacity" in kwargs:
            self.capacity = kwargs["capacity"]
        if "cluster_id" in kwargs:
            self.cluster_id = kwargs["cluster_id"]
        if "height" in kwargs:
            self.height = kwargs["height"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "position" in kwargs:
            self.position = kwargs["position"]

    @property
    def tag_position_in_brick(self):
        """Gets the tag_position_in_brick of this BrickTopoCreationParams.  # noqa: E501


        :return: The tag_position_in_brick of this BrickTopoCreationParams.  # noqa: E501
        :rtype: list[NestedTagPosition]
        """
        return self._tag_position_in_brick

    @tag_position_in_brick.setter
    def tag_position_in_brick(self, tag_position_in_brick):
        """Sets the tag_position_in_brick of this BrickTopoCreationParams.


        :param tag_position_in_brick: The tag_position_in_brick of this BrickTopoCreationParams.  # noqa: E501
        :type tag_position_in_brick: list[NestedTagPosition]
        """

        self._tag_position_in_brick = tag_position_in_brick

    @property
    def node_topoes(self):
        """Gets the node_topoes of this BrickTopoCreationParams.  # noqa: E501


        :return: The node_topoes of this BrickTopoCreationParams.  # noqa: E501
        :rtype: NodeTopoWhereInput
        """
        return self._node_topoes

    @node_topoes.setter
    def node_topoes(self, node_topoes):
        """Sets the node_topoes of this BrickTopoCreationParams.


        :param node_topoes: The node_topoes of this BrickTopoCreationParams.  # noqa: E501
        :type node_topoes: NodeTopoWhereInput
        """

        self._node_topoes = node_topoes

    @property
    def rack_topo_id(self):
        """Gets the rack_topo_id of this BrickTopoCreationParams.  # noqa: E501


        :return: The rack_topo_id of this BrickTopoCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._rack_topo_id

    @rack_topo_id.setter
    def rack_topo_id(self, rack_topo_id):
        """Sets the rack_topo_id of this BrickTopoCreationParams.


        :param rack_topo_id: The rack_topo_id of this BrickTopoCreationParams.  # noqa: E501
        :type rack_topo_id: str
        """

        self._rack_topo_id = rack_topo_id

    @property
    def capacity(self):
        """Gets the capacity of this BrickTopoCreationParams.  # noqa: E501


        :return: The capacity of this BrickTopoCreationParams.  # noqa: E501
        :rtype: NestedCapacity
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this BrickTopoCreationParams.


        :param capacity: The capacity of this BrickTopoCreationParams.  # noqa: E501
        :type capacity: NestedCapacity
        """

        self._capacity = capacity

    @property
    def cluster_id(self):
        """Gets the cluster_id of this BrickTopoCreationParams.  # noqa: E501


        :return: The cluster_id of this BrickTopoCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this BrickTopoCreationParams.


        :param cluster_id: The cluster_id of this BrickTopoCreationParams.  # noqa: E501
        :type cluster_id: str
        """
        if self.local_vars_configuration.client_side_validation and cluster_id is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def height(self):
        """Gets the height of this BrickTopoCreationParams.  # noqa: E501


        :return: The height of this BrickTopoCreationParams.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this BrickTopoCreationParams.


        :param height: The height of this BrickTopoCreationParams.  # noqa: E501
        :type height: int
        """
        if self.local_vars_configuration.client_side_validation and height is None:  # noqa: E501
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    @property
    def name(self):
        """Gets the name of this BrickTopoCreationParams.  # noqa: E501


        :return: The name of this BrickTopoCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BrickTopoCreationParams.


        :param name: The name of this BrickTopoCreationParams.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def position(self):
        """Gets the position of this BrickTopoCreationParams.  # noqa: E501


        :return: The position of this BrickTopoCreationParams.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this BrickTopoCreationParams.


        :param position: The position of this BrickTopoCreationParams.  # noqa: E501
        :type position: int
        """
        if self.local_vars_configuration.client_side_validation and position is None:  # noqa: E501
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501

        self._position = position

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
        if not isinstance(other, BrickTopoCreationParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BrickTopoCreationParams):
            return True

        return self.to_dict() != other.to_dict()
