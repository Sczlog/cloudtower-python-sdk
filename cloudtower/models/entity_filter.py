# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class EntityFilter(object):
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
        'apply_to_all_clusters': 'bool',
        'clusters': 'list[NestedCluster]',
        'entity_type': 'EntityType',
        'exclude_ids': 'list[str]',
        'exec_failed_cluster': 'list[NestedCluster]',
        'filter_error': 'list[str]',
        'filter_status': 'FilterStatus',
        'id': 'str',
        'ids': 'list[str]',
        'last_executed_at': 'str',
        'name': 'str',
        'preset': 'str',
        'rules': 'list[NestedFilterRule]'
    }

    attribute_map = {
        'apply_to_all_clusters': 'apply_to_all_clusters',
        'clusters': 'clusters',
        'entity_type': 'entity_type',
        'exclude_ids': 'exclude_ids',
        'exec_failed_cluster': 'exec_failed_cluster',
        'filter_error': 'filter_error',
        'filter_status': 'filter_status',
        'id': 'id',
        'ids': 'ids',
        'last_executed_at': 'last_executed_at',
        'name': 'name',
        'preset': 'preset',
        'rules': 'rules'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """EntityFilter - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._apply_to_all_clusters = None
        self._clusters = None
        self._entity_type = None
        self._exclude_ids = None
        self._exec_failed_cluster = None
        self._filter_error = None
        self._filter_status = None
        self._id = None
        self._ids = None
        self._last_executed_at = None
        self._name = None
        self._preset = None
        self._rules = None
        self.discriminator = None

        self.apply_to_all_clusters = kwargs.get("apply_to_all_clusters", None)
        self.clusters = kwargs.get("clusters", None)
        if "entity_type" in kwargs:
            self.entity_type = kwargs["entity_type"]
        if "exclude_ids" in kwargs:
            self.exclude_ids = kwargs["exclude_ids"]
        self.exec_failed_cluster = kwargs.get("exec_failed_cluster", None)
        if "filter_error" in kwargs:
            self.filter_error = kwargs["filter_error"]
        if "filter_status" in kwargs:
            self.filter_status = kwargs["filter_status"]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "ids" in kwargs:
            self.ids = kwargs["ids"]
        self.last_executed_at = kwargs.get("last_executed_at", None)
        if "name" in kwargs:
            self.name = kwargs["name"]
        self.preset = kwargs.get("preset", None)
        if "rules" in kwargs:
            self.rules = kwargs["rules"]

    @property
    def apply_to_all_clusters(self):
        """Gets the apply_to_all_clusters of this EntityFilter.  # noqa: E501


        :return: The apply_to_all_clusters of this EntityFilter.  # noqa: E501
        :rtype: bool
        """
        return self._apply_to_all_clusters

    @apply_to_all_clusters.setter
    def apply_to_all_clusters(self, apply_to_all_clusters):
        """Sets the apply_to_all_clusters of this EntityFilter.


        :param apply_to_all_clusters: The apply_to_all_clusters of this EntityFilter.  # noqa: E501
        :type apply_to_all_clusters: bool
        """

        self._apply_to_all_clusters = apply_to_all_clusters

    @property
    def clusters(self):
        """Gets the clusters of this EntityFilter.  # noqa: E501


        :return: The clusters of this EntityFilter.  # noqa: E501
        :rtype: list[NestedCluster]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this EntityFilter.


        :param clusters: The clusters of this EntityFilter.  # noqa: E501
        :type clusters: list[NestedCluster]
        """

        self._clusters = clusters

    @property
    def entity_type(self):
        """Gets the entity_type of this EntityFilter.  # noqa: E501


        :return: The entity_type of this EntityFilter.  # noqa: E501
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this EntityFilter.


        :param entity_type: The entity_type of this EntityFilter.  # noqa: E501
        :type entity_type: EntityType
        """
        if self.local_vars_configuration.client_side_validation and entity_type is None:  # noqa: E501
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def exclude_ids(self):
        """Gets the exclude_ids of this EntityFilter.  # noqa: E501


        :return: The exclude_ids of this EntityFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclude_ids

    @exclude_ids.setter
    def exclude_ids(self, exclude_ids):
        """Sets the exclude_ids of this EntityFilter.


        :param exclude_ids: The exclude_ids of this EntityFilter.  # noqa: E501
        :type exclude_ids: list[str]
        """
        if self.local_vars_configuration.client_side_validation and exclude_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `exclude_ids`, must not be `None`")  # noqa: E501

        self._exclude_ids = exclude_ids

    @property
    def exec_failed_cluster(self):
        """Gets the exec_failed_cluster of this EntityFilter.  # noqa: E501


        :return: The exec_failed_cluster of this EntityFilter.  # noqa: E501
        :rtype: list[NestedCluster]
        """
        return self._exec_failed_cluster

    @exec_failed_cluster.setter
    def exec_failed_cluster(self, exec_failed_cluster):
        """Sets the exec_failed_cluster of this EntityFilter.


        :param exec_failed_cluster: The exec_failed_cluster of this EntityFilter.  # noqa: E501
        :type exec_failed_cluster: list[NestedCluster]
        """

        self._exec_failed_cluster = exec_failed_cluster

    @property
    def filter_error(self):
        """Gets the filter_error of this EntityFilter.  # noqa: E501


        :return: The filter_error of this EntityFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._filter_error

    @filter_error.setter
    def filter_error(self, filter_error):
        """Sets the filter_error of this EntityFilter.


        :param filter_error: The filter_error of this EntityFilter.  # noqa: E501
        :type filter_error: list[str]
        """
        if self.local_vars_configuration.client_side_validation and filter_error is None:  # noqa: E501
            raise ValueError("Invalid value for `filter_error`, must not be `None`")  # noqa: E501

        self._filter_error = filter_error

    @property
    def filter_status(self):
        """Gets the filter_status of this EntityFilter.  # noqa: E501


        :return: The filter_status of this EntityFilter.  # noqa: E501
        :rtype: FilterStatus
        """
        return self._filter_status

    @filter_status.setter
    def filter_status(self, filter_status):
        """Sets the filter_status of this EntityFilter.


        :param filter_status: The filter_status of this EntityFilter.  # noqa: E501
        :type filter_status: FilterStatus
        """
        if self.local_vars_configuration.client_side_validation and filter_status is None:  # noqa: E501
            raise ValueError("Invalid value for `filter_status`, must not be `None`")  # noqa: E501

        self._filter_status = filter_status

    @property
    def id(self):
        """Gets the id of this EntityFilter.  # noqa: E501


        :return: The id of this EntityFilter.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EntityFilter.


        :param id: The id of this EntityFilter.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def ids(self):
        """Gets the ids of this EntityFilter.  # noqa: E501


        :return: The ids of this EntityFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this EntityFilter.


        :param ids: The ids of this EntityFilter.  # noqa: E501
        :type ids: list[str]
        """
        if self.local_vars_configuration.client_side_validation and ids is None:  # noqa: E501
            raise ValueError("Invalid value for `ids`, must not be `None`")  # noqa: E501

        self._ids = ids

    @property
    def last_executed_at(self):
        """Gets the last_executed_at of this EntityFilter.  # noqa: E501


        :return: The last_executed_at of this EntityFilter.  # noqa: E501
        :rtype: str
        """
        return self._last_executed_at

    @last_executed_at.setter
    def last_executed_at(self, last_executed_at):
        """Sets the last_executed_at of this EntityFilter.


        :param last_executed_at: The last_executed_at of this EntityFilter.  # noqa: E501
        :type last_executed_at: str
        """

        self._last_executed_at = last_executed_at

    @property
    def name(self):
        """Gets the name of this EntityFilter.  # noqa: E501


        :return: The name of this EntityFilter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EntityFilter.


        :param name: The name of this EntityFilter.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def preset(self):
        """Gets the preset of this EntityFilter.  # noqa: E501


        :return: The preset of this EntityFilter.  # noqa: E501
        :rtype: str
        """
        return self._preset

    @preset.setter
    def preset(self, preset):
        """Sets the preset of this EntityFilter.


        :param preset: The preset of this EntityFilter.  # noqa: E501
        :type preset: str
        """

        self._preset = preset

    @property
    def rules(self):
        """Gets the rules of this EntityFilter.  # noqa: E501


        :return: The rules of this EntityFilter.  # noqa: E501
        :rtype: list[NestedFilterRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this EntityFilter.


        :param rules: The rules of this EntityFilter.  # noqa: E501
        :type rules: list[NestedFilterRule]
        """
        if self.local_vars_configuration.client_side_validation and rules is None:  # noqa: E501
            raise ValueError("Invalid value for `rules`, must not be `None`")  # noqa: E501

        self._rules = rules

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
        if not isinstance(other, EntityFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EntityFilter):
            return True

        return self.to_dict() != other.to_dict()
