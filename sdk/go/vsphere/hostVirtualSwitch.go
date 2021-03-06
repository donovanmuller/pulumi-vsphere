// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package vsphere

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type HostVirtualSwitch struct {
	pulumi.CustomResourceState

	// The list of active network adapters used for load
	// balancing.
	ActiveNics pulumi.StringArrayOutput `pulumi:"activeNics"`
	// Controls whether or not the virtual
	// network adapter is allowed to send network traffic with a different MAC
	// address than that of its own. Default: `true`.
	AllowForgedTransmits pulumi.BoolPtrOutput `pulumi:"allowForgedTransmits"`
	// Controls whether or not the Media Access
	// Control (MAC) address can be changed. Default: `true`.
	AllowMacChanges pulumi.BoolPtrOutput `pulumi:"allowMacChanges"`
	// Enable promiscuous mode on the network. This
	// flag indicates whether or not all traffic is seen on a given port. Default:
	// `false`.
	AllowPromiscuous pulumi.BoolPtrOutput `pulumi:"allowPromiscuous"`
	// The interval, in seconds, that a NIC beacon
	// packet is sent out. This can be used with `checkBeacon` to
	// offer link failure capability beyond link status only. Default: `1`.
	BeaconInterval pulumi.IntPtrOutput `pulumi:"beaconInterval"`
	// Enable beacon probing - this requires that the
	// `beaconInterval` option has been set in the bridge
	// options. If this is set to `false`, only link status is used to check for
	// failed NICs.  Default: `false`.
	CheckBeacon pulumi.BoolPtrOutput `pulumi:"checkBeacon"`
	// If set to `true`, the teaming policy will re-activate
	// failed interfaces higher in precedence when they come back up.  Default:
	// `true`.
	Failback pulumi.BoolPtrOutput `pulumi:"failback"`
	// The managed object ID of
	// the host to set the virtual switch up on. Forces a new resource if changed.
	HostSystemId pulumi.StringOutput `pulumi:"hostSystemId"`
	// Whether to `advertise` or `listen`
	// for link discovery traffic. Default: `listen`.
	LinkDiscoveryOperation pulumi.StringPtrOutput `pulumi:"linkDiscoveryOperation"`
	// The discovery protocol type.  Valid
	// types are `cpd` and `lldp`. Default: `cdp`.
	LinkDiscoveryProtocol pulumi.StringPtrOutput `pulumi:"linkDiscoveryProtocol"`
	// The maximum transmission unit (MTU) for the virtual
	// switch. Default: `1500`.
	Mtu pulumi.IntPtrOutput `pulumi:"mtu"`
	// The name of the virtual switch. Forces a new resource if
	// changed.
	Name pulumi.StringOutput `pulumi:"name"`
	// The network interfaces to bind to the bridge.
	NetworkAdapters pulumi.StringArrayOutput `pulumi:"networkAdapters"`
	// If set to `true`, the teaming policy will
	// notify the broadcast network of a NIC failover, triggering cache updates.
	// Default: `true`.
	NotifySwitches pulumi.BoolPtrOutput `pulumi:"notifySwitches"`
	// The number of ports to create with this
	// virtual switch. Default: `128`.
	NumberOfPorts pulumi.IntPtrOutput `pulumi:"numberOfPorts"`
	// The average bandwidth in bits per
	// second if traffic shaping is enabled. Default: `0`
	ShapingAverageBandwidth pulumi.IntPtrOutput `pulumi:"shapingAverageBandwidth"`
	// The maximum burst size allowed in bytes if
	// shaping is enabled. Default: `0`
	ShapingBurstSize pulumi.IntPtrOutput `pulumi:"shapingBurstSize"`
	// Set to `true` to enable the traffic shaper for
	// ports managed by this virtual switch. Default: `false`.
	ShapingEnabled pulumi.BoolPtrOutput `pulumi:"shapingEnabled"`
	// The peak bandwidth during bursts in
	// bits per second if traffic shaping is enabled. Default: `0`
	ShapingPeakBandwidth pulumi.IntPtrOutput `pulumi:"shapingPeakBandwidth"`
	// The list of standby network adapters used for
	// failover.
	StandbyNics pulumi.StringArrayOutput `pulumi:"standbyNics"`
	// The network adapter teaming policy. Can be one
	// of `loadbalanceIp`, `loadbalanceSrcmac`, `loadbalanceSrcid`, or
	// `failoverExplicit`. Default: `loadbalanceSrcid`.
	TeamingPolicy pulumi.StringPtrOutput `pulumi:"teamingPolicy"`
}

