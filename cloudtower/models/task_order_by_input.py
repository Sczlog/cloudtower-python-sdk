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


class TaskOrderByInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    ARGS_ASC = "args_ASC"
    ARGS_DESC = "args_DESC"
    DESCRIPTION_ASC = "description_ASC"
    DESCRIPTION_DESC = "description_DESC"
    ERROR_CODE_ASC = "error_code_ASC"
    ERROR_CODE_DESC = "error_code_DESC"
    ERROR_MESSAGE_ASC = "error_message_ASC"
    ERROR_MESSAGE_DESC = "error_message_DESC"
    FINISHED_AT_ASC = "finished_at_ASC"
    FINISHED_AT_DESC = "finished_at_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    INTERNAL_ASC = "internal_ASC"
    INTERNAL_DESC = "internal_DESC"
    KEY_ASC = "key_ASC"
    KEY_DESC = "key_DESC"
    LOCAL_CREATED_AT_ASC = "local_created_at_ASC"
    LOCAL_CREATED_AT_DESC = "local_created_at_DESC"
    PROGRESS_ASC = "progress_ASC"
    PROGRESS_DESC = "progress_DESC"
    RESOURCE_ID_ASC = "resource_id_ASC"
    RESOURCE_ID_DESC = "resource_id_DESC"
    RESOURCE_MUTATION_ASC = "resource_mutation_ASC"
    RESOURCE_MUTATION_DESC = "resource_mutation_DESC"
    RESOURCE_ROLLBACK_ERROR_ASC = "resource_rollback_error_ASC"
    RESOURCE_ROLLBACK_ERROR_DESC = "resource_rollback_error_DESC"
    RESOURCE_ROLLBACK_RETRY_COUNT_ASC = "resource_rollback_retry_count_ASC"
    RESOURCE_ROLLBACK_RETRY_COUNT_DESC = "resource_rollback_retry_count_DESC"
    RESOURCE_ROLLBACKED_ASC = "resource_rollbacked_ASC"
    RESOURCE_ROLLBACKED_DESC = "resource_rollbacked_DESC"
    RESOURCE_TYPE_ASC = "resource_type_ASC"
    RESOURCE_TYPE_DESC = "resource_type_DESC"
    SNAPSHOT_ASC = "snapshot_ASC"
    SNAPSHOT_DESC = "snapshot_DESC"
    STARTED_AT_ASC = "started_at_ASC"
    STARTED_AT_DESC = "started_at_DESC"
    STATUS_ASC = "status_ASC"
    STATUS_DESC = "status_DESC"
    STEPS_ASC = "steps_ASC"
    STEPS_DESC = "steps_DESC"
    TYPE_ASC = "type_ASC"
    TYPE_DESC = "type_DESC"

    allowable_values = [ARGS_ASC, ARGS_DESC, DESCRIPTION_ASC, DESCRIPTION_DESC, ERROR_CODE_ASC, ERROR_CODE_DESC, ERROR_MESSAGE_ASC, ERROR_MESSAGE_DESC, FINISHED_AT_ASC, FINISHED_AT_DESC, ID_ASC, ID_DESC, INTERNAL_ASC, INTERNAL_DESC, KEY_ASC, KEY_DESC, LOCAL_CREATED_AT_ASC, LOCAL_CREATED_AT_DESC, PROGRESS_ASC, PROGRESS_DESC, RESOURCE_ID_ASC, RESOURCE_ID_DESC, RESOURCE_MUTATION_ASC, RESOURCE_MUTATION_DESC, RESOURCE_ROLLBACK_ERROR_ASC, RESOURCE_ROLLBACK_ERROR_DESC, RESOURCE_ROLLBACK_RETRY_COUNT_ASC, RESOURCE_ROLLBACK_RETRY_COUNT_DESC, RESOURCE_ROLLBACKED_ASC, RESOURCE_ROLLBACKED_DESC, RESOURCE_TYPE_ASC, RESOURCE_TYPE_DESC, SNAPSHOT_ASC, SNAPSHOT_DESC, STARTED_AT_ASC, STARTED_AT_DESC, STATUS_ASC, STATUS_DESC, STEPS_ASC, STEPS_DESC, TYPE_ASC, TYPE_DESC]  # noqa: E501

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
        """TaskOrderByInput - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, TaskOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskOrderByInput):
            return True

        return self.to_dict() != other.to_dict()
