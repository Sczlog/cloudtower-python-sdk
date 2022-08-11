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


class VmOrderByInput(object):
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
    CPU_USAGE_ASC = "cpu_usage_ASC"
    CPU_USAGE_DESC = "cpu_usage_DESC"
    DELETED_AT_ASC = "deleted_at_ASC"
    DELETED_AT_DESC = "deleted_at_DESC"
    DESCRIPTION_ASC = "description_ASC"
    DESCRIPTION_DESC = "description_DESC"
    DNS_SERVERS_ASC = "dns_servers_ASC"
    DNS_SERVERS_DESC = "dns_servers_DESC"
    ENTITYASYNCSTATUS_ASC = "entityAsyncStatus_ASC"
    ENTITYASYNCSTATUS_DESC = "entityAsyncStatus_DESC"
    FIRMWARE_ASC = "firmware_ASC"
    FIRMWARE_DESC = "firmware_DESC"
    GUEST_CPU_MODEL_ASC = "guest_cpu_model_ASC"
    GUEST_CPU_MODEL_DESC = "guest_cpu_model_DESC"
    GUEST_OS_TYPE_ASC = "guest_os_type_ASC"
    GUEST_OS_TYPE_DESC = "guest_os_type_DESC"
    GUEST_SIZE_USAGE_ASC = "guest_size_usage_ASC"
    GUEST_SIZE_USAGE_DESC = "guest_size_usage_DESC"
    GUEST_USED_SIZE_ASC = "guest_used_size_ASC"
    GUEST_USED_SIZE_DESC = "guest_used_size_DESC"
    HA_ASC = "ha_ASC"
    HA_DESC = "ha_DESC"
    HOSTNAME_ASC = "hostname_ASC"
    HOSTNAME_DESC = "hostname_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    IN_RECYCLE_BIN_ASC = "in_recycle_bin_ASC"
    IN_RECYCLE_BIN_DESC = "in_recycle_bin_DESC"
    INTERNAL_ASC = "internal_ASC"
    INTERNAL_DESC = "internal_DESC"
    IO_POLICY_ASC = "io_policy_ASC"
    IO_POLICY_DESC = "io_policy_DESC"
    IPS_ASC = "ips_ASC"
    IPS_DESC = "ips_DESC"
    KERNEL_INFO_ASC = "kernel_info_ASC"
    KERNEL_INFO_DESC = "kernel_info_DESC"
    LAST_SHUTDOWN_TIME_ASC = "last_shutdown_time_ASC"
    LAST_SHUTDOWN_TIME_DESC = "last_shutdown_time_DESC"
    LOCAL_CREATED_AT_ASC = "local_created_at_ASC"
    LOCAL_CREATED_AT_DESC = "local_created_at_DESC"
    LOCAL_ID_ASC = "local_id_ASC"
    LOCAL_ID_DESC = "local_id_DESC"
    LOGICAL_SIZE_BYTES_ASC = "logical_size_bytes_ASC"
    LOGICAL_SIZE_BYTES_DESC = "logical_size_bytes_DESC"
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
    MEMORY_USAGE_ASC = "memory_usage_ASC"
    MEMORY_USAGE_DESC = "memory_usage_DESC"
    NAME_ASC = "name_ASC"
    NAME_DESC = "name_DESC"
    NESTED_VIRTUALIZATION_ASC = "nested_virtualization_ASC"
    NESTED_VIRTUALIZATION_DESC = "nested_virtualization_DESC"
    NODE_IP_ASC = "node_ip_ASC"
    NODE_IP_DESC = "node_ip_DESC"
    ORIGINAL_NAME_ASC = "original_name_ASC"
    ORIGINAL_NAME_DESC = "original_name_DESC"
    OS_ASC = "os_ASC"
    OS_DESC = "os_DESC"
    PROTECTED_ASC = "protected_ASC"
    PROTECTED_DESC = "protected_DESC"
    PROVISIONED_SIZE_ASC = "provisioned_size_ASC"
    PROVISIONED_SIZE_DESC = "provisioned_size_DESC"
    SIZE_ASC = "size_ASC"
    SIZE_DESC = "size_DESC"
    STATUS_ASC = "status_ASC"
    STATUS_DESC = "status_DESC"
    UNIQUE_SIZE_ASC = "unique_size_ASC"
    UNIQUE_SIZE_DESC = "unique_size_DESC"
    VCPU_ASC = "vcpu_ASC"
    VCPU_DESC = "vcpu_DESC"
    VIDEO_TYPE_ASC = "video_type_ASC"
    VIDEO_TYPE_DESC = "video_type_DESC"
    VM_TOOLS_STATUS_ASC = "vm_tools_status_ASC"
    VM_TOOLS_STATUS_DESC = "vm_tools_status_DESC"
    VM_TOOLS_VERSION_ASC = "vm_tools_version_ASC"
    VM_TOOLS_VERSION_DESC = "vm_tools_version_DESC"
    VM_USAGE_ASC = "vm_usage_ASC"
    VM_USAGE_DESC = "vm_usage_DESC"
    WIN_OPT_ASC = "win_opt_ASC"
    WIN_OPT_DESC = "win_opt_DESC"

    allowable_values = [CLOCK_OFFSET_ASC, CLOCK_OFFSET_DESC, CLOUD_INIT_SUPPORTED_ASC, CLOUD_INIT_SUPPORTED_DESC, CPU_ASC, CPU_DESC, CPU_MODEL_ASC, CPU_MODEL_DESC, CPU_USAGE_ASC, CPU_USAGE_DESC, DELETED_AT_ASC, DELETED_AT_DESC, DESCRIPTION_ASC, DESCRIPTION_DESC, DNS_SERVERS_ASC, DNS_SERVERS_DESC, ENTITYASYNCSTATUS_ASC, ENTITYASYNCSTATUS_DESC, FIRMWARE_ASC, FIRMWARE_DESC, GUEST_CPU_MODEL_ASC, GUEST_CPU_MODEL_DESC, GUEST_OS_TYPE_ASC, GUEST_OS_TYPE_DESC, GUEST_SIZE_USAGE_ASC, GUEST_SIZE_USAGE_DESC, GUEST_USED_SIZE_ASC, GUEST_USED_SIZE_DESC, HA_ASC, HA_DESC, HOSTNAME_ASC, HOSTNAME_DESC, ID_ASC, ID_DESC, IN_RECYCLE_BIN_ASC, IN_RECYCLE_BIN_DESC, INTERNAL_ASC, INTERNAL_DESC, IO_POLICY_ASC, IO_POLICY_DESC, IPS_ASC, IPS_DESC, KERNEL_INFO_ASC, KERNEL_INFO_DESC, LAST_SHUTDOWN_TIME_ASC, LAST_SHUTDOWN_TIME_DESC, LOCAL_CREATED_AT_ASC, LOCAL_CREATED_AT_DESC, LOCAL_ID_ASC, LOCAL_ID_DESC, LOGICAL_SIZE_BYTES_ASC, LOGICAL_SIZE_BYTES_DESC, MAX_BANDWIDTH_ASC, MAX_BANDWIDTH_DESC, MAX_BANDWIDTH_POLICY_ASC, MAX_BANDWIDTH_POLICY_DESC, MAX_IOPS_ASC, MAX_IOPS_DESC, MAX_IOPS_POLICY_ASC, MAX_IOPS_POLICY_DESC, MEMORY_ASC, MEMORY_DESC, MEMORY_USAGE_ASC, MEMORY_USAGE_DESC, NAME_ASC, NAME_DESC, NESTED_VIRTUALIZATION_ASC, NESTED_VIRTUALIZATION_DESC, NODE_IP_ASC, NODE_IP_DESC, ORIGINAL_NAME_ASC, ORIGINAL_NAME_DESC, OS_ASC, OS_DESC, PROTECTED_ASC, PROTECTED_DESC, PROVISIONED_SIZE_ASC, PROVISIONED_SIZE_DESC, SIZE_ASC, SIZE_DESC, STATUS_ASC, STATUS_DESC, UNIQUE_SIZE_ASC, UNIQUE_SIZE_DESC, VCPU_ASC, VCPU_DESC, VIDEO_TYPE_ASC, VIDEO_TYPE_DESC, VM_TOOLS_STATUS_ASC, VM_TOOLS_STATUS_DESC, VM_TOOLS_VERSION_ASC, VM_TOOLS_VERSION_DESC, VM_USAGE_ASC, VM_USAGE_DESC, WIN_OPT_ASC, WIN_OPT_DESC]  # noqa: E501

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
        """VmOrderByInput - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, VmOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmOrderByInput):
            return True

        return self.to_dict() != other.to_dict()
