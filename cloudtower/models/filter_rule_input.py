# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.0.0
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


class FilterRuleInput(object):
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
        'threshold': 'float',
        'quantile': 'int',
        'op': 'FilterRuleOpEnum',
        'metric': 'FilterRuleMetricEnum',
        'duration': 'int',
        'aggregation': 'FilterRuleAggregationEnum'
    }

    attribute_map = {
        'threshold': 'threshold',
        'quantile': 'quantile',
        'op': 'op',
        'metric': 'metric',
        'duration': 'duration',
        'aggregation': 'aggregation'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """FilterRuleInput - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._threshold = None
        self._quantile = None
        self._op = None
        self._metric = None
        self._duration = None
        self._aggregation = None
        self.discriminator = None

        if "threshold" in kwargs:
            self.threshold = kwargs["threshold"]
        if "quantile" in kwargs:
            self.quantile = kwargs["quantile"]
        if "op" in kwargs:
            self.op = kwargs["op"]
        if "metric" in kwargs:
            self.metric = kwargs["metric"]
        if "duration" in kwargs:
            self.duration = kwargs["duration"]
        if "aggregation" in kwargs:
            self.aggregation = kwargs["aggregation"]

    @property
    def threshold(self):
        """Gets the threshold of this FilterRuleInput.  # noqa: E501


        :return: The threshold of this FilterRuleInput.  # noqa: E501
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this FilterRuleInput.


        :param threshold: The threshold of this FilterRuleInput.  # noqa: E501
        :type threshold: float
        """
        if self.local_vars_configuration.client_side_validation and threshold is None:  # noqa: E501
            raise ValueError("Invalid value for `threshold`, must not be `None`")  # noqa: E501

        self._threshold = threshold

    @property
    def quantile(self):
        """Gets the quantile of this FilterRuleInput.  # noqa: E501


        :return: The quantile of this FilterRuleInput.  # noqa: E501
        :rtype: int
        """
        return self._quantile

    @quantile.setter
    def quantile(self, quantile):
        """Sets the quantile of this FilterRuleInput.


        :param quantile: The quantile of this FilterRuleInput.  # noqa: E501
        :type quantile: int
        """
        if self.local_vars_configuration.client_side_validation and quantile is None:  # noqa: E501
            raise ValueError("Invalid value for `quantile`, must not be `None`")  # noqa: E501

        self._quantile = quantile

    @property
    def op(self):
        """Gets the op of this FilterRuleInput.  # noqa: E501


        :return: The op of this FilterRuleInput.  # noqa: E501
        :rtype: FilterRuleOpEnum
        """
        return self._op

    @op.setter
    def op(self, op):
        """Sets the op of this FilterRuleInput.


        :param op: The op of this FilterRuleInput.  # noqa: E501
        :type op: FilterRuleOpEnum
        """
        if self.local_vars_configuration.client_side_validation and op is None:  # noqa: E501
            raise ValueError("Invalid value for `op`, must not be `None`")  # noqa: E501

        self._op = op

    @property
    def metric(self):
        """Gets the metric of this FilterRuleInput.  # noqa: E501


        :return: The metric of this FilterRuleInput.  # noqa: E501
        :rtype: FilterRuleMetricEnum
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this FilterRuleInput.


        :param metric: The metric of this FilterRuleInput.  # noqa: E501
        :type metric: FilterRuleMetricEnum
        """
        if self.local_vars_configuration.client_side_validation and metric is None:  # noqa: E501
            raise ValueError("Invalid value for `metric`, must not be `None`")  # noqa: E501

        self._metric = metric

    @property
    def duration(self):
        """Gets the duration of this FilterRuleInput.  # noqa: E501


        :return: The duration of this FilterRuleInput.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this FilterRuleInput.


        :param duration: The duration of this FilterRuleInput.  # noqa: E501
        :type duration: int
        """
        if self.local_vars_configuration.client_side_validation and duration is None:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def aggregation(self):
        """Gets the aggregation of this FilterRuleInput.  # noqa: E501


        :return: The aggregation of this FilterRuleInput.  # noqa: E501
        :rtype: FilterRuleAggregationEnum
        """
        return self._aggregation

    @aggregation.setter
    def aggregation(self, aggregation):
        """Sets the aggregation of this FilterRuleInput.


        :param aggregation: The aggregation of this FilterRuleInput.  # noqa: E501
        :type aggregation: FilterRuleAggregationEnum
        """
        if self.local_vars_configuration.client_side_validation and aggregation is None:  # noqa: E501
            raise ValueError("Invalid value for `aggregation`, must not be `None`")  # noqa: E501

        self._aggregation = aggregation

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
        if not isinstance(other, FilterRuleInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FilterRuleInput):
            return True

        return self.to_dict() != other.to_dict()
