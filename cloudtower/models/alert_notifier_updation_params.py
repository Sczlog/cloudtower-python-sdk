# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class AlertNotifierUpdationParams(object):
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
        'notice_severities': 'list[str]',
        'language_code': 'NotifierLanguageCode',
        'email_tos': 'list[str]',
        'email_from': 'str',
        'disabled': 'bool'
    }

    attribute_map = {
        'notice_severities': 'notice_severities',
        'language_code': 'language_code',
        'email_tos': 'email_tos',
        'email_from': 'email_from',
        'disabled': 'disabled'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """AlertNotifierUpdationParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._notice_severities = None
        self._language_code = None
        self._email_tos = None
        self._email_from = None
        self._disabled = None
        self.discriminator = None

        if "notice_severities" in kwargs:
            self.notice_severities = kwargs["notice_severities"]
        if "language_code" in kwargs:
            self.language_code = kwargs["language_code"]
        if "email_tos" in kwargs:
            self.email_tos = kwargs["email_tos"]
        if "email_from" in kwargs:
            self.email_from = kwargs["email_from"]
        if "disabled" in kwargs:
            self.disabled = kwargs["disabled"]

    @property
    def notice_severities(self):
        """Gets the notice_severities of this AlertNotifierUpdationParams.  # noqa: E501


        :return: The notice_severities of this AlertNotifierUpdationParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._notice_severities

    @notice_severities.setter
    def notice_severities(self, notice_severities):
        """Sets the notice_severities of this AlertNotifierUpdationParams.


        :param notice_severities: The notice_severities of this AlertNotifierUpdationParams.  # noqa: E501
        :type notice_severities: list[str]
        """
        allowed_values = ["CRITICAL", "NOTICE", "INFO"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(notice_severities).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `notice_severities` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(notice_severities) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._notice_severities = notice_severities

    @property
    def language_code(self):
        """Gets the language_code of this AlertNotifierUpdationParams.  # noqa: E501


        :return: The language_code of this AlertNotifierUpdationParams.  # noqa: E501
        :rtype: NotifierLanguageCode
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this AlertNotifierUpdationParams.


        :param language_code: The language_code of this AlertNotifierUpdationParams.  # noqa: E501
        :type language_code: NotifierLanguageCode
        """

        self._language_code = language_code

    @property
    def email_tos(self):
        """Gets the email_tos of this AlertNotifierUpdationParams.  # noqa: E501


        :return: The email_tos of this AlertNotifierUpdationParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_tos

    @email_tos.setter
    def email_tos(self, email_tos):
        """Sets the email_tos of this AlertNotifierUpdationParams.


        :param email_tos: The email_tos of this AlertNotifierUpdationParams.  # noqa: E501
        :type email_tos: list[str]
        """

        self._email_tos = email_tos

    @property
    def email_from(self):
        """Gets the email_from of this AlertNotifierUpdationParams.  # noqa: E501


        :return: The email_from of this AlertNotifierUpdationParams.  # noqa: E501
        :rtype: str
        """
        return self._email_from

    @email_from.setter
    def email_from(self, email_from):
        """Sets the email_from of this AlertNotifierUpdationParams.


        :param email_from: The email_from of this AlertNotifierUpdationParams.  # noqa: E501
        :type email_from: str
        """

        self._email_from = email_from

    @property
    def disabled(self):
        """Gets the disabled of this AlertNotifierUpdationParams.  # noqa: E501


        :return: The disabled of this AlertNotifierUpdationParams.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this AlertNotifierUpdationParams.


        :param disabled: The disabled of this AlertNotifierUpdationParams.  # noqa: E501
        :type disabled: bool
        """

        self._disabled = disabled

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
        if not isinstance(other, AlertNotifierUpdationParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertNotifierUpdationParams):
            return True

        return self.to_dict() != other.to_dict()
