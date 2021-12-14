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


class UserRoleNextWhereInput(object):
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
        '_and': 'list[UserRoleNextWhereInput]',
        'id': 'str',
        'id_contains': 'str',
        'id_ends_with': 'str',
        'id_gt': 'str',
        'id_gte': 'str',
        'id_in': 'list[str]',
        'id_lt': 'str',
        'id_lte': 'str',
        'id_not': 'str',
        'id_not_contains': 'str',
        'id_not_ends_with': 'str',
        'id_not_in': 'list[str]',
        'id_not_starts_with': 'str',
        'id_starts_with': 'str',
        'name': 'str',
        'name_contains': 'str',
        'name_ends_with': 'str',
        'name_gt': 'str',
        'name_gte': 'str',
        'name_in': 'list[str]',
        'name_lt': 'str',
        'name_lte': 'str',
        'name_not': 'str',
        'name_not_contains': 'str',
        'name_not_ends_with': 'str',
        'name_not_in': 'list[str]',
        'name_not_starts_with': 'str',
        'name_starts_with': 'str',
        '_not': 'list[UserRoleNextWhereInput]',
        '_or': 'list[UserRoleNextWhereInput]',
        'platform': 'UserRolePlatform',
        'platform_in': 'list[UserRolePlatform]',
        'platform_not': 'UserRolePlatform',
        'platform_not_in': 'list[UserRolePlatform]',
        'preset': 'UserRolePreset',
        'preset_in': 'list[UserRolePreset]',
        'preset_not': 'UserRolePreset',
        'preset_not_in': 'list[UserRolePreset]',
        'users_every': 'UserWhereInput',
        'users_none': 'UserWhereInput',
        'users_some': 'UserWhereInput'
    }

    attribute_map = {
        '_and': 'AND',
        'id': 'id',
        'id_contains': 'id_contains',
        'id_ends_with': 'id_ends_with',
        'id_gt': 'id_gt',
        'id_gte': 'id_gte',
        'id_in': 'id_in',
        'id_lt': 'id_lt',
        'id_lte': 'id_lte',
        'id_not': 'id_not',
        'id_not_contains': 'id_not_contains',
        'id_not_ends_with': 'id_not_ends_with',
        'id_not_in': 'id_not_in',
        'id_not_starts_with': 'id_not_starts_with',
        'id_starts_with': 'id_starts_with',
        'name': 'name',
        'name_contains': 'name_contains',
        'name_ends_with': 'name_ends_with',
        'name_gt': 'name_gt',
        'name_gte': 'name_gte',
        'name_in': 'name_in',
        'name_lt': 'name_lt',
        'name_lte': 'name_lte',
        'name_not': 'name_not',
        'name_not_contains': 'name_not_contains',
        'name_not_ends_with': 'name_not_ends_with',
        'name_not_in': 'name_not_in',
        'name_not_starts_with': 'name_not_starts_with',
        'name_starts_with': 'name_starts_with',
        '_not': 'NOT',
        '_or': 'OR',
        'platform': 'platform',
        'platform_in': 'platform_in',
        'platform_not': 'platform_not',
        'platform_not_in': 'platform_not_in',
        'preset': 'preset',
        'preset_in': 'preset_in',
        'preset_not': 'preset_not',
        'preset_not_in': 'preset_not_in',
        'users_every': 'users_every',
        'users_none': 'users_none',
        'users_some': 'users_some'
    }

    def __init__(self, _and=None, id=None, id_contains=None, id_ends_with=None, id_gt=None, id_gte=None, id_in=None, id_lt=None, id_lte=None, id_not=None, id_not_contains=None, id_not_ends_with=None, id_not_in=None, id_not_starts_with=None, id_starts_with=None, name=None, name_contains=None, name_ends_with=None, name_gt=None, name_gte=None, name_in=None, name_lt=None, name_lte=None, name_not=None, name_not_contains=None, name_not_ends_with=None, name_not_in=None, name_not_starts_with=None, name_starts_with=None, _not=None, _or=None, platform=None, platform_in=None, platform_not=None, platform_not_in=None, preset=None, preset_in=None, preset_not=None, preset_not_in=None, users_every=None, users_none=None, users_some=None, local_vars_configuration=None):  # noqa: E501
        """UserRoleNextWhereInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self.__and = None
        self._id = None
        self._id_contains = None
        self._id_ends_with = None
        self._id_gt = None
        self._id_gte = None
        self._id_in = None
        self._id_lt = None
        self._id_lte = None
        self._id_not = None
        self._id_not_contains = None
        self._id_not_ends_with = None
        self._id_not_in = None
        self._id_not_starts_with = None
        self._id_starts_with = None
        self._name = None
        self._name_contains = None
        self._name_ends_with = None
        self._name_gt = None
        self._name_gte = None
        self._name_in = None
        self._name_lt = None
        self._name_lte = None
        self._name_not = None
        self._name_not_contains = None
        self._name_not_ends_with = None
        self._name_not_in = None
        self._name_not_starts_with = None
        self._name_starts_with = None
        self.__not = None
        self.__or = None
        self._platform = None
        self._platform_in = None
        self._platform_not = None
        self._platform_not_in = None
        self._preset = None
        self._preset_in = None
        self._preset_not = None
        self._preset_not_in = None
        self._users_every = None
        self._users_none = None
        self._users_some = None
        self.discriminator = None

        self._and = _and
        self.id = id
        self.id_contains = id_contains
        self.id_ends_with = id_ends_with
        self.id_gt = id_gt
        self.id_gte = id_gte
        self.id_in = id_in
        self.id_lt = id_lt
        self.id_lte = id_lte
        self.id_not = id_not
        self.id_not_contains = id_not_contains
        self.id_not_ends_with = id_not_ends_with
        self.id_not_in = id_not_in
        self.id_not_starts_with = id_not_starts_with
        self.id_starts_with = id_starts_with
        self.name = name
        self.name_contains = name_contains
        self.name_ends_with = name_ends_with
        self.name_gt = name_gt
        self.name_gte = name_gte
        self.name_in = name_in
        self.name_lt = name_lt
        self.name_lte = name_lte
        self.name_not = name_not
        self.name_not_contains = name_not_contains
        self.name_not_ends_with = name_not_ends_with
        self.name_not_in = name_not_in
        self.name_not_starts_with = name_not_starts_with
        self.name_starts_with = name_starts_with
        self._not = _not
        self._or = _or
        self.platform = platform
        self.platform_in = platform_in
        self.platform_not = platform_not
        self.platform_not_in = platform_not_in
        self.preset = preset
        self.preset_in = preset_in
        self.preset_not = preset_not
        self.preset_not_in = preset_not_in
        self.users_every = users_every
        self.users_none = users_none
        self.users_some = users_some

    @property
    def _and(self):
        """Gets the _and of this UserRoleNextWhereInput.  # noqa: E501


        :return: The _and of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: list[UserRoleNextWhereInput]
        """
        return self.__and

    @_and.setter
    def _and(self, _and):
        """Sets the _and of this UserRoleNextWhereInput.


        :param _and: The _and of this UserRoleNextWhereInput.  # noqa: E501
        :type _and: list[UserRoleNextWhereInput]
        """

        self.__and = _and

    @property
    def id(self):
        """Gets the id of this UserRoleNextWhereInput.  # noqa: E501


        :return: The id of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserRoleNextWhereInput.


        :param id: The id of this UserRoleNextWhereInput.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def id_contains(self):
        """Gets the id_contains of this UserRoleNextWhereInput.  # noqa: E501


        :return: The id_contains of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_contains

    @id_contains.setter
    def id_contains(self, id_contains):
        """Sets the id_contains of this UserRoleNextWhereInput.


        :param id_contains: The id_contains of this UserRoleNextWhereInput.  # noqa: E501
        :type id_contains: str
        """

        self._id_contains = id_contains

    @property
    def id_ends_with(self):
        """Gets the id_ends_with of this UserRoleNextWhereInput.  # noqa: E501


        :return: The id_ends_with of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_ends_with

    @id_ends_with.setter
    def id_ends_with(self, id_ends_with):
        """Sets the id_ends_with of this UserRoleNextWhereInput.


        :param id_ends_with: The id_ends_with of this UserRoleNextWhereInput.  # noqa: E501
        :type id_ends_with: str
        """

        self._id_ends_with = id_ends_with

    @property
    def id_gt(self):
        """Gets the id_gt of this UserRoleNextWhereInput.  # noqa: E501


        :return: The id_gt of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_gt

    @id_gt.setter
    def id_gt(self, id_gt):
        """Sets the id_gt of this UserRoleNextWhereInput.


        :param id_gt: The id_gt of this UserRoleNextWhereInput.  # noqa: E501
        :type id_gt: str
        """

        self._id_gt = id_gt

    @property
    def id_gte(self):
        """Gets the id_gte of this UserRoleNextWhereInput.  # noqa: E501


        :return: The id_gte of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_gte

    @id_gte.setter
    def id_gte(self, id_gte):
        """Sets the id_gte of this UserRoleNextWhereInput.


        :param id_gte: The id_gte of this UserRoleNextWhereInput.  # noqa: E501
        :type id_gte: str
        """

        self._id_gte = id_gte

    @property
    def id_in(self):
        """Gets the id_in of this UserRoleNextWhereInput.  # noqa: E501


        :return: The id_in of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._id_in

    @id_in.setter
    def id_in(self, id_in):
        """Sets the id_in of this UserRoleNextWhereInput.


        :param id_in: The id_in of this UserRoleNextWhereInput.  # noqa: E501
        :type id_in: list[str]
        """

        self._id_in = id_in

    @property
    def id_lt(self):
        """Gets the id_lt of this UserRoleNextWhereInput.  # noqa: E501


        :return: The id_lt of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_lt

    @id_lt.setter
    def id_lt(self, id_lt):
        """Sets the id_lt of this UserRoleNextWhereInput.


        :param id_lt: The id_lt of this UserRoleNextWhereInput.  # noqa: E501
        :type id_lt: str
        """

        self._id_lt = id_lt

    @property
    def id_lte(self):
        """Gets the id_lte of this UserRoleNextWhereInput.  # noqa: E501


        :return: The id_lte of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_lte

    @id_lte.setter
    def id_lte(self, id_lte):
        """Sets the id_lte of this UserRoleNextWhereInput.


        :param id_lte: The id_lte of this UserRoleNextWhereInput.  # noqa: E501
        :type id_lte: str
        """

        self._id_lte = id_lte

    @property
    def id_not(self):
        """Gets the id_not of this UserRoleNextWhereInput.  # noqa: E501


        :return: The id_not of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not

    @id_not.setter
    def id_not(self, id_not):
        """Sets the id_not of this UserRoleNextWhereInput.


        :param id_not: The id_not of this UserRoleNextWhereInput.  # noqa: E501
        :type id_not: str
        """

        self._id_not = id_not

    @property
    def id_not_contains(self):
        """Gets the id_not_contains of this UserRoleNextWhereInput.  # noqa: E501


        :return: The id_not_contains of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not_contains

    @id_not_contains.setter
    def id_not_contains(self, id_not_contains):
        """Sets the id_not_contains of this UserRoleNextWhereInput.


        :param id_not_contains: The id_not_contains of this UserRoleNextWhereInput.  # noqa: E501
        :type id_not_contains: str
        """

        self._id_not_contains = id_not_contains

    @property
    def id_not_ends_with(self):
        """Gets the id_not_ends_with of this UserRoleNextWhereInput.  # noqa: E501


        :return: The id_not_ends_with of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not_ends_with

    @id_not_ends_with.setter
    def id_not_ends_with(self, id_not_ends_with):
        """Sets the id_not_ends_with of this UserRoleNextWhereInput.


        :param id_not_ends_with: The id_not_ends_with of this UserRoleNextWhereInput.  # noqa: E501
        :type id_not_ends_with: str
        """

        self._id_not_ends_with = id_not_ends_with

    @property
    def id_not_in(self):
        """Gets the id_not_in of this UserRoleNextWhereInput.  # noqa: E501


        :return: The id_not_in of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._id_not_in

    @id_not_in.setter
    def id_not_in(self, id_not_in):
        """Sets the id_not_in of this UserRoleNextWhereInput.


        :param id_not_in: The id_not_in of this UserRoleNextWhereInput.  # noqa: E501
        :type id_not_in: list[str]
        """

        self._id_not_in = id_not_in

    @property
    def id_not_starts_with(self):
        """Gets the id_not_starts_with of this UserRoleNextWhereInput.  # noqa: E501


        :return: The id_not_starts_with of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_not_starts_with

    @id_not_starts_with.setter
    def id_not_starts_with(self, id_not_starts_with):
        """Sets the id_not_starts_with of this UserRoleNextWhereInput.


        :param id_not_starts_with: The id_not_starts_with of this UserRoleNextWhereInput.  # noqa: E501
        :type id_not_starts_with: str
        """

        self._id_not_starts_with = id_not_starts_with

    @property
    def id_starts_with(self):
        """Gets the id_starts_with of this UserRoleNextWhereInput.  # noqa: E501


        :return: The id_starts_with of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._id_starts_with

    @id_starts_with.setter
    def id_starts_with(self, id_starts_with):
        """Sets the id_starts_with of this UserRoleNextWhereInput.


        :param id_starts_with: The id_starts_with of this UserRoleNextWhereInput.  # noqa: E501
        :type id_starts_with: str
        """

        self._id_starts_with = id_starts_with

    @property
    def name(self):
        """Gets the name of this UserRoleNextWhereInput.  # noqa: E501


        :return: The name of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserRoleNextWhereInput.


        :param name: The name of this UserRoleNextWhereInput.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def name_contains(self):
        """Gets the name_contains of this UserRoleNextWhereInput.  # noqa: E501


        :return: The name_contains of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_contains

    @name_contains.setter
    def name_contains(self, name_contains):
        """Sets the name_contains of this UserRoleNextWhereInput.


        :param name_contains: The name_contains of this UserRoleNextWhereInput.  # noqa: E501
        :type name_contains: str
        """

        self._name_contains = name_contains

    @property
    def name_ends_with(self):
        """Gets the name_ends_with of this UserRoleNextWhereInput.  # noqa: E501


        :return: The name_ends_with of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_ends_with

    @name_ends_with.setter
    def name_ends_with(self, name_ends_with):
        """Sets the name_ends_with of this UserRoleNextWhereInput.


        :param name_ends_with: The name_ends_with of this UserRoleNextWhereInput.  # noqa: E501
        :type name_ends_with: str
        """

        self._name_ends_with = name_ends_with

    @property
    def name_gt(self):
        """Gets the name_gt of this UserRoleNextWhereInput.  # noqa: E501


        :return: The name_gt of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_gt

    @name_gt.setter
    def name_gt(self, name_gt):
        """Sets the name_gt of this UserRoleNextWhereInput.


        :param name_gt: The name_gt of this UserRoleNextWhereInput.  # noqa: E501
        :type name_gt: str
        """

        self._name_gt = name_gt

    @property
    def name_gte(self):
        """Gets the name_gte of this UserRoleNextWhereInput.  # noqa: E501


        :return: The name_gte of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_gte

    @name_gte.setter
    def name_gte(self, name_gte):
        """Sets the name_gte of this UserRoleNextWhereInput.


        :param name_gte: The name_gte of this UserRoleNextWhereInput.  # noqa: E501
        :type name_gte: str
        """

        self._name_gte = name_gte

    @property
    def name_in(self):
        """Gets the name_in of this UserRoleNextWhereInput.  # noqa: E501


        :return: The name_in of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._name_in

    @name_in.setter
    def name_in(self, name_in):
        """Sets the name_in of this UserRoleNextWhereInput.


        :param name_in: The name_in of this UserRoleNextWhereInput.  # noqa: E501
        :type name_in: list[str]
        """

        self._name_in = name_in

    @property
    def name_lt(self):
        """Gets the name_lt of this UserRoleNextWhereInput.  # noqa: E501


        :return: The name_lt of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_lt

    @name_lt.setter
    def name_lt(self, name_lt):
        """Sets the name_lt of this UserRoleNextWhereInput.


        :param name_lt: The name_lt of this UserRoleNextWhereInput.  # noqa: E501
        :type name_lt: str
        """

        self._name_lt = name_lt

    @property
    def name_lte(self):
        """Gets the name_lte of this UserRoleNextWhereInput.  # noqa: E501


        :return: The name_lte of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_lte

    @name_lte.setter
    def name_lte(self, name_lte):
        """Sets the name_lte of this UserRoleNextWhereInput.


        :param name_lte: The name_lte of this UserRoleNextWhereInput.  # noqa: E501
        :type name_lte: str
        """

        self._name_lte = name_lte

    @property
    def name_not(self):
        """Gets the name_not of this UserRoleNextWhereInput.  # noqa: E501


        :return: The name_not of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_not

    @name_not.setter
    def name_not(self, name_not):
        """Sets the name_not of this UserRoleNextWhereInput.


        :param name_not: The name_not of this UserRoleNextWhereInput.  # noqa: E501
        :type name_not: str
        """

        self._name_not = name_not

    @property
    def name_not_contains(self):
        """Gets the name_not_contains of this UserRoleNextWhereInput.  # noqa: E501


        :return: The name_not_contains of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_not_contains

    @name_not_contains.setter
    def name_not_contains(self, name_not_contains):
        """Sets the name_not_contains of this UserRoleNextWhereInput.


        :param name_not_contains: The name_not_contains of this UserRoleNextWhereInput.  # noqa: E501
        :type name_not_contains: str
        """

        self._name_not_contains = name_not_contains

    @property
    def name_not_ends_with(self):
        """Gets the name_not_ends_with of this UserRoleNextWhereInput.  # noqa: E501


        :return: The name_not_ends_with of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_not_ends_with

    @name_not_ends_with.setter
    def name_not_ends_with(self, name_not_ends_with):
        """Sets the name_not_ends_with of this UserRoleNextWhereInput.


        :param name_not_ends_with: The name_not_ends_with of this UserRoleNextWhereInput.  # noqa: E501
        :type name_not_ends_with: str
        """

        self._name_not_ends_with = name_not_ends_with

    @property
    def name_not_in(self):
        """Gets the name_not_in of this UserRoleNextWhereInput.  # noqa: E501


        :return: The name_not_in of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._name_not_in

    @name_not_in.setter
    def name_not_in(self, name_not_in):
        """Sets the name_not_in of this UserRoleNextWhereInput.


        :param name_not_in: The name_not_in of this UserRoleNextWhereInput.  # noqa: E501
        :type name_not_in: list[str]
        """

        self._name_not_in = name_not_in

    @property
    def name_not_starts_with(self):
        """Gets the name_not_starts_with of this UserRoleNextWhereInput.  # noqa: E501


        :return: The name_not_starts_with of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_not_starts_with

    @name_not_starts_with.setter
    def name_not_starts_with(self, name_not_starts_with):
        """Sets the name_not_starts_with of this UserRoleNextWhereInput.


        :param name_not_starts_with: The name_not_starts_with of this UserRoleNextWhereInput.  # noqa: E501
        :type name_not_starts_with: str
        """

        self._name_not_starts_with = name_not_starts_with

    @property
    def name_starts_with(self):
        """Gets the name_starts_with of this UserRoleNextWhereInput.  # noqa: E501


        :return: The name_starts_with of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: str
        """
        return self._name_starts_with

    @name_starts_with.setter
    def name_starts_with(self, name_starts_with):
        """Sets the name_starts_with of this UserRoleNextWhereInput.


        :param name_starts_with: The name_starts_with of this UserRoleNextWhereInput.  # noqa: E501
        :type name_starts_with: str
        """

        self._name_starts_with = name_starts_with

    @property
    def _not(self):
        """Gets the _not of this UserRoleNextWhereInput.  # noqa: E501


        :return: The _not of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: list[UserRoleNextWhereInput]
        """
        return self.__not

    @_not.setter
    def _not(self, _not):
        """Sets the _not of this UserRoleNextWhereInput.


        :param _not: The _not of this UserRoleNextWhereInput.  # noqa: E501
        :type _not: list[UserRoleNextWhereInput]
        """

        self.__not = _not

    @property
    def _or(self):
        """Gets the _or of this UserRoleNextWhereInput.  # noqa: E501


        :return: The _or of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: list[UserRoleNextWhereInput]
        """
        return self.__or

    @_or.setter
    def _or(self, _or):
        """Sets the _or of this UserRoleNextWhereInput.


        :param _or: The _or of this UserRoleNextWhereInput.  # noqa: E501
        :type _or: list[UserRoleNextWhereInput]
        """

        self.__or = _or

    @property
    def platform(self):
        """Gets the platform of this UserRoleNextWhereInput.  # noqa: E501


        :return: The platform of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: UserRolePlatform
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this UserRoleNextWhereInput.


        :param platform: The platform of this UserRoleNextWhereInput.  # noqa: E501
        :type platform: UserRolePlatform
        """

        self._platform = platform

    @property
    def platform_in(self):
        """Gets the platform_in of this UserRoleNextWhereInput.  # noqa: E501


        :return: The platform_in of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: list[UserRolePlatform]
        """
        return self._platform_in

    @platform_in.setter
    def platform_in(self, platform_in):
        """Sets the platform_in of this UserRoleNextWhereInput.


        :param platform_in: The platform_in of this UserRoleNextWhereInput.  # noqa: E501
        :type platform_in: list[UserRolePlatform]
        """

        self._platform_in = platform_in

    @property
    def platform_not(self):
        """Gets the platform_not of this UserRoleNextWhereInput.  # noqa: E501


        :return: The platform_not of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: UserRolePlatform
        """
        return self._platform_not

    @platform_not.setter
    def platform_not(self, platform_not):
        """Sets the platform_not of this UserRoleNextWhereInput.


        :param platform_not: The platform_not of this UserRoleNextWhereInput.  # noqa: E501
        :type platform_not: UserRolePlatform
        """

        self._platform_not = platform_not

    @property
    def platform_not_in(self):
        """Gets the platform_not_in of this UserRoleNextWhereInput.  # noqa: E501


        :return: The platform_not_in of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: list[UserRolePlatform]
        """
        return self._platform_not_in

    @platform_not_in.setter
    def platform_not_in(self, platform_not_in):
        """Sets the platform_not_in of this UserRoleNextWhereInput.


        :param platform_not_in: The platform_not_in of this UserRoleNextWhereInput.  # noqa: E501
        :type platform_not_in: list[UserRolePlatform]
        """

        self._platform_not_in = platform_not_in

    @property
    def preset(self):
        """Gets the preset of this UserRoleNextWhereInput.  # noqa: E501


        :return: The preset of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: UserRolePreset
        """
        return self._preset

    @preset.setter
    def preset(self, preset):
        """Sets the preset of this UserRoleNextWhereInput.


        :param preset: The preset of this UserRoleNextWhereInput.  # noqa: E501
        :type preset: UserRolePreset
        """

        self._preset = preset

    @property
    def preset_in(self):
        """Gets the preset_in of this UserRoleNextWhereInput.  # noqa: E501


        :return: The preset_in of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: list[UserRolePreset]
        """
        return self._preset_in

    @preset_in.setter
    def preset_in(self, preset_in):
        """Sets the preset_in of this UserRoleNextWhereInput.


        :param preset_in: The preset_in of this UserRoleNextWhereInput.  # noqa: E501
        :type preset_in: list[UserRolePreset]
        """

        self._preset_in = preset_in

    @property
    def preset_not(self):
        """Gets the preset_not of this UserRoleNextWhereInput.  # noqa: E501


        :return: The preset_not of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: UserRolePreset
        """
        return self._preset_not

    @preset_not.setter
    def preset_not(self, preset_not):
        """Sets the preset_not of this UserRoleNextWhereInput.


        :param preset_not: The preset_not of this UserRoleNextWhereInput.  # noqa: E501
        :type preset_not: UserRolePreset
        """

        self._preset_not = preset_not

    @property
    def preset_not_in(self):
        """Gets the preset_not_in of this UserRoleNextWhereInput.  # noqa: E501


        :return: The preset_not_in of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: list[UserRolePreset]
        """
        return self._preset_not_in

    @preset_not_in.setter
    def preset_not_in(self, preset_not_in):
        """Sets the preset_not_in of this UserRoleNextWhereInput.


        :param preset_not_in: The preset_not_in of this UserRoleNextWhereInput.  # noqa: E501
        :type preset_not_in: list[UserRolePreset]
        """

        self._preset_not_in = preset_not_in

    @property
    def users_every(self):
        """Gets the users_every of this UserRoleNextWhereInput.  # noqa: E501


        :return: The users_every of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: UserWhereInput
        """
        return self._users_every

    @users_every.setter
    def users_every(self, users_every):
        """Sets the users_every of this UserRoleNextWhereInput.


        :param users_every: The users_every of this UserRoleNextWhereInput.  # noqa: E501
        :type users_every: UserWhereInput
        """

        self._users_every = users_every

    @property
    def users_none(self):
        """Gets the users_none of this UserRoleNextWhereInput.  # noqa: E501


        :return: The users_none of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: UserWhereInput
        """
        return self._users_none

    @users_none.setter
    def users_none(self, users_none):
        """Sets the users_none of this UserRoleNextWhereInput.


        :param users_none: The users_none of this UserRoleNextWhereInput.  # noqa: E501
        :type users_none: UserWhereInput
        """

        self._users_none = users_none

    @property
    def users_some(self):
        """Gets the users_some of this UserRoleNextWhereInput.  # noqa: E501


        :return: The users_some of this UserRoleNextWhereInput.  # noqa: E501
        :rtype: UserWhereInput
        """
        return self._users_some

    @users_some.setter
    def users_some(self, users_some):
        """Sets the users_some of this UserRoleNextWhereInput.


        :param users_some: The users_some of this UserRoleNextWhereInput.  # noqa: E501
        :type users_some: UserWhereInput
        """

        self._users_some = users_some

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
        if not isinstance(other, UserRoleNextWhereInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserRoleNextWhereInput):
            return True

        return self.to_dict() != other.to_dict()
