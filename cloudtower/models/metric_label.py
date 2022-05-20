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


class MetricLabel(object):
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
        'to_hostname': 'str',
        'serial_number': 'str',
        'pool': 'str',
        'metric_name': 'str',
        'job': 'str',
        'instance': 'str',
        'zone': 'str',
        'witness': 'str',
        'volume': 'str',
        'vm': 'str',
        'to_uuid': 'str',
        'service': 'str',
        'scvm': 'str',
        'network': 'str',
        'mac': 'str',
        'host': 'str',
        'device': 'str',
        'cluster': 'str',
        'chunk': 'str',
        'typename': 'str'
    }

    attribute_map = {
        'to_hostname': 'to_hostname',
        'serial_number': 'serial_number',
        'pool': 'pool',
        'metric_name': 'metric_name',
        'job': 'job',
        'instance': 'instance',
        'zone': '_zone',
        'witness': '_witness',
        'volume': '_volume',
        'vm': '_vm',
        'to_uuid': '_to_uuid',
        'service': '_service',
        'scvm': '_scvm',
        'network': '_network',
        'mac': '_mac',
        'host': '_host',
        'device': '_device',
        'cluster': '_cluster',
        'chunk': '_chunk',
        'typename': '__typename'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """MetricLabel - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._to_hostname = None
        self._serial_number = None
        self._pool = None
        self._metric_name = None
        self._job = None
        self._instance = None
        self._zone = None
        self._witness = None
        self._volume = None
        self._vm = None
        self._to_uuid = None
        self._service = None
        self._scvm = None
        self._network = None
        self._mac = None
        self._host = None
        self._device = None
        self._cluster = None
        self._chunk = None
        self._typename = None
        self.discriminator = None

        self.to_hostname = kwargs.get("to_hostname", None)
        self.serial_number = kwargs.get("serial_number", None)
        self.pool = kwargs.get("pool", None)
        self.metric_name = kwargs.get("metric_name", None)
        self.job = kwargs.get("job", None)
        self.instance = kwargs.get("instance", None)
        self.zone = kwargs.get("zone", None)
        self.witness = kwargs.get("witness", None)
        self.volume = kwargs.get("volume", None)
        self.vm = kwargs.get("vm", None)
        self.to_uuid = kwargs.get("to_uuid", None)
        self.service = kwargs.get("service", None)
        self.scvm = kwargs.get("scvm", None)
        self.network = kwargs.get("network", None)
        self.mac = kwargs.get("mac", None)
        self.host = kwargs.get("host", None)
        self.device = kwargs.get("device", None)
        self.cluster = kwargs.get("cluster", None)
        self.chunk = kwargs.get("chunk", None)
        if "typename" in kwargs:
            self.typename = kwargs["typename"]

    @property
    def to_hostname(self):
        """Gets the to_hostname of this MetricLabel.  # noqa: E501


        :return: The to_hostname of this MetricLabel.  # noqa: E501
        :rtype: str
        """
        return self._to_hostname

    @to_hostname.setter
    def to_hostname(self, to_hostname):
        """Sets the to_hostname of this MetricLabel.


        :param to_hostname: The to_hostname of this MetricLabel.  # noqa: E501
        :type to_hostname: str
        """

        self._to_hostname = to_hostname

    @property
    def serial_number(self):
        """Gets the serial_number of this MetricLabel.  # noqa: E501


        :return: The serial_number of this MetricLabel.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this MetricLabel.


        :param serial_number: The serial_number of this MetricLabel.  # noqa: E501
        :type serial_number: str
        """

        self._serial_number = serial_number

    @property
    def pool(self):
        """Gets the pool of this MetricLabel.  # noqa: E501


        :return: The pool of this MetricLabel.  # noqa: E501
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this MetricLabel.


        :param pool: The pool of this MetricLabel.  # noqa: E501
        :type pool: str
        """

        self._pool = pool

    @property
    def metric_name(self):
        """Gets the metric_name of this MetricLabel.  # noqa: E501


        :return: The metric_name of this MetricLabel.  # noqa: E501
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this MetricLabel.


        :param metric_name: The metric_name of this MetricLabel.  # noqa: E501
        :type metric_name: str
        """

        self._metric_name = metric_name

    @property
    def job(self):
        """Gets the job of this MetricLabel.  # noqa: E501


        :return: The job of this MetricLabel.  # noqa: E501
        :rtype: str
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this MetricLabel.


        :param job: The job of this MetricLabel.  # noqa: E501
        :type job: str
        """

        self._job = job

    @property
    def instance(self):
        """Gets the instance of this MetricLabel.  # noqa: E501


        :return: The instance of this MetricLabel.  # noqa: E501
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this MetricLabel.


        :param instance: The instance of this MetricLabel.  # noqa: E501
        :type instance: str
        """

        self._instance = instance

    @property
    def zone(self):
        """Gets the zone of this MetricLabel.  # noqa: E501


        :return: The zone of this MetricLabel.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this MetricLabel.


        :param zone: The zone of this MetricLabel.  # noqa: E501
        :type zone: str
        """

        self._zone = zone

    @property
    def witness(self):
        """Gets the witness of this MetricLabel.  # noqa: E501


        :return: The witness of this MetricLabel.  # noqa: E501
        :rtype: str
        """
        return self._witness

    @witness.setter
    def witness(self, witness):
        """Sets the witness of this MetricLabel.


        :param witness: The witness of this MetricLabel.  # noqa: E501
        :type witness: str
        """

        self._witness = witness

    @property
    def volume(self):
        """Gets the volume of this MetricLabel.  # noqa: E501


        :return: The volume of this MetricLabel.  # noqa: E501
        :rtype: str
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this MetricLabel.


        :param volume: The volume of this MetricLabel.  # noqa: E501
        :type volume: str
        """

        self._volume = volume

    @property
    def vm(self):
        """Gets the vm of this MetricLabel.  # noqa: E501


        :return: The vm of this MetricLabel.  # noqa: E501
        :rtype: str
        """
        return self._vm

    @vm.setter
    def vm(self, vm):
        """Sets the vm of this MetricLabel.


        :param vm: The vm of this MetricLabel.  # noqa: E501
        :type vm: str
        """

        self._vm = vm

    @property
    def to_uuid(self):
        """Gets the to_uuid of this MetricLabel.  # noqa: E501


        :return: The to_uuid of this MetricLabel.  # noqa: E501
        :rtype: str
        """
        return self._to_uuid

    @to_uuid.setter
    def to_uuid(self, to_uuid):
        """Sets the to_uuid of this MetricLabel.


        :param to_uuid: The to_uuid of this MetricLabel.  # noqa: E501
        :type to_uuid: str
        """

        self._to_uuid = to_uuid

    @property
    def service(self):
        """Gets the service of this MetricLabel.  # noqa: E501


        :return: The service of this MetricLabel.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this MetricLabel.


        :param service: The service of this MetricLabel.  # noqa: E501
        :type service: str
        """

        self._service = service

    @property
    def scvm(self):
        """Gets the scvm of this MetricLabel.  # noqa: E501


        :return: The scvm of this MetricLabel.  # noqa: E501
        :rtype: str
        """
        return self._scvm

    @scvm.setter
    def scvm(self, scvm):
        """Sets the scvm of this MetricLabel.


        :param scvm: The scvm of this MetricLabel.  # noqa: E501
        :type scvm: str
        """

        self._scvm = scvm

    @property
    def network(self):
        """Gets the network of this MetricLabel.  # noqa: E501


        :return: The network of this MetricLabel.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this MetricLabel.


        :param network: The network of this MetricLabel.  # noqa: E501
        :type network: str
        """

        self._network = network

    @property
    def mac(self):
        """Gets the mac of this MetricLabel.  # noqa: E501


        :return: The mac of this MetricLabel.  # noqa: E501
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this MetricLabel.


        :param mac: The mac of this MetricLabel.  # noqa: E501
        :type mac: str
        """

        self._mac = mac

    @property
    def host(self):
        """Gets the host of this MetricLabel.  # noqa: E501


        :return: The host of this MetricLabel.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this MetricLabel.


        :param host: The host of this MetricLabel.  # noqa: E501
        :type host: str
        """

        self._host = host

    @property
    def device(self):
        """Gets the device of this MetricLabel.  # noqa: E501


        :return: The device of this MetricLabel.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this MetricLabel.


        :param device: The device of this MetricLabel.  # noqa: E501
        :type device: str
        """

        self._device = device

    @property
    def cluster(self):
        """Gets the cluster of this MetricLabel.  # noqa: E501


        :return: The cluster of this MetricLabel.  # noqa: E501
        :rtype: str
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this MetricLabel.


        :param cluster: The cluster of this MetricLabel.  # noqa: E501
        :type cluster: str
        """

        self._cluster = cluster

    @property
    def chunk(self):
        """Gets the chunk of this MetricLabel.  # noqa: E501


        :return: The chunk of this MetricLabel.  # noqa: E501
        :rtype: str
        """
        return self._chunk

    @chunk.setter
    def chunk(self, chunk):
        """Sets the chunk of this MetricLabel.


        :param chunk: The chunk of this MetricLabel.  # noqa: E501
        :type chunk: str
        """

        self._chunk = chunk

    @property
    def typename(self):
        """Gets the typename of this MetricLabel.  # noqa: E501


        :return: The typename of this MetricLabel.  # noqa: E501
        :rtype: str
        """
        return self._typename

    @typename.setter
    def typename(self, typename):
        """Sets the typename of this MetricLabel.


        :param typename: The typename of this MetricLabel.  # noqa: E501
        :type typename: str
        """
        allowed_values = ["MetricLabel"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and typename not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `typename` ({0}), must be one of {1}"  # noqa: E501
                .format(typename, allowed_values)
            )

        self._typename = typename

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
        if not isinstance(other, MetricLabel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetricLabel):
            return True

        return self.to_dict() != other.to_dict()
