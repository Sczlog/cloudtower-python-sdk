# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class SecurityPolicyIngressEgressInput(object):
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
        'type': 'SecurityPolicyFlowControlType',
        'ports': 'list[NetworkPolicyRulePortInput]',
        'target': 'SecurityPolicyIngressEgressInputTarget'
    }

    attribute_map = {
        'type': 'type',
        'ports': 'ports',
        'target': 'target'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """SecurityPolicyIngressEgressInput - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._type = None
        self._ports = None
        self._target = None
        self.discriminator = None

        if "type" in kwargs:
            self.type = kwargs["type"]
        if "ports" in kwargs:
            self.ports = kwargs["ports"]
        if "target" in kwargs:
            self.target = kwargs["target"]

    @property
    def type(self):
        """Gets the type of this SecurityPolicyIngressEgressInput.  # noqa: E501


        :return: The type of this SecurityPolicyIngressEgressInput.  # noqa: E501
        :rtype: SecurityPolicyFlowControlType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SecurityPolicyIngressEgressInput.


        :param type: The type of this SecurityPolicyIngressEgressInput.  # noqa: E501
        :type type: SecurityPolicyFlowControlType
        """

        self._type = type

    @property
    def ports(self):
        """Gets the ports of this SecurityPolicyIngressEgressInput.  # noqa: E501


        :return: The ports of this SecurityPolicyIngressEgressInput.  # noqa: E501
        :rtype: list[NetworkPolicyRulePortInput]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this SecurityPolicyIngressEgressInput.


        :param ports: The ports of this SecurityPolicyIngressEgressInput.  # noqa: E501
        :type ports: list[NetworkPolicyRulePortInput]
        """

        self._ports = ports

    @property
    def target(self):
        """Gets the target of this SecurityPolicyIngressEgressInput.  # noqa: E501


        :return: The target of this SecurityPolicyIngressEgressInput.  # noqa: E501
        :rtype: SecurityPolicyIngressEgressInputTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this SecurityPolicyIngressEgressInput.


        :param target: The target of this SecurityPolicyIngressEgressInput.  # noqa: E501
        :type target: SecurityPolicyIngressEgressInputTarget
        """

        self._target = target

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
        if not isinstance(other, SecurityPolicyIngressEgressInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SecurityPolicyIngressEgressInput):
            return True

        return self.to_dict() != other.to_dict()
