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


class AlertRule(object):
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
        'cluster': 'NestedCluster',
        'customized': 'bool',
        'disabled': 'bool',
        'global_alert_rule': 'NestedGlobalAlertRule',
        'id': 'str',
        'local_id': 'str',
        'thresholds': 'list[NestedThresholds]'
    }

    attribute_map = {
        'cluster': 'cluster',
        'customized': 'customized',
        'disabled': 'disabled',
        'global_alert_rule': 'global_alert_rule',
        'id': 'id',
        'local_id': 'local_id',
        'thresholds': 'thresholds'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """AlertRule - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._cluster = None
        self._customized = None
        self._disabled = None
        self._global_alert_rule = None
        self._id = None
        self._local_id = None
        self._thresholds = None
        self.discriminator = None

        if "cluster" in kwargs:
            self.cluster = kwargs["cluster"]
        if "customized" in kwargs:
            self.customized = kwargs["customized"]
        if "disabled" in kwargs:
            self.disabled = kwargs["disabled"]
        if "global_alert_rule" in kwargs:
            self.global_alert_rule = kwargs["global_alert_rule"]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        if "thresholds" in kwargs:
            self.thresholds = kwargs["thresholds"]

    @property
    def cluster(self):
        """Gets the cluster of this AlertRule.  # noqa: E501


        :return: The cluster of this AlertRule.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this AlertRule.


        :param cluster: The cluster of this AlertRule.  # noqa: E501
        :type cluster: NestedCluster
        """
        if self.local_vars_configuration.client_side_validation and cluster is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster`, must not be `None`")  # noqa: E501

        self._cluster = cluster

    @property
    def customized(self):
        """Gets the customized of this AlertRule.  # noqa: E501


        :return: The customized of this AlertRule.  # noqa: E501
        :rtype: bool
        """
        return self._customized

    @customized.setter
    def customized(self, customized):
        """Sets the customized of this AlertRule.


        :param customized: The customized of this AlertRule.  # noqa: E501
        :type customized: bool
        """
        if self.local_vars_configuration.client_side_validation and customized is None:  # noqa: E501
            raise ValueError("Invalid value for `customized`, must not be `None`")  # noqa: E501

        self._customized = customized

    @property
    def disabled(self):
        """Gets the disabled of this AlertRule.  # noqa: E501


        :return: The disabled of this AlertRule.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this AlertRule.


        :param disabled: The disabled of this AlertRule.  # noqa: E501
        :type disabled: bool
        """
        if self.local_vars_configuration.client_side_validation and disabled is None:  # noqa: E501
            raise ValueError("Invalid value for `disabled`, must not be `None`")  # noqa: E501

        self._disabled = disabled

    @property
    def global_alert_rule(self):
        """Gets the global_alert_rule of this AlertRule.  # noqa: E501


        :return: The global_alert_rule of this AlertRule.  # noqa: E501
        :rtype: NestedGlobalAlertRule
        """
        return self._global_alert_rule

    @global_alert_rule.setter
    def global_alert_rule(self, global_alert_rule):
        """Sets the global_alert_rule of this AlertRule.


        :param global_alert_rule: The global_alert_rule of this AlertRule.  # noqa: E501
        :type global_alert_rule: NestedGlobalAlertRule
        """
        if self.local_vars_configuration.client_side_validation and global_alert_rule is None:  # noqa: E501
            raise ValueError("Invalid value for `global_alert_rule`, must not be `None`")  # noqa: E501

        self._global_alert_rule = global_alert_rule

    @property
    def id(self):
        """Gets the id of this AlertRule.  # noqa: E501


        :return: The id of this AlertRule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertRule.


        :param id: The id of this AlertRule.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def local_id(self):
        """Gets the local_id of this AlertRule.  # noqa: E501


        :return: The local_id of this AlertRule.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this AlertRule.


        :param local_id: The local_id of this AlertRule.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def thresholds(self):
        """Gets the thresholds of this AlertRule.  # noqa: E501


        :return: The thresholds of this AlertRule.  # noqa: E501
        :rtype: list[NestedThresholds]
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        """Sets the thresholds of this AlertRule.


        :param thresholds: The thresholds of this AlertRule.  # noqa: E501
        :type thresholds: list[NestedThresholds]
        """
        if self.local_vars_configuration.client_side_validation and thresholds is None:  # noqa: E501
            raise ValueError("Invalid value for `thresholds`, must not be `None`")  # noqa: E501

        self._thresholds = thresholds

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
        if not isinstance(other, AlertRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertRule):
            return True

        return self.to_dict() != other.to_dict()
