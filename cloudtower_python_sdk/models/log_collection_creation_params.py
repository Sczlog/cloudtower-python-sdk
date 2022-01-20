# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 1.9.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower_python_sdk.configuration import Configuration


class LogCollectionCreationParams(object):
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
        'witness_id': 'str',
        'groups': 'list[str]',
        'services': 'list[str]',
        'log_ended_at': 'datetime',
        'log_started_at': 'datetime',
        'cluster_id': 'str',
        'hosts': 'HostWhereInput'
    }

    attribute_map = {
        'witness_id': 'witness_id',
        'groups': 'groups',
        'services': 'services',
        'log_ended_at': 'log_ended_at',
        'log_started_at': 'log_started_at',
        'cluster_id': 'cluster_id',
        'hosts': 'hosts'
    }

    def __init__(self, witness_id=None, groups=None, services=None, log_ended_at=None, log_started_at=None, cluster_id=None, hosts=None, local_vars_configuration=None):  # noqa: E501
        """LogCollectionCreationParams - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._witness_id = None
        self._groups = None
        self._services = None
        self._log_ended_at = None
        self._log_started_at = None
        self._cluster_id = None
        self._hosts = None
        self.discriminator = None

        if witness_id is not None:
            self.witness_id = witness_id
        if groups is not None:
            self.groups = groups
        if services is not None:
            self.services = services
        self.log_ended_at = log_ended_at
        self.log_started_at = log_started_at
        self.cluster_id = cluster_id
        self.hosts = hosts

    @property
    def witness_id(self):
        """Gets the witness_id of this LogCollectionCreationParams.  # noqa: E501


        :return: The witness_id of this LogCollectionCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._witness_id

    @witness_id.setter
    def witness_id(self, witness_id):
        """Sets the witness_id of this LogCollectionCreationParams.


        :param witness_id: The witness_id of this LogCollectionCreationParams.  # noqa: E501
        :type witness_id: str
        """

        self._witness_id = witness_id

    @property
    def groups(self):
        """Gets the groups of this LogCollectionCreationParams.  # noqa: E501


        :return: The groups of this LogCollectionCreationParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this LogCollectionCreationParams.


        :param groups: The groups of this LogCollectionCreationParams.  # noqa: E501
        :type groups: list[str]
        """

        self._groups = groups

    @property
    def services(self):
        """Gets the services of this LogCollectionCreationParams.  # noqa: E501


        :return: The services of this LogCollectionCreationParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this LogCollectionCreationParams.


        :param services: The services of this LogCollectionCreationParams.  # noqa: E501
        :type services: list[str]
        """

        self._services = services

    @property
    def log_ended_at(self):
        """Gets the log_ended_at of this LogCollectionCreationParams.  # noqa: E501


        :return: The log_ended_at of this LogCollectionCreationParams.  # noqa: E501
        :rtype: datetime
        """
        return self._log_ended_at

    @log_ended_at.setter
    def log_ended_at(self, log_ended_at):
        """Sets the log_ended_at of this LogCollectionCreationParams.


        :param log_ended_at: The log_ended_at of this LogCollectionCreationParams.  # noqa: E501
        :type log_ended_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and log_ended_at is None:  # noqa: E501
            raise ValueError("Invalid value for `log_ended_at`, must not be `None`")  # noqa: E501

        self._log_ended_at = log_ended_at

    @property
    def log_started_at(self):
        """Gets the log_started_at of this LogCollectionCreationParams.  # noqa: E501


        :return: The log_started_at of this LogCollectionCreationParams.  # noqa: E501
        :rtype: datetime
        """
        return self._log_started_at

    @log_started_at.setter
    def log_started_at(self, log_started_at):
        """Sets the log_started_at of this LogCollectionCreationParams.


        :param log_started_at: The log_started_at of this LogCollectionCreationParams.  # noqa: E501
        :type log_started_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and log_started_at is None:  # noqa: E501
            raise ValueError("Invalid value for `log_started_at`, must not be `None`")  # noqa: E501

        self._log_started_at = log_started_at

    @property
    def cluster_id(self):
        """Gets the cluster_id of this LogCollectionCreationParams.  # noqa: E501


        :return: The cluster_id of this LogCollectionCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this LogCollectionCreationParams.


        :param cluster_id: The cluster_id of this LogCollectionCreationParams.  # noqa: E501
        :type cluster_id: str
        """
        if self.local_vars_configuration.client_side_validation and cluster_id is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def hosts(self):
        """Gets the hosts of this LogCollectionCreationParams.  # noqa: E501


        :return: The hosts of this LogCollectionCreationParams.  # noqa: E501
        :rtype: HostWhereInput
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this LogCollectionCreationParams.


        :param hosts: The hosts of this LogCollectionCreationParams.  # noqa: E501
        :type hosts: HostWhereInput
        """
        if self.local_vars_configuration.client_side_validation and hosts is None:  # noqa: E501
            raise ValueError("Invalid value for `hosts`, must not be `None`")  # noqa: E501

        self._hosts = hosts

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
        if not isinstance(other, LogCollectionCreationParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LogCollectionCreationParams):
            return True

        return self.to_dict() != other.to_dict()
