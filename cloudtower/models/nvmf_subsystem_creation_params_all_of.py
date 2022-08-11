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


class NvmfSubsystemCreationParamsAllOf(object):
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
        'replica_num': 'int',
        'thin_provision': 'bool',
        'stripe_size': 'int',
        'stripe_num': 'int',
        'policy': 'NvmfSubsystemPolicyType',
        'cluster_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'replica_num': 'replica_num',
        'thin_provision': 'thin_provision',
        'stripe_size': 'stripe_size',
        'stripe_num': 'stripe_num',
        'policy': 'policy',
        'cluster_id': 'cluster_id',
        'name': 'name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NvmfSubsystemCreationParamsAllOf - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._replica_num = None
        self._thin_provision = None
        self._stripe_size = None
        self._stripe_num = None
        self._policy = None
        self._cluster_id = None
        self._name = None
        self.discriminator = None

        if "replica_num" in kwargs:
            self.replica_num = kwargs["replica_num"]
        if "thin_provision" in kwargs:
            self.thin_provision = kwargs["thin_provision"]
        if "stripe_size" in kwargs:
            self.stripe_size = kwargs["stripe_size"]
        if "stripe_num" in kwargs:
            self.stripe_num = kwargs["stripe_num"]
        if "policy" in kwargs:
            self.policy = kwargs["policy"]
        if "cluster_id" in kwargs:
            self.cluster_id = kwargs["cluster_id"]
        if "name" in kwargs:
            self.name = kwargs["name"]

    @property
    def replica_num(self):
        """Gets the replica_num of this NvmfSubsystemCreationParamsAllOf.  # noqa: E501


        :return: The replica_num of this NvmfSubsystemCreationParamsAllOf.  # noqa: E501
        :rtype: int
        """
        return self._replica_num

    @replica_num.setter
    def replica_num(self, replica_num):
        """Sets the replica_num of this NvmfSubsystemCreationParamsAllOf.


        :param replica_num: The replica_num of this NvmfSubsystemCreationParamsAllOf.  # noqa: E501
        :type replica_num: int
        """
        if self.local_vars_configuration.client_side_validation and replica_num is None:  # noqa: E501
            raise ValueError("Invalid value for `replica_num`, must not be `None`")  # noqa: E501

        self._replica_num = replica_num

    @property
    def thin_provision(self):
        """Gets the thin_provision of this NvmfSubsystemCreationParamsAllOf.  # noqa: E501


        :return: The thin_provision of this NvmfSubsystemCreationParamsAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._thin_provision

    @thin_provision.setter
    def thin_provision(self, thin_provision):
        """Sets the thin_provision of this NvmfSubsystemCreationParamsAllOf.


        :param thin_provision: The thin_provision of this NvmfSubsystemCreationParamsAllOf.  # noqa: E501
        :type thin_provision: bool
        """
        if self.local_vars_configuration.client_side_validation and thin_provision is None:  # noqa: E501
            raise ValueError("Invalid value for `thin_provision`, must not be `None`")  # noqa: E501

        self._thin_provision = thin_provision

    @property
    def stripe_size(self):
        """Gets the stripe_size of this NvmfSubsystemCreationParamsAllOf.  # noqa: E501


        :return: The stripe_size of this NvmfSubsystemCreationParamsAllOf.  # noqa: E501
        :rtype: int
        """
        return self._stripe_size

    @stripe_size.setter
    def stripe_size(self, stripe_size):
        """Sets the stripe_size of this NvmfSubsystemCreationParamsAllOf.


        :param stripe_size: The stripe_size of this NvmfSubsystemCreationParamsAllOf.  # noqa: E501
        :type stripe_size: int
        """
        if self.local_vars_configuration.client_side_validation and stripe_size is None:  # noqa: E501
            raise ValueError("Invalid value for `stripe_size`, must not be `None`")  # noqa: E501

        self._stripe_size = stripe_size

    @property
    def stripe_num(self):
        """Gets the stripe_num of this NvmfSubsystemCreationParamsAllOf.  # noqa: E501


        :return: The stripe_num of this NvmfSubsystemCreationParamsAllOf.  # noqa: E501
        :rtype: int
        """
        return self._stripe_num

    @stripe_num.setter
    def stripe_num(self, stripe_num):
        """Sets the stripe_num of this NvmfSubsystemCreationParamsAllOf.


        :param stripe_num: The stripe_num of this NvmfSubsystemCreationParamsAllOf.  # noqa: E501
        :type stripe_num: int
        """
        if self.local_vars_configuration.client_side_validation and stripe_num is None:  # noqa: E501
            raise ValueError("Invalid value for `stripe_num`, must not be `None`")  # noqa: E501

        self._stripe_num = stripe_num

    @property
    def policy(self):
        """Gets the policy of this NvmfSubsystemCreationParamsAllOf.  # noqa: E501


        :return: The policy of this NvmfSubsystemCreationParamsAllOf.  # noqa: E501
        :rtype: NvmfSubsystemPolicyType
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this NvmfSubsystemCreationParamsAllOf.


        :param policy: The policy of this NvmfSubsystemCreationParamsAllOf.  # noqa: E501
        :type policy: NvmfSubsystemPolicyType
        """
        if self.local_vars_configuration.client_side_validation and policy is None:  # noqa: E501
            raise ValueError("Invalid value for `policy`, must not be `None`")  # noqa: E501

        self._policy = policy

    @property
    def cluster_id(self):
        """Gets the cluster_id of this NvmfSubsystemCreationParamsAllOf.  # noqa: E501


        :return: The cluster_id of this NvmfSubsystemCreationParamsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this NvmfSubsystemCreationParamsAllOf.


        :param cluster_id: The cluster_id of this NvmfSubsystemCreationParamsAllOf.  # noqa: E501
        :type cluster_id: str
        """
        if self.local_vars_configuration.client_side_validation and cluster_id is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def name(self):
        """Gets the name of this NvmfSubsystemCreationParamsAllOf.  # noqa: E501


        :return: The name of this NvmfSubsystemCreationParamsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NvmfSubsystemCreationParamsAllOf.


        :param name: The name of this NvmfSubsystemCreationParamsAllOf.  # noqa: E501
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
        if not isinstance(other, NvmfSubsystemCreationParamsAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NvmfSubsystemCreationParamsAllOf):
            return True

        return self.to_dict() != other.to_dict()
