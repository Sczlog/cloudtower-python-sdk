# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 1.9.0
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


class ClusterCreationParams(object):
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
        'datacenter_id': 'str',
        'secondary_zone_datacenter_id': 'str',
        'primary_zone_datacenter_id': 'str',
        'password': 'str',
        'username': 'str',
        'ip': 'str'
    }

    attribute_map = {
        'datacenter_id': 'datacenter_id',
        'secondary_zone_datacenter_id': 'secondary_zone_datacenter_id',
        'primary_zone_datacenter_id': 'primary_zone_datacenter_id',
        'password': 'password',
        'username': 'username',
        'ip': 'ip'
    }

    def __init__(self, datacenter_id=None, secondary_zone_datacenter_id=None, primary_zone_datacenter_id=None, password=None, username=None, ip=None, local_vars_configuration=None):  # noqa: E501
        """ClusterCreationParams - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._datacenter_id = None
        self._secondary_zone_datacenter_id = None
        self._primary_zone_datacenter_id = None
        self._password = None
        self._username = None
        self._ip = None
        self.discriminator = None

        if datacenter_id is not None:
            self.datacenter_id = datacenter_id
        if secondary_zone_datacenter_id is not None:
            self.secondary_zone_datacenter_id = secondary_zone_datacenter_id
        if primary_zone_datacenter_id is not None:
            self.primary_zone_datacenter_id = primary_zone_datacenter_id
        self.password = password
        self.username = username
        self.ip = ip

    @property
    def datacenter_id(self):
        """Gets the datacenter_id of this ClusterCreationParams.  # noqa: E501


        :return: The datacenter_id of this ClusterCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._datacenter_id

    @datacenter_id.setter
    def datacenter_id(self, datacenter_id):
        """Sets the datacenter_id of this ClusterCreationParams.


        :param datacenter_id: The datacenter_id of this ClusterCreationParams.  # noqa: E501
        :type datacenter_id: str
        """

        self._datacenter_id = datacenter_id

    @property
    def secondary_zone_datacenter_id(self):
        """Gets the secondary_zone_datacenter_id of this ClusterCreationParams.  # noqa: E501


        :return: The secondary_zone_datacenter_id of this ClusterCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._secondary_zone_datacenter_id

    @secondary_zone_datacenter_id.setter
    def secondary_zone_datacenter_id(self, secondary_zone_datacenter_id):
        """Sets the secondary_zone_datacenter_id of this ClusterCreationParams.


        :param secondary_zone_datacenter_id: The secondary_zone_datacenter_id of this ClusterCreationParams.  # noqa: E501
        :type secondary_zone_datacenter_id: str
        """

        self._secondary_zone_datacenter_id = secondary_zone_datacenter_id

    @property
    def primary_zone_datacenter_id(self):
        """Gets the primary_zone_datacenter_id of this ClusterCreationParams.  # noqa: E501


        :return: The primary_zone_datacenter_id of this ClusterCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._primary_zone_datacenter_id

    @primary_zone_datacenter_id.setter
    def primary_zone_datacenter_id(self, primary_zone_datacenter_id):
        """Sets the primary_zone_datacenter_id of this ClusterCreationParams.


        :param primary_zone_datacenter_id: The primary_zone_datacenter_id of this ClusterCreationParams.  # noqa: E501
        :type primary_zone_datacenter_id: str
        """

        self._primary_zone_datacenter_id = primary_zone_datacenter_id

    @property
    def password(self):
        """Gets the password of this ClusterCreationParams.  # noqa: E501


        :return: The password of this ClusterCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ClusterCreationParams.


        :param password: The password of this ClusterCreationParams.  # noqa: E501
        :type password: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def username(self):
        """Gets the username of this ClusterCreationParams.  # noqa: E501


        :return: The username of this ClusterCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ClusterCreationParams.


        :param username: The username of this ClusterCreationParams.  # noqa: E501
        :type username: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def ip(self):
        """Gets the ip of this ClusterCreationParams.  # noqa: E501


        :return: The ip of this ClusterCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ClusterCreationParams.


        :param ip: The ip of this ClusterCreationParams.  # noqa: E501
        :type ip: str
        """
        if self.local_vars_configuration.client_side_validation and ip is None:  # noqa: E501
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

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
        if not isinstance(other, ClusterCreationParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterCreationParams):
            return True

        return self.to_dict() != other.to_dict()
