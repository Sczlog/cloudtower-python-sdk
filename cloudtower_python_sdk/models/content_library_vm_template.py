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


class ContentLibraryVmTemplate(object):
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
        'cloud_init_supported': 'bool',
        'clusters': 'list[NestedCluster]',
        'cpu': 'object',
        'created_at': 'str',
        'description': 'str',
        'entity_async_status': 'EntityAsyncStatus',
        'guest_os_type': 'VmGuestsOperationSystem',
        'id': 'str',
        'labels': 'list[NestedLabel]',
        'memory': 'float',
        'name': 'str',
        'size': 'float',
        'vcpu': 'int',
        'vm_template_uuids': 'list[str]',
        'vm_templates': 'list[NestedVmTemplate]'
    }

    attribute_map = {
        'cloud_init_supported': 'cloud_init_supported',
        'clusters': 'clusters',
        'cpu': 'cpu',
        'created_at': 'createdAt',
        'description': 'description',
        'entity_async_status': 'entityAsyncStatus',
        'guest_os_type': 'guest_os_type',
        'id': 'id',
        'labels': 'labels',
        'memory': 'memory',
        'name': 'name',
        'size': 'size',
        'vcpu': 'vcpu',
        'vm_template_uuids': 'vm_template_uuids',
        'vm_templates': 'vm_templates'
    }

    def __init__(self, cloud_init_supported=None, clusters=None, cpu=None, created_at=None, description=None, entity_async_status=None, guest_os_type=None, id=None, labels=None, memory=None, name=None, size=None, vcpu=None, vm_template_uuids=None, vm_templates=None, local_vars_configuration=None):  # noqa: E501
        """ContentLibraryVmTemplate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cloud_init_supported = None
        self._clusters = None
        self._cpu = None
        self._created_at = None
        self._description = None
        self._entity_async_status = None
        self._guest_os_type = None
        self._id = None
        self._labels = None
        self._memory = None
        self._name = None
        self._size = None
        self._vcpu = None
        self._vm_template_uuids = None
        self._vm_templates = None
        self.discriminator = None

        self.cloud_init_supported = cloud_init_supported
        self.clusters = clusters
        self.cpu = cpu
        self.created_at = created_at
        self.description = description
        self.entity_async_status = entity_async_status
        self.guest_os_type = guest_os_type
        self.id = id
        self.labels = labels
        self.memory = memory
        self.name = name
        self.size = size
        self.vcpu = vcpu
        self.vm_template_uuids = vm_template_uuids
        self.vm_templates = vm_templates

    @property
    def cloud_init_supported(self):
        """Gets the cloud_init_supported of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The cloud_init_supported of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._cloud_init_supported

    @cloud_init_supported.setter
    def cloud_init_supported(self, cloud_init_supported):
        """Sets the cloud_init_supported of this ContentLibraryVmTemplate.


        :param cloud_init_supported: The cloud_init_supported of this ContentLibraryVmTemplate.  # noqa: E501
        :type cloud_init_supported: bool
        """
        if self.local_vars_configuration.client_side_validation and cloud_init_supported is None:  # noqa: E501
            raise ValueError("Invalid value for `cloud_init_supported`, must not be `None`")  # noqa: E501

        self._cloud_init_supported = cloud_init_supported

    @property
    def clusters(self):
        """Gets the clusters of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The clusters of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: list[NestedCluster]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this ContentLibraryVmTemplate.


        :param clusters: The clusters of this ContentLibraryVmTemplate.  # noqa: E501
        :type clusters: list[NestedCluster]
        """

        self._clusters = clusters

    @property
    def cpu(self):
        """Gets the cpu of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The cpu of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: object
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this ContentLibraryVmTemplate.


        :param cpu: The cpu of this ContentLibraryVmTemplate.  # noqa: E501
        :type cpu: object
        """
        if self.local_vars_configuration.client_side_validation and cpu is None:  # noqa: E501
            raise ValueError("Invalid value for `cpu`, must not be `None`")  # noqa: E501

        self._cpu = cpu

    @property
    def created_at(self):
        """Gets the created_at of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The created_at of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ContentLibraryVmTemplate.


        :param created_at: The created_at of this ContentLibraryVmTemplate.  # noqa: E501
        :type created_at: str
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The description of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ContentLibraryVmTemplate.


        :param description: The description of this ContentLibraryVmTemplate.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The entity_async_status of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this ContentLibraryVmTemplate.


        :param entity_async_status: The entity_async_status of this ContentLibraryVmTemplate.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def guest_os_type(self):
        """Gets the guest_os_type of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The guest_os_type of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: VmGuestsOperationSystem
        """
        return self._guest_os_type

    @guest_os_type.setter
    def guest_os_type(self, guest_os_type):
        """Sets the guest_os_type of this ContentLibraryVmTemplate.


        :param guest_os_type: The guest_os_type of this ContentLibraryVmTemplate.  # noqa: E501
        :type guest_os_type: VmGuestsOperationSystem
        """

        self._guest_os_type = guest_os_type

    @property
    def id(self):
        """Gets the id of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The id of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContentLibraryVmTemplate.


        :param id: The id of this ContentLibraryVmTemplate.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def labels(self):
        """Gets the labels of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The labels of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: list[NestedLabel]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ContentLibraryVmTemplate.


        :param labels: The labels of this ContentLibraryVmTemplate.  # noqa: E501
        :type labels: list[NestedLabel]
        """

        self._labels = labels

    @property
    def memory(self):
        """Gets the memory of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The memory of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: float
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this ContentLibraryVmTemplate.


        :param memory: The memory of this ContentLibraryVmTemplate.  # noqa: E501
        :type memory: float
        """
        if self.local_vars_configuration.client_side_validation and memory is None:  # noqa: E501
            raise ValueError("Invalid value for `memory`, must not be `None`")  # noqa: E501

        self._memory = memory

    @property
    def name(self):
        """Gets the name of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The name of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContentLibraryVmTemplate.


        :param name: The name of this ContentLibraryVmTemplate.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def size(self):
        """Gets the size of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The size of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ContentLibraryVmTemplate.


        :param size: The size of this ContentLibraryVmTemplate.  # noqa: E501
        :type size: float
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def vcpu(self):
        """Gets the vcpu of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The vcpu of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: int
        """
        return self._vcpu

    @vcpu.setter
    def vcpu(self, vcpu):
        """Sets the vcpu of this ContentLibraryVmTemplate.


        :param vcpu: The vcpu of this ContentLibraryVmTemplate.  # noqa: E501
        :type vcpu: int
        """
        if self.local_vars_configuration.client_side_validation and vcpu is None:  # noqa: E501
            raise ValueError("Invalid value for `vcpu`, must not be `None`")  # noqa: E501

        self._vcpu = vcpu

    @property
    def vm_template_uuids(self):
        """Gets the vm_template_uuids of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The vm_template_uuids of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._vm_template_uuids

    @vm_template_uuids.setter
    def vm_template_uuids(self, vm_template_uuids):
        """Sets the vm_template_uuids of this ContentLibraryVmTemplate.


        :param vm_template_uuids: The vm_template_uuids of this ContentLibraryVmTemplate.  # noqa: E501
        :type vm_template_uuids: list[str]
        """
        if self.local_vars_configuration.client_side_validation and vm_template_uuids is None:  # noqa: E501
            raise ValueError("Invalid value for `vm_template_uuids`, must not be `None`")  # noqa: E501

        self._vm_template_uuids = vm_template_uuids

    @property
    def vm_templates(self):
        """Gets the vm_templates of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The vm_templates of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: list[NestedVmTemplate]
        """
        return self._vm_templates

    @vm_templates.setter
    def vm_templates(self, vm_templates):
        """Sets the vm_templates of this ContentLibraryVmTemplate.


        :param vm_templates: The vm_templates of this ContentLibraryVmTemplate.  # noqa: E501
        :type vm_templates: list[NestedVmTemplate]
        """

        self._vm_templates = vm_templates

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
        if not isinstance(other, ContentLibraryVmTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContentLibraryVmTemplate):
            return True

        return self.to_dict() != other.to_dict()
