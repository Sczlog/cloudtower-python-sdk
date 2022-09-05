# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class ROLEACTION(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    _ = "*"
    MANAGE_DATA_CENTER = "MANAGE_DATA_CENTER"
    MANAGE_CLUSTER_CONNECTION = "MANAGE_CLUSTER_CONNECTION"
    MANAGE_HOST = "MANAGE_HOST"
    MANAGE_NIC_MTU = "MANAGE_NIC_MTU"
    MANAGE_DISK = "MANAGE_DISK"
    MANAGE_HARDWARE_TOPO = "MANAGE_HARDWARE_TOPO"
    MANAGE_USB_DEVICE = "MANAGE_USB_DEVICE"
    MANAGE_VDS = "MANAGE_VDS"
    MANAGE_VLAN = "MANAGE_VLAN"
    MANAGE_SYSTEM_VLAN = "MANAGE_SYSTEM_VLAN"
    MANAGE_ISCSI_DATA_STORE = "MANAGE_ISCSI_DATA_STORE"
    MANAGE_NFS_DATA_STORE = "MANAGE_NFS_DATA_STORE"
    MANAGE_NVMF_DATA_STORE = "MANAGE_NVMF_DATA_STORE"
    CREATE_VM = "CREATE_VM"
    UPDATE_VM = "UPDATE_VM"
    DELETE_VM = "DELETE_VM"
    UPDATE_VM_ADVANCED_SETTING = "UPDATE_VM_ADVANCED_SETTING"
    UPDATE_VM_GUEST = "UPDATE_VM_GUEST"
    VM_OPERATION_OPEN_TERMINAL = "VM_OPERATION_OPEN_TERMINAL"
    VM_OPERATION_MIGRATE = "VM_OPERATION_MIGRATE"
    VM_OPERATION_VM_FOLDER = "VM_OPERATION_VM_FOLDER"
    VM_OPERATION_VM_POWER = "VM_OPERATION_VM_POWER"
    VM_OPERATION_CLONE = "VM_OPERATION_CLONE"
    VM_OPERATION_INSTALL_TOOLS = "VM_OPERATION_INSTALL_TOOLS"
    MANAGE_VM_TEMPLATE = "MANAGE_VM_TEMPLATE"
    MANAGE_VM_SNAPSHOT = "MANAGE_VM_SNAPSHOT"
    MANAGE_VM_VOLUME = "MANAGE_VM_VOLUME"
    MANAGE_ISO = "MANAGE_ISO"
    QUERY_SENSITIVE_RESOURCE_LIST = "QUERY_SENSITIVE_RESOURCE_LIST"
    QUERY_SENSITIVE_RESOURCE = "QUERY_SENSITIVE_RESOURCE"
    MANAGE_SENSITIVE_RESOURCE = "MANAGE_SENSITIVE_RESOURCE"
    MANAGE_VM_PLACEMENT_GROUP = "MANAGE_VM_PLACEMENT_GROUP"
    MANAGE_SNAPSHOT_PLAN = "MANAGE_SNAPSHOT_PLAN"
    MANAGE_ALERT = "MANAGE_ALERT"
    MANAGE_MONITOR_VIEW = "MANAGE_MONITOR_VIEW"
    MANAGE_ENTITY_FILTER = "MANAGE_ENTITY_FILTER"
    MANAGE_CLUSTER_BASIC_INFO = "MANAGE_CLUSTER_BASIC_INFO"
    MANAGE_CLUSTER_LICENCE = "MANAGE_CLUSTER_LICENCE"
    MANAGE_CLUSTER_SNMP = "MANAGE_CLUSTER_SNMP"
    MANAGE_CLUSTER_VIP = "MANAGE_CLUSTER_VIP"
    MANAGE_CLUSTER_MANAGEMENT_IP = "MANAGE_CLUSTER_MANAGEMENT_IP"
    MANAGE_DNS_SERVER = "MANAGE_DNS_SERVER"
    MANAGE_NTP_SERVER = "MANAGE_NTP_SERVER"
    MANAGE_IPMI = "MANAGE_IPMI"
    MANAGE_CLUSTER_VM_CPU_MODEL = "MANAGE_CLUSTER_VM_CPU_MODEL"
    MANAGE_CLUSTER_VM_TOOLS = "MANAGE_CLUSTER_VM_TOOLS"
    MANAGE_CLUSTER_HOT_MIGRATION = "MANAGE_CLUSTER_HOT_MIGRATION"
    MANAGE_CLUSTER_HA = "MANAGE_CLUSTER_HA"
    MANAGE_SSL_CERTIFICATE = "MANAGE_SSL_CERTIFICATE"
    MANAGE_LOG_COLLECTION = "MANAGE_LOG_COLLECTION"
    MANAGE_LABEL = "MANAGE_LABEL"
    MANAGE_USER_AND_ROLE = "MANAGE_USER_AND_ROLE"
    MANAGE_PASSWORD_SETTINGS = "MANAGE_PASSWORD_SETTINGS"
    MANAGE_ACCESS_CONTROL = "MANAGE_ACCESS_CONTROL"
    MANAGE_SESSION_EXPIRATION = "MANAGE_SESSION_EXPIRATION"
    MANAGE_VCENTER_ASSOCIATION = "MANAGE_VCENTER_ASSOCIATION"
    MANAGE_ESXI_ASSOCIATION = "MANAGE_ESXI_ASSOCIATION"
    MANAGE_AUDIT_LOG = "MANAGE_AUDIT_LOG"
    MANAGE_ALERT_EMAIL_SETTING = "MANAGE_ALERT_EMAIL_SETTING"
    MANAGE_SMTP_SERVER = "MANAGE_SMTP_SERVER"
    MANAGE_CLUSTER_UPGRADE = "MANAGE_CLUSTER_UPGRADE"
    MANAGE_VM_RECYCLE_BIN_SETTING = "MANAGE_VM_RECYCLE_BIN_SETTING"
    MANAGE_REPORT = "MANAGE_REPORT"
    MANAGE_SHARING_VM_TOOLS = "MANAGE_SHARING_VM_TOOLS"
    MANAGE_ADVANCED_MONITOR = "MANAGE_ADVANCED_MONITOR"
    MANAGE_THIRD_PARTY_DRIVER = "MANAGE_THIRD_PARTY_DRIVER"
    MANAGE_ORGANIZATION_NAME = "MANAGE_ORGANIZATION_NAME"
    MANAGE_CLOUD_TOWER_LICENSE = "MANAGE_CLOUD_TOWER_LICENSE"
    MANAGE_CONSISTENCY_GROUP = "MANAGE_CONSISTENCY_GROUP"
    MANAGE_SR_IOV_NIC = "MANAGE_SR_IOV_NIC"
    MANAGE_CLUSTER_ISCSI = "MANAGE_CLUSTER_ISCSI"
    MANAGE_BACKUP_LICENSE = "MANAGE_BACKUP_LICENSE"
    MANAGE_BACKUP_PACKAGE = "MANAGE_BACKUP_PACKAGE"
    MANAGE_BACKUP_SERVICE = "MANAGE_BACKUP_SERVICE"
    MANAGE_BACKUP_STORE_REPOSITORY = "MANAGE_BACKUP_STORE_REPOSITORY"
    MANAGE_BACKUP_PLAN = "MANAGE_BACKUP_PLAN"
    MANAGE_BACKUP_TASK = "MANAGE_BACKUP_TASK"
    MANAGE_BACKUP_RESTORE_POINT = "MANAGE_BACKUP_RESTORE_POINT"
    MANAGE_BACKUP_RESTORE_POINT_TASK = "MANAGE_BACKUP_RESTORE_POINT_TASK"

    allowable_values = [_, MANAGE_DATA_CENTER, MANAGE_CLUSTER_CONNECTION, MANAGE_HOST, MANAGE_NIC_MTU, MANAGE_DISK, MANAGE_HARDWARE_TOPO, MANAGE_USB_DEVICE, MANAGE_VDS, MANAGE_VLAN, MANAGE_SYSTEM_VLAN, MANAGE_ISCSI_DATA_STORE, MANAGE_NFS_DATA_STORE, MANAGE_NVMF_DATA_STORE, CREATE_VM, UPDATE_VM, DELETE_VM, UPDATE_VM_ADVANCED_SETTING, UPDATE_VM_GUEST, VM_OPERATION_OPEN_TERMINAL, VM_OPERATION_MIGRATE, VM_OPERATION_VM_FOLDER, VM_OPERATION_VM_POWER, VM_OPERATION_CLONE, VM_OPERATION_INSTALL_TOOLS, MANAGE_VM_TEMPLATE, MANAGE_VM_SNAPSHOT, MANAGE_VM_VOLUME, MANAGE_ISO, QUERY_SENSITIVE_RESOURCE_LIST, QUERY_SENSITIVE_RESOURCE, MANAGE_SENSITIVE_RESOURCE, MANAGE_VM_PLACEMENT_GROUP, MANAGE_SNAPSHOT_PLAN, MANAGE_ALERT, MANAGE_MONITOR_VIEW, MANAGE_ENTITY_FILTER, MANAGE_CLUSTER_BASIC_INFO, MANAGE_CLUSTER_LICENCE, MANAGE_CLUSTER_SNMP, MANAGE_CLUSTER_VIP, MANAGE_CLUSTER_MANAGEMENT_IP, MANAGE_DNS_SERVER, MANAGE_NTP_SERVER, MANAGE_IPMI, MANAGE_CLUSTER_VM_CPU_MODEL, MANAGE_CLUSTER_VM_TOOLS, MANAGE_CLUSTER_HOT_MIGRATION, MANAGE_CLUSTER_HA, MANAGE_SSL_CERTIFICATE, MANAGE_LOG_COLLECTION, MANAGE_LABEL, MANAGE_USER_AND_ROLE, MANAGE_PASSWORD_SETTINGS, MANAGE_ACCESS_CONTROL, MANAGE_SESSION_EXPIRATION, MANAGE_VCENTER_ASSOCIATION, MANAGE_ESXI_ASSOCIATION, MANAGE_AUDIT_LOG, MANAGE_ALERT_EMAIL_SETTING, MANAGE_SMTP_SERVER, MANAGE_CLUSTER_UPGRADE, MANAGE_VM_RECYCLE_BIN_SETTING, MANAGE_REPORT, MANAGE_SHARING_VM_TOOLS, MANAGE_ADVANCED_MONITOR, MANAGE_THIRD_PARTY_DRIVER, MANAGE_ORGANIZATION_NAME, MANAGE_CLOUD_TOWER_LICENSE, MANAGE_CONSISTENCY_GROUP, MANAGE_SR_IOV_NIC, MANAGE_CLUSTER_ISCSI, MANAGE_BACKUP_LICENSE, MANAGE_BACKUP_PACKAGE, MANAGE_BACKUP_SERVICE, MANAGE_BACKUP_STORE_REPOSITORY, MANAGE_BACKUP_PLAN, MANAGE_BACKUP_TASK, MANAGE_BACKUP_RESTORE_POINT, MANAGE_BACKUP_RESTORE_POINT_TASK]  # noqa: E501

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
        """ROLEACTION - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, ROLEACTION):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ROLEACTION):
            return True

        return self.to_dict() != other.to_dict()
