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


class ExecutePlan(object):
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
        'start_at': 'str',
        'retain': 'int',
        'period': 'str',
        'id': 'str',
        'enabled': 'bool',
        'typename': 'str'
    }

    attribute_map = {
        'start_at': 'start_at',
        'retain': 'retain',
        'period': 'period',
        'id': 'id',
        'enabled': 'enabled',
        'typename': '__typename'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ExecutePlan - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._start_at = None
        self._retain = None
        self._period = None
        self._id = None
        self._enabled = None
        self._typename = None
        self.discriminator = None

        if "start_at" in kwargs:
            self.start_at = kwargs["start_at"]
        if "retain" in kwargs:
            self.retain = kwargs["retain"]
        if "period" in kwargs:
            self.period = kwargs["period"]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "enabled" in kwargs:
            self.enabled = kwargs["enabled"]
        if "typename" in kwargs:
            self.typename = kwargs["typename"]

    @property
    def start_at(self):
        """Gets the start_at of this ExecutePlan.  # noqa: E501


        :return: The start_at of this ExecutePlan.  # noqa: E501
        :rtype: str
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        """Sets the start_at of this ExecutePlan.


        :param start_at: The start_at of this ExecutePlan.  # noqa: E501
        :type start_at: str
        """
        if self.local_vars_configuration.client_side_validation and start_at is None:  # noqa: E501
            raise ValueError("Invalid value for `start_at`, must not be `None`")  # noqa: E501

        self._start_at = start_at

    @property
    def retain(self):
        """Gets the retain of this ExecutePlan.  # noqa: E501


        :return: The retain of this ExecutePlan.  # noqa: E501
        :rtype: int
        """
        return self._retain

    @retain.setter
    def retain(self, retain):
        """Sets the retain of this ExecutePlan.


        :param retain: The retain of this ExecutePlan.  # noqa: E501
        :type retain: int
        """
        if self.local_vars_configuration.client_side_validation and retain is None:  # noqa: E501
            raise ValueError("Invalid value for `retain`, must not be `None`")  # noqa: E501

        self._retain = retain

    @property
    def period(self):
        """Gets the period of this ExecutePlan.  # noqa: E501


        :return: The period of this ExecutePlan.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ExecutePlan.


        :param period: The period of this ExecutePlan.  # noqa: E501
        :type period: str
        """
        if self.local_vars_configuration.client_side_validation and period is None:  # noqa: E501
            raise ValueError("Invalid value for `period`, must not be `None`")  # noqa: E501

        self._period = period

    @property
    def id(self):
        """Gets the id of this ExecutePlan.  # noqa: E501


        :return: The id of this ExecutePlan.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExecutePlan.


        :param id: The id of this ExecutePlan.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def enabled(self):
        """Gets the enabled of this ExecutePlan.  # noqa: E501


        :return: The enabled of this ExecutePlan.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ExecutePlan.


        :param enabled: The enabled of this ExecutePlan.  # noqa: E501
        :type enabled: bool
        """
        if self.local_vars_configuration.client_side_validation and enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def typename(self):
        """Gets the typename of this ExecutePlan.  # noqa: E501


        :return: The typename of this ExecutePlan.  # noqa: E501
        :rtype: str
        """
        return self._typename

    @typename.setter
    def typename(self, typename):
        """Sets the typename of this ExecutePlan.


        :param typename: The typename of this ExecutePlan.  # noqa: E501
        :type typename: str
        """
        allowed_values = ["ExecutePlan"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and typename not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `typename` ({0}), must be one of {1}"  # noqa: E501
                .format(typename, allowed_values)
            )

        self._typename = typename

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
        if not isinstance(other, ExecutePlan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExecutePlan):
            return True

        return self.to_dict() != other.to_dict()
