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


class SnapshotPlanUpdationParamsData(object):
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
        'vm_ids': 'list[str]',
        'execute_intervals': 'list[int]',
        'execute_plan_type': 'SnapshotPlanExecuteType',
        'exec_h_m': 'str',
        'end_time': 'str',
        'remain_snapshot_num': 'int',
        'name': 'str'
    }

    attribute_map = {
        'vm_ids': 'vm_ids',
        'execute_intervals': 'execute_intervals',
        'execute_plan_type': 'execute_plan_type',
        'exec_h_m': 'exec_h_m',
        'end_time': 'end_time',
        'remain_snapshot_num': 'remain_snapshot_num',
        'name': 'name'
    }

    def __init__(self, vm_ids=None, execute_intervals=None, execute_plan_type=None, exec_h_m=None, end_time=None, remain_snapshot_num=None, name=None, local_vars_configuration=None):  # noqa: E501
        """SnapshotPlanUpdationParamsData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._vm_ids = None
        self._execute_intervals = None
        self._execute_plan_type = None
        self._exec_h_m = None
        self._end_time = None
        self._remain_snapshot_num = None
        self._name = None
        self.discriminator = None

        if vm_ids is not None:
            self.vm_ids = vm_ids
        if execute_intervals is not None:
            self.execute_intervals = execute_intervals
        if execute_plan_type is not None:
            self.execute_plan_type = execute_plan_type
        if exec_h_m is not None:
            self.exec_h_m = exec_h_m
        if end_time is not None:
            self.end_time = end_time
        if remain_snapshot_num is not None:
            self.remain_snapshot_num = remain_snapshot_num
        if name is not None:
            self.name = name

    @property
    def vm_ids(self):
        """Gets the vm_ids of this SnapshotPlanUpdationParamsData.  # noqa: E501


        :return: The vm_ids of this SnapshotPlanUpdationParamsData.  # noqa: E501
        :rtype: list[str]
        """
        return self._vm_ids

    @vm_ids.setter
    def vm_ids(self, vm_ids):
        """Sets the vm_ids of this SnapshotPlanUpdationParamsData.


        :param vm_ids: The vm_ids of this SnapshotPlanUpdationParamsData.  # noqa: E501
        :type vm_ids: list[str]
        """

        self._vm_ids = vm_ids

    @property
    def execute_intervals(self):
        """Gets the execute_intervals of this SnapshotPlanUpdationParamsData.  # noqa: E501


        :return: The execute_intervals of this SnapshotPlanUpdationParamsData.  # noqa: E501
        :rtype: list[int]
        """
        return self._execute_intervals

    @execute_intervals.setter
    def execute_intervals(self, execute_intervals):
        """Sets the execute_intervals of this SnapshotPlanUpdationParamsData.


        :param execute_intervals: The execute_intervals of this SnapshotPlanUpdationParamsData.  # noqa: E501
        :type execute_intervals: list[int]
        """

        self._execute_intervals = execute_intervals

    @property
    def execute_plan_type(self):
        """Gets the execute_plan_type of this SnapshotPlanUpdationParamsData.  # noqa: E501


        :return: The execute_plan_type of this SnapshotPlanUpdationParamsData.  # noqa: E501
        :rtype: SnapshotPlanExecuteType
        """
        return self._execute_plan_type

    @execute_plan_type.setter
    def execute_plan_type(self, execute_plan_type):
        """Sets the execute_plan_type of this SnapshotPlanUpdationParamsData.


        :param execute_plan_type: The execute_plan_type of this SnapshotPlanUpdationParamsData.  # noqa: E501
        :type execute_plan_type: SnapshotPlanExecuteType
        """

        self._execute_plan_type = execute_plan_type

    @property
    def exec_h_m(self):
        """Gets the exec_h_m of this SnapshotPlanUpdationParamsData.  # noqa: E501


        :return: The exec_h_m of this SnapshotPlanUpdationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._exec_h_m

    @exec_h_m.setter
    def exec_h_m(self, exec_h_m):
        """Sets the exec_h_m of this SnapshotPlanUpdationParamsData.


        :param exec_h_m: The exec_h_m of this SnapshotPlanUpdationParamsData.  # noqa: E501
        :type exec_h_m: str
        """

        self._exec_h_m = exec_h_m

    @property
    def end_time(self):
        """Gets the end_time of this SnapshotPlanUpdationParamsData.  # noqa: E501


        :return: The end_time of this SnapshotPlanUpdationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this SnapshotPlanUpdationParamsData.


        :param end_time: The end_time of this SnapshotPlanUpdationParamsData.  # noqa: E501
        :type end_time: str
        """

        self._end_time = end_time

    @property
    def remain_snapshot_num(self):
        """Gets the remain_snapshot_num of this SnapshotPlanUpdationParamsData.  # noqa: E501


        :return: The remain_snapshot_num of this SnapshotPlanUpdationParamsData.  # noqa: E501
        :rtype: int
        """
        return self._remain_snapshot_num

    @remain_snapshot_num.setter
    def remain_snapshot_num(self, remain_snapshot_num):
        """Sets the remain_snapshot_num of this SnapshotPlanUpdationParamsData.


        :param remain_snapshot_num: The remain_snapshot_num of this SnapshotPlanUpdationParamsData.  # noqa: E501
        :type remain_snapshot_num: int
        """

        self._remain_snapshot_num = remain_snapshot_num

    @property
    def name(self):
        """Gets the name of this SnapshotPlanUpdationParamsData.  # noqa: E501


        :return: The name of this SnapshotPlanUpdationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SnapshotPlanUpdationParamsData.


        :param name: The name of this SnapshotPlanUpdationParamsData.  # noqa: E501
        :type name: str
        """

        self._name = name

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
        if not isinstance(other, SnapshotPlanUpdationParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnapshotPlanUpdationParamsData):
            return True

        return self.to_dict() != other.to_dict()
