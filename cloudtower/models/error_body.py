# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class ErrorBody(object):
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
        'code': 'ErrorCode',
        'props': 'object',
        'stack': 'str',
        'message': 'str',
        'status': 'int',
        'operation_name': 'str',
        'path': 'str'
    }

    attribute_map = {
        'code': 'code',
        'props': 'props',
        'stack': 'stack',
        'message': 'message',
        'status': 'status',
        'operation_name': 'operationName',
        'path': 'path'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ErrorBody - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._code = None
        self._props = None
        self._stack = None
        self._message = None
        self._status = None
        self._operation_name = None
        self._path = None
        self.discriminator = None

        if "code" in kwargs:
            self.code = kwargs["code"]
        self.props = kwargs.get("props", None)
        if "stack" in kwargs:
            self.stack = kwargs["stack"]
        if "message" in kwargs:
            self.message = kwargs["message"]
        if "status" in kwargs:
            self.status = kwargs["status"]
        if "operation_name" in kwargs:
            self.operation_name = kwargs["operation_name"]
        if "path" in kwargs:
            self.path = kwargs["path"]

    @property
    def code(self):
        """Gets the code of this ErrorBody.  # noqa: E501


        :return: The code of this ErrorBody.  # noqa: E501
        :rtype: ErrorCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ErrorBody.


        :param code: The code of this ErrorBody.  # noqa: E501
        :type code: ErrorCode
        """

        self._code = code

    @property
    def props(self):
        """Gets the props of this ErrorBody.  # noqa: E501


        :return: The props of this ErrorBody.  # noqa: E501
        :rtype: object
        """
        return self._props

    @props.setter
    def props(self, props):
        """Sets the props of this ErrorBody.


        :param props: The props of this ErrorBody.  # noqa: E501
        :type props: object
        """

        self._props = props

    @property
    def stack(self):
        """Gets the stack of this ErrorBody.  # noqa: E501


        :return: The stack of this ErrorBody.  # noqa: E501
        :rtype: str
        """
        return self._stack

    @stack.setter
    def stack(self, stack):
        """Sets the stack of this ErrorBody.


        :param stack: The stack of this ErrorBody.  # noqa: E501
        :type stack: str
        """

        self._stack = stack

    @property
    def message(self):
        """Gets the message of this ErrorBody.  # noqa: E501


        :return: The message of this ErrorBody.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ErrorBody.


        :param message: The message of this ErrorBody.  # noqa: E501
        :type message: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def status(self):
        """Gets the status of this ErrorBody.  # noqa: E501


        :return: The status of this ErrorBody.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ErrorBody.


        :param status: The status of this ErrorBody.  # noqa: E501
        :type status: int
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def operation_name(self):
        """Gets the operation_name of this ErrorBody.  # noqa: E501


        :return: The operation_name of this ErrorBody.  # noqa: E501
        :rtype: str
        """
        return self._operation_name

    @operation_name.setter
    def operation_name(self, operation_name):
        """Sets the operation_name of this ErrorBody.


        :param operation_name: The operation_name of this ErrorBody.  # noqa: E501
        :type operation_name: str
        """

        self._operation_name = operation_name

    @property
    def path(self):
        """Gets the path of this ErrorBody.  # noqa: E501


        :return: The path of this ErrorBody.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ErrorBody.


        :param path: The path of this ErrorBody.  # noqa: E501
        :type path: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

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
        if not isinstance(other, ErrorBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorBody):
            return True

        return self.to_dict() != other.to_dict()
