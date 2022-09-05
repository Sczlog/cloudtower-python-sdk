# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class NestedTask(object):
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
        'args': 'object',
        'description': 'str',
        'id': 'str',
        'internal': 'bool',
        'local_created_at': 'str',
        'progress': 'float',
        'snapshot': 'str',
        'status': 'TaskStatus',
        'steps': 'list[NestedStep]'
    }

    attribute_map = {
        'args': 'args',
        'description': 'description',
        'id': 'id',
        'internal': 'internal',
        'local_created_at': 'local_created_at',
        'progress': 'progress',
        'snapshot': 'snapshot',
        'status': 'status',
        'steps': 'steps'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedTask - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._args = None
        self._description = None
        self._id = None
        self._internal = None
        self._local_created_at = None
        self._progress = None
        self._snapshot = None
        self._status = None
        self._steps = None
        self.discriminator = None

        if "args" in kwargs:
            self.args = kwargs["args"]
        if "description" in kwargs:
            self.description = kwargs["description"]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "internal" in kwargs:
            self.internal = kwargs["internal"]
        if "local_created_at" in kwargs:
            self.local_created_at = kwargs["local_created_at"]
        if "progress" in kwargs:
            self.progress = kwargs["progress"]
        if "snapshot" in kwargs:
            self.snapshot = kwargs["snapshot"]
        if "status" in kwargs:
            self.status = kwargs["status"]
        if "steps" in kwargs:
            self.steps = kwargs["steps"]

    @property
    def args(self):
        """Gets the args of this NestedTask.  # noqa: E501


        :return: The args of this NestedTask.  # noqa: E501
        :rtype: object
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this NestedTask.


        :param args: The args of this NestedTask.  # noqa: E501
        :type args: object
        """
        if self.local_vars_configuration.client_side_validation and args is None:  # noqa: E501
            raise ValueError("Invalid value for `args`, must not be `None`")  # noqa: E501

        self._args = args

    @property
    def description(self):
        """Gets the description of this NestedTask.  # noqa: E501


        :return: The description of this NestedTask.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NestedTask.


        :param description: The description of this NestedTask.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def id(self):
        """Gets the id of this NestedTask.  # noqa: E501


        :return: The id of this NestedTask.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NestedTask.


        :param id: The id of this NestedTask.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def internal(self):
        """Gets the internal of this NestedTask.  # noqa: E501


        :return: The internal of this NestedTask.  # noqa: E501
        :rtype: bool
        """
        return self._internal

    @internal.setter
    def internal(self, internal):
        """Sets the internal of this NestedTask.


        :param internal: The internal of this NestedTask.  # noqa: E501
        :type internal: bool
        """
        if self.local_vars_configuration.client_side_validation and internal is None:  # noqa: E501
            raise ValueError("Invalid value for `internal`, must not be `None`")  # noqa: E501

        self._internal = internal

    @property
    def local_created_at(self):
        """Gets the local_created_at of this NestedTask.  # noqa: E501


        :return: The local_created_at of this NestedTask.  # noqa: E501
        :rtype: str
        """
        return self._local_created_at

    @local_created_at.setter
    def local_created_at(self, local_created_at):
        """Sets the local_created_at of this NestedTask.


        :param local_created_at: The local_created_at of this NestedTask.  # noqa: E501
        :type local_created_at: str
        """
        if self.local_vars_configuration.client_side_validation and local_created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `local_created_at`, must not be `None`")  # noqa: E501

        self._local_created_at = local_created_at

    @property
    def progress(self):
        """Gets the progress of this NestedTask.  # noqa: E501


        :return: The progress of this NestedTask.  # noqa: E501
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this NestedTask.


        :param progress: The progress of this NestedTask.  # noqa: E501
        :type progress: float
        """
        if self.local_vars_configuration.client_side_validation and progress is None:  # noqa: E501
            raise ValueError("Invalid value for `progress`, must not be `None`")  # noqa: E501

        self._progress = progress

    @property
    def snapshot(self):
        """Gets the snapshot of this NestedTask.  # noqa: E501


        :return: The snapshot of this NestedTask.  # noqa: E501
        :rtype: str
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        """Sets the snapshot of this NestedTask.


        :param snapshot: The snapshot of this NestedTask.  # noqa: E501
        :type snapshot: str
        """
        if self.local_vars_configuration.client_side_validation and snapshot is None:  # noqa: E501
            raise ValueError("Invalid value for `snapshot`, must not be `None`")  # noqa: E501

        self._snapshot = snapshot

    @property
    def status(self):
        """Gets the status of this NestedTask.  # noqa: E501


        :return: The status of this NestedTask.  # noqa: E501
        :rtype: TaskStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NestedTask.


        :param status: The status of this NestedTask.  # noqa: E501
        :type status: TaskStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def steps(self):
        """Gets the steps of this NestedTask.  # noqa: E501


        :return: The steps of this NestedTask.  # noqa: E501
        :rtype: list[NestedStep]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this NestedTask.


        :param steps: The steps of this NestedTask.  # noqa: E501
        :type steps: list[NestedStep]
        """
        if self.local_vars_configuration.client_side_validation and steps is None:  # noqa: E501
            raise ValueError("Invalid value for `steps`, must not be `None`")  # noqa: E501

        self._steps = steps

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
        if not isinstance(other, NestedTask):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedTask):
            return True

        return self.to_dict() != other.to_dict()
