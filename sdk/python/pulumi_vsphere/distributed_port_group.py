# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class DistributedPortGroup(pulumi.CustomResource):
    active_uplinks: pulumi.Output[list]
    """
    List of active uplinks used for load balancing, matching the names of the uplinks assigned in the DVS.
    """
    allow_forged_transmits: pulumi.Output[bool]
    """
    Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than
    that of its own.
    """
    allow_mac_changes: pulumi.Output[bool]
    """
    Controls whether or not the Media Access Control (MAC) address can be changed.
    """
    allow_promiscuous: pulumi.Output[bool]
    """
    Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port.
    """
    auto_expand: pulumi.Output[bool]
    """
    Allows the port group to create additional ports
    past the limit specified in `number_of_ports` if necessary. Default: `true`.
    """
    block_all_ports: pulumi.Output[bool]
    """
    Indicates whether to block all ports by default.
    """
    block_override_allowed: pulumi.Output[bool]
    """
    Allow the port shutdown
    policy to be overridden on an individual port.
    """
    check_beacon: pulumi.Output[bool]
    """
    Enable beacon probing on the ports this policy applies to.
    """
    config_version: pulumi.Output[str]
    """
    Version string of the configuration that this spec is trying to change.
    """
    custom_attributes: pulumi.Output[dict]
    """
    Map of custom attribute ids to attribute
    value string to set for port group.
    """
    description: pulumi.Output[str]
    """
    An optional description for the port group.
    """
    directpath_gen2_allowed: pulumi.Output[bool]
    """
    Allow VMDirectPath Gen2 on the ports this policy applies to.
    """
    distributed_virtual_switch_uuid: pulumi.Output[str]
    """
    The ID of the DVS to add the
    port group to. Forces a new resource if changed.
    """
    egress_shaping_average_bandwidth: pulumi.Output[float]
    """
    The average egress bandwidth in bits per second if egress shaping is enabled on the port.
    """
    egress_shaping_burst_size: pulumi.Output[float]
    """
    The maximum egress burst size allowed in bytes if egress shaping is enabled on the port.
    """
    egress_shaping_enabled: pulumi.Output[bool]
    """
    True if the traffic shaper is enabled for egress traffic on the port.
    """
    egress_shaping_peak_bandwidth: pulumi.Output[float]
    """
    The peak egress bandwidth during bursts in bits per second if egress traffic shaping is enabled on the port.
    """
    failback: pulumi.Output[bool]
    """
    If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.
    """
    ingress_shaping_average_bandwidth: pulumi.Output[float]
    """
    The average ingress bandwidth in bits per second if ingress shaping is enabled on the port.
    """
    ingress_shaping_burst_size: pulumi.Output[float]
    """
    The maximum ingress burst size allowed in bytes if ingress shaping is enabled on the port.
    """
    ingress_shaping_enabled: pulumi.Output[bool]
    """
    True if the traffic shaper is enabled for ingress traffic on the port.
    """
    ingress_shaping_peak_bandwidth: pulumi.Output[float]
    """
    The peak ingress bandwidth during bursts in bits per second if ingress traffic shaping is enabled on the port.
    """
    key: pulumi.Output[str]
    """
    The generated UUID of the portgroup.
    """
    lacp_enabled: pulumi.Output[bool]
    """
    Whether or not to enable LACP on all uplink ports.
    """
    lacp_mode: pulumi.Output[str]
    """
    The uplink LACP mode to use. Can be one of active or passive.
    """
    live_port_moving_allowed: pulumi.Output[bool]
    """
    Allow a port in this port group to be
    moved to another port group while it is connected.
    """
    name: pulumi.Output[str]
    """
    The name of the port group.
    """
    netflow_enabled: pulumi.Output[bool]
    """
    Indicates whether to enable netflow on all ports.
    """
    netflow_override_allowed: pulumi.Output[bool]
    """
    Allow the Netflow
    policy on this port group to be overridden on an individual
    port.
    """
    network_resource_pool_key: pulumi.Output[str]
    """
    The key of a network resource pool
    to associate with this port group. The default is `-1`, which implies no
    association.
    """
    network_resource_pool_override_allowed: pulumi.Output[bool]
    """
    Allow the network
    resource pool set on this port group to be overridden on an individual port.
    """
    notify_switches: pulumi.Output[bool]
    """
    If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.
    """
    number_of_ports: pulumi.Output[float]
    """
    The number of ports available on this port
    group. Cannot be decreased below the amount of used ports on the port group.
    """
    port_config_reset_at_disconnect: pulumi.Output[bool]
    """
    Reset a port's settings to the
    settings defined on this port group policy when the port disconnects.
    """
    port_name_format: pulumi.Output[str]
    """
    An optional formatting policy for naming of
    the ports in this port group. See the `portNameFormat` attribute listed
    [here][ext-vsphere-portname-format] for details on the format syntax.
    """
    port_private_secondary_vlan_id: pulumi.Output[float]
    """
    The secondary VLAN ID for this port.
    """
    security_policy_override_allowed: pulumi.Output[bool]
    """
    Allow the security policy
    settings defined in this port group policy to be
    overridden on an individual port.
    """
    shaping_override_allowed: pulumi.Output[bool]
    """
    Allow the traffic shaping
    options on this port group policy to be overridden
    on an individual port.
    """
    standby_uplinks: pulumi.Output[list]
    """
    List of active uplinks used for load balancing, matching the names of the uplinks assigned in the DVS.
    """
    tags: pulumi.Output[list]
    """
    A list of tag IDs to apply to this object.
    """
    teaming_policy: pulumi.Output[str]
    """
    The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid,
    failover_explicit, or loadbalance_loadbased.
    """
    traffic_filter_override_allowed: pulumi.Output[bool]
    """
    Allow any traffic filters on
    this port group to be overridden on an individual port.
    """
    tx_uplink: pulumi.Output[bool]
    """
    If true, a copy of packets sent to the switch will always be forwarded to an uplink in addition to the regular packet
    forwarded done by the switch.
    """
    type: pulumi.Output[str]
    """
    The port group type. Can be one of `earlyBinding` (static
    binding) or `ephemeral`. Default: `earlyBinding`.
    """
    uplink_teaming_override_allowed: pulumi.Output[bool]
    """
    Allow the uplink teaming
    options on this port group to be overridden on an
    individual port.
    """
    vlan_id: pulumi.Output[float]
    """
    The VLAN ID for single VLAN mode. 0 denotes no VLAN.
    """
    vlan_override_allowed: pulumi.Output[bool]
    """
    Allow the VLAN settings
    on this port group to be overridden on an individual port.
    """
    vlan_ranges: pulumi.Output[list]
    """
    The VLAN ID for single VLAN mode. 0 denotes no VLAN.

      * `maxVlan` (`float`)
      * `minVlan` (`float`)
    """
    def __init__(__self__, resource_name, opts=None, active_uplinks=None, allow_forged_transmits=None, allow_mac_changes=None, allow_promiscuous=None, auto_expand=None, block_all_ports=None, block_override_allowed=None, check_beacon=None, custom_attributes=None, description=None, directpath_gen2_allowed=None, distributed_virtual_switch_uuid=None, egress_shaping_average_bandwidth=None, egress_shaping_burst_size=None, egress_shaping_enabled=None, egress_shaping_peak_bandwidth=None, failback=None, ingress_shaping_average_bandwidth=None, ingress_shaping_burst_size=None, ingress_shaping_enabled=None, ingress_shaping_peak_bandwidth=None, lacp_enabled=None, lacp_mode=None, live_port_moving_allowed=None, name=None, netflow_enabled=None, netflow_override_allowed=None, network_resource_pool_key=None, network_resource_pool_override_allowed=None, notify_switches=None, number_of_ports=None, port_config_reset_at_disconnect=None, port_name_format=None, port_private_secondary_vlan_id=None, security_policy_override_allowed=None, shaping_override_allowed=None, standby_uplinks=None, tags=None, teaming_policy=None, traffic_filter_override_allowed=None, tx_uplink=None, type=None, uplink_teaming_override_allowed=None, vlan_id=None, vlan_override_allowed=None, vlan_ranges=None, __props__=None, __name__=None, __opts__=None):
        """
        The `.DistributedPortGroup` resource can be used to manage vSphere
        distributed virtual port groups. These port groups are connected to distributed
        virtual switches, which can be managed by the
        `.DistributedVirtualSwitch` resource.

        Distributed port groups can be used as networks for virtual machines, allowing
        VMs to use the networking supplied by a distributed virtual switch (DVS), with
        a set of policies that apply to that individual newtork, if desired.

        For an overview on vSphere networking concepts, see [this
        page][ref-vsphere-net-concepts]. For more information on vSphere DVS
        portgroups, see [this page][ref-vsphere-dvportgroup].

        [ref-vsphere-net-concepts]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-2B11DBB8-CB3C-4AFF-8885-EFEA0FC562F4.html
        [ref-vsphere-dvportgroup]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-69933F6E-2442-46CF-AA17-1196CB9A0A09.html

        > **NOTE:** This resource requires vCenter and is not available on direct ESXi
        connections.

        ## Example Usage

        ### Overriding DVS policies

        ```python
        import pulumi
        import pulumi_vsphere as vsphere

        dvs = vsphere.DistributedVirtualSwitch("dvs",
            active_uplinks=["tfup1"],
            datacenter_id=data[".Datacenter"]["dc"]["id"],
            standby_uplinks=["tfup2"],
            uplinks=[
                "tfup1",
                "tfup2",
            ])
        pg = vsphere.DistributedPortGroup("pg",
            active_uplinks=[
                "tfup1",
                "tfup2",
            ],
            distributed_virtual_switch_uuid=dvs.id,
            standby_uplinks=[],
            vlan_id=1000)
        ```


        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] active_uplinks: List of active uplinks used for load balancing, matching the names of the uplinks assigned in the DVS.
        :param pulumi.Input[bool] allow_forged_transmits: Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than
               that of its own.
        :param pulumi.Input[bool] allow_mac_changes: Controls whether or not the Media Access Control (MAC) address can be changed.
        :param pulumi.Input[bool] allow_promiscuous: Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port.
        :param pulumi.Input[bool] auto_expand: Allows the port group to create additional ports
               past the limit specified in `number_of_ports` if necessary. Default: `true`.
        :param pulumi.Input[bool] block_all_ports: Indicates whether to block all ports by default.
        :param pulumi.Input[bool] block_override_allowed: Allow the port shutdown
               policy to be overridden on an individual port.
        :param pulumi.Input[bool] check_beacon: Enable beacon probing on the ports this policy applies to.
        :param pulumi.Input[dict] custom_attributes: Map of custom attribute ids to attribute
               value string to set for port group.
        :param pulumi.Input[str] description: An optional description for the port group.
        :param pulumi.Input[bool] directpath_gen2_allowed: Allow VMDirectPath Gen2 on the ports this policy applies to.
        :param pulumi.Input[str] distributed_virtual_switch_uuid: The ID of the DVS to add the
               port group to. Forces a new resource if changed.
        :param pulumi.Input[float] egress_shaping_average_bandwidth: The average egress bandwidth in bits per second if egress shaping is enabled on the port.
        :param pulumi.Input[float] egress_shaping_burst_size: The maximum egress burst size allowed in bytes if egress shaping is enabled on the port.
        :param pulumi.Input[bool] egress_shaping_enabled: True if the traffic shaper is enabled for egress traffic on the port.
        :param pulumi.Input[float] egress_shaping_peak_bandwidth: The peak egress bandwidth during bursts in bits per second if egress traffic shaping is enabled on the port.
        :param pulumi.Input[bool] failback: If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.
        :param pulumi.Input[float] ingress_shaping_average_bandwidth: The average ingress bandwidth in bits per second if ingress shaping is enabled on the port.
        :param pulumi.Input[float] ingress_shaping_burst_size: The maximum ingress burst size allowed in bytes if ingress shaping is enabled on the port.
        :param pulumi.Input[bool] ingress_shaping_enabled: True if the traffic shaper is enabled for ingress traffic on the port.
        :param pulumi.Input[float] ingress_shaping_peak_bandwidth: The peak ingress bandwidth during bursts in bits per second if ingress traffic shaping is enabled on the port.
        :param pulumi.Input[bool] lacp_enabled: Whether or not to enable LACP on all uplink ports.
        :param pulumi.Input[str] lacp_mode: The uplink LACP mode to use. Can be one of active or passive.
        :param pulumi.Input[bool] live_port_moving_allowed: Allow a port in this port group to be
               moved to another port group while it is connected.
        :param pulumi.Input[str] name: The name of the port group.
        :param pulumi.Input[bool] netflow_enabled: Indicates whether to enable netflow on all ports.
        :param pulumi.Input[bool] netflow_override_allowed: Allow the Netflow
               policy on this port group to be overridden on an individual
               port.
        :param pulumi.Input[str] network_resource_pool_key: The key of a network resource pool
               to associate with this port group. The default is `-1`, which implies no
               association.
        :param pulumi.Input[bool] network_resource_pool_override_allowed: Allow the network
               resource pool set on this port group to be overridden on an individual port.
        :param pulumi.Input[bool] notify_switches: If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.
        :param pulumi.Input[float] number_of_ports: The number of ports available on this port
               group. Cannot be decreased below the amount of used ports on the port group.
        :param pulumi.Input[bool] port_config_reset_at_disconnect: Reset a port's settings to the
               settings defined on this port group policy when the port disconnects.
        :param pulumi.Input[str] port_name_format: An optional formatting policy for naming of
               the ports in this port group. See the `portNameFormat` attribute listed
               [here][ext-vsphere-portname-format] for details on the format syntax.
        :param pulumi.Input[float] port_private_secondary_vlan_id: The secondary VLAN ID for this port.
        :param pulumi.Input[bool] security_policy_override_allowed: Allow the security policy
               settings defined in this port group policy to be
               overridden on an individual port.
        :param pulumi.Input[bool] shaping_override_allowed: Allow the traffic shaping
               options on this port group policy to be overridden
               on an individual port.
        :param pulumi.Input[list] standby_uplinks: List of active uplinks used for load balancing, matching the names of the uplinks assigned in the DVS.
        :param pulumi.Input[list] tags: A list of tag IDs to apply to this object.
        :param pulumi.Input[str] teaming_policy: The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid,
               failover_explicit, or loadbalance_loadbased.
        :param pulumi.Input[bool] traffic_filter_override_allowed: Allow any traffic filters on
               this port group to be overridden on an individual port.
        :param pulumi.Input[bool] tx_uplink: If true, a copy of packets sent to the switch will always be forwarded to an uplink in addition to the regular packet
               forwarded done by the switch.
        :param pulumi.Input[str] type: The port group type. Can be one of `earlyBinding` (static
               binding) or `ephemeral`. Default: `earlyBinding`.
        :param pulumi.Input[bool] uplink_teaming_override_allowed: Allow the uplink teaming
               options on this port group to be overridden on an
               individual port.
        :param pulumi.Input[float] vlan_id: The VLAN ID for single VLAN mode. 0 denotes no VLAN.
        :param pulumi.Input[bool] vlan_override_allowed: Allow the VLAN settings
               on this port group to be overridden on an individual port.
        :param pulumi.Input[list] vlan_ranges: The VLAN ID for single VLAN mode. 0 denotes no VLAN.

        The **vlan_ranges** object supports the following:

          * `maxVlan` (`pulumi.Input[float]`)
          * `minVlan` (`pulumi.Input[float]`)
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['active_uplinks'] = active_uplinks
            __props__['allow_forged_transmits'] = allow_forged_transmits
            __props__['allow_mac_changes'] = allow_mac_changes
            __props__['allow_promiscuous'] = allow_promiscuous
            __props__['auto_expand'] = auto_expand
            __props__['block_all_ports'] = block_all_ports
            __props__['block_override_allowed'] = block_override_allowed
            __props__['check_beacon'] = check_beacon
            __props__['custom_attributes'] = custom_attributes
            __props__['description'] = description
            __props__['directpath_gen2_allowed'] = directpath_gen2_allowed
            if distributed_virtual_switch_uuid is None:
                raise TypeError("Missing required property 'distributed_virtual_switch_uuid'")
            __props__['distributed_virtual_switch_uuid'] = distributed_virtual_switch_uuid
            __props__['egress_shaping_average_bandwidth'] = egress_shaping_average_bandwidth
            __props__['egress_shaping_burst_size'] = egress_shaping_burst_size
            __props__['egress_shaping_enabled'] = egress_shaping_enabled
            __props__['egress_shaping_peak_bandwidth'] = egress_shaping_peak_bandwidth
            __props__['failback'] = failback
            __props__['ingress_shaping_average_bandwidth'] = ingress_shaping_average_bandwidth
            __props__['ingress_shaping_burst_size'] = ingress_shaping_burst_size
            __props__['ingress_shaping_enabled'] = ingress_shaping_enabled
            __props__['ingress_shaping_peak_bandwidth'] = ingress_shaping_peak_bandwidth
            __props__['lacp_enabled'] = lacp_enabled
            __props__['lacp_mode'] = lacp_mode
            __props__['live_port_moving_allowed'] = live_port_moving_allowed
            __props__['name'] = name
            __props__['netflow_enabled'] = netflow_enabled
            __props__['netflow_override_allowed'] = netflow_override_allowed
            __props__['network_resource_pool_key'] = network_resource_pool_key
            __props__['network_resource_pool_override_allowed'] = network_resource_pool_override_allowed
            __props__['notify_switches'] = notify_switches
            __props__['number_of_ports'] = number_of_ports
            __props__['port_config_reset_at_disconnect'] = port_config_reset_at_disconnect
            __props__['port_name_format'] = port_name_format
            __props__['port_private_secondary_vlan_id'] = port_private_secondary_vlan_id
            __props__['security_policy_override_allowed'] = security_policy_override_allowed
            __props__['shaping_override_allowed'] = shaping_override_allowed
            __props__['standby_uplinks'] = standby_uplinks
            __props__['tags'] = tags
            __props__['teaming_policy'] = teaming_policy
            __props__['traffic_filter_override_allowed'] = traffic_filter_override_allowed
            __props__['tx_uplink'] = tx_uplink
            __props__['type'] = type
            __props__['uplink_teaming_override_allowed'] = uplink_teaming_override_allowed
            __props__['vlan_id'] = vlan_id
            __props__['vlan_override_allowed'] = vlan_override_allowed
            __props__['vlan_ranges'] = vlan_ranges
            __props__['config_version'] = None
            __props__['key'] = None
        super(DistributedPortGroup, __self__).__init__(
            'vsphere:index/distributedPortGroup:DistributedPortGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, active_uplinks=None, allow_forged_transmits=None, allow_mac_changes=None, allow_promiscuous=None, auto_expand=None, block_all_ports=None, block_override_allowed=None, check_beacon=None, config_version=None, custom_attributes=None, description=None, directpath_gen2_allowed=None, distributed_virtual_switch_uuid=None, egress_shaping_average_bandwidth=None, egress_shaping_burst_size=None, egress_shaping_enabled=None, egress_shaping_peak_bandwidth=None, failback=None, ingress_shaping_average_bandwidth=None, ingress_shaping_burst_size=None, ingress_shaping_enabled=None, ingress_shaping_peak_bandwidth=None, key=None, lacp_enabled=None, lacp_mode=None, live_port_moving_allowed=None, name=None, netflow_enabled=None, netflow_override_allowed=None, network_resource_pool_key=None, network_resource_pool_override_allowed=None, notify_switches=None, number_of_ports=None, port_config_reset_at_disconnect=None, port_name_format=None, port_private_secondary_vlan_id=None, security_policy_override_allowed=None, shaping_override_allowed=None, standby_uplinks=None, tags=None, teaming_policy=None, traffic_filter_override_allowed=None, tx_uplink=None, type=None, uplink_teaming_override_allowed=None, vlan_id=None, vlan_override_allowed=None, vlan_ranges=None):
        """
        Get an existing DistributedPortGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] active_uplinks: List of active uplinks used for load balancing, matching the names of the uplinks assigned in the DVS.
        :param pulumi.Input[bool] allow_forged_transmits: Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than
               that of its own.
        :param pulumi.Input[bool] allow_mac_changes: Controls whether or not the Media Access Control (MAC) address can be changed.
        :param pulumi.Input[bool] allow_promiscuous: Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port.
        :param pulumi.Input[bool] auto_expand: Allows the port group to create additional ports
               past the limit specified in `number_of_ports` if necessary. Default: `true`.
        :param pulumi.Input[bool] block_all_ports: Indicates whether to block all ports by default.
        :param pulumi.Input[bool] block_override_allowed: Allow the port shutdown
               policy to be overridden on an individual port.
        :param pulumi.Input[bool] check_beacon: Enable beacon probing on the ports this policy applies to.
        :param pulumi.Input[str] config_version: Version string of the configuration that this spec is trying to change.
        :param pulumi.Input[dict] custom_attributes: Map of custom attribute ids to attribute
               value string to set for port group.
        :param pulumi.Input[str] description: An optional description for the port group.
        :param pulumi.Input[bool] directpath_gen2_allowed: Allow VMDirectPath Gen2 on the ports this policy applies to.
        :param pulumi.Input[str] distributed_virtual_switch_uuid: The ID of the DVS to add the
               port group to. Forces a new resource if changed.
        :param pulumi.Input[float] egress_shaping_average_bandwidth: The average egress bandwidth in bits per second if egress shaping is enabled on the port.
        :param pulumi.Input[float] egress_shaping_burst_size: The maximum egress burst size allowed in bytes if egress shaping is enabled on the port.
        :param pulumi.Input[bool] egress_shaping_enabled: True if the traffic shaper is enabled for egress traffic on the port.
        :param pulumi.Input[float] egress_shaping_peak_bandwidth: The peak egress bandwidth during bursts in bits per second if egress traffic shaping is enabled on the port.
        :param pulumi.Input[bool] failback: If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.
        :param pulumi.Input[float] ingress_shaping_average_bandwidth: The average ingress bandwidth in bits per second if ingress shaping is enabled on the port.
        :param pulumi.Input[float] ingress_shaping_burst_size: The maximum ingress burst size allowed in bytes if ingress shaping is enabled on the port.
        :param pulumi.Input[bool] ingress_shaping_enabled: True if the traffic shaper is enabled for ingress traffic on the port.
        :param pulumi.Input[float] ingress_shaping_peak_bandwidth: The peak ingress bandwidth during bursts in bits per second if ingress traffic shaping is enabled on the port.
        :param pulumi.Input[str] key: The generated UUID of the portgroup.
        :param pulumi.Input[bool] lacp_enabled: Whether or not to enable LACP on all uplink ports.
        :param pulumi.Input[str] lacp_mode: The uplink LACP mode to use. Can be one of active or passive.
        :param pulumi.Input[bool] live_port_moving_allowed: Allow a port in this port group to be
               moved to another port group while it is connected.
        :param pulumi.Input[str] name: The name of the port group.
        :param pulumi.Input[bool] netflow_enabled: Indicates whether to enable netflow on all ports.
        :param pulumi.Input[bool] netflow_override_allowed: Allow the Netflow
               policy on this port group to be overridden on an individual
               port.
        :param pulumi.Input[str] network_resource_pool_key: The key of a network resource pool
               to associate with this port group. The default is `-1`, which implies no
               association.
        :param pulumi.Input[bool] network_resource_pool_override_allowed: Allow the network
               resource pool set on this port group to be overridden on an individual port.
        :param pulumi.Input[bool] notify_switches: If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.
        :param pulumi.Input[float] number_of_ports: The number of ports available on this port
               group. Cannot be decreased below the amount of used ports on the port group.
        :param pulumi.Input[bool] port_config_reset_at_disconnect: Reset a port's settings to the
               settings defined on this port group policy when the port disconnects.
        :param pulumi.Input[str] port_name_format: An optional formatting policy for naming of
               the ports in this port group. See the `portNameFormat` attribute listed
               [here][ext-vsphere-portname-format] for details on the format syntax.
        :param pulumi.Input[float] port_private_secondary_vlan_id: The secondary VLAN ID for this port.
        :param pulumi.Input[bool] security_policy_override_allowed: Allow the security policy
               settings defined in this port group policy to be
               overridden on an individual port.
        :param pulumi.Input[bool] shaping_override_allowed: Allow the traffic shaping
               options on this port group policy to be overridden
               on an individual port.
        :param pulumi.Input[list] standby_uplinks: List of active uplinks used for load balancing, matching the names of the uplinks assigned in the DVS.
        :param pulumi.Input[list] tags: A list of tag IDs to apply to this object.
        :param pulumi.Input[str] teaming_policy: The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid,
               failover_explicit, or loadbalance_loadbased.
        :param pulumi.Input[bool] traffic_filter_override_allowed: Allow any traffic filters on
               this port group to be overridden on an individual port.
        :param pulumi.Input[bool] tx_uplink: If true, a copy of packets sent to the switch will always be forwarded to an uplink in addition to the regular packet
               forwarded done by the switch.
        :param pulumi.Input[str] type: The port group type. Can be one of `earlyBinding` (static
               binding) or `ephemeral`. Default: `earlyBinding`.
        :param pulumi.Input[bool] uplink_teaming_override_allowed: Allow the uplink teaming
               options on this port group to be overridden on an
               individual port.
        :param pulumi.Input[float] vlan_id: The VLAN ID for single VLAN mode. 0 denotes no VLAN.
        :param pulumi.Input[bool] vlan_override_allowed: Allow the VLAN settings
               on this port group to be overridden on an individual port.
        :param pulumi.Input[list] vlan_ranges: The VLAN ID for single VLAN mode. 0 denotes no VLAN.

        The **vlan_ranges** object supports the following:

          * `maxVlan` (`pulumi.Input[float]`)
          * `minVlan` (`pulumi.Input[float]`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["active_uplinks"] = active_uplinks
        __props__["allow_forged_transmits"] = allow_forged_transmits
        __props__["allow_mac_changes"] = allow_mac_changes
        __props__["allow_promiscuous"] = allow_promiscuous
        __props__["auto_expand"] = auto_expand
        __props__["block_all_ports"] = block_all_ports
        __props__["block_override_allowed"] = block_override_allowed
        __props__["check_beacon"] = check_beacon
        __props__["config_version"] = config_version
        __props__["custom_attributes"] = custom_attributes
        __props__["description"] = description
        __props__["directpath_gen2_allowed"] = directpath_gen2_allowed
        __props__["distributed_virtual_switch_uuid"] = distributed_virtual_switch_uuid
        __props__["egress_shaping_average_bandwidth"] = egress_shaping_average_bandwidth
        __props__["egress_shaping_burst_size"] = egress_shaping_burst_size
        __props__["egress_shaping_enabled"] = egress_shaping_enabled
        __props__["egress_shaping_peak_bandwidth"] = egress_shaping_peak_bandwidth
        __props__["failback"] = failback
        __props__["ingress_shaping_average_bandwidth"] = ingress_shaping_average_bandwidth
        __props__["ingress_shaping_burst_size"] = ingress_shaping_burst_size
        __props__["ingress_shaping_enabled"] = ingress_shaping_enabled
        __props__["ingress_shaping_peak_bandwidth"] = ingress_shaping_peak_bandwidth
        __props__["key"] = key
        __props__["lacp_enabled"] = lacp_enabled
        __props__["lacp_mode"] = lacp_mode
        __props__["live_port_moving_allowed"] = live_port_moving_allowed
        __props__["name"] = name
        __props__["netflow_enabled"] = netflow_enabled
        __props__["netflow_override_allowed"] = netflow_override_allowed
        __props__["network_resource_pool_key"] = network_resource_pool_key
        __props__["network_resource_pool_override_allowed"] = network_resource_pool_override_allowed
        __props__["notify_switches"] = notify_switches
        __props__["number_of_ports"] = number_of_ports
        __props__["port_config_reset_at_disconnect"] = port_config_reset_at_disconnect
        __props__["port_name_format"] = port_name_format
        __props__["port_private_secondary_vlan_id"] = port_private_secondary_vlan_id
        __props__["security_policy_override_allowed"] = security_policy_override_allowed
        __props__["shaping_override_allowed"] = shaping_override_allowed
        __props__["standby_uplinks"] = standby_uplinks
        __props__["tags"] = tags
        __props__["teaming_policy"] = teaming_policy
        __props__["traffic_filter_override_allowed"] = traffic_filter_override_allowed
        __props__["tx_uplink"] = tx_uplink
        __props__["type"] = type
        __props__["uplink_teaming_override_allowed"] = uplink_teaming_override_allowed
        __props__["vlan_id"] = vlan_id
        __props__["vlan_override_allowed"] = vlan_override_allowed
        __props__["vlan_ranges"] = vlan_ranges
        return DistributedPortGroup(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