// NewHostVirtualSwitch registers a new resource with the given unique name, arguments, and options.
func NewHostVirtualSwitch(ctx *pulumi.Context,
	name string, args *HostVirtualSwitchArgs, opts ...pulumi.ResourceOption) (*HostVirtualSwitch, error) {
	if args == nil || args.ActiveNics == nil {
		return nil, errors.New("missing required argument 'ActiveNics'")
	}
	if args == nil || args.HostSystemId == nil {
		return nil, errors.New("missing required argument 'HostSystemId'")
	}
	if args == nil || args.NetworkAdapters == nil {
		return nil, errors.New("missing required argument 'NetworkAdapters'")
	}
	if args == nil || args.StandbyNics == nil {
		return nil, errors.New("missing required argument 'StandbyNics'")
	}
	if args == nil {
		args = &HostVirtualSwitchArgs{}
	}
	var resource HostVirtualSwitch
	err := ctx.RegisterResource("vsphere:index/hostVirtualSwitch:HostVirtualSwitch", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetHostVirtualSwitch gets an existing HostVirtualSwitch resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetHostVirtualSwitch(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *HostVirtualSwitchState, opts ...pulumi.ResourceOption) (*HostVirtualSwitch, error) {
	var resource HostVirtualSwitch
	err := ctx.ReadResource("vsphere:index/hostVirtualSwitch:HostVirtualSwitch", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering HostVirtualSwitch resources.
type hostVirtualSwitchState struct {
	// The list of active network adapters used for load
	// balancing.
	ActiveNics []string `pulumi:"activeNics"`
	// Controls whether or not the virtual
	// network adapter is allowed to send network traffic with a different MAC
	// address than that of its own. Default: `true`.
	AllowForgedTransmits *bool `pulumi:"allowForgedTransmits"`
	// Controls whether or not the Media Access
	// Control (MAC) address can be changed. Default: `true`.
	AllowMacChanges *bool `pulumi:"allowMacChanges"`
	// Enable promiscuous mode on the network. This
	// flag indicates whether or not all traffic is seen on a given port. Default:
	// `false`.
	AllowPromiscuous *bool `pulumi:"allowPromiscuous"`
	// The interval, in seconds, that a NIC beacon
	// packet is sent out. This can be used with `checkBeacon` to
	// offer link failure capability beyond link status only. Default: `1`.
	BeaconInterval *int `pulumi:"beaconInterval"`
	// Enable beacon probing - this requires that the
	// `beaconInterval` option has been set in the bridge
	// options. If this is set to `false`, only link status is used to check for
	// failed NICs.  Default: `false`.
	CheckBeacon *bool `pulumi:"checkBeacon"`
	// If set to `true`, the teaming policy will re-activate
	// failed interfaces higher in precedence when they come back up.  Default:
	// `true`.
	Failback *bool `pulumi:"failback"`
	// The managed object ID of
	// the host to set the virtual switch up on. Forces a new resource if changed.
	HostSystemId *string `pulumi:"hostSystemId"`
	// Whether to `advertise` or `listen`
	// for link discovery traffic. Default: `listen`.
	LinkDiscoveryOperation *string `pulumi:"linkDiscoveryOperation"`
	// The discovery protocol type.  Valid
	// types are `cpd` and `lldp`. Default: `cdp`.
	LinkDiscoveryProtocol *string `pulumi:"linkDiscoveryProtocol"`
	// The maximum transmission unit (MTU) for the virtual
	// switch. Default: `1500`.
	Mtu *int `pulumi:"mtu"`
	// The name of the virtual switch. Forces a new resource if
	// changed.
	Name *string `pulumi:"name"`
	// The network interfaces to bind to the bridge.
	NetworkAdapters []string `pulumi:"networkAdapters"`
	// If set to `true`, the teaming policy will
	// notify the broadcast network of a NIC failover, triggering cache updates.
	// Default: `true`.
	NotifySwitches *bool `pulumi:"notifySwitches"`
	// The number of ports to create with this
	// virtual switch. Default: `128`.
	NumberOfPorts *int `pulumi:"numberOfPorts"`
	// The average bandwidth in bits per
	// second if traffic shaping is enabled. Default: `0`
	ShapingAverageBandwidth *int `pulumi:"shapingAverageBandwidth"`
	// The maximum burst size allowed in bytes if
	// shaping is enabled. Default: `0`
	ShapingBurstSize *int `pulumi:"shapingBurstSize"`
	// Set to `true` to enable the traffic shaper for
	// ports managed by this virtual switch. Default: `false`.
	ShapingEnabled *bool `pulumi:"shapingEnabled"`
	// The peak bandwidth during bursts in
	// bits per second if traffic shaping is enabled. Default: `0`
	ShapingPeakBandwidth *int `pulumi:"shapingPeakBandwidth"`
	// The list of standby network adapters used for
	// failover.
	StandbyNics []string `pulumi:"standbyNics"`
	// The network adapter teaming policy. Can be one
	// of `loadbalanceIp`, `loadbalanceSrcmac`, `loadbalanceSrcid`, or
	// `failoverExplicit`. Default: `loadbalanceSrcid`.
	TeamingPolicy *string `pulumi:"teamingPolicy"`
}

type HostVirtualSwitchState struct {
	// The list of active network adapters used for load
	// balancing.
	ActiveNics pulumi.StringArrayInput
	// Controls whether or not the virtual
	// network adapter is allowed to send network traffic with a different MAC
	// address than that of its own. Default: `true`.
	AllowForgedTransmits pulumi.BoolPtrInput
	// Controls whether or not the Media Access
	// Control (MAC) address can be changed. Default: `true`.
	AllowMacChanges pulumi.BoolPtrInput
	// Enable promiscuous mode on the network. This
	// flag indicates whether or not all traffic is seen on a given port. Default:
	// `false`.
	AllowPromiscuous pulumi.BoolPtrInput
	// The interval, in seconds, that a NIC beacon
	// packet is sent out. This can be used with `checkBeacon` to
	// offer link failure capability beyond link status only. Default: `1`.
	BeaconInterval pulumi.IntPtrInput
	// Enable beacon probing - this requires that the
	// `beaconInterval` option has been set in the bridge
	// options. If this is set to `false`, only link status is used to check for
	// failed NICs.  Default: `false`.
	CheckBeacon pulumi.BoolPtrInput
	// If set to `true`, the teaming policy will re-activate
	// failed interfaces higher in precedence when they come back up.  Default:
	// `true`.
	Failback pulumi.BoolPtrInput
	// The managed object ID of
	// the host to set the virtual switch up on. Forces a new resource if changed.
	HostSystemId pulumi.StringPtrInput
	// Whether to `advertise` or `listen`
	// for link discovery traffic. Default: `listen`.
	LinkDiscoveryOperation pulumi.StringPtrInput
	// The discovery protocol type.  Valid
	// types are `cpd` and `lldp`. Default: `cdp`.
	LinkDiscoveryProtocol pulumi.StringPtrInput
	// The maximum transmission unit (MTU) for the virtual
	// switch. Default: `1500`.
	Mtu pulumi.IntPtrInput
	// The name of the virtual switch. Forces a new resource if
	// changed.
	Name pulumi.StringPtrInput
	// The network interfaces to bind to the bridge.
	NetworkAdapters pulumi.StringArrayInput
	// If set to `true`, the teaming policy will
	// notify the broadcast network of a NIC failover, triggering cache updates.
	// Default: `true`.
	NotifySwitches pulumi.BoolPtrInput
	// The number of ports to create with this
	// virtual switch. Default: `128`.
	NumberOfPorts pulumi.IntPtrInput
	// The average bandwidth in bits per
	// second if traffic shaping is enabled. Default: `0`
	ShapingAverageBandwidth pulumi.IntPtrInput
	// The maximum burst size allowed in bytes if
	// shaping is enabled. Default: `0`
	ShapingBurstSize pulumi.IntPtrInput
	// Set to `true` to enable the traffic shaper for
	// ports managed by this virtual switch. Default: `false`.
	ShapingEnabled pulumi.BoolPtrInput
	// The peak bandwidth during bursts in
	// bits per second if traffic shaping is enabled. Default: `0`
	ShapingPeakBandwidth pulumi.IntPtrInput
	// The list of standby network adapters used for
	// failover.
	StandbyNics pulumi.StringArrayInput
	// The network adapter teaming policy. Can be one
	// of `loadbalanceIp`, `loadbalanceSrcmac`, `loadbalanceSrcid`, or
	// `failoverExplicit`. Default: `loadbalanceSrcid`.
	TeamingPolicy pulumi.StringPtrInput
}

func (HostVirtualSwitchState) ElementType() reflect.Type {
	return reflect.TypeOf((*hostVirtualSwitchState)(nil)).Elem()
}

type hostVirtualSwitchArgs struct {
	// The list of active network adapters used for load
	// balancing.
	ActiveNics []string `pulumi:"activeNics"`
	// Controls whether or not the virtual
	// network adapter is allowed to send network traffic with a different MAC
	// address than that of its own. Default: `true`.
	AllowForgedTransmits *bool `pulumi:"allowForgedTransmits"`
	// Controls whether or not the Media Access
	// Control (MAC) address can be changed. Default: `true`.
	AllowMacChanges *bool `pulumi:"allowMacChanges"`
	// Enable promiscuous mode on the network. This
	// flag indicates whether or not all traffic is seen on a given port. Default:
	// `false`.
	AllowPromiscuous *bool `pulumi:"allowPromiscuous"`
	// The interval, in seconds, that a NIC beacon
	// packet is sent out. This can be used with `checkBeacon` to
	// offer link failure capability beyond link status only. Default: `1`.
	BeaconInterval *int `pulumi:"beaconInterval"`
	// Enable beacon probing - this requires that the
	// `beaconInterval` option has been set in the bridge
	// options. If this is set to `false`, only link status is used to check for
	// failed NICs.  Default: `false`.
	CheckBeacon *bool `pulumi:"checkBeacon"`
	// If set to `true`, the teaming policy will re-activate
	// failed interfaces higher in precedence when they come back up.  Default:
	// `true`.
	Failback *bool `pulumi:"failback"`
	// The managed object ID of
	// the host to set the virtual switch up on. Forces a new resource if changed.
	HostSystemId string `pulumi:"hostSystemId"`
	// Whether to `advertise` or `listen`
	// for link discovery traffic. Default: `listen`.
	LinkDiscoveryOperation *string `pulumi:"linkDiscoveryOperation"`
	// The discovery protocol type.  Valid
	// types are `cpd` and `lldp`. Default: `cdp`.
	LinkDiscoveryProtocol *string `pulumi:"linkDiscoveryProtocol"`
	// The maximum transmission unit (MTU) for the virtual
	// switch. Default: `1500`.
	Mtu *int `pulumi:"mtu"`
	// The name of the virtual switch. Forces a new resource if
	// changed.
	Name *string `pulumi:"name"`
	// The network interfaces to bind to the bridge.
	NetworkAdapters []string `pulumi:"networkAdapters"`
	// If set to `true`, the teaming policy will
	// notify the broadcast network of a NIC failover, triggering cache updates.
	// Default: `true`.
	NotifySwitches *bool `pulumi:"notifySwitches"`
	// The number of ports to create with this
	// virtual switch. Default: `128`.
	NumberOfPorts *int `pulumi:"numberOfPorts"`
	// The average bandwidth in bits per
	// second if traffic shaping is enabled. Default: `0`
	ShapingAverageBandwidth *int `pulumi:"shapingAverageBandwidth"`
	// The maximum burst size allowed in bytes if
	// shaping is enabled. Default: `0`
	ShapingBurstSize *int `pulumi:"shapingBurstSize"`
	// Set to `true` to enable the traffic shaper for
	// ports managed by this virtual switch. Default: `false`.
	ShapingEnabled *bool `pulumi:"shapingEnabled"`
	// The peak bandwidth during bursts in
	// bits per second if traffic shaping is enabled. Default: `0`
	ShapingPeakBandwidth *int `pulumi:"shapingPeakBandwidth"`
	// The list of standby network adapters used for
	// failover.
	StandbyNics []string `pulumi:"standbyNics"`
	// The network adapter teaming policy. Can be one
	// of `loadbalanceIp`, `loadbalanceSrcmac`, `loadbalanceSrcid`, or
	// `failoverExplicit`. Default: `loadbalanceSrcid`.
	TeamingPolicy *string `pulumi:"teamingPolicy"`
}

// The set of arguments for constructing a HostVirtualSwitch resource.
type HostVirtualSwitchArgs struct {
	// The list of active network adapters used for load
	// balancing.
	ActiveNics pulumi.StringArrayInput
	// Controls whether or not the virtual
	// network adapter is allowed to send network traffic with a different MAC
	// address than that of its own. Default: `true`.
	AllowForgedTransmits pulumi.BoolPtrInput
	// Controls whether or not the Media Access
	// Control (MAC) address can be changed. Default: `true`.
	AllowMacChanges pulumi.BoolPtrInput
	// Enable promiscuous mode on the network. This
	// flag indicates whether or not all traffic is seen on a given port. Default:
	// `false`.
	AllowPromiscuous pulumi.BoolPtrInput
	// The interval, in seconds, that a NIC beacon
	// packet is sent out. This can be used with `checkBeacon` to
	// offer link failure capability beyond link status only. Default: `1`.
	BeaconInterval pulumi.IntPtrInput
	// Enable beacon probing - this requires that the
	// `beaconInterval` option has been set in the bridge
	// options. If this is set to `false`, only link status is used to check for
	// failed NICs.  Default: `false`.
	CheckBeacon pulumi.BoolPtrInput
	// If set to `true`, the teaming policy will re-activate
	// failed interfaces higher in precedence when they come back up.  Default:
	// `true`.
	Failback pulumi.BoolPtrInput
	// The managed object ID of
	// the host to set the virtual switch up on. Forces a new resource if changed.
	HostSystemId pulumi.StringInput
	// Whether to `advertise` or `listen`
	// for link discovery traffic. Default: `listen`.
	LinkDiscoveryOperation pulumi.StringPtrInput
	// The discovery protocol type.  Valid
	// types are `cpd` and `lldp`. Default: `cdp`.
	LinkDiscoveryProtocol pulumi.StringPtrInput
	// The maximum transmission unit (MTU) for the virtual
	// switch. Default: `1500`.
	Mtu pulumi.IntPtrInput
	// The name of the virtual switch. Forces a new resource if
	// changed.
	Name pulumi.StringPtrInput
	// The network interfaces to bind to the bridge.
	NetworkAdapters pulumi.StringArrayInput
	// If set to `true`, the teaming policy will
	// notify the broadcast network of a NIC failover, triggering cache updates.
	// Default: `true`.
	NotifySwitches pulumi.BoolPtrInput
	// The number of ports to create with this
	// virtual switch. Default: `128`.
	NumberOfPorts pulumi.IntPtrInput
	// The average bandwidth in bits per
	// second if traffic shaping is enabled. Default: `0`
	ShapingAverageBandwidth pulumi.IntPtrInput
	// The maximum burst size allowed in bytes if
	// shaping is enabled. Default: `0`
	ShapingBurstSize pulumi.IntPtrInput
	// Set to `true` to enable the traffic shaper for
	// ports managed by this virtual switch. Default: `false`.
	ShapingEnabled pulumi.BoolPtrInput
	// The peak bandwidth during bursts in
	// bits per second if traffic shaping is enabled. Default: `0`
	ShapingPeakBandwidth pulumi.IntPtrInput
	// The list of standby network adapters used for
	// failover.
	StandbyNics pulumi.StringArrayInput
	// The network adapter teaming policy. Can be one
	// of `loadbalanceIp`, `loadbalanceSrcmac`, `loadbalanceSrcid`, or
	// `failoverExplicit`. Default: `loadbalanceSrcid`.
	TeamingPolicy pulumi.StringPtrInput
}

func (HostVirtualSwitchArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*hostVirtualSwitchArgs)(nil)).Elem()
}
