# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.0.0
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


class NestedMetroAvailabilityChecklist(object):
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
        'primary_zone': 'NestedMetroCheckResult',
        'primary_zone_and_witness': 'NestedMetroCheckResult',
        'secondary_zone': 'NestedMetroCheckResult',
        'secondary_zone_and_witness': 'NestedMetroCheckResult',
        'witness': 'NestedMetroCheckResult',
        'zone_and_zone': 'NestedMetroCheckResult'
    }

    attribute_map = {
        'primary_zone': 'primaryZone',
        'primary_zone_and_witness': 'primaryZoneAndWitness',
        'secondary_zone': 'secondaryZone',
        'secondary_zone_and_witness': 'secondaryZoneAndWitness',
        'witness': 'witness',
        'zone_and_zone': 'zoneAndZone'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedMetroAvailabilityChecklist - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._primary_zone = None
        self._primary_zone_and_witness = None
        self._secondary_zone = None
        self._secondary_zone_and_witness = None
        self._witness = None
        self._zone_and_zone = None
        self.discriminator = None

        if "primary_zone" in kwargs:
            self.primary_zone = kwargs["primary_zone"]
        if "primary_zone_and_witness" in kwargs:
            self.primary_zone_and_witness = kwargs["primary_zone_and_witness"]
        if "secondary_zone" in kwargs:
            self.secondary_zone = kwargs["secondary_zone"]
        if "secondary_zone_and_witness" in kwargs:
            self.secondary_zone_and_witness = kwargs["secondary_zone_and_witness"]
        if "witness" in kwargs:
            self.witness = kwargs["witness"]
        if "zone_and_zone" in kwargs:
            self.zone_and_zone = kwargs["zone_and_zone"]

    @property
    def primary_zone(self):
        """Gets the primary_zone of this NestedMetroAvailabilityChecklist.  # noqa: E501


        :return: The primary_zone of this NestedMetroAvailabilityChecklist.  # noqa: E501
        :rtype: NestedMetroCheckResult
        """
        return self._primary_zone

    @primary_zone.setter
    def primary_zone(self, primary_zone):
        """Sets the primary_zone of this NestedMetroAvailabilityChecklist.


        :param primary_zone: The primary_zone of this NestedMetroAvailabilityChecklist.  # noqa: E501
        :type primary_zone: NestedMetroCheckResult
        """
        if self.local_vars_configuration.client_side_validation and primary_zone is None:  # noqa: E501
            raise ValueError("Invalid value for `primary_zone`, must not be `None`")  # noqa: E501

        self._primary_zone = primary_zone

    @property
    def primary_zone_and_witness(self):
        """Gets the primary_zone_and_witness of this NestedMetroAvailabilityChecklist.  # noqa: E501


        :return: The primary_zone_and_witness of this NestedMetroAvailabilityChecklist.  # noqa: E501
        :rtype: NestedMetroCheckResult
        """
        return self._primary_zone_and_witness

    @primary_zone_and_witness.setter
    def primary_zone_and_witness(self, primary_zone_and_witness):
        """Sets the primary_zone_and_witness of this NestedMetroAvailabilityChecklist.


        :param primary_zone_and_witness: The primary_zone_and_witness of this NestedMetroAvailabilityChecklist.  # noqa: E501
        :type primary_zone_and_witness: NestedMetroCheckResult
        """
        if self.local_vars_configuration.client_side_validation and primary_zone_and_witness is None:  # noqa: E501
            raise ValueError("Invalid value for `primary_zone_and_witness`, must not be `None`")  # noqa: E501

        self._primary_zone_and_witness = primary_zone_and_witness

    @property
    def secondary_zone(self):
        """Gets the secondary_zone of this NestedMetroAvailabilityChecklist.  # noqa: E501


        :return: The secondary_zone of this NestedMetroAvailabilityChecklist.  # noqa: E501
        :rtype: NestedMetroCheckResult
        """
        return self._secondary_zone

    @secondary_zone.setter
    def secondary_zone(self, secondary_zone):
        """Sets the secondary_zone of this NestedMetroAvailabilityChecklist.


        :param secondary_zone: The secondary_zone of this NestedMetroAvailabilityChecklist.  # noqa: E501
        :type secondary_zone: NestedMetroCheckResult
        """
        if self.local_vars_configuration.client_side_validation and secondary_zone is None:  # noqa: E501
            raise ValueError("Invalid value for `secondary_zone`, must not be `None`")  # noqa: E501

        self._secondary_zone = secondary_zone

    @property
    def secondary_zone_and_witness(self):
        """Gets the secondary_zone_and_witness of this NestedMetroAvailabilityChecklist.  # noqa: E501


        :return: The secondary_zone_and_witness of this NestedMetroAvailabilityChecklist.  # noqa: E501
        :rtype: NestedMetroCheckResult
        """
        return self._secondary_zone_and_witness

    @secondary_zone_and_witness.setter
    def secondary_zone_and_witness(self, secondary_zone_and_witness):
        """Sets the secondary_zone_and_witness of this NestedMetroAvailabilityChecklist.


        :param secondary_zone_and_witness: The secondary_zone_and_witness of this NestedMetroAvailabilityChecklist.  # noqa: E501
        :type secondary_zone_and_witness: NestedMetroCheckResult
        """
        if self.local_vars_configuration.client_side_validation and secondary_zone_and_witness is None:  # noqa: E501
            raise ValueError("Invalid value for `secondary_zone_and_witness`, must not be `None`")  # noqa: E501

        self._secondary_zone_and_witness = secondary_zone_and_witness

    @property
    def witness(self):
        """Gets the witness of this NestedMetroAvailabilityChecklist.  # noqa: E501


        :return: The witness of this NestedMetroAvailabilityChecklist.  # noqa: E501
        :rtype: NestedMetroCheckResult
        """
        return self._witness

    @witness.setter
    def witness(self, witness):
        """Sets the witness of this NestedMetroAvailabilityChecklist.


        :param witness: The witness of this NestedMetroAvailabilityChecklist.  # noqa: E501
        :type witness: NestedMetroCheckResult
        """
        if self.local_vars_configuration.client_side_validation and witness is None:  # noqa: E501
            raise ValueError("Invalid value for `witness`, must not be `None`")  # noqa: E501

        self._witness = witness

    @property
    def zone_and_zone(self):
        """Gets the zone_and_zone of this NestedMetroAvailabilityChecklist.  # noqa: E501


        :return: The zone_and_zone of this NestedMetroAvailabilityChecklist.  # noqa: E501
        :rtype: NestedMetroCheckResult
        """
        return self._zone_and_zone

    @zone_and_zone.setter
    def zone_and_zone(self, zone_and_zone):
        """Sets the zone_and_zone of this NestedMetroAvailabilityChecklist.


        :param zone_and_zone: The zone_and_zone of this NestedMetroAvailabilityChecklist.  # noqa: E501
        :type zone_and_zone: NestedMetroCheckResult
        """
        if self.local_vars_configuration.client_side_validation and zone_and_zone is None:  # noqa: E501
            raise ValueError("Invalid value for `zone_and_zone`, must not be `None`")  # noqa: E501

        self._zone_and_zone = zone_and_zone

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
        if not isinstance(other, NestedMetroAvailabilityChecklist):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedMetroAvailabilityChecklist):
            return True

        return self.to_dict() != other.to_dict()
