# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class HostPortGroup(pulumi.CustomResource):
    active_nics: pulumi.Output[list]
    allow_forged_transmits: pulumi.Output[bool]
    allow_mac_changes: pulumi.Output[bool]
    allow_promiscuous: pulumi.Output[bool]
    check_beacon: pulumi.Output[bool]
    computed_policy: pulumi.Output[dict]
    """
    A map with a full set of the [policy
    options][host-vswitch-policy-options] computed from defaults and overrides,
    explaining the effective policy for this port group.
    """
    failback: pulumi.Output[bool]
    host_system_id: pulumi.Output[str]
    """
    The [managed object ID][docs-about-morefs] of
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
    ports: pulumi.Output[dict]
    """
    A list of ports that currently exist and are used on this port group.
    """
    shaping_average_bandwidth: pulumi.Output[float]
    shaping_burst_size: pulumi.Output[float]
    shaping_enabled: pulumi.Output[bool]
    shaping_peak_bandwidth: pulumi.Output[float]
    standby_nics: pulumi.Output[list]
    teaming_policy: pulumi.Output[str]
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
    def __init__(__self__, resource_name, opts=None, active_nics=None, allow_forged_transmits=None, allow_mac_changes=None, allow_promiscuous=None, check_beacon=None, failback=None, host_system_id=None, name=None, notify_switches=None, shaping_average_bandwidth=None, shaping_burst_size=None, shaping_enabled=None, shaping_peak_bandwidth=None, standby_nics=None, teaming_policy=None, virtual_switch_name=None, vlan_id=None, __name__=None, __opts__=None):
        """
        The `vsphere_host_port_group` resource can be used to manage vSphere standard
        port groups on an ESXi host. These port groups are connected to standard
        virtual switches, which can be managed by the
        [`vsphere_host_virtual_switch`][host-virtual-switch] resource.
        
        For an overview on vSphere networking concepts, see [this page][ref-vsphere-net-concepts].
        
        [host-virtual-switch]: /docs/providers/vsphere/r/host_virtual_switch.html
        [ref-vsphere-net-concepts]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-2B11DBB8-CB3C-4AFF-8885-EFEA0FC562F4.html
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] host_system_id: The [managed object ID][docs-about-morefs] of
               the host to set the port group up on. Forces a new resource if changed.
        :param pulumi.Input[str] name: The name of the port group.  Forces a new resource if
               changed.
        :param pulumi.Input[str] virtual_switch_name: The name of the virtual switch to bind
               this port group to. Forces a new resource if changed.
        :param pulumi.Input[float] vlan_id: The VLAN ID/trunk mode for this port group.  An ID of
               `0` denotes no tagging, an ID of `1`-`4094` tags with the specific ID, and an
               ID of `4095` enables trunk mode, allowing the guest to manage its own
               tagging. Default: `0`.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/r/host_port_group.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

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

        if opts is None:
            opts = pulumi.ResourceOptions()
        if opts.version is None:
            opts.version = utilities.get_version()
        super(HostPortGroup, __self__).__init__(
            'vsphere:index/hostPortGroup:HostPortGroup',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

