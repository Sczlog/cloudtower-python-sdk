# coding: utf-8

"""
    Tower SDK API

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 1.8.0
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


class AlertNotifier(object):
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
        'disabled': 'bool',
        'email_from': 'str',
        'email_tos': 'list[str]',
        'id': 'str',
        'language_code': 'NotifierLanguageCode',
        'notice_severities': 'list[str]',
        'security_mode': 'NotifierSecurityMode',
        'smtp_server_host': 'str',
        'smtp_server_port': 'int',
        'username': 'str'
    }

    attribute_map = {
        'disabled': 'disabled',
        'email_from': 'email_from',
        'email_tos': 'email_tos',
        'id': 'id',
        'language_code': 'language_code',
        'notice_severities': 'notice_severities',
        'security_mode': 'security_mode',
        'smtp_server_host': 'smtp_server_host',
        'smtp_server_port': 'smtp_server_port',
        'username': 'username'
    }

    def __init__(self, disabled=None, email_from=None, email_tos=None, id=None, language_code=None, notice_severities=None, security_mode=None, smtp_server_host=None, smtp_server_port=None, username=None, local_vars_configuration=None):  # noqa: E501
        """AlertNotifier - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._disabled = None
        self._email_from = None
        self._email_tos = None
        self._id = None
        self._language_code = None
        self._notice_severities = None
        self._security_mode = None
        self._smtp_server_host = None
        self._smtp_server_port = None
        self._username = None
        self.discriminator = None

        self.disabled = disabled
        self.email_from = email_from
        self.email_tos = email_tos
        self.id = id
        self.language_code = language_code
        self.notice_severities = notice_severities
        self.security_mode = security_mode
        self.smtp_server_host = smtp_server_host
        self.smtp_server_port = smtp_server_port
        self.username = username

    @property
    def disabled(self):
        """Gets the disabled of this AlertNotifier.  # noqa: E501


        :return: The disabled of this AlertNotifier.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this AlertNotifier.


        :param disabled: The disabled of this AlertNotifier.  # noqa: E501
        :type disabled: bool
        """
        if self.local_vars_configuration.client_side_validation and disabled is None:  # noqa: E501
            raise ValueError("Invalid value for `disabled`, must not be `None`")  # noqa: E501

        self._disabled = disabled

    @property
    def email_from(self):
        """Gets the email_from of this AlertNotifier.  # noqa: E501


        :return: The email_from of this AlertNotifier.  # noqa: E501
        :rtype: str
        """
        return self._email_from

    @email_from.setter
    def email_from(self, email_from):
        """Sets the email_from of this AlertNotifier.


        :param email_from: The email_from of this AlertNotifier.  # noqa: E501
        :type email_from: str
        """

        self._email_from = email_from

    @property
    def email_tos(self):
        """Gets the email_tos of this AlertNotifier.  # noqa: E501


        :return: The email_tos of this AlertNotifier.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_tos

    @email_tos.setter
    def email_tos(self, email_tos):
        """Sets the email_tos of this AlertNotifier.


        :param email_tos: The email_tos of this AlertNotifier.  # noqa: E501
        :type email_tos: list[str]
        """
        if self.local_vars_configuration.client_side_validation and email_tos is None:  # noqa: E501
            raise ValueError("Invalid value for `email_tos`, must not be `None`")  # noqa: E501

        self._email_tos = email_tos

    @property
    def id(self):
        """Gets the id of this AlertNotifier.  # noqa: E501


        :return: The id of this AlertNotifier.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertNotifier.


        :param id: The id of this AlertNotifier.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def language_code(self):
        """Gets the language_code of this AlertNotifier.  # noqa: E501


        :return: The language_code of this AlertNotifier.  # noqa: E501
        :rtype: NotifierLanguageCode
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this AlertNotifier.


        :param language_code: The language_code of this AlertNotifier.  # noqa: E501
        :type language_code: NotifierLanguageCode
        """

        self._language_code = language_code

    @property
    def notice_severities(self):
        """Gets the notice_severities of this AlertNotifier.  # noqa: E501


        :return: The notice_severities of this AlertNotifier.  # noqa: E501
        :rtype: list[str]
        """
        return self._notice_severities

    @notice_severities.setter
    def notice_severities(self, notice_severities):
        """Sets the notice_severities of this AlertNotifier.


        :param notice_severities: The notice_severities of this AlertNotifier.  # noqa: E501
        :type notice_severities: list[str]
        """
        if self.local_vars_configuration.client_side_validation and notice_severities is None:  # noqa: E501
            raise ValueError("Invalid value for `notice_severities`, must not be `None`")  # noqa: E501

        self._notice_severities = notice_severities

    @property
    def security_mode(self):
        """Gets the security_mode of this AlertNotifier.  # noqa: E501


        :return: The security_mode of this AlertNotifier.  # noqa: E501
        :rtype: NotifierSecurityMode
        """
        return self._security_mode

    @security_mode.setter
    def security_mode(self, security_mode):
        """Sets the security_mode of this AlertNotifier.


        :param security_mode: The security_mode of this AlertNotifier.  # noqa: E501
        :type security_mode: NotifierSecurityMode
        """

        self._security_mode = security_mode

    @property
    def smtp_server_host(self):
        """Gets the smtp_server_host of this AlertNotifier.  # noqa: E501


        :return: The smtp_server_host of this AlertNotifier.  # noqa: E501
        :rtype: str
        """
        return self._smtp_server_host

    @smtp_server_host.setter
    def smtp_server_host(self, smtp_server_host):
        """Sets the smtp_server_host of this AlertNotifier.


        :param smtp_server_host: The smtp_server_host of this AlertNotifier.  # noqa: E501
        :type smtp_server_host: str
        """

        self._smtp_server_host = smtp_server_host

    @property
    def smtp_server_port(self):
        """Gets the smtp_server_port of this AlertNotifier.  # noqa: E501


        :return: The smtp_server_port of this AlertNotifier.  # noqa: E501
        :rtype: int
        """
        return self._smtp_server_port

    @smtp_server_port.setter
    def smtp_server_port(self, smtp_server_port):
        """Sets the smtp_server_port of this AlertNotifier.


        :param smtp_server_port: The smtp_server_port of this AlertNotifier.  # noqa: E501
        :type smtp_server_port: int
        """

        self._smtp_server_port = smtp_server_port

    @property
    def username(self):
        """Gets the username of this AlertNotifier.  # noqa: E501


        :return: The username of this AlertNotifier.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AlertNotifier.


        :param username: The username of this AlertNotifier.  # noqa: E501
        :type username: str
        """

        self._username = username

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
        if not isinstance(other, AlertNotifier):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertNotifier):
            return True

        return self.to_dict() != other.to_dict()
