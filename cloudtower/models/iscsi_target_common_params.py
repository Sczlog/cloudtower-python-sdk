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


class IscsiTargetCommonParams(object):
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
        'bps_wr_max_length': 'int',
        'bps_wr_max': 'int',
        'bps_rd_max_length': 'int',
        'bps_rd_max': 'int',
        'bps_max_length': 'int',
        'bps_max': 'int',
        'iops_wr_max_length': 'int',
        'iops_wr_max': 'int',
        'iops_rd_max_length': 'int',
        'iops_rd_max': 'int',
        'iops_max_length': 'int',
        'iops_max': 'int',
        'bps_wr': 'int',
        'bps_rd': 'int',
        'bps': 'int',
        'iops_wr': 'int',
        'iops_rd': 'int',
        'iops': 'int',
        'initiator_chaps': 'list[IscsiTargetCommonParamsInitiatorChaps]',
        'chap_secret': 'str',
        'chap_name': 'str',
        'chap_enabled': 'bool',
        'description': 'str',
        'iqn_whitelist': 'str',
        'ip_whitelist': 'str'
    }

    attribute_map = {
        'bps_wr_max_length': 'bps_wr_max_length',
        'bps_wr_max': 'bps_wr_max',
        'bps_rd_max_length': 'bps_rd_max_length',
        'bps_rd_max': 'bps_rd_max',
        'bps_max_length': 'bps_max_length',
        'bps_max': 'bps_max',
        'iops_wr_max_length': 'iops_wr_max_length',
        'iops_wr_max': 'iops_wr_max',
        'iops_rd_max_length': 'iops_rd_max_length',
        'iops_rd_max': 'iops_rd_max',
        'iops_max_length': 'iops_max_length',
        'iops_max': 'iops_max',
        'bps_wr': 'bps_wr',
        'bps_rd': 'bps_rd',
        'bps': 'bps',
        'iops_wr': 'iops_wr',
        'iops_rd': 'iops_rd',
        'iops': 'iops',
        'initiator_chaps': 'initiator_chaps',
        'chap_secret': 'chap_secret',
        'chap_name': 'chap_name',
        'chap_enabled': 'chap_enabled',
        'description': 'description',
        'iqn_whitelist': 'iqn_whitelist',
        'ip_whitelist': 'ip_whitelist'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """IscsiTargetCommonParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._bps_wr_max_length = None
        self._bps_wr_max = None
        self._bps_rd_max_length = None
        self._bps_rd_max = None
        self._bps_max_length = None
        self._bps_max = None
        self._iops_wr_max_length = None
        self._iops_wr_max = None
        self._iops_rd_max_length = None
        self._iops_rd_max = None
        self._iops_max_length = None
        self._iops_max = None
        self._bps_wr = None
        self._bps_rd = None
        self._bps = None
        self._iops_wr = None
        self._iops_rd = None
        self._iops = None
        self._initiator_chaps = None
        self._chap_secret = None
        self._chap_name = None
        self._chap_enabled = None
        self._description = None
        self._iqn_whitelist = None
        self._ip_whitelist = None
        self.discriminator = None

        if "bps_wr_max_length" in kwargs:
            self.bps_wr_max_length = kwargs["bps_wr_max_length"]
        if "bps_wr_max" in kwargs:
            self.bps_wr_max = kwargs["bps_wr_max"]
        if "bps_rd_max_length" in kwargs:
            self.bps_rd_max_length = kwargs["bps_rd_max_length"]
        if "bps_rd_max" in kwargs:
            self.bps_rd_max = kwargs["bps_rd_max"]
        if "bps_max_length" in kwargs:
            self.bps_max_length = kwargs["bps_max_length"]
        if "bps_max" in kwargs:
            self.bps_max = kwargs["bps_max"]
        if "iops_wr_max_length" in kwargs:
            self.iops_wr_max_length = kwargs["iops_wr_max_length"]
        if "iops_wr_max" in kwargs:
            self.iops_wr_max = kwargs["iops_wr_max"]
        if "iops_rd_max_length" in kwargs:
            self.iops_rd_max_length = kwargs["iops_rd_max_length"]
        if "iops_rd_max" in kwargs:
            self.iops_rd_max = kwargs["iops_rd_max"]
        if "iops_max_length" in kwargs:
            self.iops_max_length = kwargs["iops_max_length"]
        if "iops_max" in kwargs:
            self.iops_max = kwargs["iops_max"]
        if "bps_wr" in kwargs:
            self.bps_wr = kwargs["bps_wr"]
        if "bps_rd" in kwargs:
            self.bps_rd = kwargs["bps_rd"]
        if "bps" in kwargs:
            self.bps = kwargs["bps"]
        if "iops_wr" in kwargs:
            self.iops_wr = kwargs["iops_wr"]
        if "iops_rd" in kwargs:
            self.iops_rd = kwargs["iops_rd"]
        if "iops" in kwargs:
            self.iops = kwargs["iops"]
        if "initiator_chaps" in kwargs:
            self.initiator_chaps = kwargs["initiator_chaps"]
        if "chap_secret" in kwargs:
            self.chap_secret = kwargs["chap_secret"]
        if "chap_name" in kwargs:
            self.chap_name = kwargs["chap_name"]
        if "chap_enabled" in kwargs:
            self.chap_enabled = kwargs["chap_enabled"]
        if "description" in kwargs:
            self.description = kwargs["description"]
        if "iqn_whitelist" in kwargs:
            self.iqn_whitelist = kwargs["iqn_whitelist"]
        if "ip_whitelist" in kwargs:
            self.ip_whitelist = kwargs["ip_whitelist"]

    @property
    def bps_wr_max_length(self):
        """Gets the bps_wr_max_length of this IscsiTargetCommonParams.  # noqa: E501


        :return: The bps_wr_max_length of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: int
        """
        return self._bps_wr_max_length

    @bps_wr_max_length.setter
    def bps_wr_max_length(self, bps_wr_max_length):
        """Sets the bps_wr_max_length of this IscsiTargetCommonParams.


        :param bps_wr_max_length: The bps_wr_max_length of this IscsiTargetCommonParams.  # noqa: E501
        :type bps_wr_max_length: int
        """

        self._bps_wr_max_length = bps_wr_max_length

    @property
    def bps_wr_max(self):
        """Gets the bps_wr_max of this IscsiTargetCommonParams.  # noqa: E501


        :return: The bps_wr_max of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: int
        """
        return self._bps_wr_max

    @bps_wr_max.setter
    def bps_wr_max(self, bps_wr_max):
        """Sets the bps_wr_max of this IscsiTargetCommonParams.


        :param bps_wr_max: The bps_wr_max of this IscsiTargetCommonParams.  # noqa: E501
        :type bps_wr_max: int
        """

        self._bps_wr_max = bps_wr_max

    @property
    def bps_rd_max_length(self):
        """Gets the bps_rd_max_length of this IscsiTargetCommonParams.  # noqa: E501


        :return: The bps_rd_max_length of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: int
        """
        return self._bps_rd_max_length

    @bps_rd_max_length.setter
    def bps_rd_max_length(self, bps_rd_max_length):
        """Sets the bps_rd_max_length of this IscsiTargetCommonParams.


        :param bps_rd_max_length: The bps_rd_max_length of this IscsiTargetCommonParams.  # noqa: E501
        :type bps_rd_max_length: int
        """

        self._bps_rd_max_length = bps_rd_max_length

    @property
    def bps_rd_max(self):
        """Gets the bps_rd_max of this IscsiTargetCommonParams.  # noqa: E501


        :return: The bps_rd_max of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: int
        """
        return self._bps_rd_max

    @bps_rd_max.setter
    def bps_rd_max(self, bps_rd_max):
        """Sets the bps_rd_max of this IscsiTargetCommonParams.


        :param bps_rd_max: The bps_rd_max of this IscsiTargetCommonParams.  # noqa: E501
        :type bps_rd_max: int
        """

        self._bps_rd_max = bps_rd_max

    @property
    def bps_max_length(self):
        """Gets the bps_max_length of this IscsiTargetCommonParams.  # noqa: E501


        :return: The bps_max_length of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: int
        """
        return self._bps_max_length

    @bps_max_length.setter
    def bps_max_length(self, bps_max_length):
        """Sets the bps_max_length of this IscsiTargetCommonParams.


        :param bps_max_length: The bps_max_length of this IscsiTargetCommonParams.  # noqa: E501
        :type bps_max_length: int
        """

        self._bps_max_length = bps_max_length

    @property
    def bps_max(self):
        """Gets the bps_max of this IscsiTargetCommonParams.  # noqa: E501


        :return: The bps_max of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: int
        """
        return self._bps_max

    @bps_max.setter
    def bps_max(self, bps_max):
        """Sets the bps_max of this IscsiTargetCommonParams.


        :param bps_max: The bps_max of this IscsiTargetCommonParams.  # noqa: E501
        :type bps_max: int
        """

        self._bps_max = bps_max

    @property
    def iops_wr_max_length(self):
        """Gets the iops_wr_max_length of this IscsiTargetCommonParams.  # noqa: E501


        :return: The iops_wr_max_length of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: int
        """
        return self._iops_wr_max_length

    @iops_wr_max_length.setter
    def iops_wr_max_length(self, iops_wr_max_length):
        """Sets the iops_wr_max_length of this IscsiTargetCommonParams.


        :param iops_wr_max_length: The iops_wr_max_length of this IscsiTargetCommonParams.  # noqa: E501
        :type iops_wr_max_length: int
        """

        self._iops_wr_max_length = iops_wr_max_length

    @property
    def iops_wr_max(self):
        """Gets the iops_wr_max of this IscsiTargetCommonParams.  # noqa: E501


        :return: The iops_wr_max of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: int
        """
        return self._iops_wr_max

    @iops_wr_max.setter
    def iops_wr_max(self, iops_wr_max):
        """Sets the iops_wr_max of this IscsiTargetCommonParams.


        :param iops_wr_max: The iops_wr_max of this IscsiTargetCommonParams.  # noqa: E501
        :type iops_wr_max: int
        """

        self._iops_wr_max = iops_wr_max

    @property
    def iops_rd_max_length(self):
        """Gets the iops_rd_max_length of this IscsiTargetCommonParams.  # noqa: E501


        :return: The iops_rd_max_length of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: int
        """
        return self._iops_rd_max_length

    @iops_rd_max_length.setter
    def iops_rd_max_length(self, iops_rd_max_length):
        """Sets the iops_rd_max_length of this IscsiTargetCommonParams.


        :param iops_rd_max_length: The iops_rd_max_length of this IscsiTargetCommonParams.  # noqa: E501
        :type iops_rd_max_length: int
        """

        self._iops_rd_max_length = iops_rd_max_length

    @property
    def iops_rd_max(self):
        """Gets the iops_rd_max of this IscsiTargetCommonParams.  # noqa: E501


        :return: The iops_rd_max of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: int
        """
        return self._iops_rd_max

    @iops_rd_max.setter
    def iops_rd_max(self, iops_rd_max):
        """Sets the iops_rd_max of this IscsiTargetCommonParams.


        :param iops_rd_max: The iops_rd_max of this IscsiTargetCommonParams.  # noqa: E501
        :type iops_rd_max: int
        """

        self._iops_rd_max = iops_rd_max

    @property
    def iops_max_length(self):
        """Gets the iops_max_length of this IscsiTargetCommonParams.  # noqa: E501


        :return: The iops_max_length of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: int
        """
        return self._iops_max_length

    @iops_max_length.setter
    def iops_max_length(self, iops_max_length):
        """Sets the iops_max_length of this IscsiTargetCommonParams.


        :param iops_max_length: The iops_max_length of this IscsiTargetCommonParams.  # noqa: E501
        :type iops_max_length: int
        """

        self._iops_max_length = iops_max_length

    @property
    def iops_max(self):
        """Gets the iops_max of this IscsiTargetCommonParams.  # noqa: E501


        :return: The iops_max of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: int
        """
        return self._iops_max

    @iops_max.setter
    def iops_max(self, iops_max):
        """Sets the iops_max of this IscsiTargetCommonParams.


        :param iops_max: The iops_max of this IscsiTargetCommonParams.  # noqa: E501
        :type iops_max: int
        """

        self._iops_max = iops_max

    @property
    def bps_wr(self):
        """Gets the bps_wr of this IscsiTargetCommonParams.  # noqa: E501


        :return: The bps_wr of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: int
        """
        return self._bps_wr

    @bps_wr.setter
    def bps_wr(self, bps_wr):
        """Sets the bps_wr of this IscsiTargetCommonParams.


        :param bps_wr: The bps_wr of this IscsiTargetCommonParams.  # noqa: E501
        :type bps_wr: int
        """

        self._bps_wr = bps_wr

    @property
    def bps_rd(self):
        """Gets the bps_rd of this IscsiTargetCommonParams.  # noqa: E501


        :return: The bps_rd of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: int
        """
        return self._bps_rd

    @bps_rd.setter
    def bps_rd(self, bps_rd):
        """Sets the bps_rd of this IscsiTargetCommonParams.


        :param bps_rd: The bps_rd of this IscsiTargetCommonParams.  # noqa: E501
        :type bps_rd: int
        """

        self._bps_rd = bps_rd

    @property
    def bps(self):
        """Gets the bps of this IscsiTargetCommonParams.  # noqa: E501


        :return: The bps of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: int
        """
        return self._bps

    @bps.setter
    def bps(self, bps):
        """Sets the bps of this IscsiTargetCommonParams.


        :param bps: The bps of this IscsiTargetCommonParams.  # noqa: E501
        :type bps: int
        """

        self._bps = bps

    @property
    def iops_wr(self):
        """Gets the iops_wr of this IscsiTargetCommonParams.  # noqa: E501


        :return: The iops_wr of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: int
        """
        return self._iops_wr

    @iops_wr.setter
    def iops_wr(self, iops_wr):
        """Sets the iops_wr of this IscsiTargetCommonParams.


        :param iops_wr: The iops_wr of this IscsiTargetCommonParams.  # noqa: E501
        :type iops_wr: int
        """

        self._iops_wr = iops_wr

    @property
    def iops_rd(self):
        """Gets the iops_rd of this IscsiTargetCommonParams.  # noqa: E501


        :return: The iops_rd of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: int
        """
        return self._iops_rd

    @iops_rd.setter
    def iops_rd(self, iops_rd):
        """Sets the iops_rd of this IscsiTargetCommonParams.


        :param iops_rd: The iops_rd of this IscsiTargetCommonParams.  # noqa: E501
        :type iops_rd: int
        """

        self._iops_rd = iops_rd

    @property
    def iops(self):
        """Gets the iops of this IscsiTargetCommonParams.  # noqa: E501


        :return: The iops of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: int
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """Sets the iops of this IscsiTargetCommonParams.


        :param iops: The iops of this IscsiTargetCommonParams.  # noqa: E501
        :type iops: int
        """

        self._iops = iops

    @property
    def initiator_chaps(self):
        """Gets the initiator_chaps of this IscsiTargetCommonParams.  # noqa: E501


        :return: The initiator_chaps of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: list[IscsiTargetCommonParamsInitiatorChaps]
        """
        return self._initiator_chaps

    @initiator_chaps.setter
    def initiator_chaps(self, initiator_chaps):
        """Sets the initiator_chaps of this IscsiTargetCommonParams.


        :param initiator_chaps: The initiator_chaps of this IscsiTargetCommonParams.  # noqa: E501
        :type initiator_chaps: list[IscsiTargetCommonParamsInitiatorChaps]
        """

        self._initiator_chaps = initiator_chaps

    @property
    def chap_secret(self):
        """Gets the chap_secret of this IscsiTargetCommonParams.  # noqa: E501


        :return: The chap_secret of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: str
        """
        return self._chap_secret

    @chap_secret.setter
    def chap_secret(self, chap_secret):
        """Sets the chap_secret of this IscsiTargetCommonParams.


        :param chap_secret: The chap_secret of this IscsiTargetCommonParams.  # noqa: E501
        :type chap_secret: str
        """

        self._chap_secret = chap_secret

    @property
    def chap_name(self):
        """Gets the chap_name of this IscsiTargetCommonParams.  # noqa: E501


        :return: The chap_name of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: str
        """
        return self._chap_name

    @chap_name.setter
    def chap_name(self, chap_name):
        """Sets the chap_name of this IscsiTargetCommonParams.


        :param chap_name: The chap_name of this IscsiTargetCommonParams.  # noqa: E501
        :type chap_name: str
        """

        self._chap_name = chap_name

    @property
    def chap_enabled(self):
        """Gets the chap_enabled of this IscsiTargetCommonParams.  # noqa: E501


        :return: The chap_enabled of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: bool
        """
        return self._chap_enabled

    @chap_enabled.setter
    def chap_enabled(self, chap_enabled):
        """Sets the chap_enabled of this IscsiTargetCommonParams.


        :param chap_enabled: The chap_enabled of this IscsiTargetCommonParams.  # noqa: E501
        :type chap_enabled: bool
        """

        self._chap_enabled = chap_enabled

    @property
    def description(self):
        """Gets the description of this IscsiTargetCommonParams.  # noqa: E501


        :return: The description of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IscsiTargetCommonParams.


        :param description: The description of this IscsiTargetCommonParams.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def iqn_whitelist(self):
        """Gets the iqn_whitelist of this IscsiTargetCommonParams.  # noqa: E501


        :return: The iqn_whitelist of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: str
        """
        return self._iqn_whitelist

    @iqn_whitelist.setter
    def iqn_whitelist(self, iqn_whitelist):
        """Sets the iqn_whitelist of this IscsiTargetCommonParams.


        :param iqn_whitelist: The iqn_whitelist of this IscsiTargetCommonParams.  # noqa: E501
        :type iqn_whitelist: str
        """

        self._iqn_whitelist = iqn_whitelist

    @property
    def ip_whitelist(self):
        """Gets the ip_whitelist of this IscsiTargetCommonParams.  # noqa: E501


        :return: The ip_whitelist of this IscsiTargetCommonParams.  # noqa: E501
        :rtype: str
        """
        return self._ip_whitelist

    @ip_whitelist.setter
    def ip_whitelist(self, ip_whitelist):
        """Sets the ip_whitelist of this IscsiTargetCommonParams.


        :param ip_whitelist: The ip_whitelist of this IscsiTargetCommonParams.  # noqa: E501
        :type ip_whitelist: str
        """

        self._ip_whitelist = ip_whitelist

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
        if not isinstance(other, IscsiTargetCommonParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IscsiTargetCommonParams):
            return True

        return self.to_dict() != other.to_dict()
