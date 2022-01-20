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


class BackupStoreRepositoryOrderByInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CREATEDAT_ASC = "createdAt_ASC"
    CREATEDAT_DESC = "createdAt_DESC"
    DESCRIPTION_ASC = "description_ASC"
    DESCRIPTION_DESC = "description_DESC"
    ENTITYASYNCSTATUS_ASC = "entityAsyncStatus_ASC"
    ENTITYASYNCSTATUS_DESC = "entityAsyncStatus_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    ISCSI_CHAP_NAME_ASC = "iscsi_chap_name_ASC"
    ISCSI_CHAP_NAME_DESC = "iscsi_chap_name_DESC"
    ISCSI_CHAP_SECRET_ASC = "iscsi_chap_secret_ASC"
    ISCSI_CHAP_SECRET_DESC = "iscsi_chap_secret_DESC"
    ISCSI_IP_ASC = "iscsi_ip_ASC"
    ISCSI_IP_DESC = "iscsi_ip_DESC"
    ISCSI_LUN_ID_ASC = "iscsi_lun_id_ASC"
    ISCSI_LUN_ID_DESC = "iscsi_lun_id_DESC"
    ISCSI_PORT_ASC = "iscsi_port_ASC"
    ISCSI_PORT_DESC = "iscsi_port_DESC"
    ISCSI_TARGET_IQN_ASC = "iscsi_target_iqn_ASC"
    ISCSI_TARGET_IQN_DESC = "iscsi_target_iqn_DESC"
    NAME_ASC = "name_ASC"
    NAME_DESC = "name_DESC"
    NFS_PATH_ASC = "nfs_path_ASC"
    NFS_PATH_DESC = "nfs_path_DESC"
    NFS_SERVER_ASC = "nfs_server_ASC"
    NFS_SERVER_DESC = "nfs_server_DESC"
    RESOURCE_VERSION_ASC = "resource_version_ASC"
    RESOURCE_VERSION_DESC = "resource_version_DESC"
    STATUS_ASC = "status_ASC"
    STATUS_DESC = "status_DESC"
    TOTAL_CAPACITY_ASC = "total_capacity_ASC"
    TOTAL_CAPACITY_DESC = "total_capacity_DESC"
    TYPE_ASC = "type_ASC"
    TYPE_DESC = "type_DESC"
    UPDATEDAT_ASC = "updatedAt_ASC"
    UPDATEDAT_DESC = "updatedAt_DESC"
    USED_DATA_SPACE_ASC = "used_data_space_ASC"
    USED_DATA_SPACE_DESC = "used_data_space_DESC"
    VALID_DATA_SPACE_ASC = "valid_data_space_ASC"
    VALID_DATA_SPACE_DESC = "valid_data_space_DESC"

    allowable_values = [CREATEDAT_ASC, CREATEDAT_DESC, DESCRIPTION_ASC, DESCRIPTION_DESC, ENTITYASYNCSTATUS_ASC, ENTITYASYNCSTATUS_DESC, ID_ASC, ID_DESC, ISCSI_CHAP_NAME_ASC, ISCSI_CHAP_NAME_DESC, ISCSI_CHAP_SECRET_ASC, ISCSI_CHAP_SECRET_DESC, ISCSI_IP_ASC, ISCSI_IP_DESC, ISCSI_LUN_ID_ASC, ISCSI_LUN_ID_DESC, ISCSI_PORT_ASC, ISCSI_PORT_DESC, ISCSI_TARGET_IQN_ASC, ISCSI_TARGET_IQN_DESC, NAME_ASC, NAME_DESC, NFS_PATH_ASC, NFS_PATH_DESC, NFS_SERVER_ASC, NFS_SERVER_DESC, RESOURCE_VERSION_ASC, RESOURCE_VERSION_DESC, STATUS_ASC, STATUS_DESC, TOTAL_CAPACITY_ASC, TOTAL_CAPACITY_DESC, TYPE_ASC, TYPE_DESC, UPDATEDAT_ASC, UPDATEDAT_DESC, USED_DATA_SPACE_ASC, USED_DATA_SPACE_DESC, VALID_DATA_SPACE_ASC, VALID_DATA_SPACE_DESC]  # noqa: E501

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
        """BackupStoreRepositoryOrderByInput - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, BackupStoreRepositoryOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BackupStoreRepositoryOrderByInput):
            return True

        return self.to_dict() != other.to_dict()
