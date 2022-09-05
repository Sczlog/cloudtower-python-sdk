# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class EverouteCluster(object):
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
        'agent_elf_clusters': 'list[NestedCluster]',
        'agent_elf_vdses': 'list[NestedVds]',
        'controller_instances': 'list[NestedEverouteControllerInstance]',
        'controller_template': 'NestedEverouteControllerTemplate',
        'entity_async_status': 'EntityAsyncStatus',
        'global_default_action': 'GlobalPolicyAction',
        'global_whitelist': 'NestedEverouteClusterWhitelist',
        'id': 'str',
        'installed': 'bool',
        'name': 'str',
        'phase': 'EverouteClusterPhase',
        'status': 'NestedEverouteClusterStatus',
        'version': 'str'
    }

    attribute_map = {
        'agent_elf_clusters': 'agent_elf_clusters',
        'agent_elf_vdses': 'agent_elf_vdses',
        'controller_instances': 'controller_instances',
        'controller_template': 'controller_template',
        'entity_async_status': 'entityAsyncStatus',
        'global_default_action': 'global_default_action',
        'global_whitelist': 'global_whitelist',
        'id': 'id',
        'installed': 'installed',
        'name': 'name',
        'phase': 'phase',
        'status': 'status',
        'version': 'version'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """EverouteCluster - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._agent_elf_clusters = None
        self._agent_elf_vdses = None
        self._controller_instances = None
        self._controller_template = None
        self._entity_async_status = None
        self._global_default_action = None
        self._global_whitelist = None
        self._id = None
        self._installed = None
        self._name = None
        self._phase = None
        self._status = None
        self._version = None
        self.discriminator = None

        self.agent_elf_clusters = kwargs.get("agent_elf_clusters", None)
        self.agent_elf_vdses = kwargs.get("agent_elf_vdses", None)
        if "controller_instances" in kwargs:
            self.controller_instances = kwargs["controller_instances"]
        if "controller_template" in kwargs:
            self.controller_template = kwargs["controller_template"]
        self.entity_async_status = kwargs.get("entity_async_status", None)
        if "global_default_action" in kwargs:
            self.global_default_action = kwargs["global_default_action"]
        self.global_whitelist = kwargs.get("global_whitelist", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        self.installed = kwargs.get("installed", None)
        if "name" in kwargs:
            self.name = kwargs["name"]
        self.phase = kwargs.get("phase", None)
        if "status" in kwargs:
            self.status = kwargs["status"]
        if "version" in kwargs:
            self.version = kwargs["version"]

    @property
    def agent_elf_clusters(self):
        """Gets the agent_elf_clusters of this EverouteCluster.  # noqa: E501


        :return: The agent_elf_clusters of this EverouteCluster.  # noqa: E501
        :rtype: list[NestedCluster]
        """
        return self._agent_elf_clusters

    @agent_elf_clusters.setter
    def agent_elf_clusters(self, agent_elf_clusters):
        """Sets the agent_elf_clusters of this EverouteCluster.


        :param agent_elf_clusters: The agent_elf_clusters of this EverouteCluster.  # noqa: E501
        :type agent_elf_clusters: list[NestedCluster]
        """

        self._agent_elf_clusters = agent_elf_clusters

    @property
    def agent_elf_vdses(self):
        """Gets the agent_elf_vdses of this EverouteCluster.  # noqa: E501


        :return: The agent_elf_vdses of this EverouteCluster.  # noqa: E501
        :rtype: list[NestedVds]
        """
        return self._agent_elf_vdses

    @agent_elf_vdses.setter
    def agent_elf_vdses(self, agent_elf_vdses):
        """Sets the agent_elf_vdses of this EverouteCluster.


        :param agent_elf_vdses: The agent_elf_vdses of this EverouteCluster.  # noqa: E501
        :type agent_elf_vdses: list[NestedVds]
        """

        self._agent_elf_vdses = agent_elf_vdses

    @property
    def controller_instances(self):
        """Gets the controller_instances of this EverouteCluster.  # noqa: E501


        :return: The controller_instances of this EverouteCluster.  # noqa: E501
        :rtype: list[NestedEverouteControllerInstance]
        """
        return self._controller_instances

    @controller_instances.setter
    def controller_instances(self, controller_instances):
        """Sets the controller_instances of this EverouteCluster.


        :param controller_instances: The controller_instances of this EverouteCluster.  # noqa: E501
        :type controller_instances: list[NestedEverouteControllerInstance]
        """
        if self.local_vars_configuration.client_side_validation and controller_instances is None:  # noqa: E501
            raise ValueError("Invalid value for `controller_instances`, must not be `None`")  # noqa: E501

        self._controller_instances = controller_instances

    @property
    def controller_template(self):
        """Gets the controller_template of this EverouteCluster.  # noqa: E501


        :return: The controller_template of this EverouteCluster.  # noqa: E501
        :rtype: NestedEverouteControllerTemplate
        """
        return self._controller_template

    @controller_template.setter
    def controller_template(self, controller_template):
        """Sets the controller_template of this EverouteCluster.


        :param controller_template: The controller_template of this EverouteCluster.  # noqa: E501
        :type controller_template: NestedEverouteControllerTemplate
        """
        if self.local_vars_configuration.client_side_validation and controller_template is None:  # noqa: E501
            raise ValueError("Invalid value for `controller_template`, must not be `None`")  # noqa: E501

        self._controller_template = controller_template

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this EverouteCluster.  # noqa: E501


        :return: The entity_async_status of this EverouteCluster.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this EverouteCluster.


        :param entity_async_status: The entity_async_status of this EverouteCluster.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def global_default_action(self):
        """Gets the global_default_action of this EverouteCluster.  # noqa: E501


        :return: The global_default_action of this EverouteCluster.  # noqa: E501
        :rtype: GlobalPolicyAction
        """
        return self._global_default_action

    @global_default_action.setter
    def global_default_action(self, global_default_action):
        """Sets the global_default_action of this EverouteCluster.


        :param global_default_action: The global_default_action of this EverouteCluster.  # noqa: E501
        :type global_default_action: GlobalPolicyAction
        """
        if self.local_vars_configuration.client_side_validation and global_default_action is None:  # noqa: E501
            raise ValueError("Invalid value for `global_default_action`, must not be `None`")  # noqa: E501

        self._global_default_action = global_default_action

    @property
    def global_whitelist(self):
        """Gets the global_whitelist of this EverouteCluster.  # noqa: E501


        :return: The global_whitelist of this EverouteCluster.  # noqa: E501
        :rtype: NestedEverouteClusterWhitelist
        """
        return self._global_whitelist

    @global_whitelist.setter
    def global_whitelist(self, global_whitelist):
        """Sets the global_whitelist of this EverouteCluster.


        :param global_whitelist: The global_whitelist of this EverouteCluster.  # noqa: E501
        :type global_whitelist: NestedEverouteClusterWhitelist
        """

        self._global_whitelist = global_whitelist

    @property
    def id(self):
        """Gets the id of this EverouteCluster.  # noqa: E501


        :return: The id of this EverouteCluster.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EverouteCluster.


        :param id: The id of this EverouteCluster.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def installed(self):
        """Gets the installed of this EverouteCluster.  # noqa: E501


        :return: The installed of this EverouteCluster.  # noqa: E501
        :rtype: bool
        """
        return self._installed

    @installed.setter
    def installed(self, installed):
        """Sets the installed of this EverouteCluster.


        :param installed: The installed of this EverouteCluster.  # noqa: E501
        :type installed: bool
        """

        self._installed = installed

    @property
    def name(self):
        """Gets the name of this EverouteCluster.  # noqa: E501


        :return: The name of this EverouteCluster.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EverouteCluster.


        :param name: The name of this EverouteCluster.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def phase(self):
        """Gets the phase of this EverouteCluster.  # noqa: E501


        :return: The phase of this EverouteCluster.  # noqa: E501
        :rtype: EverouteClusterPhase
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this EverouteCluster.


        :param phase: The phase of this EverouteCluster.  # noqa: E501
        :type phase: EverouteClusterPhase
        """

        self._phase = phase

    @property
    def status(self):
        """Gets the status of this EverouteCluster.  # noqa: E501


        :return: The status of this EverouteCluster.  # noqa: E501
        :rtype: NestedEverouteClusterStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EverouteCluster.


        :param status: The status of this EverouteCluster.  # noqa: E501
        :type status: NestedEverouteClusterStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def version(self):
        """Gets the version of this EverouteCluster.  # noqa: E501


        :return: The version of this EverouteCluster.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this EverouteCluster.


        :param version: The version of this EverouteCluster.  # noqa: E501
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
        if not isinstance(other, EverouteCluster):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EverouteCluster):
            return True

        return self.to_dict() != other.to_dict()
