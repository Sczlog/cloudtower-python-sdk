# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class NestedSecurityPolicyApply(object):
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
        'communicable': 'bool',
        'security_group': 'NestedSecurityGroup',
        'security_group_id': 'str',
        'selector': 'list[NestedLabel]',
        'selector_ids': 'list[str]'
    }

    attribute_map = {
        'communicable': 'communicable',
        'security_group': 'security_group',
        'security_group_id': 'security_group_id',
        'selector': 'selector',
        'selector_ids': 'selector_ids'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedSecurityPolicyApply - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._communicable = None
        self._security_group = None
        self._security_group_id = None
        self._selector = None
        self._selector_ids = None
        self.discriminator = None

        if "communicable" in kwargs:
            self.communicable = kwargs["communicable"]
        self.security_group = kwargs.get("security_group", None)
        self.security_group_id = kwargs.get("security_group_id", None)
        if "selector" in kwargs:
            self.selector = kwargs["selector"]
        if "selector_ids" in kwargs:
            self.selector_ids = kwargs["selector_ids"]

    @property
    def communicable(self):
        """Gets the communicable of this NestedSecurityPolicyApply.  # noqa: E501


        :return: The communicable of this NestedSecurityPolicyApply.  # noqa: E501
        :rtype: bool
        """
        return self._communicable

    @communicable.setter
    def communicable(self, communicable):
        """Sets the communicable of this NestedSecurityPolicyApply.


        :param communicable: The communicable of this NestedSecurityPolicyApply.  # noqa: E501
        :type communicable: bool
        """
        if self.local_vars_configuration.client_side_validation and communicable is None:  # noqa: E501
            raise ValueError("Invalid value for `communicable`, must not be `None`")  # noqa: E501

        self._communicable = communicable

    @property
    def security_group(self):
        """Gets the security_group of this NestedSecurityPolicyApply.  # noqa: E501


        :return: The security_group of this NestedSecurityPolicyApply.  # noqa: E501
        :rtype: NestedSecurityGroup
        """
        return self._security_group

    @security_group.setter
    def security_group(self, security_group):
        """Sets the security_group of this NestedSecurityPolicyApply.


        :param security_group: The security_group of this NestedSecurityPolicyApply.  # noqa: E501
        :type security_group: NestedSecurityGroup
        """

        self._security_group = security_group

    @property
    def security_group_id(self):
        """Gets the security_group_id of this NestedSecurityPolicyApply.  # noqa: E501


        :return: The security_group_id of this NestedSecurityPolicyApply.  # noqa: E501
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this NestedSecurityPolicyApply.


        :param security_group_id: The security_group_id of this NestedSecurityPolicyApply.  # noqa: E501
        :type security_group_id: str
        """

        self._security_group_id = security_group_id

    @property
    def selector(self):
        """Gets the selector of this NestedSecurityPolicyApply.  # noqa: E501


        :return: The selector of this NestedSecurityPolicyApply.  # noqa: E501
        :rtype: list[NestedLabel]
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this NestedSecurityPolicyApply.


        :param selector: The selector of this NestedSecurityPolicyApply.  # noqa: E501
        :type selector: list[NestedLabel]
        """
        if self.local_vars_configuration.client_side_validation and selector is None:  # noqa: E501
            raise ValueError("Invalid value for `selector`, must not be `None`")  # noqa: E501

        self._selector = selector

    @property
    def selector_ids(self):
        """Gets the selector_ids of this NestedSecurityPolicyApply.  # noqa: E501


        :return: The selector_ids of this NestedSecurityPolicyApply.  # noqa: E501
        :rtype: list[str]
        """
        return self._selector_ids

    @selector_ids.setter
    def selector_ids(self, selector_ids):
        """Sets the selector_ids of this NestedSecurityPolicyApply.


        :param selector_ids: The selector_ids of this NestedSecurityPolicyApply.  # noqa: E501
        :type selector_ids: list[str]
        """
        if self.local_vars_configuration.client_side_validation and selector_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `selector_ids`, must not be `None`")  # noqa: E501

        self._selector_ids = selector_ids

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
        if not isinstance(other, NestedSecurityPolicyApply):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedSecurityPolicyApply):
            return True

        return self.to_dict() != other.to_dict()
