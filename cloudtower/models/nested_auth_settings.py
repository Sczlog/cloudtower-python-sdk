# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class NestedAuthSettings(object):
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
        'access_list': 'list[str]',
        'access_mode': 'AccessMode',
        'enable_single_session_login': 'bool',
        'login_miss_num_threshold': 'int',
        'login_miss_time_threshold': 'int',
        'password_complexity': 'PasswordComplexity',
        'password_expire_days': 'int',
        'session_max_age': 'int'
    }

    attribute_map = {
        'access_list': 'access_list',
        'access_mode': 'access_mode',
        'enable_single_session_login': 'enable_single_session_login',
        'login_miss_num_threshold': 'login_miss_num_threshold',
        'login_miss_time_threshold': 'login_miss_time_threshold',
        'password_complexity': 'password_complexity',
        'password_expire_days': 'password_expire_days',
        'session_max_age': 'session_max_age'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedAuthSettings - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._access_list = None
        self._access_mode = None
        self._enable_single_session_login = None
        self._login_miss_num_threshold = None
        self._login_miss_time_threshold = None
        self._password_complexity = None
        self._password_expire_days = None
        self._session_max_age = None
        self.discriminator = None

        self.access_list = kwargs.get("access_list", None)
        self.access_mode = kwargs.get("access_mode", None)
        self.enable_single_session_login = kwargs.get("enable_single_session_login", None)
        self.login_miss_num_threshold = kwargs.get("login_miss_num_threshold", None)
        self.login_miss_time_threshold = kwargs.get("login_miss_time_threshold", None)
        self.password_complexity = kwargs.get("password_complexity", None)
        self.password_expire_days = kwargs.get("password_expire_days", None)
        self.session_max_age = kwargs.get("session_max_age", None)

    @property
    def access_list(self):
        """Gets the access_list of this NestedAuthSettings.  # noqa: E501


        :return: The access_list of this NestedAuthSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._access_list

    @access_list.setter
    def access_list(self, access_list):
        """Sets the access_list of this NestedAuthSettings.


        :param access_list: The access_list of this NestedAuthSettings.  # noqa: E501
        :type access_list: list[str]
        """

        self._access_list = access_list

    @property
    def access_mode(self):
        """Gets the access_mode of this NestedAuthSettings.  # noqa: E501


        :return: The access_mode of this NestedAuthSettings.  # noqa: E501
        :rtype: AccessMode
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        """Sets the access_mode of this NestedAuthSettings.


        :param access_mode: The access_mode of this NestedAuthSettings.  # noqa: E501
        :type access_mode: AccessMode
        """

        self._access_mode = access_mode

    @property
    def enable_single_session_login(self):
        """Gets the enable_single_session_login of this NestedAuthSettings.  # noqa: E501


        :return: The enable_single_session_login of this NestedAuthSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_single_session_login

    @enable_single_session_login.setter
    def enable_single_session_login(self, enable_single_session_login):
        """Sets the enable_single_session_login of this NestedAuthSettings.


        :param enable_single_session_login: The enable_single_session_login of this NestedAuthSettings.  # noqa: E501
        :type enable_single_session_login: bool
        """

        self._enable_single_session_login = enable_single_session_login

    @property
    def login_miss_num_threshold(self):
        """Gets the login_miss_num_threshold of this NestedAuthSettings.  # noqa: E501


        :return: The login_miss_num_threshold of this NestedAuthSettings.  # noqa: E501
        :rtype: int
        """
        return self._login_miss_num_threshold

    @login_miss_num_threshold.setter
    def login_miss_num_threshold(self, login_miss_num_threshold):
        """Sets the login_miss_num_threshold of this NestedAuthSettings.


        :param login_miss_num_threshold: The login_miss_num_threshold of this NestedAuthSettings.  # noqa: E501
        :type login_miss_num_threshold: int
        """

        self._login_miss_num_threshold = login_miss_num_threshold

    @property
    def login_miss_time_threshold(self):
        """Gets the login_miss_time_threshold of this NestedAuthSettings.  # noqa: E501


        :return: The login_miss_time_threshold of this NestedAuthSettings.  # noqa: E501
        :rtype: int
        """
        return self._login_miss_time_threshold

    @login_miss_time_threshold.setter
    def login_miss_time_threshold(self, login_miss_time_threshold):
        """Sets the login_miss_time_threshold of this NestedAuthSettings.


        :param login_miss_time_threshold: The login_miss_time_threshold of this NestedAuthSettings.  # noqa: E501
        :type login_miss_time_threshold: int
        """

        self._login_miss_time_threshold = login_miss_time_threshold

    @property
    def password_complexity(self):
        """Gets the password_complexity of this NestedAuthSettings.  # noqa: E501


        :return: The password_complexity of this NestedAuthSettings.  # noqa: E501
        :rtype: PasswordComplexity
        """
        return self._password_complexity

    @password_complexity.setter
    def password_complexity(self, password_complexity):
        """Sets the password_complexity of this NestedAuthSettings.


        :param password_complexity: The password_complexity of this NestedAuthSettings.  # noqa: E501
        :type password_complexity: PasswordComplexity
        """

        self._password_complexity = password_complexity

    @property
    def password_expire_days(self):
        """Gets the password_expire_days of this NestedAuthSettings.  # noqa: E501


        :return: The password_expire_days of this NestedAuthSettings.  # noqa: E501
        :rtype: int
        """
        return self._password_expire_days

    @password_expire_days.setter
    def password_expire_days(self, password_expire_days):
        """Sets the password_expire_days of this NestedAuthSettings.


        :param password_expire_days: The password_expire_days of this NestedAuthSettings.  # noqa: E501
        :type password_expire_days: int
        """

        self._password_expire_days = password_expire_days

    @property
    def session_max_age(self):
        """Gets the session_max_age of this NestedAuthSettings.  # noqa: E501


        :return: The session_max_age of this NestedAuthSettings.  # noqa: E501
        :rtype: int
        """
        return self._session_max_age

    @session_max_age.setter
    def session_max_age(self, session_max_age):
        """Sets the session_max_age of this NestedAuthSettings.


        :param session_max_age: The session_max_age of this NestedAuthSettings.  # noqa: E501
        :type session_max_age: int
        """

        self._session_max_age = session_max_age

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
        if not isinstance(other, NestedAuthSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedAuthSettings):
            return True

        return self.to_dict() != other.to_dict()
