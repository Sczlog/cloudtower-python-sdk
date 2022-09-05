# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class ReportTask(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'created_at': 'str',
        'id': 'str',
        'internal': 'bool',
        'name': 'str',
        'plan_id': 'str',
        'status': 'TaskStatus',
        'template': 'NestedReportTemplate'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'id': 'id',
        'internal': 'internal',
        'name': 'name',
        'plan_id': 'plan_id',
        'status': 'status',
        'template': 'template'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ReportTask - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._created_at = None
        self._id = None
        self._internal = None
        self._name = None
        self._plan_id = None
        self._status = None
        self._template = None
        self.discriminator = None

        if "created_at" in kwargs:
            self.created_at = kwargs["created_at"]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "internal" in kwargs:
            self.internal = kwargs["internal"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        self.plan_id = kwargs.get("plan_id", None)
        if "status" in kwargs:
            self.status = kwargs["status"]
        if "template" in kwargs:
            self.template = kwargs["template"]

    @property
    def created_at(self):
        """Gets the created_at of this ReportTask.  # noqa: E501


        :return: The created_at of this ReportTask.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ReportTask.


        :param created_at: The created_at of this ReportTask.  # noqa: E501
        :type created_at: str
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this ReportTask.  # noqa: E501


        :return: The id of this ReportTask.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReportTask.


        :param id: The id of this ReportTask.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def internal(self):
        """Gets the internal of this ReportTask.  # noqa: E501


        :return: The internal of this ReportTask.  # noqa: E501
        :rtype: bool
        """
        return self._internal

    @internal.setter
    def internal(self, internal):
        """Sets the internal of this ReportTask.


        :param internal: The internal of this ReportTask.  # noqa: E501
        :type internal: bool
        """
        if self.local_vars_configuration.client_side_validation and internal is None:  # noqa: E501
            raise ValueError("Invalid value for `internal`, must not be `None`")  # noqa: E501

        self._internal = internal

    @property
    def name(self):
        """Gets the name of this ReportTask.  # noqa: E501


        :return: The name of this ReportTask.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReportTask.


        :param name: The name of this ReportTask.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def plan_id(self):
        """Gets the plan_id of this ReportTask.  # noqa: E501


        :return: The plan_id of this ReportTask.  # noqa: E501
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this ReportTask.


        :param plan_id: The plan_id of this ReportTask.  # noqa: E501
        :type plan_id: str
        """

        self._plan_id = plan_id

    @property
    def status(self):
        """Gets the status of this ReportTask.  # noqa: E501


        :return: The status of this ReportTask.  # noqa: E501
        :rtype: TaskStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ReportTask.


        :param status: The status of this ReportTask.  # noqa: E501
        :type status: TaskStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def template(self):
        """Gets the template of this ReportTask.  # noqa: E501


        :return: The template of this ReportTask.  # noqa: E501
        :rtype: NestedReportTemplate
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this ReportTask.


        :param template: The template of this ReportTask.  # noqa: E501
        :type template: NestedReportTemplate
        """
        if self.local_vars_configuration.client_side_validation and template is None:  # noqa: E501
            raise ValueError("Invalid value for `template`, must not be `None`")  # noqa: E501

        self._template = template

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
        if not isinstance(other, ReportTask):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportTask):
            return True

        return self.to_dict() != other.to_dict()
