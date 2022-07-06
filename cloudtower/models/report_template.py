# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.1.0
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


class ReportTemplate(object):
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
        'description': 'str',
        'execute_plan': 'list[NestedExecutePlan]',
        'id': 'str',
        'name': 'str',
        'preset': 'str',
        'resource_meta': 'list[NestedResourceMeta]',
        'task_num': 'int',
        'tasks': 'list[NestedReportTask]'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'description': 'description',
        'execute_plan': 'execute_plan',
        'id': 'id',
        'name': 'name',
        'preset': 'preset',
        'resource_meta': 'resource_meta',
        'task_num': 'task_num',
        'tasks': 'tasks'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ReportTemplate - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._created_at = None
        self._description = None
        self._execute_plan = None
        self._id = None
        self._name = None
        self._preset = None
        self._resource_meta = None
        self._task_num = None
        self._tasks = None
        self.discriminator = None

        if "created_at" in kwargs:
            self.created_at = kwargs["created_at"]
        if "description" in kwargs:
            self.description = kwargs["description"]
        if "execute_plan" in kwargs:
            self.execute_plan = kwargs["execute_plan"]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        self.preset = kwargs.get("preset", None)
        if "resource_meta" in kwargs:
            self.resource_meta = kwargs["resource_meta"]
        if "task_num" in kwargs:
            self.task_num = kwargs["task_num"]
        self.tasks = kwargs.get("tasks", None)

    @property
    def created_at(self):
        """Gets the created_at of this ReportTemplate.  # noqa: E501


        :return: The created_at of this ReportTemplate.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ReportTemplate.


        :param created_at: The created_at of this ReportTemplate.  # noqa: E501
        :type created_at: str
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this ReportTemplate.  # noqa: E501


        :return: The description of this ReportTemplate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReportTemplate.


        :param description: The description of this ReportTemplate.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def execute_plan(self):
        """Gets the execute_plan of this ReportTemplate.  # noqa: E501


        :return: The execute_plan of this ReportTemplate.  # noqa: E501
        :rtype: list[NestedExecutePlan]
        """
        return self._execute_plan

    @execute_plan.setter
    def execute_plan(self, execute_plan):
        """Sets the execute_plan of this ReportTemplate.


        :param execute_plan: The execute_plan of this ReportTemplate.  # noqa: E501
        :type execute_plan: list[NestedExecutePlan]
        """
        if self.local_vars_configuration.client_side_validation and execute_plan is None:  # noqa: E501
            raise ValueError("Invalid value for `execute_plan`, must not be `None`")  # noqa: E501

        self._execute_plan = execute_plan

    @property
    def id(self):
        """Gets the id of this ReportTemplate.  # noqa: E501


        :return: The id of this ReportTemplate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReportTemplate.


        :param id: The id of this ReportTemplate.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this ReportTemplate.  # noqa: E501


        :return: The name of this ReportTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReportTemplate.


        :param name: The name of this ReportTemplate.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def preset(self):
        """Gets the preset of this ReportTemplate.  # noqa: E501


        :return: The preset of this ReportTemplate.  # noqa: E501
        :rtype: str
        """
        return self._preset

    @preset.setter
    def preset(self, preset):
        """Sets the preset of this ReportTemplate.


        :param preset: The preset of this ReportTemplate.  # noqa: E501
        :type preset: str
        """

        self._preset = preset

    @property
    def resource_meta(self):
        """Gets the resource_meta of this ReportTemplate.  # noqa: E501


        :return: The resource_meta of this ReportTemplate.  # noqa: E501
        :rtype: list[NestedResourceMeta]
        """
        return self._resource_meta

    @resource_meta.setter
    def resource_meta(self, resource_meta):
        """Sets the resource_meta of this ReportTemplate.


        :param resource_meta: The resource_meta of this ReportTemplate.  # noqa: E501
        :type resource_meta: list[NestedResourceMeta]
        """
        if self.local_vars_configuration.client_side_validation and resource_meta is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_meta`, must not be `None`")  # noqa: E501

        self._resource_meta = resource_meta

    @property
    def task_num(self):
        """Gets the task_num of this ReportTemplate.  # noqa: E501


        :return: The task_num of this ReportTemplate.  # noqa: E501
        :rtype: int
        """
        return self._task_num

    @task_num.setter
    def task_num(self, task_num):
        """Sets the task_num of this ReportTemplate.


        :param task_num: The task_num of this ReportTemplate.  # noqa: E501
        :type task_num: int
        """
        if self.local_vars_configuration.client_side_validation and task_num is None:  # noqa: E501
            raise ValueError("Invalid value for `task_num`, must not be `None`")  # noqa: E501

        self._task_num = task_num

    @property
    def tasks(self):
        """Gets the tasks of this ReportTemplate.  # noqa: E501


        :return: The tasks of this ReportTemplate.  # noqa: E501
        :rtype: list[NestedReportTask]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this ReportTemplate.


        :param tasks: The tasks of this ReportTemplate.  # noqa: E501
        :type tasks: list[NestedReportTask]
        """

        self._tasks = tasks

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
        if not isinstance(other, ReportTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportTemplate):
            return True

        return self.to_dict() != other.to_dict()
