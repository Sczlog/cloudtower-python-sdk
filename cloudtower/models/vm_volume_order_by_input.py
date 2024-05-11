# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VmVolumeOrderByInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    DESCRIPTION_ASC = "description_ASC"
    DESCRIPTION_DESC = "description_DESC"
    ELF_STORAGE_POLICY_ASC = "elf_storage_policy_ASC"
    ELF_STORAGE_POLICY_DESC = "elf_storage_policy_DESC"
    ENTITYASYNCSTATUS_ASC = "entityAsyncStatus_ASC"
    ENTITYASYNCSTATUS_DESC = "entityAsyncStatus_DESC"
    GUEST_SIZE_USAGE_ASC = "guest_size_usage_ASC"
    GUEST_SIZE_USAGE_DESC = "guest_size_usage_DESC"
    GUEST_USED_SIZE_ASC = "guest_used_size_ASC"
    GUEST_USED_SIZE_DESC = "guest_used_size_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    LOCAL_CREATED_AT_ASC = "local_created_at_ASC"
    LOCAL_CREATED_AT_DESC = "local_created_at_DESC"
    LOCAL_ID_ASC = "local_id_ASC"
    LOCAL_ID_DESC = "local_id_DESC"
    MOUNTING_ASC = "mounting_ASC"
    MOUNTING_DESC = "mounting_DESC"
    NAME_ASC = "name_ASC"
    NAME_DESC = "name_DESC"
    PATH_ASC = "path_ASC"
    PATH_DESC = "path_DESC"
    SHARING_ASC = "sharing_ASC"
    SHARING_DESC = "sharing_DESC"
    SIZE_ASC = "size_ASC"
    SIZE_DESC = "size_DESC"
    TYPE_ASC = "type_ASC"
    TYPE_DESC = "type_DESC"
    UNIQUE_LOGICAL_SIZE_ASC = "unique_logical_size_ASC"
    UNIQUE_LOGICAL_SIZE_DESC = "unique_logical_size_DESC"
    UNIQUE_SIZE_ASC = "unique_size_ASC"
    UNIQUE_SIZE_DESC = "unique_size_DESC"

    allowable_values = [DESCRIPTION_ASC, DESCRIPTION_DESC, ELF_STORAGE_POLICY_ASC, ELF_STORAGE_POLICY_DESC, ENTITYASYNCSTATUS_ASC, ENTITYASYNCSTATUS_DESC, GUEST_SIZE_USAGE_ASC, GUEST_SIZE_USAGE_DESC, GUEST_USED_SIZE_ASC, GUEST_USED_SIZE_DESC, ID_ASC, ID_DESC, LOCAL_CREATED_AT_ASC, LOCAL_CREATED_AT_DESC, LOCAL_ID_ASC, LOCAL_ID_DESC, MOUNTING_ASC, MOUNTING_DESC, NAME_ASC, NAME_DESC, PATH_ASC, PATH_DESC, SHARING_ASC, SHARING_DESC, SIZE_ASC, SIZE_DESC, TYPE_ASC, TYPE_DESC, UNIQUE_LOGICAL_SIZE_ASC, UNIQUE_LOGICAL_SIZE_DESC, UNIQUE_SIZE_ASC, UNIQUE_SIZE_DESC]  # noqa: E501

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
        """VmVolumeOrderByInput - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, VmVolumeOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmVolumeOrderByInput):
            return True

        return self.to_dict() != other.to_dict()
