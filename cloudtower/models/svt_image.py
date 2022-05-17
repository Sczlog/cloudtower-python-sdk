# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 1.10.0
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


class SvtImage(object):
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
        'cluster': 'NestedCluster',
        'entity_async_status': 'EntityAsyncStatus',
        'id': 'str',
        'local_created_at': 'str',
        'local_id': 'str',
        'name': 'str',
        'path': 'str',
        'size': 'int',
        'version': 'int',
        'vm_disks': 'list[NestedVmDisk]'
    }

    attribute_map = {
        'cluster': 'cluster',
        'entity_async_status': 'entityAsyncStatus',
        'id': 'id',
        'local_created_at': 'local_created_at',
        'local_id': 'local_id',
        'name': 'name',
        'path': 'path',
        'size': 'size',
        'version': 'version',
        'vm_disks': 'vm_disks'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """SvtImage - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._cluster = None
        self._entity_async_status = None
        self._id = None
        self._local_created_at = None
        self._local_id = None
        self._name = None
        self._path = None
        self._size = None
        self._version = None
        self._vm_disks = None
        self.discriminator = None

        if "cluster" in kwargs:
            self.cluster = kwargs["cluster"]
        self.entity_async_status = kwargs.get("entity_async_status", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "local_created_at" in kwargs:
            self.local_created_at = kwargs["local_created_at"]
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "path" in kwargs:
            self.path = kwargs["path"]
        if "size" in kwargs:
            self.size = kwargs["size"]
        if "version" in kwargs:
            self.version = kwargs["version"]
        self.vm_disks = kwargs.get("vm_disks", None)

    @property
    def cluster(self):
        """Gets the cluster of this SvtImage.  # noqa: E501


        :return: The cluster of this SvtImage.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this SvtImage.


        :param cluster: The cluster of this SvtImage.  # noqa: E501
        :type cluster: NestedCluster
        """
        if self.local_vars_configuration.client_side_validation and cluster is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster`, must not be `None`")  # noqa: E501

        self._cluster = cluster

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this SvtImage.  # noqa: E501


        :return: The entity_async_status of this SvtImage.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this SvtImage.


        :param entity_async_status: The entity_async_status of this SvtImage.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def id(self):
        """Gets the id of this SvtImage.  # noqa: E501


        :return: The id of this SvtImage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SvtImage.


        :param id: The id of this SvtImage.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def local_created_at(self):
        """Gets the local_created_at of this SvtImage.  # noqa: E501


        :return: The local_created_at of this SvtImage.  # noqa: E501
        :rtype: str
        """
        return self._local_created_at

    @local_created_at.setter
    def local_created_at(self, local_created_at):
        """Sets the local_created_at of this SvtImage.


        :param local_created_at: The local_created_at of this SvtImage.  # noqa: E501
        :type local_created_at: str
        """
        if self.local_vars_configuration.client_side_validation and local_created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `local_created_at`, must not be `None`")  # noqa: E501

        self._local_created_at = local_created_at

    @property
    def local_id(self):
        """Gets the local_id of this SvtImage.  # noqa: E501


        :return: The local_id of this SvtImage.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this SvtImage.


        :param local_id: The local_id of this SvtImage.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def name(self):
        """Gets the name of this SvtImage.  # noqa: E501


        :return: The name of this SvtImage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SvtImage.


        :param name: The name of this SvtImage.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def path(self):
        """Gets the path of this SvtImage.  # noqa: E501


        :return: The path of this SvtImage.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SvtImage.


        :param path: The path of this SvtImage.  # noqa: E501
        :type path: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def size(self):
        """Gets the size of this SvtImage.  # noqa: E501


        :return: The size of this SvtImage.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SvtImage.


        :param size: The size of this SvtImage.  # noqa: E501
        :type size: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def version(self):
        """Gets the version of this SvtImage.  # noqa: E501


        :return: The version of this SvtImage.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SvtImage.


        :param version: The version of this SvtImage.  # noqa: E501
        :type version: int
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def vm_disks(self):
        """Gets the vm_disks of this SvtImage.  # noqa: E501


        :return: The vm_disks of this SvtImage.  # noqa: E501
        :rtype: list[NestedVmDisk]
        """
        return self._vm_disks

    @vm_disks.setter
    def vm_disks(self, vm_disks):
        """Sets the vm_disks of this SvtImage.


        :param vm_disks: The vm_disks of this SvtImage.  # noqa: E501
        :type vm_disks: list[NestedVmDisk]
        """

        self._vm_disks = vm_disks

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
        if not isinstance(other, SvtImage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SvtImage):
            return True

        return self.to_dict() != other.to_dict()
