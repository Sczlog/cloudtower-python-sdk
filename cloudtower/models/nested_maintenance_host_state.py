# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class NestedMaintenanceHostState(object):
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
        'enter_maintenance_time': 'str',
        'maintenance_job_id': 'str',
        'state': 'MaintenanceModeEnum'
    }

    attribute_map = {
        'enter_maintenance_time': 'enter_maintenance_time',
        'maintenance_job_id': 'maintenance_job_id',
        'state': 'state'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedMaintenanceHostState - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._enter_maintenance_time = None
        self._maintenance_job_id = None
        self._state = None
        self.discriminator = None

        if "enter_maintenance_time" in kwargs:
            self.enter_maintenance_time = kwargs["enter_maintenance_time"]
        if "maintenance_job_id" in kwargs:
            self.maintenance_job_id = kwargs["maintenance_job_id"]
        if "state" in kwargs:
            self.state = kwargs["state"]

    @property
    def enter_maintenance_time(self):
        """Gets the enter_maintenance_time of this NestedMaintenanceHostState.  # noqa: E501


        :return: The enter_maintenance_time of this NestedMaintenanceHostState.  # noqa: E501
        :rtype: str
        """
        return self._enter_maintenance_time

    @enter_maintenance_time.setter
    def enter_maintenance_time(self, enter_maintenance_time):
        """Sets the enter_maintenance_time of this NestedMaintenanceHostState.


        :param enter_maintenance_time: The enter_maintenance_time of this NestedMaintenanceHostState.  # noqa: E501
        :type enter_maintenance_time: str
        """
        if self.local_vars_configuration.client_side_validation and enter_maintenance_time is None:  # noqa: E501
            raise ValueError("Invalid value for `enter_maintenance_time`, must not be `None`")  # noqa: E501

        self._enter_maintenance_time = enter_maintenance_time

    @property
    def maintenance_job_id(self):
        """Gets the maintenance_job_id of this NestedMaintenanceHostState.  # noqa: E501


        :return: The maintenance_job_id of this NestedMaintenanceHostState.  # noqa: E501
        :rtype: str
        """
        return self._maintenance_job_id

    @maintenance_job_id.setter
    def maintenance_job_id(self, maintenance_job_id):
        """Sets the maintenance_job_id of this NestedMaintenanceHostState.


        :param maintenance_job_id: The maintenance_job_id of this NestedMaintenanceHostState.  # noqa: E501
        :type maintenance_job_id: str
        """
        if self.local_vars_configuration.client_side_validation and maintenance_job_id is None:  # noqa: E501
            raise ValueError("Invalid value for `maintenance_job_id`, must not be `None`")  # noqa: E501

        self._maintenance_job_id = maintenance_job_id

    @property
    def state(self):
        """Gets the state of this NestedMaintenanceHostState.  # noqa: E501


        :return: The state of this NestedMaintenanceHostState.  # noqa: E501
        :rtype: MaintenanceModeEnum
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this NestedMaintenanceHostState.


        :param state: The state of this NestedMaintenanceHostState.  # noqa: E501
        :type state: MaintenanceModeEnum
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

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
        if not isinstance(other, NestedMaintenanceHostState):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedMaintenanceHostState):
            return True

        return self.to_dict() != other.to_dict()
