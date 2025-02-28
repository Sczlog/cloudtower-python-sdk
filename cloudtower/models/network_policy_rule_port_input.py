# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class NetworkPolicyRulePortInput(object):
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
        'alg_protocol': 'NetworkPolicyRuleAlgProtocol',
        'protocol': 'NetworkPolicyRulePortProtocol',
        'port': 'str'
    }

    attribute_map = {
        'alg_protocol': 'alg_protocol',
        'protocol': 'protocol',
        'port': 'port'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NetworkPolicyRulePortInput - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._alg_protocol = None
        self._protocol = None
        self._port = None
        self.discriminator = None

        if "alg_protocol" in kwargs:
            self.alg_protocol = kwargs["alg_protocol"]
        if "protocol" in kwargs:
            self.protocol = kwargs["protocol"]
        if "port" in kwargs:
            self.port = kwargs["port"]

    @property
    def alg_protocol(self):
        """Gets the alg_protocol of this NetworkPolicyRulePortInput.  # noqa: E501


        :return: The alg_protocol of this NetworkPolicyRulePortInput.  # noqa: E501
        :rtype: NetworkPolicyRuleAlgProtocol
        """
        return self._alg_protocol

    @alg_protocol.setter
    def alg_protocol(self, alg_protocol):
        """Sets the alg_protocol of this NetworkPolicyRulePortInput.


        :param alg_protocol: The alg_protocol of this NetworkPolicyRulePortInput.  # noqa: E501
        :type alg_protocol: NetworkPolicyRuleAlgProtocol
        """

        self._alg_protocol = alg_protocol

    @property
    def protocol(self):
        """Gets the protocol of this NetworkPolicyRulePortInput.  # noqa: E501


        :return: The protocol of this NetworkPolicyRulePortInput.  # noqa: E501
        :rtype: NetworkPolicyRulePortProtocol
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this NetworkPolicyRulePortInput.


        :param protocol: The protocol of this NetworkPolicyRulePortInput.  # noqa: E501
        :type protocol: NetworkPolicyRulePortProtocol
        """
        if self.local_vars_configuration.client_side_validation and protocol is None:  # noqa: E501
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self._protocol = protocol

    @property
    def port(self):
        """Gets the port of this NetworkPolicyRulePortInput.  # noqa: E501


        :return: The port of this NetworkPolicyRulePortInput.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this NetworkPolicyRulePortInput.


        :param port: The port of this NetworkPolicyRulePortInput.  # noqa: E501
        :type port: str
        """

        self._port = port

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
        if not isinstance(other, NetworkPolicyRulePortInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkPolicyRulePortInput):
            return True

        return self.to_dict() != other.to_dict()
