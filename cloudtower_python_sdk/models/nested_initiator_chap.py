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


class NestedInitiatorChap(object):
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
        'chap_name': 'str',
        'chap_secret': 'str',
        'initiator_iqn': 'str'
    }

    attribute_map = {
        'chap_name': 'chap_name',
        'chap_secret': 'chap_secret',
        'initiator_iqn': 'initiator_iqn'
    }

    def __init__(self, chap_name=None, chap_secret=None, initiator_iqn=None, local_vars_configuration=None):  # noqa: E501
        """NestedInitiatorChap - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._chap_name = None
        self._chap_secret = None
        self._initiator_iqn = None
        self.discriminator = None

        self.chap_name = chap_name
        self.chap_secret = chap_secret
        self.initiator_iqn = initiator_iqn

    @property
    def chap_name(self):
        """Gets the chap_name of this NestedInitiatorChap.  # noqa: E501


        :return: The chap_name of this NestedInitiatorChap.  # noqa: E501
        :rtype: str
        """
        return self._chap_name

    @chap_name.setter
    def chap_name(self, chap_name):
        """Sets the chap_name of this NestedInitiatorChap.


        :param chap_name: The chap_name of this NestedInitiatorChap.  # noqa: E501
        :type chap_name: str
        """
        if self.local_vars_configuration.client_side_validation and chap_name is None:  # noqa: E501
            raise ValueError("Invalid value for `chap_name`, must not be `None`")  # noqa: E501

        self._chap_name = chap_name

    @property
    def chap_secret(self):
        """Gets the chap_secret of this NestedInitiatorChap.  # noqa: E501


        :return: The chap_secret of this NestedInitiatorChap.  # noqa: E501
        :rtype: str
        """
        return self._chap_secret

    @chap_secret.setter
    def chap_secret(self, chap_secret):
        """Sets the chap_secret of this NestedInitiatorChap.


        :param chap_secret: The chap_secret of this NestedInitiatorChap.  # noqa: E501
        :type chap_secret: str
        """
        if self.local_vars_configuration.client_side_validation and chap_secret is None:  # noqa: E501
            raise ValueError("Invalid value for `chap_secret`, must not be `None`")  # noqa: E501

        self._chap_secret = chap_secret

    @property
    def initiator_iqn(self):
        """Gets the initiator_iqn of this NestedInitiatorChap.  # noqa: E501


        :return: The initiator_iqn of this NestedInitiatorChap.  # noqa: E501
        :rtype: str
        """
        return self._initiator_iqn

    @initiator_iqn.setter
    def initiator_iqn(self, initiator_iqn):
        """Sets the initiator_iqn of this NestedInitiatorChap.


        :param initiator_iqn: The initiator_iqn of this NestedInitiatorChap.  # noqa: E501
        :type initiator_iqn: str
        """
        if self.local_vars_configuration.client_side_validation and initiator_iqn is None:  # noqa: E501
            raise ValueError("Invalid value for `initiator_iqn`, must not be `None`")  # noqa: E501

        self._initiator_iqn = initiator_iqn

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
        if not isinstance(other, NestedInitiatorChap):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedInitiatorChap):
            return True

        return self.to_dict() != other.to_dict()
