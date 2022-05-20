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


class AddLabelsToResourcesParamsData(object):
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
        'vms': 'VmWhereInput',
        'vm_volumes': 'VmVolumeWhereInput',
        'vm_templates': 'VmTemplateWhereInput',
        'vm_snapshots': 'VmSnapshotWhereInput',
        'vlans': 'VlanWhereInput',
        'vdses': 'VdsWhereInput',
        'nvmf_subsystems': 'NvmfSubsystemWhereInput',
        'nvmf_namespace_snapshots': 'NvmfNamespaceSnapshotWhereInput',
        'nvmf_namespaces': 'NvmfNamespaceWhereInput',
        'nics': 'NicWhereInput',
        'nfs_inodes': 'NfsInodeWhereInput',
        'nfs_exports': 'NfsExportWhereInput',
        'namespace_groups': 'NamespaceGroupWhereInput',
        'iscsi_targets': 'IscsiTargetWhereInput',
        'iscsi_lun_snapshots': 'IscsiLunSnapshotWhereInput',
        'iscsi_luns': 'IscsiLunWhereInput',
        'hosts': 'HostWhereInput',
        'elf_images': 'ElfImageWhereInput',
        'disks': 'DiskWhereInput',
        'datacenters': 'DatacenterWhereInput',
        'consistency_group_snapshots': 'ConsistencyGroupSnapshotWhereInput',
        'consistency_groups': 'ConsistencyGroupWhereInput',
        'clusters': 'ClusterWhereInput'
    }

    attribute_map = {
        'vms': 'vms',
        'vm_volumes': 'vm_volumes',
        'vm_templates': 'vm_templates',
        'vm_snapshots': 'vm_snapshots',
        'vlans': 'vlans',
        'vdses': 'vdses',
        'nvmf_subsystems': 'nvmf_subsystems',
        'nvmf_namespace_snapshots': 'nvmf_namespace_snapshots',
        'nvmf_namespaces': 'nvmf_namespaces',
        'nics': 'nics',
        'nfs_inodes': 'nfs_inodes',
        'nfs_exports': 'nfs_exports',
        'namespace_groups': 'namespace_groups',
        'iscsi_targets': 'iscsi_targets',
        'iscsi_lun_snapshots': 'iscsi_lun_snapshots',
        'iscsi_luns': 'iscsi_luns',
        'hosts': 'hosts',
        'elf_images': 'elf_images',
        'disks': 'disks',
        'datacenters': 'datacenters',
        'consistency_group_snapshots': 'consistency_group_snapshots',
        'consistency_groups': 'consistency_groups',
        'clusters': 'clusters'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """AddLabelsToResourcesParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._vms = None
        self._vm_volumes = None
        self._vm_templates = None
        self._vm_snapshots = None
        self._vlans = None
        self._vdses = None
        self._nvmf_subsystems = None
        self._nvmf_namespace_snapshots = None
        self._nvmf_namespaces = None
        self._nics = None
        self._nfs_inodes = None
        self._nfs_exports = None
        self._namespace_groups = None
        self._iscsi_targets = None
        self._iscsi_lun_snapshots = None
        self._iscsi_luns = None
        self._hosts = None
        self._elf_images = None
        self._disks = None
        self._datacenters = None
        self._consistency_group_snapshots = None
        self._consistency_groups = None
        self._clusters = None
        self.discriminator = None

        if "vms" in kwargs:
            self.vms = kwargs["vms"]
        if "vm_volumes" in kwargs:
            self.vm_volumes = kwargs["vm_volumes"]
        if "vm_templates" in kwargs:
            self.vm_templates = kwargs["vm_templates"]
        if "vm_snapshots" in kwargs:
            self.vm_snapshots = kwargs["vm_snapshots"]
        if "vlans" in kwargs:
            self.vlans = kwargs["vlans"]
        if "vdses" in kwargs:
            self.vdses = kwargs["vdses"]
        if "nvmf_subsystems" in kwargs:
            self.nvmf_subsystems = kwargs["nvmf_subsystems"]
        if "nvmf_namespace_snapshots" in kwargs:
            self.nvmf_namespace_snapshots = kwargs["nvmf_namespace_snapshots"]
        if "nvmf_namespaces" in kwargs:
            self.nvmf_namespaces = kwargs["nvmf_namespaces"]
        if "nics" in kwargs:
            self.nics = kwargs["nics"]
        if "nfs_inodes" in kwargs:
            self.nfs_inodes = kwargs["nfs_inodes"]
        if "nfs_exports" in kwargs:
            self.nfs_exports = kwargs["nfs_exports"]
        if "namespace_groups" in kwargs:
            self.namespace_groups = kwargs["namespace_groups"]
        if "iscsi_targets" in kwargs:
            self.iscsi_targets = kwargs["iscsi_targets"]
        if "iscsi_lun_snapshots" in kwargs:
            self.iscsi_lun_snapshots = kwargs["iscsi_lun_snapshots"]
        if "iscsi_luns" in kwargs:
            self.iscsi_luns = kwargs["iscsi_luns"]
        if "hosts" in kwargs:
            self.hosts = kwargs["hosts"]
        if "elf_images" in kwargs:
            self.elf_images = kwargs["elf_images"]
        if "disks" in kwargs:
            self.disks = kwargs["disks"]
        if "datacenters" in kwargs:
            self.datacenters = kwargs["datacenters"]
        if "consistency_group_snapshots" in kwargs:
            self.consistency_group_snapshots = kwargs["consistency_group_snapshots"]
        if "consistency_groups" in kwargs:
            self.consistency_groups = kwargs["consistency_groups"]
        if "clusters" in kwargs:
            self.clusters = kwargs["clusters"]

    @property
    def vms(self):
        """Gets the vms of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The vms of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: VmWhereInput
        """
        return self._vms

    @vms.setter
    def vms(self, vms):
        """Sets the vms of this AddLabelsToResourcesParamsData.


        :param vms: The vms of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type vms: VmWhereInput
        """

        self._vms = vms

    @property
    def vm_volumes(self):
        """Gets the vm_volumes of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The vm_volumes of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: VmVolumeWhereInput
        """
        return self._vm_volumes

    @vm_volumes.setter
    def vm_volumes(self, vm_volumes):
        """Sets the vm_volumes of this AddLabelsToResourcesParamsData.


        :param vm_volumes: The vm_volumes of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type vm_volumes: VmVolumeWhereInput
        """

        self._vm_volumes = vm_volumes

    @property
    def vm_templates(self):
        """Gets the vm_templates of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The vm_templates of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: VmTemplateWhereInput
        """
        return self._vm_templates

    @vm_templates.setter
    def vm_templates(self, vm_templates):
        """Sets the vm_templates of this AddLabelsToResourcesParamsData.


        :param vm_templates: The vm_templates of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type vm_templates: VmTemplateWhereInput
        """

        self._vm_templates = vm_templates

    @property
    def vm_snapshots(self):
        """Gets the vm_snapshots of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The vm_snapshots of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: VmSnapshotWhereInput
        """
        return self._vm_snapshots

    @vm_snapshots.setter
    def vm_snapshots(self, vm_snapshots):
        """Sets the vm_snapshots of this AddLabelsToResourcesParamsData.


        :param vm_snapshots: The vm_snapshots of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type vm_snapshots: VmSnapshotWhereInput
        """

        self._vm_snapshots = vm_snapshots

    @property
    def vlans(self):
        """Gets the vlans of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The vlans of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: VlanWhereInput
        """
        return self._vlans

    @vlans.setter
    def vlans(self, vlans):
        """Sets the vlans of this AddLabelsToResourcesParamsData.


        :param vlans: The vlans of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type vlans: VlanWhereInput
        """

        self._vlans = vlans

    @property
    def vdses(self):
        """Gets the vdses of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The vdses of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: VdsWhereInput
        """
        return self._vdses

    @vdses.setter
    def vdses(self, vdses):
        """Sets the vdses of this AddLabelsToResourcesParamsData.


        :param vdses: The vdses of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type vdses: VdsWhereInput
        """

        self._vdses = vdses

    @property
    def nvmf_subsystems(self):
        """Gets the nvmf_subsystems of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The nvmf_subsystems of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: NvmfSubsystemWhereInput
        """
        return self._nvmf_subsystems

    @nvmf_subsystems.setter
    def nvmf_subsystems(self, nvmf_subsystems):
        """Sets the nvmf_subsystems of this AddLabelsToResourcesParamsData.


        :param nvmf_subsystems: The nvmf_subsystems of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type nvmf_subsystems: NvmfSubsystemWhereInput
        """

        self._nvmf_subsystems = nvmf_subsystems

    @property
    def nvmf_namespace_snapshots(self):
        """Gets the nvmf_namespace_snapshots of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The nvmf_namespace_snapshots of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: NvmfNamespaceSnapshotWhereInput
        """
        return self._nvmf_namespace_snapshots

    @nvmf_namespace_snapshots.setter
    def nvmf_namespace_snapshots(self, nvmf_namespace_snapshots):
        """Sets the nvmf_namespace_snapshots of this AddLabelsToResourcesParamsData.


        :param nvmf_namespace_snapshots: The nvmf_namespace_snapshots of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type nvmf_namespace_snapshots: NvmfNamespaceSnapshotWhereInput
        """

        self._nvmf_namespace_snapshots = nvmf_namespace_snapshots

    @property
    def nvmf_namespaces(self):
        """Gets the nvmf_namespaces of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The nvmf_namespaces of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: NvmfNamespaceWhereInput
        """
        return self._nvmf_namespaces

    @nvmf_namespaces.setter
    def nvmf_namespaces(self, nvmf_namespaces):
        """Sets the nvmf_namespaces of this AddLabelsToResourcesParamsData.


        :param nvmf_namespaces: The nvmf_namespaces of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type nvmf_namespaces: NvmfNamespaceWhereInput
        """

        self._nvmf_namespaces = nvmf_namespaces

    @property
    def nics(self):
        """Gets the nics of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The nics of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: NicWhereInput
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this AddLabelsToResourcesParamsData.


        :param nics: The nics of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type nics: NicWhereInput
        """

        self._nics = nics

    @property
    def nfs_inodes(self):
        """Gets the nfs_inodes of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The nfs_inodes of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: NfsInodeWhereInput
        """
        return self._nfs_inodes

    @nfs_inodes.setter
    def nfs_inodes(self, nfs_inodes):
        """Sets the nfs_inodes of this AddLabelsToResourcesParamsData.


        :param nfs_inodes: The nfs_inodes of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type nfs_inodes: NfsInodeWhereInput
        """

        self._nfs_inodes = nfs_inodes

    @property
    def nfs_exports(self):
        """Gets the nfs_exports of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The nfs_exports of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: NfsExportWhereInput
        """
        return self._nfs_exports

    @nfs_exports.setter
    def nfs_exports(self, nfs_exports):
        """Sets the nfs_exports of this AddLabelsToResourcesParamsData.


        :param nfs_exports: The nfs_exports of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type nfs_exports: NfsExportWhereInput
        """

        self._nfs_exports = nfs_exports

    @property
    def namespace_groups(self):
        """Gets the namespace_groups of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The namespace_groups of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: NamespaceGroupWhereInput
        """
        return self._namespace_groups

    @namespace_groups.setter
    def namespace_groups(self, namespace_groups):
        """Sets the namespace_groups of this AddLabelsToResourcesParamsData.


        :param namespace_groups: The namespace_groups of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type namespace_groups: NamespaceGroupWhereInput
        """

        self._namespace_groups = namespace_groups

    @property
    def iscsi_targets(self):
        """Gets the iscsi_targets of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The iscsi_targets of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: IscsiTargetWhereInput
        """
        return self._iscsi_targets

    @iscsi_targets.setter
    def iscsi_targets(self, iscsi_targets):
        """Sets the iscsi_targets of this AddLabelsToResourcesParamsData.


        :param iscsi_targets: The iscsi_targets of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type iscsi_targets: IscsiTargetWhereInput
        """

        self._iscsi_targets = iscsi_targets

    @property
    def iscsi_lun_snapshots(self):
        """Gets the iscsi_lun_snapshots of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The iscsi_lun_snapshots of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: IscsiLunSnapshotWhereInput
        """
        return self._iscsi_lun_snapshots

    @iscsi_lun_snapshots.setter
    def iscsi_lun_snapshots(self, iscsi_lun_snapshots):
        """Sets the iscsi_lun_snapshots of this AddLabelsToResourcesParamsData.


        :param iscsi_lun_snapshots: The iscsi_lun_snapshots of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type iscsi_lun_snapshots: IscsiLunSnapshotWhereInput
        """

        self._iscsi_lun_snapshots = iscsi_lun_snapshots

    @property
    def iscsi_luns(self):
        """Gets the iscsi_luns of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The iscsi_luns of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: IscsiLunWhereInput
        """
        return self._iscsi_luns

    @iscsi_luns.setter
    def iscsi_luns(self, iscsi_luns):
        """Sets the iscsi_luns of this AddLabelsToResourcesParamsData.


        :param iscsi_luns: The iscsi_luns of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type iscsi_luns: IscsiLunWhereInput
        """

        self._iscsi_luns = iscsi_luns

    @property
    def hosts(self):
        """Gets the hosts of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The hosts of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: HostWhereInput
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this AddLabelsToResourcesParamsData.


        :param hosts: The hosts of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type hosts: HostWhereInput
        """

        self._hosts = hosts

    @property
    def elf_images(self):
        """Gets the elf_images of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The elf_images of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: ElfImageWhereInput
        """
        return self._elf_images

    @elf_images.setter
    def elf_images(self, elf_images):
        """Sets the elf_images of this AddLabelsToResourcesParamsData.


        :param elf_images: The elf_images of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type elf_images: ElfImageWhereInput
        """

        self._elf_images = elf_images

    @property
    def disks(self):
        """Gets the disks of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The disks of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: DiskWhereInput
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this AddLabelsToResourcesParamsData.


        :param disks: The disks of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type disks: DiskWhereInput
        """

        self._disks = disks

    @property
    def datacenters(self):
        """Gets the datacenters of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The datacenters of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: DatacenterWhereInput
        """
        return self._datacenters

    @datacenters.setter
    def datacenters(self, datacenters):
        """Sets the datacenters of this AddLabelsToResourcesParamsData.


        :param datacenters: The datacenters of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type datacenters: DatacenterWhereInput
        """

        self._datacenters = datacenters

    @property
    def consistency_group_snapshots(self):
        """Gets the consistency_group_snapshots of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The consistency_group_snapshots of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: ConsistencyGroupSnapshotWhereInput
        """
        return self._consistency_group_snapshots

    @consistency_group_snapshots.setter
    def consistency_group_snapshots(self, consistency_group_snapshots):
        """Sets the consistency_group_snapshots of this AddLabelsToResourcesParamsData.


        :param consistency_group_snapshots: The consistency_group_snapshots of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type consistency_group_snapshots: ConsistencyGroupSnapshotWhereInput
        """

        self._consistency_group_snapshots = consistency_group_snapshots

    @property
    def consistency_groups(self):
        """Gets the consistency_groups of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The consistency_groups of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: ConsistencyGroupWhereInput
        """
        return self._consistency_groups

    @consistency_groups.setter
    def consistency_groups(self, consistency_groups):
        """Sets the consistency_groups of this AddLabelsToResourcesParamsData.


        :param consistency_groups: The consistency_groups of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type consistency_groups: ConsistencyGroupWhereInput
        """

        self._consistency_groups = consistency_groups

    @property
    def clusters(self):
        """Gets the clusters of this AddLabelsToResourcesParamsData.  # noqa: E501


        :return: The clusters of this AddLabelsToResourcesParamsData.  # noqa: E501
        :rtype: ClusterWhereInput
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this AddLabelsToResourcesParamsData.


        :param clusters: The clusters of this AddLabelsToResourcesParamsData.  # noqa: E501
        :type clusters: ClusterWhereInput
        """

        self._clusters = clusters

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
        if not isinstance(other, AddLabelsToResourcesParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddLabelsToResourcesParamsData):
            return True

        return self.to_dict() != other.to_dict()
