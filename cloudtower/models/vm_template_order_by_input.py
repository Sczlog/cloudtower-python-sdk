# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 1.10.0
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


class VmTemplateOrderByInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CLOCK_OFFSET_ASC = "clock_offset_ASC"
    CLOCK_OFFSET_DESC = "clock_offset_DESC"
    CLOUD_INIT_SUPPORTED_ASC = "cloud_init_supported_ASC"
    CLOUD_INIT_SUPPORTED_DESC = "cloud_init_supported_DESC"
    CPU_ASC = "cpu_ASC"
    CPU_DESC = "cpu_DESC"
    CPU_MODEL_ASC = "cpu_model_ASC"
    CPU_MODEL_DESC = "cpu_model_DESC"
    CREATEDAT_ASC = "createdAt_ASC"
    CREATEDAT_DESC = "createdAt_DESC"
    DESCRIPTION_ASC = "description_ASC"
    DESCRIPTION_DESC = "description_DESC"
    ENTITYASYNCSTATUS_ASC = "entityAsyncStatus_ASC"
    ENTITYASYNCSTATUS_DESC = "entityAsyncStatus_DESC"
    FIRMWARE_ASC = "firmware_ASC"
    FIRMWARE_DESC = "firmware_DESC"
    HA_ASC = "ha_ASC"
    HA_DESC = "ha_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    IO_POLICY_ASC = "io_policy_ASC"
    IO_POLICY_DESC = "io_policy_DESC"
    LOCAL_CREATED_AT_ASC = "local_created_at_ASC"
    LOCAL_CREATED_AT_DESC = "local_created_at_DESC"
    LOCAL_ID_ASC = "local_id_ASC"
    LOCAL_ID_DESC = "local_id_DESC"
    MAX_BANDWIDTH_ASC = "max_bandwidth_ASC"
    MAX_BANDWIDTH_DESC = "max_bandwidth_DESC"
    MAX_BANDWIDTH_POLICY_ASC = "max_bandwidth_policy_ASC"
    MAX_BANDWIDTH_POLICY_DESC = "max_bandwidth_policy_DESC"
    MAX_IOPS_ASC = "max_iops_ASC"
    MAX_IOPS_DESC = "max_iops_DESC"
    MAX_IOPS_POLICY_ASC = "max_iops_policy_ASC"
    MAX_IOPS_POLICY_DESC = "max_iops_policy_DESC"
    MEMORY_ASC = "memory_ASC"
    MEMORY_DESC = "memory_DESC"
    NAME_ASC = "name_ASC"
    NAME_DESC = "name_DESC"
    SIZE_ASC = "size_ASC"
    SIZE_DESC = "size_DESC"
    UPDATEDAT_ASC = "updatedAt_ASC"
    UPDATEDAT_DESC = "updatedAt_DESC"
    VCPU_ASC = "vcpu_ASC"
    VCPU_DESC = "vcpu_DESC"
    VIDEO_TYPE_ASC = "video_type_ASC"
    VIDEO_TYPE_DESC = "video_type_DESC"
    VM_DISKS_ASC = "vm_disks_ASC"
    VM_DISKS_DESC = "vm_disks_DESC"
    VM_NICS_ASC = "vm_nics_ASC"
    VM_NICS_DESC = "vm_nics_DESC"
    WIN_OPT_ASC = "win_opt_ASC"
    WIN_OPT_DESC = "win_opt_DESC"

    allowable_values = [CLOCK_OFFSET_ASC, CLOCK_OFFSET_DESC, CLOUD_INIT_SUPPORTED_ASC, CLOUD_INIT_SUPPORTED_DESC, CPU_ASC, CPU_DESC, CPU_MODEL_ASC, CPU_MODEL_DESC, CREATEDAT_ASC, CREATEDAT_DESC, DESCRIPTION_ASC, DESCRIPTION_DESC, ENTITYASYNCSTATUS_ASC, ENTITYASYNCSTATUS_DESC, FIRMWARE_ASC, FIRMWARE_DESC, HA_ASC, HA_DESC, ID_ASC, ID_DESC, IO_POLICY_ASC, IO_POLICY_DESC, LOCAL_CREATED_AT_ASC, LOCAL_CREATED_AT_DESC, LOCAL_ID_ASC, LOCAL_ID_DESC, MAX_BANDWIDTH_ASC, MAX_BANDWIDTH_DESC, MAX_BANDWIDTH_POLICY_ASC, MAX_BANDWIDTH_POLICY_DESC, MAX_IOPS_ASC, MAX_IOPS_DESC, MAX_IOPS_POLICY_ASC, MAX_IOPS_POLICY_DESC, MEMORY_ASC, MEMORY_DESC, NAME_ASC, NAME_DESC, SIZE_ASC, SIZE_DESC, UPDATEDAT_ASC, UPDATEDAT_DESC, VCPU_ASC, VCPU_DESC, VIDEO_TYPE_ASC, VIDEO_TYPE_DESC, VM_DISKS_ASC, VM_DISKS_DESC, VM_NICS_ASC, VM_NICS_DESC, WIN_OPT_ASC, WIN_OPT_DESC]  # noqa: E501

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
        """VmTemplateOrderByInput - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, VmTemplateOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmTemplateOrderByInput):
            return True

        return self.to_dict() != other.to_dict()
