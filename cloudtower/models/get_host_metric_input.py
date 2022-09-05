# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class GetHostMetricInput(object):
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
        'range': 'str',
        'hosts': 'HostWhereInput',
        'metrics': 'list[str]'
    }

    attribute_map = {
        'range': 'range',
        'hosts': 'hosts',
        'metrics': 'metrics'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """GetHostMetricInput - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._range = None
        self._hosts = None
        self._metrics = None
        self.discriminator = None

        if "range" in kwargs:
            self.range = kwargs["range"]
        if "hosts" in kwargs:
            self.hosts = kwargs["hosts"]
        if "metrics" in kwargs:
            self.metrics = kwargs["metrics"]

    @property
    def range(self):
        """Gets the range of this GetHostMetricInput.  # noqa: E501


        :return: The range of this GetHostMetricInput.  # noqa: E501
        :rtype: str
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this GetHostMetricInput.


        :param range: The range of this GetHostMetricInput.  # noqa: E501
        :type range: str
        """
        if self.local_vars_configuration.client_side_validation and range is None:  # noqa: E501
            raise ValueError("Invalid value for `range`, must not be `None`")  # noqa: E501

        self._range = range

    @property
    def hosts(self):
        """Gets the hosts of this GetHostMetricInput.  # noqa: E501


        :return: The hosts of this GetHostMetricInput.  # noqa: E501
        :rtype: HostWhereInput
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this GetHostMetricInput.


        :param hosts: The hosts of this GetHostMetricInput.  # noqa: E501
        :type hosts: HostWhereInput
        """
        if self.local_vars_configuration.client_side_validation and hosts is None:  # noqa: E501
            raise ValueError("Invalid value for `hosts`, must not be `None`")  # noqa: E501

        self._hosts = hosts

    @property
    def metrics(self):
        """Gets the metrics of this GetHostMetricInput.  # noqa: E501


        :return: The metrics of this GetHostMetricInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this GetHostMetricInput.


        :param metrics: The metrics of this GetHostMetricInput.  # noqa: E501
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
        if not isinstance(other, GetHostMetricInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetHostMetricInput):
            return True

        return self.to_dict() != other.to_dict()
