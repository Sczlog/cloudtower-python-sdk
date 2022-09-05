# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class IscsiLunOrderByInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    ALLOWED_INITIATORS_ASC = "allowed_initiators_ASC"
    ALLOWED_INITIATORS_DESC = "allowed_initiators_DESC"
    ASSIGNED_SIZE_ASC = "assigned_size_ASC"
    ASSIGNED_SIZE_DESC = "assigned_size_DESC"
    BPS_ASC = "bps_ASC"
    BPS_DESC = "bps_DESC"
    BPS_MAX_ASC = "bps_max_ASC"
    BPS_MAX_DESC = "bps_max_DESC"
    BPS_MAX_LENGTH_ASC = "bps_max_length_ASC"
    BPS_MAX_LENGTH_DESC = "bps_max_length_DESC"
    BPS_RD_ASC = "bps_rd_ASC"
    BPS_RD_DESC = "bps_rd_DESC"
    BPS_RD_MAX_ASC = "bps_rd_max_ASC"
    BPS_RD_MAX_DESC = "bps_rd_max_DESC"
    BPS_RD_MAX_LENGTH_ASC = "bps_rd_max_length_ASC"
    BPS_RD_MAX_LENGTH_DESC = "bps_rd_max_length_DESC"
    BPS_WR_ASC = "bps_wr_ASC"
    BPS_WR_DESC = "bps_wr_DESC"
    BPS_WR_MAX_ASC = "bps_wr_max_ASC"
    BPS_WR_MAX_DESC = "bps_wr_max_DESC"
    BPS_WR_MAX_LENGTH_ASC = "bps_wr_max_length_ASC"
    BPS_WR_MAX_LENGTH_DESC = "bps_wr_max_length_DESC"
    ENTITYASYNCSTATUS_ASC = "entityAsyncStatus_ASC"
    ENTITYASYNCSTATUS_DESC = "entityAsyncStatus_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    IO_SIZE_ASC = "io_size_ASC"
    IO_SIZE_DESC = "io_size_DESC"
    IOPS_ASC = "iops_ASC"
    IOPS_DESC = "iops_DESC"
    IOPS_MAX_ASC = "iops_max_ASC"
    IOPS_MAX_DESC = "iops_max_DESC"
    IOPS_MAX_LENGTH_ASC = "iops_max_length_ASC"
    IOPS_MAX_LENGTH_DESC = "iops_max_length_DESC"
    IOPS_RD_ASC = "iops_rd_ASC"
    IOPS_RD_DESC = "iops_rd_DESC"
    IOPS_RD_MAX_ASC = "iops_rd_max_ASC"
    IOPS_RD_MAX_DESC = "iops_rd_max_DESC"
    IOPS_RD_MAX_LENGTH_ASC = "iops_rd_max_length_ASC"
    IOPS_RD_MAX_LENGTH_DESC = "iops_rd_max_length_DESC"
    IOPS_WR_ASC = "iops_wr_ASC"
    IOPS_WR_DESC = "iops_wr_DESC"
    IOPS_WR_MAX_ASC = "iops_wr_max_ASC"
    IOPS_WR_MAX_DESC = "iops_wr_max_DESC"
    IOPS_WR_MAX_LENGTH_ASC = "iops_wr_max_length_ASC"
    IOPS_WR_MAX_LENGTH_DESC = "iops_wr_max_length_DESC"
    LOCAL_CREATED_AT_ASC = "local_created_at_ASC"
    LOCAL_CREATED_AT_DESC = "local_created_at_DESC"
    LOCAL_ID_ASC = "local_id_ASC"
    LOCAL_ID_DESC = "local_id_DESC"
    LUN_ID_ASC = "lun_id_ASC"
    LUN_ID_DESC = "lun_id_DESC"
    NAME_ASC = "name_ASC"
    NAME_DESC = "name_DESC"
    REPLICA_NUM_ASC = "replica_num_ASC"
    REPLICA_NUM_DESC = "replica_num_DESC"
    SHARED_SIZE_ASC = "shared_size_ASC"
    SHARED_SIZE_DESC = "shared_size_DESC"
    SNAPSHOT_NUM_ASC = "snapshot_num_ASC"
    SNAPSHOT_NUM_DESC = "snapshot_num_DESC"
    STRIPE_NUM_ASC = "stripe_num_ASC"
    STRIPE_NUM_DESC = "stripe_num_DESC"
    STRIPE_SIZE_ASC = "stripe_size_ASC"
    STRIPE_SIZE_DESC = "stripe_size_DESC"
    THIN_PROVISION_ASC = "thin_provision_ASC"
    THIN_PROVISION_DESC = "thin_provision_DESC"
    UNIQUE_SIZE_ASC = "unique_size_ASC"
    UNIQUE_SIZE_DESC = "unique_size_DESC"
    ZBS_VOLUME_ID_ASC = "zbs_volume_id_ASC"
    ZBS_VOLUME_ID_DESC = "zbs_volume_id_DESC"

    allowable_values = [ALLOWED_INITIATORS_ASC, ALLOWED_INITIATORS_DESC, ASSIGNED_SIZE_ASC, ASSIGNED_SIZE_DESC, BPS_ASC, BPS_DESC, BPS_MAX_ASC, BPS_MAX_DESC, BPS_MAX_LENGTH_ASC, BPS_MAX_LENGTH_DESC, BPS_RD_ASC, BPS_RD_DESC, BPS_RD_MAX_ASC, BPS_RD_MAX_DESC, BPS_RD_MAX_LENGTH_ASC, BPS_RD_MAX_LENGTH_DESC, BPS_WR_ASC, BPS_WR_DESC, BPS_WR_MAX_ASC, BPS_WR_MAX_DESC, BPS_WR_MAX_LENGTH_ASC, BPS_WR_MAX_LENGTH_DESC, ENTITYASYNCSTATUS_ASC, ENTITYASYNCSTATUS_DESC, ID_ASC, ID_DESC, IO_SIZE_ASC, IO_SIZE_DESC, IOPS_ASC, IOPS_DESC, IOPS_MAX_ASC, IOPS_MAX_DESC, IOPS_MAX_LENGTH_ASC, IOPS_MAX_LENGTH_DESC, IOPS_RD_ASC, IOPS_RD_DESC, IOPS_RD_MAX_ASC, IOPS_RD_MAX_DESC, IOPS_RD_MAX_LENGTH_ASC, IOPS_RD_MAX_LENGTH_DESC, IOPS_WR_ASC, IOPS_WR_DESC, IOPS_WR_MAX_ASC, IOPS_WR_MAX_DESC, IOPS_WR_MAX_LENGTH_ASC, IOPS_WR_MAX_LENGTH_DESC, LOCAL_CREATED_AT_ASC, LOCAL_CREATED_AT_DESC, LOCAL_ID_ASC, LOCAL_ID_DESC, LUN_ID_ASC, LUN_ID_DESC, NAME_ASC, NAME_DESC, REPLICA_NUM_ASC, REPLICA_NUM_DESC, SHARED_SIZE_ASC, SHARED_SIZE_DESC, SNAPSHOT_NUM_ASC, SNAPSHOT_NUM_DESC, STRIPE_NUM_ASC, STRIPE_NUM_DESC, STRIPE_SIZE_ASC, STRIPE_SIZE_DESC, THIN_PROVISION_ASC, THIN_PROVISION_DESC, UNIQUE_SIZE_ASC, UNIQUE_SIZE_DESC, ZBS_VOLUME_ID_ASC, ZBS_VOLUME_ID_DESC]  # noqa: E501

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
        """IscsiLunOrderByInput - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, IscsiLunOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IscsiLunOrderByInput):
            return True

        return self.to_dict() != other.to_dict()
