# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class GlobalAlertRuleOrderByInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    BOOLEAN_ASC = "boolean_ASC"
    BOOLEAN_DESC = "boolean_DESC"
    CAUSE_ASC = "cause_ASC"
    CAUSE_DESC = "cause_DESC"
    DEFAULT_THRESHOLDS_ASC = "default_thresholds_ASC"
    DEFAULT_THRESHOLDS_DESC = "default_thresholds_DESC"
    DISABLED_ASC = "disabled_ASC"
    DISABLED_DESC = "disabled_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    IMPACT_ASC = "impact_ASC"
    IMPACT_DESC = "impact_DESC"
    MESSAGE_ASC = "message_ASC"
    MESSAGE_DESC = "message_DESC"
    NAME_ASC = "name_ASC"
    NAME_DESC = "name_DESC"
    OBJECT_ASC = "object_ASC"
    OBJECT_DESC = "object_DESC"
    OPERATOR_ASC = "operator_ASC"
    OPERATOR_DESC = "operator_DESC"
    SOLUTION_ASC = "solution_ASC"
    SOLUTION_DESC = "solution_DESC"
    THRESHOLDS_ASC = "thresholds_ASC"
    THRESHOLDS_DESC = "thresholds_DESC"
    UNIT_ASC = "unit_ASC"
    UNIT_DESC = "unit_DESC"

    allowable_values = [BOOLEAN_ASC, BOOLEAN_DESC, CAUSE_ASC, CAUSE_DESC, DEFAULT_THRESHOLDS_ASC, DEFAULT_THRESHOLDS_DESC, DISABLED_ASC, DISABLED_DESC, ID_ASC, ID_DESC, IMPACT_ASC, IMPACT_DESC, MESSAGE_ASC, MESSAGE_DESC, NAME_ASC, NAME_DESC, OBJECT_ASC, OBJECT_DESC, OPERATOR_ASC, OPERATOR_DESC, SOLUTION_ASC, SOLUTION_DESC, THRESHOLDS_ASC, THRESHOLDS_DESC, UNIT_ASC, UNIT_DESC]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, **kwargs):  # noqa: E501
        """GlobalAlertRuleOrderByInput - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())
        self.discriminator = None

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
        if not isinstance(other, GlobalAlertRuleOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GlobalAlertRuleOrderByInput):
            return True

        return self.to_dict() != other.to_dict()
