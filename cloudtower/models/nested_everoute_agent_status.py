# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class NestedEverouteAgentStatus(object):
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
        'host': 'NestedHost',
        'host_id': 'str',
        'ip_addr': 'str',
        'is_health': 'bool',
        'message': 'str',
        'phase': 'EverouteClusterPhase',
        'reason': 'str'
    }

    attribute_map = {
        'host': 'host',
        'host_id': 'hostID',
        'ip_addr': 'ipAddr',
        'is_health': 'isHealth',
        'message': 'message',
        'phase': 'phase',
        'reason': 'reason'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedEverouteAgentStatus - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._host = None
        self._host_id = None
        self._ip_addr = None
        self._is_health = None
        self._message = None
        self._phase = None
        self._reason = None
        self.discriminator = None

        self.host = kwargs.get("host", None)
        if "host_id" in kwargs:
            self.host_id = kwargs["host_id"]
        if "ip_addr" in kwargs:
            self.ip_addr = kwargs["ip_addr"]
        if "is_health" in kwargs:
            self.is_health = kwargs["is_health"]
        if "message" in kwargs:
            self.message = kwargs["message"]
        self.phase = kwargs.get("phase", None)
        if "reason" in kwargs:
            self.reason = kwargs["reason"]

    @property
    def host(self):
        """Gets the host of this NestedEverouteAgentStatus.  # noqa: E501


        :return: The host of this NestedEverouteAgentStatus.  # noqa: E501
        :rtype: NestedHost
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this NestedEverouteAgentStatus.


        :param host: The host of this NestedEverouteAgentStatus.  # noqa: E501
        :type host: NestedHost
        """

        self._host = host

    @property
    def host_id(self):
        """Gets the host_id of this NestedEverouteAgentStatus.  # noqa: E501


        :return: The host_id of this NestedEverouteAgentStatus.  # noqa: E501
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this NestedEverouteAgentStatus.


        :param host_id: The host_id of this NestedEverouteAgentStatus.  # noqa: E501
        :type host_id: str
        """
        if self.local_vars_configuration.client_side_validation and host_id is None:  # noqa: E501
            raise ValueError("Invalid value for `host_id`, must not be `None`")  # noqa: E501

        self._host_id = host_id

    @property
    def ip_addr(self):
        """Gets the ip_addr of this NestedEverouteAgentStatus.  # noqa: E501


        :return: The ip_addr of this NestedEverouteAgentStatus.  # noqa: E501
        :rtype: str
        """
        return self._ip_addr

    @ip_addr.setter
    def ip_addr(self, ip_addr):
        """Sets the ip_addr of this NestedEverouteAgentStatus.


        :param ip_addr: The ip_addr of this NestedEverouteAgentStatus.  # noqa: E501
        :type ip_addr: str
        """
        if self.local_vars_configuration.client_side_validation and ip_addr is None:  # noqa: E501
            raise ValueError("Invalid value for `ip_addr`, must not be `None`")  # noqa: E501

        self._ip_addr = ip_addr

    @property
    def is_health(self):
        """Gets the is_health of this NestedEverouteAgentStatus.  # noqa: E501


        :return: The is_health of this NestedEverouteAgentStatus.  # noqa: E501
        :rtype: bool
        """
        return self._is_health

    @is_health.setter
    def is_health(self, is_health):
        """Sets the is_health of this NestedEverouteAgentStatus.


        :param is_health: The is_health of this NestedEverouteAgentStatus.  # noqa: E501
        :type is_health: bool
        """
        if self.local_vars_configuration.client_side_validation and is_health is None:  # noqa: E501
            raise ValueError("Invalid value for `is_health`, must not be `None`")  # noqa: E501

        self._is_health = is_health

    @property
    def message(self):
        """Gets the message of this NestedEverouteAgentStatus.  # noqa: E501


        :return: The message of this NestedEverouteAgentStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this NestedEverouteAgentStatus.


        :param message: The message of this NestedEverouteAgentStatus.  # noqa: E501
        :type message: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def phase(self):
        """Gets the phase of this NestedEverouteAgentStatus.  # noqa: E501


        :return: The phase of this NestedEverouteAgentStatus.  # noqa: E501
        :rtype: EverouteClusterPhase
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this NestedEverouteAgentStatus.


        :param phase: The phase of this NestedEverouteAgentStatus.  # noqa: E501
        :type phase: EverouteClusterPhase
        """

        self._phase = phase

    @property
    def reason(self):
        """Gets the reason of this NestedEverouteAgentStatus.  # noqa: E501


        :return: The reason of this NestedEverouteAgentStatus.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this NestedEverouteAgentStatus.


        :param reason: The reason of this NestedEverouteAgentStatus.  # noqa: E501
        :type reason: str
        """
        if self.local_vars_configuration.client_side_validation and reason is None:  # noqa: E501
            raise ValueError("Invalid value for `reason`, must not be `None`")  # noqa: E501

        self._reason = reason

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
        if not isinstance(other, NestedEverouteAgentStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedEverouteAgentStatus):
            return True

        return self.to_dict() != other.to_dict()
