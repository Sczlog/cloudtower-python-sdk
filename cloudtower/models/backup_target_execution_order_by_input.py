# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class BackupTargetExecutionOrderByInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    BACKUP_GROUP_ASC = "backup_group_ASC"
    BACKUP_GROUP_DESC = "backup_group_DESC"
    CLUSTER_LOCAL_ID_ASC = "cluster_local_id_ASC"
    CLUSTER_LOCAL_ID_DESC = "cluster_local_id_DESC"
    DURATION_ASC = "duration_ASC"
    DURATION_DESC = "duration_DESC"
    ENTITYASYNCSTATUS_ASC = "entityAsyncStatus_ASC"
    ENTITYASYNCSTATUS_DESC = "entityAsyncStatus_DESC"
    EXECUTED_AT_ASC = "executed_at_ASC"
    EXECUTED_AT_DESC = "executed_at_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    LOCAL_ID_ASC = "local_id_ASC"
    LOCAL_ID_DESC = "local_id_DESC"
    PARENT_BACKUP_ASC = "parent_backup_ASC"
    PARENT_BACKUP_DESC = "parent_backup_DESC"
    READ_BYTES_ASC = "read_bytes_ASC"
    READ_BYTES_DESC = "read_bytes_DESC"
    RETRY_TIMES_ASC = "retry_times_ASC"
    RETRY_TIMES_DESC = "retry_times_DESC"
    STATUS_ASC = "status_ASC"
    STATUS_DESC = "status_DESC"
    TOTAL_BYTES_ASC = "total_bytes_ASC"
    TOTAL_BYTES_DESC = "total_bytes_DESC"
    TYPE_ASC = "type_ASC"
    TYPE_DESC = "type_DESC"
    VM_LOCAL_ID_ASC = "vm_local_id_ASC"
    VM_LOCAL_ID_DESC = "vm_local_id_DESC"
    VM_NAME_ASC = "vm_name_ASC"
    VM_NAME_DESC = "vm_name_DESC"

    allowable_values = [BACKUP_GROUP_ASC, BACKUP_GROUP_DESC, CLUSTER_LOCAL_ID_ASC, CLUSTER_LOCAL_ID_DESC, DURATION_ASC, DURATION_DESC, ENTITYASYNCSTATUS_ASC, ENTITYASYNCSTATUS_DESC, EXECUTED_AT_ASC, EXECUTED_AT_DESC, ID_ASC, ID_DESC, LOCAL_ID_ASC, LOCAL_ID_DESC, PARENT_BACKUP_ASC, PARENT_BACKUP_DESC, READ_BYTES_ASC, READ_BYTES_DESC, RETRY_TIMES_ASC, RETRY_TIMES_DESC, STATUS_ASC, STATUS_DESC, TOTAL_BYTES_ASC, TOTAL_BYTES_DESC, TYPE_ASC, TYPE_DESC, VM_LOCAL_ID_ASC, VM_LOCAL_ID_DESC, VM_NAME_ASC, VM_NAME_DESC]  # noqa: E501

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
        """BackupTargetExecutionOrderByInput - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, BackupTargetExecutionOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BackupTargetExecutionOrderByInput):
            return True

        return self.to_dict() != other.to_dict()
