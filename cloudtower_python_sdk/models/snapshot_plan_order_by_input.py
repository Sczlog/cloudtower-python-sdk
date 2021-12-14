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


class SnapshotPlanOrderByInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    AUTO_DELETE_NUM_ASC = "auto_delete_num_ASC"
    AUTO_DELETE_NUM_DESC = "auto_delete_num_DESC"
    AUTO_EXECUTE_NUM_ASC = "auto_execute_num_ASC"
    AUTO_EXECUTE_NUM_DESC = "auto_execute_num_DESC"
    CREATEDAT_ASC = "createdAt_ASC"
    CREATEDAT_DESC = "createdAt_DESC"
    DESCRIPTION_ASC = "description_ASC"
    DESCRIPTION_DESC = "description_DESC"
    END_TIME_ASC = "end_time_ASC"
    END_TIME_DESC = "end_time_DESC"
    ENTITYASYNCSTATUS_ASC = "entityAsyncStatus_ASC"
    ENTITYASYNCSTATUS_DESC = "entityAsyncStatus_DESC"
    EXEC_H_M_ASC = "exec_h_m_ASC"
    EXEC_H_M_DESC = "exec_h_m_DESC"
    EXECUTE_PLAN_TYPE_ASC = "execute_plan_type_ASC"
    EXECUTE_PLAN_TYPE_DESC = "execute_plan_type_DESC"
    HEALTHY_ASC = "healthy_ASC"
    HEALTHY_DESC = "healthy_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    LAST_EXECUTE_END_TIME_ASC = "last_execute_end_time_ASC"
    LAST_EXECUTE_END_TIME_DESC = "last_execute_end_time_DESC"
    LAST_EXECUTE_STATUS_ASC = "last_execute_status_ASC"
    LAST_EXECUTE_STATUS_DESC = "last_execute_status_DESC"
    LAST_EXECUTE_TIME_ASC = "last_execute_time_ASC"
    LAST_EXECUTE_TIME_DESC = "last_execute_time_DESC"
    LOCAL_ID_ASC = "local_id_ASC"
    LOCAL_ID_DESC = "local_id_DESC"
    LOGICAL_SIZE_BYTES_ASC = "logical_size_bytes_ASC"
    LOGICAL_SIZE_BYTES_DESC = "logical_size_bytes_DESC"
    MANUAL_DELETE_NUM_ASC = "manual_delete_num_ASC"
    MANUAL_DELETE_NUM_DESC = "manual_delete_num_DESC"
    MANUAL_EXECUTE_NUM_ASC = "manual_execute_num_ASC"
    MANUAL_EXECUTE_NUM_DESC = "manual_execute_num_DESC"
    MIRROR_ASC = "mirror_ASC"
    MIRROR_DESC = "mirror_DESC"
    NAME_ASC = "name_ASC"
    NAME_DESC = "name_DESC"
    NEXT_EXECUTE_TIME_ASC = "next_execute_time_ASC"
    NEXT_EXECUTE_TIME_DESC = "next_execute_time_DESC"
    OBJECT_NUM_ASC = "object_num_ASC"
    OBJECT_NUM_DESC = "object_num_DESC"
    PHYSICAL_SIZE_BYTES_ASC = "physical_size_bytes_ASC"
    PHYSICAL_SIZE_BYTES_DESC = "physical_size_bytes_DESC"
    REMAIN_SNAPSHOT_NUM_ASC = "remain_snapshot_num_ASC"
    REMAIN_SNAPSHOT_NUM_DESC = "remain_snapshot_num_DESC"
    SNAPSHOT_GROUP_NUM_ASC = "snapshot_group_num_ASC"
    SNAPSHOT_GROUP_NUM_DESC = "snapshot_group_num_DESC"
    START_TIME_ASC = "start_time_ASC"
    START_TIME_DESC = "start_time_DESC"
    STATUS_ASC = "status_ASC"
    STATUS_DESC = "status_DESC"
    UPDATEDAT_ASC = "updatedAt_ASC"
    UPDATEDAT_DESC = "updatedAt_DESC"

    allowable_values = [AUTO_DELETE_NUM_ASC, AUTO_DELETE_NUM_DESC, AUTO_EXECUTE_NUM_ASC, AUTO_EXECUTE_NUM_DESC, CREATEDAT_ASC, CREATEDAT_DESC, DESCRIPTION_ASC, DESCRIPTION_DESC, END_TIME_ASC, END_TIME_DESC, ENTITYASYNCSTATUS_ASC, ENTITYASYNCSTATUS_DESC, EXEC_H_M_ASC, EXEC_H_M_DESC, EXECUTE_PLAN_TYPE_ASC, EXECUTE_PLAN_TYPE_DESC, HEALTHY_ASC, HEALTHY_DESC, ID_ASC, ID_DESC, LAST_EXECUTE_END_TIME_ASC, LAST_EXECUTE_END_TIME_DESC, LAST_EXECUTE_STATUS_ASC, LAST_EXECUTE_STATUS_DESC, LAST_EXECUTE_TIME_ASC, LAST_EXECUTE_TIME_DESC, LOCAL_ID_ASC, LOCAL_ID_DESC, LOGICAL_SIZE_BYTES_ASC, LOGICAL_SIZE_BYTES_DESC, MANUAL_DELETE_NUM_ASC, MANUAL_DELETE_NUM_DESC, MANUAL_EXECUTE_NUM_ASC, MANUAL_EXECUTE_NUM_DESC, MIRROR_ASC, MIRROR_DESC, NAME_ASC, NAME_DESC, NEXT_EXECUTE_TIME_ASC, NEXT_EXECUTE_TIME_DESC, OBJECT_NUM_ASC, OBJECT_NUM_DESC, PHYSICAL_SIZE_BYTES_ASC, PHYSICAL_SIZE_BYTES_DESC, REMAIN_SNAPSHOT_NUM_ASC, REMAIN_SNAPSHOT_NUM_DESC, SNAPSHOT_GROUP_NUM_ASC, SNAPSHOT_GROUP_NUM_DESC, START_TIME_ASC, START_TIME_DESC, STATUS_ASC, STATUS_DESC, UPDATEDAT_ASC, UPDATEDAT_DESC]  # noqa: E501

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
        """SnapshotPlanOrderByInput - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, SnapshotPlanOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnapshotPlanOrderByInput):
            return True

        return self.to_dict() != other.to_dict()
