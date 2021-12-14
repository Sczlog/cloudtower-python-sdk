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


class DiskOrderByInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CREATEDAT_ASC = "createdAt_ASC"
    CREATEDAT_DESC = "createdAt_DESC"
    ENTITYASYNCSTATUS_ASC = "entityAsyncStatus_ASC"
    ENTITYASYNCSTATUS_DESC = "entityAsyncStatus_DESC"
    FAILURE_INFORMATION_ASC = "failure_information_ASC"
    FAILURE_INFORMATION_DESC = "failure_information_DESC"
    FIRMWARE_ASC = "firmware_ASC"
    FIRMWARE_DESC = "firmware_DESC"
    FUNCTION_ASC = "function_ASC"
    FUNCTION_DESC = "function_DESC"
    HEALTH_STATUS_ASC = "health_status_ASC"
    HEALTH_STATUS_DESC = "health_status_DESC"
    HEALTHY_ASC = "healthy_ASC"
    HEALTHY_DESC = "healthy_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    LOCAL_ID_ASC = "local_id_ASC"
    LOCAL_ID_DESC = "local_id_DESC"
    MODEL_ASC = "model_ASC"
    MODEL_DESC = "model_DESC"
    MOUNTED_ASC = "mounted_ASC"
    MOUNTED_DESC = "mounted_DESC"
    NAME_ASC = "name_ASC"
    NAME_DESC = "name_DESC"
    NUMA_NODE_ASC = "numa_node_ASC"
    NUMA_NODE_DESC = "numa_node_DESC"
    OFFLINE_ASC = "offline_ASC"
    OFFLINE_DESC = "offline_DESC"
    PARTITIONS_ASC = "partitions_ASC"
    PARTITIONS_DESC = "partitions_DESC"
    PATH_ASC = "path_ASC"
    PATH_DESC = "path_DESC"
    PERSISTENT_MEMORY_TYPE_ASC = "persistent_memory_type_ASC"
    PERSISTENT_MEMORY_TYPE_DESC = "persistent_memory_type_DESC"
    PHYSICAL_SLOT_ON_BRICK_ASC = "physical_slot_on_brick_ASC"
    PHYSICAL_SLOT_ON_BRICK_DESC = "physical_slot_on_brick_DESC"
    RECOMMENDED_USAGE_ASC = "recommended_usage_ASC"
    RECOMMENDED_USAGE_DESC = "recommended_usage_DESC"
    REMAINING_LIFE_PERCENT_ASC = "remaining_life_percent_ASC"
    REMAINING_LIFE_PERCENT_DESC = "remaining_life_percent_DESC"
    SERIAL_ASC = "serial_ASC"
    SERIAL_DESC = "serial_DESC"
    SIZE_ASC = "size_ASC"
    SIZE_DESC = "size_DESC"
    TYPE_ASC = "type_ASC"
    TYPE_DESC = "type_DESC"
    UPDATEDAT_ASC = "updatedAt_ASC"
    UPDATEDAT_DESC = "updatedAt_DESC"
    USAGE_ASC = "usage_ASC"
    USAGE_DESC = "usage_DESC"
    USAGE_STATUS_ASC = "usage_status_ASC"
    USAGE_STATUS_DESC = "usage_status_DESC"

    allowable_values = [CREATEDAT_ASC, CREATEDAT_DESC, ENTITYASYNCSTATUS_ASC, ENTITYASYNCSTATUS_DESC, FAILURE_INFORMATION_ASC, FAILURE_INFORMATION_DESC, FIRMWARE_ASC, FIRMWARE_DESC, FUNCTION_ASC, FUNCTION_DESC, HEALTH_STATUS_ASC, HEALTH_STATUS_DESC, HEALTHY_ASC, HEALTHY_DESC, ID_ASC, ID_DESC, LOCAL_ID_ASC, LOCAL_ID_DESC, MODEL_ASC, MODEL_DESC, MOUNTED_ASC, MOUNTED_DESC, NAME_ASC, NAME_DESC, NUMA_NODE_ASC, NUMA_NODE_DESC, OFFLINE_ASC, OFFLINE_DESC, PARTITIONS_ASC, PARTITIONS_DESC, PATH_ASC, PATH_DESC, PERSISTENT_MEMORY_TYPE_ASC, PERSISTENT_MEMORY_TYPE_DESC, PHYSICAL_SLOT_ON_BRICK_ASC, PHYSICAL_SLOT_ON_BRICK_DESC, RECOMMENDED_USAGE_ASC, RECOMMENDED_USAGE_DESC, REMAINING_LIFE_PERCENT_ASC, REMAINING_LIFE_PERCENT_DESC, SERIAL_ASC, SERIAL_DESC, SIZE_ASC, SIZE_DESC, TYPE_ASC, TYPE_DESC, UPDATEDAT_ASC, UPDATEDAT_DESC, USAGE_ASC, USAGE_DESC, USAGE_STATUS_ASC, USAGE_STATUS_DESC]  # noqa: E501

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
        """DiskOrderByInput - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, DiskOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DiskOrderByInput):
            return True

        return self.to_dict() != other.to_dict()
