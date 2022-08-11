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


class GetHostNetworkMetricInput(object):
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
        'hosts': 'HostWhereInput',
        'range': 'str',
        'nics': 'NicWhereInput',
        'metrics': 'list[str]'
    }

    attribute_map = {
        'hosts': 'hosts',
        'range': 'range',
        'nics': 'nics',
        'metrics': 'metrics'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """GetHostNetworkMetricInput - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._hosts = None
        self._range = None
        self._nics = None
        self._metrics = None
        self.discriminator = None

        if "hosts" in kwargs:
            self.hosts = kwargs["hosts"]
        if "range" in kwargs:
            self.range = kwargs["range"]
        if "nics" in kwargs:
            self.nics = kwargs["nics"]
        if "metrics" in kwargs:
            self.metrics = kwargs["metrics"]

    @property
    def hosts(self):
        """Gets the hosts of this GetHostNetworkMetricInput.  # noqa: E501


        :return: The hosts of this GetHostNetworkMetricInput.  # noqa: E501
        :rtype: HostWhereInput
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this GetHostNetworkMetricInput.


        :param hosts: The hosts of this GetHostNetworkMetricInput.  # noqa: E501
        :type hosts: HostWhereInput
        """
        if self.local_vars_configuration.client_side_validation and hosts is None:  # noqa: E501
            raise ValueError("Invalid value for `hosts`, must not be `None`")  # noqa: E501

        self._hosts = hosts

    @property
    def range(self):
        """Gets the range of this GetHostNetworkMetricInput.  # noqa: E501


        :return: The range of this GetHostNetworkMetricInput.  # noqa: E501
        :rtype: str
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this GetHostNetworkMetricInput.


        :param range: The range of this GetHostNetworkMetricInput.  # noqa: E501
        :type range: str
        """
        if self.local_vars_configuration.client_side_validation and range is None:  # noqa: E501
            raise ValueError("Invalid value for `range`, must not be `None`")  # noqa: E501

        self._range = range

    @property
    def nics(self):
        """Gets the nics of this GetHostNetworkMetricInput.  # noqa: E501


        :return: The nics of this GetHostNetworkMetricInput.  # noqa: E501
        :rtype: NicWhereInput
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this GetHostNetworkMetricInput.


        :param nics: The nics of this GetHostNetworkMetricInput.  # noqa: E501
        :type nics: NicWhereInput
        """

        self._nics = nics

    @property
    def metrics(self):
        """Gets the metrics of this GetHostNetworkMetricInput.  # noqa: E501


        :return: The metrics of this GetHostNetworkMetricInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this GetHostNetworkMetricInput.


        :param metrics: The metrics of this GetHostNetworkMetricInput.  # noqa: E501
        :type metrics: list[str]
        """
        if self.local_vars_configuration.client_side_validation and metrics is None:  # noqa: E501
            raise ValueError("Invalid value for `metrics`, must not be `None`")  # noqa: E501

        self._metrics = metrics

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
        if not isinstance(other, GetHostNetworkMetricInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetHostNetworkMetricInput):
            return True

        return self.to_dict() != other.to_dict()
