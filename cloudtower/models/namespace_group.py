# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Contact: info@smartx.com
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


class NamespaceGroup(object):
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
        'entity_async_status': 'EntityAsyncStatus',
        'id': 'str',
        'labels': 'list[NestedLabel]',
        'local_create_time': 'str',
        'local_id': 'str',
        'name': 'str',
        'namespaces': 'list[NestedNvmfNamespace]',
        'nvmf_subsystem': 'NestedNvmfSubsystem'
    }

    attribute_map = {
        'entity_async_status': 'entityAsyncStatus',
        'id': 'id',
        'labels': 'labels',
        'local_create_time': 'local_create_time',
        'local_id': 'local_id',
        'name': 'name',
        'namespaces': 'namespaces',
        'nvmf_subsystem': 'nvmf_subsystem'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NamespaceGroup - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._entity_async_status = None
        self._id = None
        self._labels = None
        self._local_create_time = None
        self._local_id = None
        self._name = None
        self._namespaces = None
        self._nvmf_subsystem = None
        self.discriminator = None

        self.entity_async_status = kwargs.get("entity_async_status", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        self.labels = kwargs.get("labels", None)
        if "local_create_time" in kwargs:
            self.local_create_time = kwargs["local_create_time"]
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        self.namespaces = kwargs.get("namespaces", None)
        if "nvmf_subsystem" in kwargs:
            self.nvmf_subsystem = kwargs["nvmf_subsystem"]

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this NamespaceGroup.  # noqa: E501


        :return: The entity_async_status of this NamespaceGroup.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this NamespaceGroup.


        :param entity_async_status: The entity_async_status of this NamespaceGroup.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def id(self):
        """Gets the id of this NamespaceGroup.  # noqa: E501


        :return: The id of this NamespaceGroup.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NamespaceGroup.


        :param id: The id of this NamespaceGroup.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def labels(self):
        """Gets the labels of this NamespaceGroup.  # noqa: E501


        :return: The labels of this NamespaceGroup.  # noqa: E501
        :rtype: list[NestedLabel]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this NamespaceGroup.


        :param labels: The labels of this NamespaceGroup.  # noqa: E501
        :type labels: list[NestedLabel]
        """

        self._labels = labels

    @property
    def local_create_time(self):
        """Gets the local_create_time of this NamespaceGroup.  # noqa: E501


        :return: The local_create_time of this NamespaceGroup.  # noqa: E501
        :rtype: str
        """
        return self._local_create_time

    @local_create_time.setter
    def local_create_time(self, local_create_time):
        """Sets the local_create_time of this NamespaceGroup.


        :param local_create_time: The local_create_time of this NamespaceGroup.  # noqa: E501
        :type local_create_time: str
        """
        if self.local_vars_configuration.client_side_validation and local_create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `local_create_time`, must not be `None`")  # noqa: E501

        self._local_create_time = local_create_time

    @property
    def local_id(self):
        """Gets the local_id of this NamespaceGroup.  # noqa: E501


        :return: The local_id of this NamespaceGroup.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this NamespaceGroup.


        :param local_id: The local_id of this NamespaceGroup.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def name(self):
        """Gets the name of this NamespaceGroup.  # noqa: E501


        :return: The name of this NamespaceGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NamespaceGroup.


        :param name: The name of this NamespaceGroup.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespaces(self):
        """Gets the namespaces of this NamespaceGroup.  # noqa: E501


        :return: The namespaces of this NamespaceGroup.  # noqa: E501
        :rtype: list[NestedNvmfNamespace]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this NamespaceGroup.


        :param namespaces: The namespaces of this NamespaceGroup.  # noqa: E501
        :type namespaces: list[NestedNvmfNamespace]
        """

        self._namespaces = namespaces

    @property
    def nvmf_subsystem(self):
        """Gets the nvmf_subsystem of this NamespaceGroup.  # noqa: E501


        :return: The nvmf_subsystem of this NamespaceGroup.  # noqa: E501
        :rtype: NestedNvmfSubsystem
        """
        return self._nvmf_subsystem

    @nvmf_subsystem.setter
    def nvmf_subsystem(self, nvmf_subsystem):
        """Sets the nvmf_subsystem of this NamespaceGroup.


        :param nvmf_subsystem: The nvmf_subsystem of this NamespaceGroup.  # noqa: E501
        :type nvmf_subsystem: NestedNvmfSubsystem
        """
        if self.local_vars_configuration.client_side_validation and nvmf_subsystem is None:  # noqa: E501
            raise ValueError("Invalid value for `nvmf_subsystem`, must not be `None`")  # noqa: E501

        self._nvmf_subsystem = nvmf_subsystem

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
        if not isinstance(other, NamespaceGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NamespaceGroup):
            return True

        return self.to_dict() != other.to_dict()
