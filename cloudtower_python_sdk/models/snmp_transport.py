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


class SnmpTransport(object):
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
        'auth_pass_phrase': 'str',
        'auth_protocol': 'SnmpAuthProtocol',
        'cluster': 'NestedCluster',
        'community': 'str',
        'disabled': 'bool',
        'entity_async_status': 'EntityAsyncStatus',
        'id': 'str',
        'local_id': 'str',
        'name': 'str',
        'port': 'int',
        'privacy_pass_phrase': 'str',
        'privacy_protocol': 'SnmpPrivacyProtocol',
        'protocol': 'SnmpProtocol',
        'username': 'str',
        'version': 'SnmpVersion'
    }

    attribute_map = {
        'auth_pass_phrase': 'auth_pass_phrase',
        'auth_protocol': 'auth_protocol',
        'cluster': 'cluster',
        'community': 'community',
        'disabled': 'disabled',
        'entity_async_status': 'entityAsyncStatus',
        'id': 'id',
        'local_id': 'local_id',
        'name': 'name',
        'port': 'port',
        'privacy_pass_phrase': 'privacy_pass_phrase',
        'privacy_protocol': 'privacy_protocol',
        'protocol': 'protocol',
        'username': 'username',
        'version': 'version'
    }

    def __init__(self, auth_pass_phrase=None, auth_protocol=None, cluster=None, community=None, disabled=None, entity_async_status=None, id=None, local_id=None, name=None, port=None, privacy_pass_phrase=None, privacy_protocol=None, protocol=None, username=None, version=None, local_vars_configuration=None):  # noqa: E501
        """SnmpTransport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._auth_pass_phrase = None
        self._auth_protocol = None
        self._cluster = None
        self._community = None
        self._disabled = None
        self._entity_async_status = None
        self._id = None
        self._local_id = None
        self._name = None
        self._port = None
        self._privacy_pass_phrase = None
        self._privacy_protocol = None
        self._protocol = None
        self._username = None
        self._version = None
        self.discriminator = None

        self.auth_pass_phrase = auth_pass_phrase
        self.auth_protocol = auth_protocol
        self.cluster = cluster
        self.community = community
        self.disabled = disabled
        self.entity_async_status = entity_async_status
        self.id = id
        self.local_id = local_id
        self.name = name
        self.port = port
        self.privacy_pass_phrase = privacy_pass_phrase
        self.privacy_protocol = privacy_protocol
        self.protocol = protocol
        self.username = username
        self.version = version

    @property
    def auth_pass_phrase(self):
        """Gets the auth_pass_phrase of this SnmpTransport.  # noqa: E501


        :return: The auth_pass_phrase of this SnmpTransport.  # noqa: E501
        :rtype: str
        """
        return self._auth_pass_phrase

    @auth_pass_phrase.setter
    def auth_pass_phrase(self, auth_pass_phrase):
        """Sets the auth_pass_phrase of this SnmpTransport.


        :param auth_pass_phrase: The auth_pass_phrase of this SnmpTransport.  # noqa: E501
        :type auth_pass_phrase: str
        """

        self._auth_pass_phrase = auth_pass_phrase

    @property
    def auth_protocol(self):
        """Gets the auth_protocol of this SnmpTransport.  # noqa: E501


        :return: The auth_protocol of this SnmpTransport.  # noqa: E501
        :rtype: SnmpAuthProtocol
        """
        return self._auth_protocol

    @auth_protocol.setter
    def auth_protocol(self, auth_protocol):
        """Sets the auth_protocol of this SnmpTransport.


        :param auth_protocol: The auth_protocol of this SnmpTransport.  # noqa: E501
        :type auth_protocol: SnmpAuthProtocol
        """

        self._auth_protocol = auth_protocol

    @property
    def cluster(self):
        """Gets the cluster of this SnmpTransport.  # noqa: E501


        :return: The cluster of this SnmpTransport.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this SnmpTransport.


        :param cluster: The cluster of this SnmpTransport.  # noqa: E501
        :type cluster: NestedCluster
        """
        if self.local_vars_configuration.client_side_validation and cluster is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster`, must not be `None`")  # noqa: E501

        self._cluster = cluster

    @property
    def community(self):
        """Gets the community of this SnmpTransport.  # noqa: E501


        :return: The community of this SnmpTransport.  # noqa: E501
        :rtype: str
        """
        return self._community

    @community.setter
    def community(self, community):
        """Sets the community of this SnmpTransport.


        :param community: The community of this SnmpTransport.  # noqa: E501
        :type community: str
        """

        self._community = community

    @property
    def disabled(self):
        """Gets the disabled of this SnmpTransport.  # noqa: E501


        :return: The disabled of this SnmpTransport.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this SnmpTransport.


        :param disabled: The disabled of this SnmpTransport.  # noqa: E501
        :type disabled: bool
        """
        if self.local_vars_configuration.client_side_validation and disabled is None:  # noqa: E501
            raise ValueError("Invalid value for `disabled`, must not be `None`")  # noqa: E501

        self._disabled = disabled

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this SnmpTransport.  # noqa: E501


        :return: The entity_async_status of this SnmpTransport.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this SnmpTransport.


        :param entity_async_status: The entity_async_status of this SnmpTransport.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def id(self):
        """Gets the id of this SnmpTransport.  # noqa: E501


        :return: The id of this SnmpTransport.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SnmpTransport.


        :param id: The id of this SnmpTransport.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def local_id(self):
        """Gets the local_id of this SnmpTransport.  # noqa: E501


        :return: The local_id of this SnmpTransport.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this SnmpTransport.


        :param local_id: The local_id of this SnmpTransport.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def name(self):
        """Gets the name of this SnmpTransport.  # noqa: E501


        :return: The name of this SnmpTransport.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SnmpTransport.


        :param name: The name of this SnmpTransport.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def port(self):
        """Gets the port of this SnmpTransport.  # noqa: E501


        :return: The port of this SnmpTransport.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SnmpTransport.


        :param port: The port of this SnmpTransport.  # noqa: E501
        :type port: int
        """
        if self.local_vars_configuration.client_side_validation and port is None:  # noqa: E501
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def privacy_pass_phrase(self):
        """Gets the privacy_pass_phrase of this SnmpTransport.  # noqa: E501


        :return: The privacy_pass_phrase of this SnmpTransport.  # noqa: E501
        :rtype: str
        """
        return self._privacy_pass_phrase

    @privacy_pass_phrase.setter
    def privacy_pass_phrase(self, privacy_pass_phrase):
        """Sets the privacy_pass_phrase of this SnmpTransport.


        :param privacy_pass_phrase: The privacy_pass_phrase of this SnmpTransport.  # noqa: E501
        :type privacy_pass_phrase: str
        """

        self._privacy_pass_phrase = privacy_pass_phrase

    @property
    def privacy_protocol(self):
        """Gets the privacy_protocol of this SnmpTransport.  # noqa: E501


        :return: The privacy_protocol of this SnmpTransport.  # noqa: E501
        :rtype: SnmpPrivacyProtocol
        """
        return self._privacy_protocol

    @privacy_protocol.setter
    def privacy_protocol(self, privacy_protocol):
        """Sets the privacy_protocol of this SnmpTransport.


        :param privacy_protocol: The privacy_protocol of this SnmpTransport.  # noqa: E501
        :type privacy_protocol: SnmpPrivacyProtocol
        """

        self._privacy_protocol = privacy_protocol

    @property
    def protocol(self):
        """Gets the protocol of this SnmpTransport.  # noqa: E501


        :return: The protocol of this SnmpTransport.  # noqa: E501
        :rtype: SnmpProtocol
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this SnmpTransport.


        :param protocol: The protocol of this SnmpTransport.  # noqa: E501
        :type protocol: SnmpProtocol
        """
        if self.local_vars_configuration.client_side_validation and protocol is None:  # noqa: E501
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self._protocol = protocol

    @property
    def username(self):
        """Gets the username of this SnmpTransport.  # noqa: E501


        :return: The username of this SnmpTransport.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SnmpTransport.


        :param username: The username of this SnmpTransport.  # noqa: E501
        :type username: str
        """

        self._username = username

    @property
    def version(self):
        """Gets the version of this SnmpTransport.  # noqa: E501


        :return: The version of this SnmpTransport.  # noqa: E501
        :rtype: SnmpVersion
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SnmpTransport.


        :param version: The version of this SnmpTransport.  # noqa: E501
        :type version: SnmpVersion
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, SnmpTransport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnmpTransport):
            return True

        return self.to_dict() != other.to_dict()
