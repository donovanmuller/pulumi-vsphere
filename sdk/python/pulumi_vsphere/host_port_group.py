# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class HostPortGroup(pulumi.CustomResource):
    active_nics: pulumi.Output[list]
    """
    List of active network adapters used for load balancing.
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
    check_beacon: pulumi.Output[bool]
    """
    Enable beacon probing. Requires that the vSwitch has been configured to use a beacon. If disabled, link status is used
    only.
    """
    computed_policy: pulumi.Output[dict]
    """
    A map with a full set of the policy
    options computed from defaults and overrides,
    explaining the effective policy for this port group.
    """
    failback: pulumi.Output[bool]
    """
    If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.
    """
    host_system_id: pulumi.Output[str]
    """
    The managed object ID of
    the host to set the port group up on. Forces a new resource if changed.
    """
    key: pulumi.Output[str]
    """
    The key for this port group as returned from the vSphere API.
    """
    name: pulumi.Output[str]
    """
    The name of the port group.  Forces a new resource if
    changed.
    """
    notify_switches: pulumi.Output[bool]
    """
    If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.
    """
    ports: pulumi.Output[dict]
    """
    A list of ports that currently exist and are used on this port group.

      * `key` (`str`) - The key for this port group as returned from the vSphere API.
      * `macAddresses` (`list`)
      * `type` (`str`)
    """
    shaping_average_bandwidth: pulumi.Output[float]
    """
    The average bandwidth in bits per second if traffic shaping is enabled.
    """
    shaping_burst_size: pulumi.Output[float]
    """
    The maximum burst size allowed in bytes if traffic shaping is enabled.
    """
    shaping_enabled: pulumi.Output[bool]
    """
    Enable traffic shaping on this virtual switch or port group.
    """
    shaping_peak_bandwidth: pulumi.Output[float]
    """
    The peak bandwidth during bursts in bits per second if traffic shaping is enabled.
    """
    standby_nics: pulumi.Output[list]
    """
    List of standby network adapters used for failover.
    """
    teaming_policy: pulumi.Output[str]
    """
    The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, or
    failover_explicit.
    """
    virtual_switch_name: pulumi.Output[str]
    """
    The name of the virtual switch to bind
    this port group to. Forces a new resource if changed.
    """
    vlan_id: pulumi.Output[float]
    """
    The VLAN ID/trunk mode for this port group.  An ID of
    `0` denotes no tagging, an ID of `1`-`4094` tags with the specific ID, and an
    ID of `4095` enables trunk mode, allowing the guest to manage its own
    tagging. Default: `0`.
    """
    def __init__(__self__, resource_name, opts=None, active_nics=None, allow_forged_transmits=None, allow_mac_changes=None, allow_promiscuous=None, check_beacon=None, failback=None, host_system_id=None, name=None, notify_switches=None, shaping_average_bandwidth=None, shaping_burst_size=None, shaping_enabled=None, shaping_peak_bandwidth=None, standby_nics=None, teaming_policy=None, virtual_switch_name=None, vlan_id=None, __props__=None, __name__=None, __opts__=None):
        """
        The `.HostPortGroup` resource can be used to manage vSphere standard
        port groups on an ESXi host. These port groups are connected to standard
        virtual switches, which can be managed by the
        `.HostVirtualSwitch` resource.

        For an overview on vSphere networking concepts, see [this page][ref-vsphere-net-concepts].

        [ref-vsphere-net-concepts]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-2B11DBB8-CB3C-4AFF-8885-EFEA0FC562F4.html

        ## Example Usage

        ### Create a virtual switch and bind a port group to it

        ```python
        import pulumi
        import pulumi_vsphere as vsphere

        datacenter = vsphere.get_datacenter(name="dc1")
        esxi_host = vsphere.get_host(datacenter_id=datacenter.id,
            name="esxi1")
        switch = vsphere.HostVirtualSwitch("switch",
            active_nics=["vmnic0"],
            host_system_id=esxi_host.id,
            network_adapters=[
                "vmnic0",
                "vmnic1",
            ],
            standby_nics=["vmnic1"])
        pg = vsphere.HostPortGroup("pg",
            host_system_id=esxi_host.id,
            virtual_switch_name=switch.name)
        ```

        ### Create a port group with VLAN set and some overrides

        ```python
        import pulumi
        import pulumi_vsphere as vsphere

        datacenter = vsphere.get_datacenter(name="dc1")
        esxi_host = vsphere.get_host(datacenter_id=datacenter.id,
            name="esxi1")
        switch = vsphere.HostVirtualSwitch("switch",
            active_nics=["vmnic0"],
            host_system_id=esxi_host.id,
            network_adapters=[
                "vmnic0",
                "vmnic1",
            ],
            standby_nics=["vmnic1"])
        pg = vsphere.HostPortGroup("pg",
            allow_promiscuous=True,
            host_system_id=esxi_host.id,
            virtual_switch_name=switch.name,
            vlan_id=4095)
        ```


        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] active_nics: List of active network adapters used for load balancing.
        :param pulumi.Input[bool] allow_forged_transmits: Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than
               that of its own.
        :param pulumi.Input[bool] allow_mac_changes: Controls whether or not the Media Access Control (MAC) address can be changed.
        :param pulumi.Input[bool] allow_promiscuous: Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port.
        :param pulumi.Input[bool] check_beacon: Enable beacon probing. Requires that the vSwitch has been configured to use a beacon. If disabled, link status is used
               only.
        :param pulumi.Input[bool] failback: If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.
        :param pulumi.Input[str] host_system_id: The managed object ID of
               the host to set the port group up on. Forces a new resource if changed.
        :param pulumi.Input[str] name: The name of the port group.  Forces a new resource if
               changed.
        :param pulumi.Input[bool] notify_switches: If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.
        :param pulumi.Input[float] shaping_average_bandwidth: The average bandwidth in bits per second if traffic shaping is enabled.
        :param pulumi.Input[float] shaping_burst_size: The maximum burst size allowed in bytes if traffic shaping is enabled.
        :param pulumi.Input[bool] shaping_enabled: Enable traffic shaping on this virtual switch or port group.
        :param pulumi.Input[float] shaping_peak_bandwidth: The peak bandwidth during bursts in bits per second if traffic shaping is enabled.
        :param pulumi.Input[list] standby_nics: List of standby network adapters used for failover.
        :param pulumi.Input[str] teaming_policy: The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, or
               failover_explicit.
        :param pulumi.Input[str] virtual_switch_name: The name of the virtual switch to bind
               this port group to. Forces a new resource if changed.
        :param pulumi.Input[float] vlan_id: The VLAN ID/trunk mode for this port group.  An ID of
               `0` denotes no tagging, an ID of `1`-`4094` tags with the specific ID, and an
               ID of `4095` enables trunk mode, allowing the guest to manage its own
               tagging. Default: `0`.
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

            __props__['active_nics'] = active_nics
            __props__['allow_forged_transmits'] = allow_forged_transmits
            __props__['allow_mac_changes'] = allow_mac_changes
            __props__['allow_promiscuous'] = allow_promiscuous
            __props__['check_beacon'] = check_beacon
            __props__['failback'] = failback
            if host_system_id is None:
                raise TypeError("Missing required property 'host_system_id'")
            __props__['host_system_id'] = host_system_id
            __props__['name'] = name
            __props__['notify_switches'] = notify_switches
            __props__['shaping_average_bandwidth'] = shaping_average_bandwidth
            __props__['shaping_burst_size'] = shaping_burst_size
            __props__['shaping_enabled'] = shaping_enabled
            __props__['shaping_peak_bandwidth'] = shaping_peak_bandwidth
            __props__['standby_nics'] = standby_nics
            __props__['teaming_policy'] = teaming_policy
            if virtual_switch_name is None:
                raise TypeError("Missing required property 'virtual_switch_name'")
            __props__['virtual_switch_name'] = virtual_switch_name
            __props__['vlan_id'] = vlan_id
            __props__['computed_policy'] = None
            __props__['key'] = None
            __props__['ports'] = None
        super(HostPortGroup, __self__).__init__(
            'vsphere:index/hostPortGroup:HostPortGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, active_nics=None, allow_forged_transmits=None, allow_mac_changes=None, allow_promiscuous=None, check_beacon=None, computed_policy=None, failback=None, host_system_id=None, key=None, name=None, notify_switches=None, ports=None, shaping_average_bandwidth=None, shaping_burst_size=None, shaping_enabled=None, shaping_peak_bandwidth=None, standby_nics=None, teaming_policy=None, virtual_switch_name=None, vlan_id=None):
        """
        Get an existing HostPortGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] active_nics: List of active network adapters used for load balancing.
        :param pulumi.Input[bool] allow_forged_transmits: Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than
               that of its own.
        :param pulumi.Input[bool] allow_mac_changes: Controls whether or not the Media Access Control (MAC) address can be changed.
        :param pulumi.Input[bool] allow_promiscuous: Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port.
        :param pulumi.Input[bool] check_beacon: Enable beacon probing. Requires that the vSwitch has been configured to use a beacon. If disabled, link status is used
               only.
        :param pulumi.Input[dict] computed_policy: A map with a full set of the policy
               options computed from defaults and overrides,
               explaining the effective policy for this port group.
        :param pulumi.Input[bool] failback: If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.
        :param pulumi.Input[str] host_system_id: The managed object ID of
               the host to set the port group up on. Forces a new resource if changed.
        :param pulumi.Input[str] key: The key for this port group as returned from the vSphere API.
        :param pulumi.Input[str] name: The name of the port group.  Forces a new resource if
               changed.
        :param pulumi.Input[bool] notify_switches: If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.
        :param pulumi.Input[dict] ports: A list of ports that currently exist and are used on this port group.
        :param pulumi.Input[float] shaping_average_bandwidth: The average bandwidth in bits per second if traffic shaping is enabled.
        :param pulumi.Input[float] shaping_burst_size: The maximum burst size allowed in bytes if traffic shaping is enabled.
        :param pulumi.Input[bool] shaping_enabled: Enable traffic shaping on this virtual switch or port group.
        :param pulumi.Input[float] shaping_peak_bandwidth: The peak bandwidth during bursts in bits per second if traffic shaping is enabled.
        :param pulumi.Input[list] standby_nics: List of standby network adapters used for failover.
        :param pulumi.Input[str] teaming_policy: The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, or
               failover_explicit.
        :param pulumi.Input[str] virtual_switch_name: The name of the virtual switch to bind
               this port group to. Forces a new resource if changed.
        :param pulumi.Input[float] vlan_id: The VLAN ID/trunk mode for this port group.  An ID of
               `0` denotes no tagging, an ID of `1`-`4094` tags with the specific ID, and an
               ID of `4095` enables trunk mode, allowing the guest to manage its own
               tagging. Default: `0`.

        The **ports** object supports the following:

          * `key` (`pulumi.Input[str]`) - The key for this port group as returned from the vSphere API.
          * `macAddresses` (`pulumi.Input[list]`)
          * `type` (`pulumi.Input[str]`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["active_nics"] = active_nics
        __props__["allow_forged_transmits"] = allow_forged_transmits
        __props__["allow_mac_changes"] = allow_mac_changes
        __props__["allow_promiscuous"] = allow_promiscuous
        __props__["check_beacon"] = check_beacon
        __props__["computed_policy"] = computed_policy
        __props__["failback"] = failback
        __props__["host_system_id"] = host_system_id
        __props__["key"] = key
        __props__["name"] = name
        __props__["notify_switches"] = notify_switches
        __props__["ports"] = ports
        __props__["shaping_average_bandwidth"] = shaping_average_bandwidth
        __props__["shaping_burst_size"] = shaping_burst_size
        __props__["shaping_enabled"] = shaping_enabled
        __props__["shaping_peak_bandwidth"] = shaping_peak_bandwidth
        __props__["standby_nics"] = standby_nics
        __props__["teaming_policy"] = teaming_policy
        __props__["virtual_switch_name"] = virtual_switch_name
        __props__["vlan_id"] = vlan_id
        return HostPortGroup(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

