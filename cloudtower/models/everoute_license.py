# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.1.0
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


class EverouteLicense(object):
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
        'code': 'str',
        'expire_date': 'str',
        'id': 'str',
        'max_socket_num': 'int',
        'serial': 'str',
        'sign_date': 'str',
        'software_edition': 'SoftwareEdition',
        'type': 'LicenseType',
        'uid': 'str'
    }

    attribute_map = {
        'code': 'code',
        'expire_date': 'expire_date',
        'id': 'id',
        'max_socket_num': 'max_socket_num',
        'serial': 'serial',
        'sign_date': 'sign_date',
        'software_edition': 'software_edition',
        'type': 'type',
        'uid': 'uid'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """EverouteLicense - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._code = None
        self._expire_date = None
        self._id = None
        self._max_socket_num = None
        self._serial = None
        self._sign_date = None
        self._software_edition = None
        self._type = None
        self._uid = None
        self.discriminator = None

        if "code" in kwargs:
            self.code = kwargs["code"]
        if "expire_date" in kwargs:
            self.expire_date = kwargs["expire_date"]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "max_socket_num" in kwargs:
            self.max_socket_num = kwargs["max_socket_num"]
        if "serial" in kwargs:
            self.serial = kwargs["serial"]
        if "sign_date" in kwargs:
            self.sign_date = kwargs["sign_date"]
        if "software_edition" in kwargs:
            self.software_edition = kwargs["software_edition"]
        if "type" in kwargs:
            self.type = kwargs["type"]
        if "uid" in kwargs:
            self.uid = kwargs["uid"]

    @property
    def code(self):
        """Gets the code of this EverouteLicense.  # noqa: E501


        :return: The code of this EverouteLicense.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this EverouteLicense.


        :param code: The code of this EverouteLicense.  # noqa: E501
        :type code: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def expire_date(self):
        """Gets the expire_date of this EverouteLicense.  # noqa: E501


        :return: The expire_date of this EverouteLicense.  # noqa: E501
        :rtype: str
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        """Sets the expire_date of this EverouteLicense.


        :param expire_date: The expire_date of this EverouteLicense.  # noqa: E501
        :type expire_date: str
        """
        if self.local_vars_configuration.client_side_validation and expire_date is None:  # noqa: E501
            raise ValueError("Invalid value for `expire_date`, must not be `None`")  # noqa: E501

        self._expire_date = expire_date

    @property
    def id(self):
        """Gets the id of this EverouteLicense.  # noqa: E501


        :return: The id of this EverouteLicense.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EverouteLicense.


        :param id: The id of this EverouteLicense.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def max_socket_num(self):
        """Gets the max_socket_num of this EverouteLicense.  # noqa: E501


        :return: The max_socket_num of this EverouteLicense.  # noqa: E501
        :rtype: int
        """
        return self._max_socket_num

    @max_socket_num.setter
    def max_socket_num(self, max_socket_num):
        """Sets the max_socket_num of this EverouteLicense.


        :param max_socket_num: The max_socket_num of this EverouteLicense.  # noqa: E501
        :type max_socket_num: int
        """
        if self.local_vars_configuration.client_side_validation and max_socket_num is None:  # noqa: E501
            raise ValueError("Invalid value for `max_socket_num`, must not be `None`")  # noqa: E501

        self._max_socket_num = max_socket_num

    @property
    def serial(self):
        """Gets the serial of this EverouteLicense.  # noqa: E501


        :return: The serial of this EverouteLicense.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this EverouteLicense.


        :param serial: The serial of this EverouteLicense.  # noqa: E501
        :type serial: str
        """
        if self.local_vars_configuration.client_side_validation and serial is None:  # noqa: E501
            raise ValueError("Invalid value for `serial`, must not be `None`")  # noqa: E501

        self._serial = serial

    @property
    def sign_date(self):
        """Gets the sign_date of this EverouteLicense.  # noqa: E501


        :return: The sign_date of this EverouteLicense.  # noqa: E501
        :rtype: str
        """
        return self._sign_date

    @sign_date.setter
    def sign_date(self, sign_date):
        """Sets the sign_date of this EverouteLicense.


        :param sign_date: The sign_date of this EverouteLicense.  # noqa: E501
        :type sign_date: str
        """
        if self.local_vars_configuration.client_side_validation and sign_date is None:  # noqa: E501
            raise ValueError("Invalid value for `sign_date`, must not be `None`")  # noqa: E501

        self._sign_date = sign_date

    @property
    def software_edition(self):
        """Gets the software_edition of this EverouteLicense.  # noqa: E501


        :return: The software_edition of this EverouteLicense.  # noqa: E501
        :rtype: SoftwareEdition
        """
        return self._software_edition

    @software_edition.setter
    def software_edition(self, software_edition):
        """Sets the software_edition of this EverouteLicense.


        :param software_edition: The software_edition of this EverouteLicense.  # noqa: E501
        :type software_edition: SoftwareEdition
        """
        if self.local_vars_configuration.client_side_validation and software_edition is None:  # noqa: E501
            raise ValueError("Invalid value for `software_edition`, must not be `None`")  # noqa: E501

        self._software_edition = software_edition

    @property
    def type(self):
        """Gets the type of this EverouteLicense.  # noqa: E501


        :return: The type of this EverouteLicense.  # noqa: E501
        :rtype: LicenseType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EverouteLicense.


        :param type: The type of this EverouteLicense.  # noqa: E501
        :type type: LicenseType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def uid(self):
        """Gets the uid of this EverouteLicense.  # noqa: E501


        :return: The uid of this EverouteLicense.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this EverouteLicense.


        :param uid: The uid of this EverouteLicense.  # noqa: E501
        :type uid: str
        """
        if self.local_vars_configuration.client_side_validation and uid is None:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

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
        if not isinstance(other, EverouteLicense):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EverouteLicense):
            return True

        return self.to_dict() != other.to_dict()
