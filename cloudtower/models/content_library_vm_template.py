# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


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
        'architecture': 'Architecture',
        'clock_offset': 'VmClockOffset',
        'cloud_init_supported': 'bool',
        'clusters': 'list[NestedCluster]',
        'cpu': 'NestedCpu',
        'cpu_model': 'str',
        'created_at': 'str',
        'description': 'str',
        'entity_async_status': 'EntityAsyncStatus',
        'firmware': 'VmFirmware',
        'ha': 'bool',
        'id': 'str',
        'io_policy': 'VmDiskIoPolicy',
        'labels': 'list[NestedLabel]',
        'max_bandwidth': 'int',
        'max_bandwidth_policy': 'VmDiskIoRestrictType',
        'max_iops': 'int',
        'max_iops_policy': 'VmDiskIoRestrictType',
        'memory': 'int',
        'name': 'str',
        'os': 'str',
        'size': 'int',
        'template_config': 'NestedTemplateConfig',
        'vcpu': 'int',
        'video_type': 'str',
        'vm_disks': 'list[NestedContentLibraryVmTemplateDisk]',
        'vm_nics': 'list[NestedContentLibraryVmTemplateNic]',
        'vm_template_uuids': 'list[str]',
        'vm_templates': 'list[NestedVmTemplate]',
        'win_opt': 'bool',
        'zbs_storage_info': 'list[NestedZbsStorageInfo]'
    }

    attribute_map = {
        'architecture': 'architecture',
        'clock_offset': 'clock_offset',
        'cloud_init_supported': 'cloud_init_supported',
        'clusters': 'clusters',
        'cpu': 'cpu',
        'cpu_model': 'cpu_model',
        'created_at': 'createdAt',
        'description': 'description',
        'entity_async_status': 'entityAsyncStatus',
        'firmware': 'firmware',
        'ha': 'ha',
        'id': 'id',
        'io_policy': 'io_policy',
        'labels': 'labels',
        'max_bandwidth': 'max_bandwidth',
        'max_bandwidth_policy': 'max_bandwidth_policy',
        'max_iops': 'max_iops',
        'max_iops_policy': 'max_iops_policy',
        'memory': 'memory',
        'name': 'name',
        'os': 'os',
        'size': 'size',
        'template_config': 'template_config',
        'vcpu': 'vcpu',
        'video_type': 'video_type',
        'vm_disks': 'vm_disks',
        'vm_nics': 'vm_nics',
        'vm_template_uuids': 'vm_template_uuids',
        'vm_templates': 'vm_templates',
        'win_opt': 'win_opt',
        'zbs_storage_info': 'zbs_storage_info'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ContentLibraryVmTemplate - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._architecture = None
        self._clock_offset = None
        self._cloud_init_supported = None
        self._clusters = None
        self._cpu = None
        self._cpu_model = None
        self._created_at = None
        self._description = None
        self._entity_async_status = None
        self._firmware = None
        self._ha = None
        self._id = None
        self._io_policy = None
        self._labels = None
        self._max_bandwidth = None
        self._max_bandwidth_policy = None
        self._max_iops = None
        self._max_iops_policy = None
        self._memory = None
        self._name = None
        self._os = None
        self._size = None
        self._template_config = None
        self._vcpu = None
        self._video_type = None
        self._vm_disks = None
        self._vm_nics = None
        self._vm_template_uuids = None
        self._vm_templates = None
        self._win_opt = None
        self._zbs_storage_info = None
        self.discriminator = None

        if "architecture" in kwargs:
            self.architecture = kwargs["architecture"]
        self.clock_offset = kwargs.get("clock_offset", None)
        if "cloud_init_supported" in kwargs:
            self.cloud_init_supported = kwargs["cloud_init_supported"]
        self.clusters = kwargs.get("clusters", None)
        self.cpu = kwargs.get("cpu", None)
        self.cpu_model = kwargs.get("cpu_model", None)
        if "created_at" in kwargs:
            self.created_at = kwargs["created_at"]
        if "description" in kwargs:
            self.description = kwargs["description"]
        self.entity_async_status = kwargs.get("entity_async_status", None)
        self.firmware = kwargs.get("firmware", None)
        self.ha = kwargs.get("ha", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        self.io_policy = kwargs.get("io_policy", None)
        self.labels = kwargs.get("labels", None)
        self.max_bandwidth = kwargs.get("max_bandwidth", None)
        self.max_bandwidth_policy = kwargs.get("max_bandwidth_policy", None)
        self.max_iops = kwargs.get("max_iops", None)
        self.max_iops_policy = kwargs.get("max_iops_policy", None)
        if "memory" in kwargs:
            self.memory = kwargs["memory"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        self.os = kwargs.get("os", None)
        if "size" in kwargs:
            self.size = kwargs["size"]
        self.template_config = kwargs.get("template_config", None)
        if "vcpu" in kwargs:
            self.vcpu = kwargs["vcpu"]
        self.video_type = kwargs.get("video_type", None)
        self.vm_disks = kwargs.get("vm_disks", None)
        self.vm_nics = kwargs.get("vm_nics", None)
        if "vm_template_uuids" in kwargs:
            self.vm_template_uuids = kwargs["vm_template_uuids"]
        self.vm_templates = kwargs.get("vm_templates", None)
        self.win_opt = kwargs.get("win_opt", None)
        self.zbs_storage_info = kwargs.get("zbs_storage_info", None)

    @property
    def architecture(self):
        """Gets the architecture of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The architecture of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: Architecture
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this ContentLibraryVmTemplate.


        :param architecture: The architecture of this ContentLibraryVmTemplate.  # noqa: E501
        :type architecture: Architecture
        """
        if self.local_vars_configuration.client_side_validation and architecture is None:  # noqa: E501
            raise ValueError("Invalid value for `architecture`, must not be `None`")  # noqa: E501

        self._architecture = architecture

    @property
    def clock_offset(self):
        """Gets the clock_offset of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The clock_offset of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: VmClockOffset
        """
        return self._clock_offset

    @clock_offset.setter
    def clock_offset(self, clock_offset):
        """Sets the clock_offset of this ContentLibraryVmTemplate.


        :param clock_offset: The clock_offset of this ContentLibraryVmTemplate.  # noqa: E501
        :type clock_offset: VmClockOffset
        """

        self._clock_offset = clock_offset

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
        :rtype: NestedCpu
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this ContentLibraryVmTemplate.


        :param cpu: The cpu of this ContentLibraryVmTemplate.  # noqa: E501
        :type cpu: NestedCpu
        """

        self._cpu = cpu

    @property
    def cpu_model(self):
        """Gets the cpu_model of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The cpu_model of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: str
        """
        return self._cpu_model

    @cpu_model.setter
    def cpu_model(self, cpu_model):
        """Sets the cpu_model of this ContentLibraryVmTemplate.


        :param cpu_model: The cpu_model of this ContentLibraryVmTemplate.  # noqa: E501
        :type cpu_model: str
        """

        self._cpu_model = cpu_model

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
    def firmware(self):
        """Gets the firmware of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The firmware of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: VmFirmware
        """
        return self._firmware

    @firmware.setter
    def firmware(self, firmware):
        """Sets the firmware of this ContentLibraryVmTemplate.


        :param firmware: The firmware of this ContentLibraryVmTemplate.  # noqa: E501
        :type firmware: VmFirmware
        """

        self._firmware = firmware

    @property
    def ha(self):
        """Gets the ha of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The ha of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._ha

    @ha.setter
    def ha(self, ha):
        """Sets the ha of this ContentLibraryVmTemplate.


        :param ha: The ha of this ContentLibraryVmTemplate.  # noqa: E501
        :type ha: bool
        """

        self._ha = ha

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
    def io_policy(self):
        """Gets the io_policy of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The io_policy of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: VmDiskIoPolicy
        """
        return self._io_policy

    @io_policy.setter
    def io_policy(self, io_policy):
        """Sets the io_policy of this ContentLibraryVmTemplate.


        :param io_policy: The io_policy of this ContentLibraryVmTemplate.  # noqa: E501
        :type io_policy: VmDiskIoPolicy
        """

        self._io_policy = io_policy

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
    def max_bandwidth(self):
        """Gets the max_bandwidth of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The max_bandwidth of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: int
        """
        return self._max_bandwidth

    @max_bandwidth.setter
    def max_bandwidth(self, max_bandwidth):
        """Sets the max_bandwidth of this ContentLibraryVmTemplate.


        :param max_bandwidth: The max_bandwidth of this ContentLibraryVmTemplate.  # noqa: E501
        :type max_bandwidth: int
        """

        self._max_bandwidth = max_bandwidth

    @property
    def max_bandwidth_policy(self):
        """Gets the max_bandwidth_policy of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The max_bandwidth_policy of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: VmDiskIoRestrictType
        """
        return self._max_bandwidth_policy

    @max_bandwidth_policy.setter
    def max_bandwidth_policy(self, max_bandwidth_policy):
        """Sets the max_bandwidth_policy of this ContentLibraryVmTemplate.


        :param max_bandwidth_policy: The max_bandwidth_policy of this ContentLibraryVmTemplate.  # noqa: E501
        :type max_bandwidth_policy: VmDiskIoRestrictType
        """

        self._max_bandwidth_policy = max_bandwidth_policy

    @property
    def max_iops(self):
        """Gets the max_iops of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The max_iops of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: int
        """
        return self._max_iops

    @max_iops.setter
    def max_iops(self, max_iops):
        """Sets the max_iops of this ContentLibraryVmTemplate.


        :param max_iops: The max_iops of this ContentLibraryVmTemplate.  # noqa: E501
        :type max_iops: int
        """

        self._max_iops = max_iops

    @property
    def max_iops_policy(self):
        """Gets the max_iops_policy of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The max_iops_policy of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: VmDiskIoRestrictType
        """
        return self._max_iops_policy

    @max_iops_policy.setter
    def max_iops_policy(self, max_iops_policy):
        """Sets the max_iops_policy of this ContentLibraryVmTemplate.


        :param max_iops_policy: The max_iops_policy of this ContentLibraryVmTemplate.  # noqa: E501
        :type max_iops_policy: VmDiskIoRestrictType
        """

        self._max_iops_policy = max_iops_policy

    @property
    def memory(self):
        """Gets the memory of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The memory of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this ContentLibraryVmTemplate.


        :param memory: The memory of this ContentLibraryVmTemplate.  # noqa: E501
        :type memory: int
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
    def os(self):
        """Gets the os of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The os of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this ContentLibraryVmTemplate.


        :param os: The os of this ContentLibraryVmTemplate.  # noqa: E501
        :type os: str
        """

        self._os = os

    @property
    def size(self):
        """Gets the size of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The size of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ContentLibraryVmTemplate.


        :param size: The size of this ContentLibraryVmTemplate.  # noqa: E501
        :type size: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def template_config(self):
        """Gets the template_config of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The template_config of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: NestedTemplateConfig
        """
        return self._template_config

    @template_config.setter
    def template_config(self, template_config):
        """Sets the template_config of this ContentLibraryVmTemplate.


        :param template_config: The template_config of this ContentLibraryVmTemplate.  # noqa: E501
        :type template_config: NestedTemplateConfig
        """

        self._template_config = template_config

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
    def video_type(self):
        """Gets the video_type of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The video_type of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: str
        """
        return self._video_type

    @video_type.setter
    def video_type(self, video_type):
        """Sets the video_type of this ContentLibraryVmTemplate.


        :param video_type: The video_type of this ContentLibraryVmTemplate.  # noqa: E501
        :type video_type: str
        """

        self._video_type = video_type

    @property
    def vm_disks(self):
        """Gets the vm_disks of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The vm_disks of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: list[NestedContentLibraryVmTemplateDisk]
        """
        return self._vm_disks

    @vm_disks.setter
    def vm_disks(self, vm_disks):
        """Sets the vm_disks of this ContentLibraryVmTemplate.


        :param vm_disks: The vm_disks of this ContentLibraryVmTemplate.  # noqa: E501
        :type vm_disks: list[NestedContentLibraryVmTemplateDisk]
        """

        self._vm_disks = vm_disks

    @property
    def vm_nics(self):
        """Gets the vm_nics of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The vm_nics of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: list[NestedContentLibraryVmTemplateNic]
        """
        return self._vm_nics

    @vm_nics.setter
    def vm_nics(self, vm_nics):
        """Sets the vm_nics of this ContentLibraryVmTemplate.


        :param vm_nics: The vm_nics of this ContentLibraryVmTemplate.  # noqa: E501
        :type vm_nics: list[NestedContentLibraryVmTemplateNic]
        """

        self._vm_nics = vm_nics

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

    @property
    def win_opt(self):
        """Gets the win_opt of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The win_opt of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._win_opt

    @win_opt.setter
    def win_opt(self, win_opt):
        """Sets the win_opt of this ContentLibraryVmTemplate.


        :param win_opt: The win_opt of this ContentLibraryVmTemplate.  # noqa: E501
        :type win_opt: bool
        """

        self._win_opt = win_opt

    @property
    def zbs_storage_info(self):
        """Gets the zbs_storage_info of this ContentLibraryVmTemplate.  # noqa: E501


        :return: The zbs_storage_info of this ContentLibraryVmTemplate.  # noqa: E501
        :rtype: list[NestedZbsStorageInfo]
        """
        return self._zbs_storage_info

    @zbs_storage_info.setter
    def zbs_storage_info(self, zbs_storage_info):
        """Sets the zbs_storage_info of this ContentLibraryVmTemplate.


        :param zbs_storage_info: The zbs_storage_info of this ContentLibraryVmTemplate.  # noqa: E501
        :type zbs_storage_info: list[NestedZbsStorageInfo]
        """

        self._zbs_storage_info = zbs_storage_info

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
