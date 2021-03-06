// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.VSphere
{
    /// <summary>
    /// The `vsphere.HostPortGroup` resource can be used to manage vSphere standard
    /// port groups on an ESXi host. These port groups are connected to standard
    /// virtual switches, which can be managed by the
    /// `vsphere.HostVirtualSwitch` resource.
    /// 
    /// For an overview on vSphere networking concepts, see [this page][ref-vsphere-net-concepts].
    /// 
    /// [ref-vsphere-net-concepts]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-2B11DBB8-CB3C-4AFF-8885-EFEA0FC562F4.html
    /// 
    /// ## Example Usage
    /// ### Create a virtual switch and bind a port group to it
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using VSphere = Pulumi.VSphere;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var datacenter = Output.Create(VSphere.GetDatacenter.InvokeAsync(new VSphere.GetDatacenterArgs
    ///         {
    ///             Name = "dc1",
    ///         }));
    ///         var esxiHost = datacenter.Apply(datacenter =&gt; Output.Create(VSphere.GetHost.InvokeAsync(new VSphere.GetHostArgs
    ///         {
    ///             DatacenterId = datacenter.Id,
    ///             Name = "esxi1",
    ///         })));
    ///         var @switch = new VSphere.HostVirtualSwitch("switch", new VSphere.HostVirtualSwitchArgs
    ///         {
    ///             ActiveNics = 
    ///             {
    ///                 "vmnic0",
    ///             },
    ///             HostSystemId = esxiHost.Apply(esxiHost =&gt; esxiHost.Id),
    ///             NetworkAdapters = 
    ///             {
    ///                 "vmnic0",
    ///                 "vmnic1",
    ///             },
    ///             StandbyNics = 
    ///             {
    ///                 "vmnic1",
    ///             },
    ///         });
    ///         var pg = new VSphere.HostPortGroup("pg", new VSphere.HostPortGroupArgs
    ///         {
    ///             HostSystemId = esxiHost.Apply(esxiHost =&gt; esxiHost.Id),
    ///             VirtualSwitchName = @switch.Name,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ### Create a port group with VLAN set and some overrides
    /// 
    /// This example sets the trunk mode VLAN (`4095`, which passes through all tags)
    /// and sets
    /// `allow_promiscuous`
    /// to ensure that all traffic is seen on the port. The latter setting overrides
    /// the implicit default of `false` set on the virtual switch.
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using VSphere = Pulumi.VSphere;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var datacenter = Output.Create(VSphere.GetDatacenter.InvokeAsync(new VSphere.GetDatacenterArgs
    ///         {
    ///             Name = "dc1",
    ///         }));
    ///         var esxiHost = datacenter.Apply(datacenter =&gt; Output.Create(VSphere.GetHost.InvokeAsync(new VSphere.GetHostArgs
    ///         {
    ///             DatacenterId = datacenter.Id,
    ///             Name = "esxi1",
    ///         })));
    ///         var @switch = new VSphere.HostVirtualSwitch("switch", new VSphere.HostVirtualSwitchArgs
    ///         {
    ///             ActiveNics = 
    ///             {
    ///                 "vmnic0",
    ///             },
    ///             HostSystemId = esxiHost.Apply(esxiHost =&gt; esxiHost.Id),
    ///             NetworkAdapters = 
    ///             {
    ///                 "vmnic0",
    ///                 "vmnic1",
    ///             },
    ///             StandbyNics = 
    ///             {
    ///                 "vmnic1",
    ///             },
    ///         });
    ///         var pg = new VSphere.HostPortGroup("pg", new VSphere.HostPortGroupArgs
    ///         {
    ///             AllowPromiscuous = true,
    ///             HostSystemId = esxiHost.Apply(esxiHost =&gt; esxiHost.Id),
    ///             VirtualSwitchName = @switch.Name,
    ///             VlanId = 4095,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class HostPortGroup : Pulumi.CustomResource
    {
        /// <summary>
        /// List of active network adapters used for load balancing.
        /// </summary>
        [Output("activeNics")]
        public Output<ImmutableArray<string>> ActiveNics { get; private set; } = null!;

        /// <summary>
        /// Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than
        /// that of its own.
        /// </summary>
        [Output("allowForgedTransmits")]
        public Output<bool?> AllowForgedTransmits { get; private set; } = null!;

        /// <summary>
        /// Controls whether or not the Media Access Control (MAC) address can be changed.
        /// </summary>
        [Output("allowMacChanges")]
        public Output<bool?> AllowMacChanges { get; private set; } = null!;

        /// <summary>
        /// Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port.
        /// </summary>
        [Output("allowPromiscuous")]
        public Output<bool?> AllowPromiscuous { get; private set; } = null!;

        /// <summary>
        /// Enable beacon probing. Requires that the vSwitch has been configured to use a beacon. If disabled, link status is used
        /// only.
        /// </summary>
        [Output("checkBeacon")]
        public Output<bool?> CheckBeacon { get; private set; } = null!;

        /// <summary>
        /// A map with a full set of the policy
        /// options computed from defaults and overrides,
        /// explaining the effective policy for this port group.
        /// </summary>
        [Output("computedPolicy")]
        public Output<ImmutableDictionary<string, string>> ComputedPolicy { get; private set; } = null!;

        /// <summary>
        /// If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.
        /// </summary>
        [Output("failback")]
        public Output<bool?> Failback { get; private set; } = null!;

        /// <summary>
        /// The managed object ID of
        /// the host to set the port group up on. Forces a new resource if changed.
        /// </summary>
        [Output("hostSystemId")]
        public Output<string> HostSystemId { get; private set; } = null!;

        /// <summary>
        /// The key for this port group as returned from the vSphere API.
        /// </summary>
        [Output("key")]
        public Output<string> Key { get; private set; } = null!;

        /// <summary>
        /// The name of the port group.  Forces a new resource if
        /// changed.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.
        /// </summary>
        [Output("notifySwitches")]
        public Output<bool?> NotifySwitches { get; private set; } = null!;

        /// <summary>
        /// A list of ports that currently exist and are used on this port group.
        /// </summary>
        [Output("ports")]
        public Output<Outputs.HostPortGroupPorts> Ports { get; private set; } = null!;

        /// <summary>
        /// The average bandwidth in bits per second if traffic shaping is enabled.
        /// </summary>
        [Output("shapingAverageBandwidth")]
        public Output<int?> ShapingAverageBandwidth { get; private set; } = null!;

        /// <summary>
        /// The maximum burst size allowed in bytes if traffic shaping is enabled.
        /// </summary>
        [Output("shapingBurstSize")]
        public Output<int?> ShapingBurstSize { get; private set; } = null!;

        /// <summary>
        /// Enable traffic shaping on this virtual switch or port group.
        /// </summary>
        [Output("shapingEnabled")]
        public Output<bool?> ShapingEnabled { get; private set; } = null!;

        /// <summary>
        /// The peak bandwidth during bursts in bits per second if traffic shaping is enabled.
        /// </summary>
        [Output("shapingPeakBandwidth")]
        public Output<int?> ShapingPeakBandwidth { get; private set; } = null!;

        /// <summary>
        /// List of standby network adapters used for failover.
        /// </summary>
        [Output("standbyNics")]
        public Output<ImmutableArray<string>> StandbyNics { get; private set; } = null!;

        /// <summary>
        /// The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, or
        /// failover_explicit.
        /// </summary>
        [Output("teamingPolicy")]
        public Output<string?> TeamingPolicy { get; private set; } = null!;

        /// <summary>
        /// The name of the virtual switch to bind
        /// this port group to. Forces a new resource if changed.
        /// </summary>
        [Output("virtualSwitchName")]
        public Output<string> VirtualSwitchName { get; private set; } = null!;

        /// <summary>
        /// The VLAN ID/trunk mode for this port group.  An ID of
        /// `0` denotes no tagging, an ID of `1`-`4094` tags with the specific ID, and an
        /// ID of `4095` enables trunk mode, allowing the guest to manage its own
        /// tagging. Default: `0`.
        /// </summary>
        [Output("vlanId")]
        public Output<int?> VlanId { get; private set; } = null!;


        /// <summary>
        /// Create a HostPortGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public HostPortGroup(string name, HostPortGroupArgs args, CustomResourceOptions? options = null)
            : base("vsphere:index/hostPortGroup:HostPortGroup", name, args ?? new HostPortGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private HostPortGroup(string name, Input<string> id, HostPortGroupState? state = null, CustomResourceOptions? options = null)
            : base("vsphere:index/hostPortGroup:HostPortGroup", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing HostPortGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static HostPortGroup Get(string name, Input<string> id, HostPortGroupState? state = null, CustomResourceOptions? options = null)
        {
            return new HostPortGroup(name, id, state, options);
        }
    }

    public sealed class HostPortGroupArgs : Pulumi.ResourceArgs
    {
        [Input("activeNics")]
        private InputList<string>? _activeNics;

        /// <summary>
        /// List of active network adapters used for load balancing.
        /// </summary>
        public InputList<string> ActiveNics
        {
            get => _activeNics ?? (_activeNics = new InputList<string>());
            set => _activeNics = value;
        }

        /// <summary>
        /// Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than
        /// that of its own.
        /// </summary>
        [Input("allowForgedTransmits")]
        public Input<bool>? AllowForgedTransmits { get; set; }

        /// <summary>
        /// Controls whether or not the Media Access Control (MAC) address can be changed.
        /// </summary>
        [Input("allowMacChanges")]
        public Input<bool>? AllowMacChanges { get; set; }

        /// <summary>
        /// Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port.
        /// </summary>
        [Input("allowPromiscuous")]
        public Input<bool>? AllowPromiscuous { get; set; }

        /// <summary>
        /// Enable beacon probing. Requires that the vSwitch has been configured to use a beacon. If disabled, link status is used
        /// only.
        /// </summary>
        [Input("checkBeacon")]
        public Input<bool>? CheckBeacon { get; set; }

        /// <summary>
        /// If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.
        /// </summary>
        [Input("failback")]
        public Input<bool>? Failback { get; set; }

        /// <summary>
        /// The managed object ID of
        /// the host to set the port group up on. Forces a new resource if changed.
        /// </summary>
        [Input("hostSystemId", required: true)]
        public Input<string> HostSystemId { get; set; } = null!;

        /// <summary>
        /// The name of the port group.  Forces a new resource if
        /// changed.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.
        /// </summary>
        [Input("notifySwitches")]
        public Input<bool>? NotifySwitches { get; set; }

        /// <summary>
        /// The average bandwidth in bits per second if traffic shaping is enabled.
        /// </summary>
        [Input("shapingAverageBandwidth")]
        public Input<int>? ShapingAverageBandwidth { get; set; }

        /// <summary>
        /// The maximum burst size allowed in bytes if traffic shaping is enabled.
        /// </summary>
        [Input("shapingBurstSize")]
        public Input<int>? ShapingBurstSize { get; set; }

        /// <summary>
        /// Enable traffic shaping on this virtual switch or port group.
        /// </summary>
        [Input("shapingEnabled")]
        public Input<bool>? ShapingEnabled { get; set; }

        /// <summary>
        /// The peak bandwidth during bursts in bits per second if traffic shaping is enabled.
        /// </summary>
        [Input("shapingPeakBandwidth")]
        public Input<int>? ShapingPeakBandwidth { get; set; }

        [Input("standbyNics")]
        private InputList<string>? _standbyNics;

        /// <summary>
        /// List of standby network adapters used for failover.
        /// </summary>
        public InputList<string> StandbyNics
        {
            get => _standbyNics ?? (_standbyNics = new InputList<string>());
            set => _standbyNics = value;
        }

        /// <summary>
        /// The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, or
        /// failover_explicit.
        /// </summary>
        [Input("teamingPolicy")]
        public Input<string>? TeamingPolicy { get; set; }

        /// <summary>
        /// The name of the virtual switch to bind
        /// this port group to. Forces a new resource if changed.
        /// </summary>
        [Input("virtualSwitchName", required: true)]
        public Input<string> VirtualSwitchName { get; set; } = null!;

        /// <summary>
        /// The VLAN ID/trunk mode for this port group.  An ID of
        /// `0` denotes no tagging, an ID of `1`-`4094` tags with the specific ID, and an
        /// ID of `4095` enables trunk mode, allowing the guest to manage its own
        /// tagging. Default: `0`.
        /// </summary>
        [Input("vlanId")]
        public Input<int>? VlanId { get; set; }

        public HostPortGroupArgs()
        {
        }
    }

    public sealed class HostPortGroupState : Pulumi.ResourceArgs
    {
        [Input("activeNics")]
        private InputList<string>? _activeNics;

        /// <summary>
        /// List of active network adapters used for load balancing.
        /// </summary>
        public InputList<string> ActiveNics
        {
            get => _activeNics ?? (_activeNics = new InputList<string>());
            set => _activeNics = value;
        }

        /// <summary>
        /// Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than
        /// that of its own.
        /// </summary>
        [Input("allowForgedTransmits")]
        public Input<bool>? AllowForgedTransmits { get; set; }

        /// <summary>
        /// Controls whether or not the Media Access Control (MAC) address can be changed.
        /// </summary>
        [Input("allowMacChanges")]
        public Input<bool>? AllowMacChanges { get; set; }

        /// <summary>
        /// Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port.
        /// </summary>
        [Input("allowPromiscuous")]
        public Input<bool>? AllowPromiscuous { get; set; }

        /// <summary>
        /// Enable beacon probing. Requires that the vSwitch has been configured to use a beacon. If disabled, link status is used
        /// only.
        /// </summary>
        [Input("checkBeacon")]
        public Input<bool>? CheckBeacon { get; set; }

        [Input("computedPolicy")]
        private InputMap<string>? _computedPolicy;

        /// <summary>
        /// A map with a full set of the policy
        /// options computed from defaults and overrides,
        /// explaining the effective policy for this port group.
        /// </summary>
        public InputMap<string> ComputedPolicy
        {
            get => _computedPolicy ?? (_computedPolicy = new InputMap<string>());
            set => _computedPolicy = value;
        }

        /// <summary>
        /// If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.
        /// </summary>
        [Input("failback")]
        public Input<bool>? Failback { get; set; }

        /// <summary>
        /// The managed object ID of
        /// the host to set the port group up on. Forces a new resource if changed.
        /// </summary>
        [Input("hostSystemId")]
        public Input<string>? HostSystemId { get; set; }

        /// <summary>
        /// The key for this port group as returned from the vSphere API.
        /// </summary>
        [Input("key")]
        public Input<string>? Key { get; set; }

        /// <summary>
        /// The name of the port group.  Forces a new resource if
        /// changed.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.
        /// </summary>
        [Input("notifySwitches")]
        public Input<bool>? NotifySwitches { get; set; }

        /// <summary>
        /// A list of ports that currently exist and are used on this port group.
        /// </summary>
        [Input("ports")]
        public Input<Inputs.HostPortGroupPortsGetArgs>? Ports { get; set; }

        /// <summary>
        /// The average bandwidth in bits per second if traffic shaping is enabled.
        /// </summary>
        [Input("shapingAverageBandwidth")]
        public Input<int>? ShapingAverageBandwidth { get; set; }

        /// <summary>
        /// The maximum burst size allowed in bytes if traffic shaping is enabled.
        /// </summary>
        [Input("shapingBurstSize")]
        public Input<int>? ShapingBurstSize { get; set; }

        /// <summary>
        /// Enable traffic shaping on this virtual switch or port group.
        /// </summary>
        [Input("shapingEnabled")]
        public Input<bool>? ShapingEnabled { get; set; }

        /// <summary>
        /// The peak bandwidth during bursts in bits per second if traffic shaping is enabled.
        /// </summary>
        [Input("shapingPeakBandwidth")]
        public Input<int>? ShapingPeakBandwidth { get; set; }

        [Input("standbyNics")]
        private InputList<string>? _standbyNics;

        /// <summary>
        /// List of standby network adapters used for failover.
        /// </summary>
        public InputList<string> StandbyNics
        {
            get => _standbyNics ?? (_standbyNics = new InputList<string>());
            set => _standbyNics = value;
        }

        /// <summary>
        /// The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, or
        /// failover_explicit.
        /// </summary>
        [Input("teamingPolicy")]
        public Input<string>? TeamingPolicy { get; set; }

        /// <summary>
        /// The name of the virtual switch to bind
        /// this port group to. Forces a new resource if changed.
        /// </summary>
        [Input("virtualSwitchName")]
        public Input<string>? VirtualSwitchName { get; set; }

        /// <summary>
        /// The VLAN ID/trunk mode for this port group.  An ID of
        /// `0` denotes no tagging, an ID of `1`-`4094` tags with the specific ID, and an
        /// ID of `4095` enables trunk mode, allowing the guest to manage its own
        /// tagging. Default: `0`.
        /// </summary>
        [Input("vlanId")]
        public Input<int>? VlanId { get; set; }

        public HostPortGroupState()
        {
        }
    }
}
