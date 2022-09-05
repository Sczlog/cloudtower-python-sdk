# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class EveroutePackage(object):
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
        'arch': 'Architecture',
        'description': 'str',
        'entity_async_status': 'EntityAsyncStatus',
        'id': 'str',
        'local_created_at': 'str',
        'name': 'str',
        'package_info': 'object',
        'size': 'int',
        'version': 'str'
    }

    attribute_map = {
        'arch': 'arch',
        'description': 'description',
        'entity_async_status': 'entityAsyncStatus',
        'id': 'id',
        'local_created_at': 'local_created_at',
        'name': 'name',
        'package_info': 'package_info',
        'size': 'size',
        'version': 'version'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """EveroutePackage - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._arch = None
        self._description = None
        self._entity_async_status = None
        self._id = None
        self._local_created_at = None
        self._name = None
        self._package_info = None
        self._size = None
        self._version = None
        self.discriminator = None

        if "arch" in kwargs:
            self.arch = kwargs["arch"]
        if "description" in kwargs:
            self.description = kwargs["description"]
        self.entity_async_status = kwargs.get("entity_async_status", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "local_created_at" in kwargs:
            self.local_created_at = kwargs["local_created_at"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "package_info" in kwargs:
            self.package_info = kwargs["package_info"]
        if "size" in kwargs:
            self.size = kwargs["size"]
        if "version" in kwargs:
            self.version = kwargs["version"]

    @property
    def arch(self):
        """Gets the arch of this EveroutePackage.  # noqa: E501


        :return: The arch of this EveroutePackage.  # noqa: E501
        :rtype: Architecture
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this EveroutePackage.


        :param arch: The arch of this EveroutePackage.  # noqa: E501
        :type arch: Architecture
        """
        if self.local_vars_configuration.client_side_validation and arch is None:  # noqa: E501
            raise ValueError("Invalid value for `arch`, must not be `None`")  # noqa: E501

        self._arch = arch

    @property
    def description(self):
        """Gets the description of this EveroutePackage.  # noqa: E501


        :return: The description of this EveroutePackage.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EveroutePackage.


        :param description: The description of this EveroutePackage.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this EveroutePackage.  # noqa: E501


        :return: The entity_async_status of this EveroutePackage.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this EveroutePackage.


        :param entity_async_status: The entity_async_status of this EveroutePackage.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def id(self):
        """Gets the id of this EveroutePackage.  # noqa: E501


        :return: The id of this EveroutePackage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EveroutePackage.


        :param id: The id of this EveroutePackage.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def local_created_at(self):
        """Gets the local_created_at of this EveroutePackage.  # noqa: E501


        :return: The local_created_at of this EveroutePackage.  # noqa: E501
        :rtype: str
        """
        return self._local_created_at

    @local_created_at.setter
    def local_created_at(self, local_created_at):
        """Sets the local_created_at of this EveroutePackage.


        :param local_created_at: The local_created_at of this EveroutePackage.  # noqa: E501
        :type local_created_at: str
        """
        if self.local_vars_configuration.client_side_validation and local_created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `local_created_at`, must not be `None`")  # noqa: E501

        self._local_created_at = local_created_at

    @property
    def name(self):
        """Gets the name of this EveroutePackage.  # noqa: E501


        :return: The name of this EveroutePackage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EveroutePackage.


        :param name: The name of this EveroutePackage.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def package_info(self):
        """Gets the package_info of this EveroutePackage.  # noqa: E501


        :return: The package_info of this EveroutePackage.  # noqa: E501
        :rtype: object
        """
        return self._package_info

    @package_info.setter
    def package_info(self, package_info):
        """Sets the package_info of this EveroutePackage.


        :param package_info: The package_info of this EveroutePackage.  # noqa: E501
        :type package_info: object
        """
        if self.local_vars_configuration.client_side_validation and package_info is None:  # noqa: E501
            raise ValueError("Invalid value for `package_info`, must not be `None`")  # noqa: E501

        self._package_info = package_info

    @property
    def size(self):
        """Gets the size of this EveroutePackage.  # noqa: E501


        :return: The size of this EveroutePackage.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this EveroutePackage.


        :param size: The size of this EveroutePackage.  # noqa: E501
        :type size: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def version(self):
        """Gets the version of this EveroutePackage.  # noqa: E501


        :return: The version of this EveroutePackage.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this EveroutePackage.


        :param version: The version of this EveroutePackage.  # noqa: E501
        :type version: str
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
        if not isinstance(other, EveroutePackage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EveroutePackage):
            return True

        return self.to_dict() != other.to_dict()
