# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class GetNvmfNamespaceMetricInput(object):
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
        'nvmf_namespaces': 'NvmfNamespaceWhereInput',
        'metrics': 'list[str]',
        'range': 'str'
    }

    attribute_map = {
        'hosts': 'hosts',
        'nvmf_namespaces': 'nvmfNamespaces',
        'metrics': 'metrics',
        'range': 'range'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """GetNvmfNamespaceMetricInput - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._hosts = None
        self._nvmf_namespaces = None
        self._metrics = None
        self._range = None
        self.discriminator = None

        if "hosts" in kwargs:
            self.hosts = kwargs["hosts"]
        if "nvmf_namespaces" in kwargs:
            self.nvmf_namespaces = kwargs["nvmf_namespaces"]
        if "metrics" in kwargs:
            self.metrics = kwargs["metrics"]
        if "range" in kwargs:
            self.range = kwargs["range"]

    @property
    def hosts(self):
        """Gets the hosts of this GetNvmfNamespaceMetricInput.  # noqa: E501


        :return: The hosts of this GetNvmfNamespaceMetricInput.  # noqa: E501
        :rtype: HostWhereInput
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this GetNvmfNamespaceMetricInput.


        :param hosts: The hosts of this GetNvmfNamespaceMetricInput.  # noqa: E501
        :type hosts: HostWhereInput
        """

        self._hosts = hosts

    @property
    def nvmf_namespaces(self):
        """Gets the nvmf_namespaces of this GetNvmfNamespaceMetricInput.  # noqa: E501


        :return: The nvmf_namespaces of this GetNvmfNamespaceMetricInput.  # noqa: E501
        :rtype: NvmfNamespaceWhereInput
        """
        return self._nvmf_namespaces

    @nvmf_namespaces.setter
    def nvmf_namespaces(self, nvmf_namespaces):
        """Sets the nvmf_namespaces of this GetNvmfNamespaceMetricInput.


        :param nvmf_namespaces: The nvmf_namespaces of this GetNvmfNamespaceMetricInput.  # noqa: E501
        :type nvmf_namespaces: NvmfNamespaceWhereInput
        """
        if self.local_vars_configuration.client_side_validation and nvmf_namespaces is None:  # noqa: E501
            raise ValueError("Invalid value for `nvmf_namespaces`, must not be `None`")  # noqa: E501

        self._nvmf_namespaces = nvmf_namespaces

    @property
    def metrics(self):
        """Gets the metrics of this GetNvmfNamespaceMetricInput.  # noqa: E501


        :return: The metrics of this GetNvmfNamespaceMetricInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this GetNvmfNamespaceMetricInput.


        :param metrics: The metrics of this GetNvmfNamespaceMetricInput.  # noqa: E501
        :type metrics: list[str]
        """
        if self.local_vars_configuration.client_side_validation and metrics is None:  # noqa: E501
            raise ValueError("Invalid value for `metrics`, must not be `None`")  # noqa: E501

        self._metrics = metrics

    @property
    def range(self):
        """Gets the range of this GetNvmfNamespaceMetricInput.  # noqa: E501


        :return: The range of this GetNvmfNamespaceMetricInput.  # noqa: E501
        :rtype: str
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this GetNvmfNamespaceMetricInput.


        :param range: The range of this GetNvmfNamespaceMetricInput.  # noqa: E501
        :type range: str
        """
        if self.local_vars_configuration.client_side_validation and range is None:  # noqa: E501
            raise ValueError("Invalid value for `range`, must not be `None`")  # noqa: E501

        self._range = range

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
        if not isinstance(other, GetNvmfNamespaceMetricInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetNvmfNamespaceMetricInput):
            return True

        return self.to_dict() != other.to_dict()
