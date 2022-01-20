# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 1.9.0
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


class UserAuditLogOrderByInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    ACTION_ASC = "action_ASC"
    ACTION_DESC = "action_DESC"
    CREATEDAT_ASC = "createdAt_ASC"
    CREATEDAT_DESC = "createdAt_DESC"
    FINISHED_AT_ASC = "finished_at_ASC"
    FINISHED_AT_DESC = "finished_at_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    IP_ADDRESS_ASC = "ip_address_ASC"
    IP_ADDRESS_DESC = "ip_address_DESC"
    MESSAGE_ASC = "message_ASC"
    MESSAGE_DESC = "message_DESC"
    RESOURCE_ID_ASC = "resource_id_ASC"
    RESOURCE_ID_DESC = "resource_id_DESC"
    RESOURCE_TYPE_ASC = "resource_type_ASC"
    RESOURCE_TYPE_DESC = "resource_type_DESC"
    STATUS_ASC = "status_ASC"
    STATUS_DESC = "status_DESC"
    UPDATEDAT_ASC = "updatedAt_ASC"
    UPDATEDAT_DESC = "updatedAt_DESC"

    allowable_values = [ACTION_ASC, ACTION_DESC, CREATEDAT_ASC, CREATEDAT_DESC, FINISHED_AT_ASC, FINISHED_AT_DESC, ID_ASC, ID_DESC, IP_ADDRESS_ASC, IP_ADDRESS_DESC, MESSAGE_ASC, MESSAGE_DESC, RESOURCE_ID_ASC, RESOURCE_ID_DESC, RESOURCE_TYPE_ASC, RESOURCE_TYPE_DESC, STATUS_ASC, STATUS_DESC, UPDATEDAT_ASC, UPDATEDAT_DESC]  # noqa: E501

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

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """UserAuditLogOrderByInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration
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
        if not isinstance(other, UserAuditLogOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserAuditLogOrderByInput):
            return True

        return self.to_dict() != other.to_dict()
