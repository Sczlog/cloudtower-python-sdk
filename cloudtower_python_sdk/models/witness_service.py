# coding: utf-8

"""
    Tower SDK API

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 1.8.0
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


class WitnessService(object):
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
        'id': 'str',
        'name': 'str',
        'role': 'str',
        'state': 'str',
        'state_duration': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'role': 'role',
        'state': 'state',
        'state_duration': 'state_duration'
    }

    def __init__(self, id=None, name=None, role=None, state=None, state_duration=None, local_vars_configuration=None):  # noqa: E501
        """WitnessService - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._role = None
        self._state = None
        self._state_duration = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.role = role
        self.state = state
        self.state_duration = state_duration

    @property
    def id(self):
        """Gets the id of this WitnessService.  # noqa: E501


        :return: The id of this WitnessService.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WitnessService.


        :param id: The id of this WitnessService.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this WitnessService.  # noqa: E501


        :return: The name of this WitnessService.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WitnessService.


        :param name: The name of this WitnessService.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def role(self):
        """Gets the role of this WitnessService.  # noqa: E501


        :return: The role of this WitnessService.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this WitnessService.


        :param role: The role of this WitnessService.  # noqa: E501
        :type role: str
        """
        if self.local_vars_configuration.client_side_validation and role is None:  # noqa: E501
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def state(self):
        """Gets the state of this WitnessService.  # noqa: E501


        :return: The state of this WitnessService.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this WitnessService.


        :param state: The state of this WitnessService.  # noqa: E501
        :type state: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def state_duration(self):
        """Gets the state_duration of this WitnessService.  # noqa: E501


        :return: The state_duration of this WitnessService.  # noqa: E501
        :rtype: float
        """
        return self._state_duration

    @state_duration.setter
    def state_duration(self, state_duration):
        """Sets the state_duration of this WitnessService.


        :param state_duration: The state_duration of this WitnessService.  # noqa: E501
        :type state_duration: float
        """
        if self.local_vars_configuration.client_side_validation and state_duration is None:  # noqa: E501
            raise ValueError("Invalid value for `state_duration`, must not be `None`")  # noqa: E501

        self._state_duration = state_duration

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
        if not isinstance(other, WitnessService):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WitnessService):
            return True

        return self.to_dict() != other.to_dict()
