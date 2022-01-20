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


class NfsExportCreationParams(object):
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
        'cluster_id': 'str',
        'ip_whitelist': 'str',
        'thin_provision': 'bool',
        'replica_num': 'int',
        'name': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'ip_whitelist': 'ip_whitelist',
        'thin_provision': 'thin_provision',
        'replica_num': 'replica_num',
        'name': 'name'
    }

    def __init__(self, cluster_id=None, ip_whitelist=None, thin_provision=None, replica_num=None, name=None, local_vars_configuration=None):  # noqa: E501
        """NfsExportCreationParams - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cluster_id = None
        self._ip_whitelist = None
        self._thin_provision = None
        self._replica_num = None
        self._name = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if ip_whitelist is not None:
            self.ip_whitelist = ip_whitelist
        self.thin_provision = thin_provision
        self.replica_num = replica_num
        self.name = name

    @property
    def cluster_id(self):
        """Gets the cluster_id of this NfsExportCreationParams.  # noqa: E501


        :return: The cluster_id of this NfsExportCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this NfsExportCreationParams.


        :param cluster_id: The cluster_id of this NfsExportCreationParams.  # noqa: E501
        :type cluster_id: str
        """
        if self.local_vars_configuration.client_side_validation and cluster_id is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def ip_whitelist(self):
        """Gets the ip_whitelist of this NfsExportCreationParams.  # noqa: E501


        :return: The ip_whitelist of this NfsExportCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._ip_whitelist

    @ip_whitelist.setter
    def ip_whitelist(self, ip_whitelist):
        """Sets the ip_whitelist of this NfsExportCreationParams.


        :param ip_whitelist: The ip_whitelist of this NfsExportCreationParams.  # noqa: E501
        :type ip_whitelist: str
        """

        self._ip_whitelist = ip_whitelist

    @property
    def thin_provision(self):
        """Gets the thin_provision of this NfsExportCreationParams.  # noqa: E501


        :return: The thin_provision of this NfsExportCreationParams.  # noqa: E501
        :rtype: bool
        """
        return self._thin_provision

    @thin_provision.setter
    def thin_provision(self, thin_provision):
        """Sets the thin_provision of this NfsExportCreationParams.


        :param thin_provision: The thin_provision of this NfsExportCreationParams.  # noqa: E501
        :type thin_provision: bool
        """
        if self.local_vars_configuration.client_side_validation and thin_provision is None:  # noqa: E501
            raise ValueError("Invalid value for `thin_provision`, must not be `None`")  # noqa: E501

        self._thin_provision = thin_provision

    @property
    def replica_num(self):
        """Gets the replica_num of this NfsExportCreationParams.  # noqa: E501


        :return: The replica_num of this NfsExportCreationParams.  # noqa: E501
        :rtype: int
        """
        return self._replica_num

    @replica_num.setter
    def replica_num(self, replica_num):
        """Sets the replica_num of this NfsExportCreationParams.


        :param replica_num: The replica_num of this NfsExportCreationParams.  # noqa: E501
        :type replica_num: int
        """
        if self.local_vars_configuration.client_side_validation and replica_num is None:  # noqa: E501
            raise ValueError("Invalid value for `replica_num`, must not be `None`")  # noqa: E501

        self._replica_num = replica_num

    @property
    def name(self):
        """Gets the name of this NfsExportCreationParams.  # noqa: E501


        :return: The name of this NfsExportCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NfsExportCreationParams.


        :param name: The name of this NfsExportCreationParams.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, NfsExportCreationParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NfsExportCreationParams):
            return True

        return self.to_dict() != other.to_dict()
