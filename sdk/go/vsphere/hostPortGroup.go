// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package vsphere

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// The `.HostPortGroup` resource can be used to manage vSphere standard
// port groups on an ESXi host. These port groups are connected to standard
// virtual switches, which can be managed by the
// [`.HostVirtualSwitch`][host-virtual-switch] resource.
//
// For an overview on vSphere networking concepts, see [this page][ref-vsphere-net-concepts].
//
// [host-virtual-switch]: /docs/providers/vsphere/r/host_virtual_switch.html
// [ref-vsphere-net-concepts]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-2B11DBB8-CB3C-4AFF-8885-EFEA0FC562F4.html
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/r/host_port_group.html.markdown.
type HostPortGroup struct {
	pulumi.CustomResourceState

	// List of active network adapters used for load balancing.
	ActiveNics pulumi.StringArrayOutput `pulumi:"activeNics"`
	// Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than
	// that of its own.
	AllowForgedTransmits pulumi.BoolPtrOutput `pulumi:"allowForgedTransmits"`
	// Controls whether or not the Media Access Control (MAC) address can be changed.
	AllowMacChanges pulumi.BoolPtrOutput `pulumi:"allowMacChanges"`
	// Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port.
	AllowPromiscuous pulumi.BoolPtrOutput `pulumi:"allowPromiscuous"`
	// Enable beacon probing. Requires that the vSwitch has been configured to use a beacon. If disabled, link status is used
	// only.
	CheckBeacon pulumi.BoolPtrOutput `pulumi:"checkBeacon"`
	// A map with a full set of the [policy
	// options][host-vswitch-policy-options] computed from defaults and overrides,
	// explaining the effective policy for this port group.
	ComputedPolicy pulumi.StringMapOutput `pulumi:"computedPolicy"`
	// If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.
	Failback pulumi.BoolPtrOutput `pulumi:"failback"`
	// The [managed object ID][docs-about-morefs] of
	// the host to set the port group up on. Forces a new resource if changed.
	HostSystemId pulumi.StringOutput `pulumi:"hostSystemId"`
	// The key for this port group as returned from the vSphere API.
	Key pulumi.StringOutput `pulumi:"key"`
	// The name of the port group.  Forces a new resource if
	// changed.
	Name pulumi.StringOutput `pulumi:"name"`
	// If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.
	NotifySwitches pulumi.BoolPtrOutput `pulumi:"notifySwitches"`
	// A list of ports that currently exist and are used on this port group.
	Ports HostPortGroupPortsOutput `pulumi:"ports"`
	// The average bandwidth in bits per second if traffic shaping is enabled.
	ShapingAverageBandwidth pulumi.IntPtrOutput `pulumi:"shapingAverageBandwidth"`
	// The maximum burst size allowed in bytes if traffic shaping is enabled.
	ShapingBurstSize pulumi.IntPtrOutput `pulumi:"shapingBurstSize"`
	// Enable traffic shaping on this virtual switch or port group.
	ShapingEnabled pulumi.BoolPtrOutput `pulumi:"shapingEnabled"`
	// The peak bandwidth during bursts in bits per second if traffic shaping is enabled.
	ShapingPeakBandwidth pulumi.IntPtrOutput `pulumi:"shapingPeakBandwidth"`
	// List of standby network adapters used for failover.
	StandbyNics pulumi.StringArrayOutput `pulumi:"standbyNics"`
	// The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, or
	// failover_explicit.
	TeamingPolicy pulumi.StringPtrOutput `pulumi:"teamingPolicy"`
	// The name of the virtual switch to bind
	// this port group to. Forces a new resource if changed.
	VirtualSwitchName pulumi.StringOutput `pulumi:"virtualSwitchName"`
	// The VLAN ID/trunk mode for this port group.  An ID of
	// `0` denotes no tagging, an ID of `1`-`4094` tags with the specific ID, and an
	// ID of `4095` enables trunk mode, allowing the guest to manage its own
	// tagging. Default: `0`.
	VlanId pulumi.IntPtrOutput `pulumi:"vlanId"`
}

// NewHostPortGroup registers a new resource with the given unique name, arguments, and options.
func NewHostPortGroup(ctx *pulumi.Context,
	name string, args *HostPortGroupArgs, opts ...pulumi.ResourceOption) (*HostPortGroup, error) {
	if args == nil || args.HostSystemId == nil {
		return nil, errors.New("missing required argument 'HostSystemId'")
	}
	if args == nil || args.VirtualSwitchName == nil {
		return nil, errors.New("missing required argument 'VirtualSwitchName'")
	}
	if args == nil {
		args = &HostPortGroupArgs{}
	}
	var resource HostPortGroup
	err := ctx.RegisterResource("vsphere:index/hostPortGroup:HostPortGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetHostPortGroup gets an existing HostPortGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetHostPortGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *HostPortGroupState, opts ...pulumi.ResourceOption) (*HostPortGroup, error) {
	var resource HostPortGroup
	err := ctx.ReadResource("vsphere:index/hostPortGroup:HostPortGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering HostPortGroup resources.
type hostPortGroupState struct {
	// List of active network adapters used for load balancing.
	ActiveNics []string `pulumi:"activeNics"`
	// Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than
	// that of its own.
	AllowForgedTransmits *bool `pulumi:"allowForgedTransmits"`
	// Controls whether or not the Media Access Control (MAC) address can be changed.
	AllowMacChanges *bool `pulumi:"allowMacChanges"`
	// Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port.
	AllowPromiscuous *bool `pulumi:"allowPromiscuous"`
	// Enable beacon probing. Requires that the vSwitch has been configured to use a beacon. If disabled, link status is used
	// only.
	CheckBeacon *bool `pulumi:"checkBeacon"`
	// A map with a full set of the [policy
	// options][host-vswitch-policy-options] computed from defaults and overrides,
	// explaining the effective policy for this port group.
	ComputedPolicy map[string]string `pulumi:"computedPolicy"`
	// If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.
	Failback *bool `pulumi:"failback"`
	// The [managed object ID][docs-about-morefs] of
	// the host to set the port group up on. Forces a new resource if changed.
	HostSystemId *string `pulumi:"hostSystemId"`
	// The key for this port group as returned from the vSphere API.
	Key *string `pulumi:"key"`
	// The name of the port group.  Forces a new resource if
	// changed.
	Name *string `pulumi:"name"`
	// If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.
	NotifySwitches *bool `pulumi:"notifySwitches"`
	// A list of ports that currently exist and are used on this port group.
	Ports *HostPortGroupPorts `pulumi:"ports"`
	// The average bandwidth in bits per second if traffic shaping is enabled.
	ShapingAverageBandwidth *int `pulumi:"shapingAverageBandwidth"`
	// The maximum burst size allowed in bytes if traffic shaping is enabled.
	ShapingBurstSize *int `pulumi:"shapingBurstSize"`
	// Enable traffic shaping on this virtual switch or port group.
	ShapingEnabled *bool `pulumi:"shapingEnabled"`
	// The peak bandwidth during bursts in bits per second if traffic shaping is enabled.
	ShapingPeakBandwidth *int `pulumi:"shapingPeakBandwidth"`
	// List of standby network adapters used for failover.
	StandbyNics []string `pulumi:"standbyNics"`
	// The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, or
	// failover_explicit.
	TeamingPolicy *string `pulumi:"teamingPolicy"`
	// The name of the virtual switch to bind
	// this port group to. Forces a new resource if changed.
	VirtualSwitchName *string `pulumi:"virtualSwitchName"`
	// The VLAN ID/trunk mode for this port group.  An ID of
	// `0` denotes no tagging, an ID of `1`-`4094` tags with the specific ID, and an
	// ID of `4095` enables trunk mode, allowing the guest to manage its own
	// tagging. Default: `0`.
	VlanId *int `pulumi:"vlanId"`
}

type HostPortGroupState struct {
	// List of active network adapters used for load balancing.
	ActiveNics pulumi.StringArrayInput
	// Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than
	// that of its own.
	AllowForgedTransmits pulumi.BoolPtrInput
	// Controls whether or not the Media Access Control (MAC) address can be changed.
	AllowMacChanges pulumi.BoolPtrInput
	// Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port.
	AllowPromiscuous pulumi.BoolPtrInput
	// Enable beacon probing. Requires that the vSwitch has been configured to use a beacon. If disabled, link status is used
	// only.
	CheckBeacon pulumi.BoolPtrInput
	// A map with a full set of the [policy
	// options][host-vswitch-policy-options] computed from defaults and overrides,
	// explaining the effective policy for this port group.
	ComputedPolicy pulumi.StringMapInput
	// If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.
	Failback pulumi.BoolPtrInput
	// The [managed object ID][docs-about-morefs] of
	// the host to set the port group up on. Forces a new resource if changed.
	HostSystemId pulumi.StringPtrInput
	// The key for this port group as returned from the vSphere API.
	Key pulumi.StringPtrInput
	// The name of the port group.  Forces a new resource if
	// changed.
	Name pulumi.StringPtrInput
	// If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.
	NotifySwitches pulumi.BoolPtrInput
	// A list of ports that currently exist and are used on this port group.
	Ports HostPortGroupPortsPtrInput
	// The average bandwidth in bits per second if traffic shaping is enabled.
	ShapingAverageBandwidth pulumi.IntPtrInput
	// The maximum burst size allowed in bytes if traffic shaping is enabled.
	ShapingBurstSize pulumi.IntPtrInput
	// Enable traffic shaping on this virtual switch or port group.
	ShapingEnabled pulumi.BoolPtrInput
	// The peak bandwidth during bursts in bits per second if traffic shaping is enabled.
	ShapingPeakBandwidth pulumi.IntPtrInput
	// List of standby network adapters used for failover.
	StandbyNics pulumi.StringArrayInput
	// The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, or
	// failover_explicit.
	TeamingPolicy pulumi.StringPtrInput
	// The name of the virtual switch to bind
	// this port group to. Forces a new resource if changed.
	VirtualSwitchName pulumi.StringPtrInput
	// The VLAN ID/trunk mode for this port group.  An ID of
	// `0` denotes no tagging, an ID of `1`-`4094` tags with the specific ID, and an
	// ID of `4095` enables trunk mode, allowing the guest to manage its own
	// tagging. Default: `0`.
	VlanId pulumi.IntPtrInput
}

func (HostPortGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*hostPortGroupState)(nil)).Elem()
}

type hostPortGroupArgs struct {
	// List of active network adapters used for load balancing.
	ActiveNics []string `pulumi:"activeNics"`
	// Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than
	// that of its own.
	AllowForgedTransmits *bool `pulumi:"allowForgedTransmits"`
	// Controls whether or not the Media Access Control (MAC) address can be changed.
	AllowMacChanges *bool `pulumi:"allowMacChanges"`
	// Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port.
	AllowPromiscuous *bool `pulumi:"allowPromiscuous"`
	// Enable beacon probing. Requires that the vSwitch has been configured to use a beacon. If disabled, link status is used
	// only.
	CheckBeacon *bool `pulumi:"checkBeacon"`
	// If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.
	Failback *bool `pulumi:"failback"`
	// The [managed object ID][docs-about-morefs] of
	// the host to set the port group up on. Forces a new resource if changed.
	HostSystemId string `pulumi:"hostSystemId"`
	// The name of the port group.  Forces a new resource if
	// changed.
	Name *string `pulumi:"name"`
	// If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.
	NotifySwitches *bool `pulumi:"notifySwitches"`
	// The average bandwidth in bits per second if traffic shaping is enabled.
	ShapingAverageBandwidth *int `pulumi:"shapingAverageBandwidth"`
	// The maximum burst size allowed in bytes if traffic shaping is enabled.
	ShapingBurstSize *int `pulumi:"shapingBurstSize"`
	// Enable traffic shaping on this virtual switch or port group.
	ShapingEnabled *bool `pulumi:"shapingEnabled"`
	// The peak bandwidth during bursts in bits per second if traffic shaping is enabled.
	ShapingPeakBandwidth *int `pulumi:"shapingPeakBandwidth"`
	// List of standby network adapters used for failover.
	StandbyNics []string `pulumi:"standbyNics"`
	// The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, or
	// failover_explicit.
	TeamingPolicy *string `pulumi:"teamingPolicy"`
	// The name of the virtual switch to bind
	// this port group to. Forces a new resource if changed.
	VirtualSwitchName string `pulumi:"virtualSwitchName"`
	// The VLAN ID/trunk mode for this port group.  An ID of
	// `0` denotes no tagging, an ID of `1`-`4094` tags with the specific ID, and an
	// ID of `4095` enables trunk mode, allowing the guest to manage its own
	// tagging. Default: `0`.
	VlanId *int `pulumi:"vlanId"`
}

// The set of arguments for constructing a HostPortGroup resource.
type HostPortGroupArgs struct {
	// List of active network adapters used for load balancing.
	ActiveNics pulumi.StringArrayInput
	// Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address than
	// that of its own.
	AllowForgedTransmits pulumi.BoolPtrInput
	// Controls whether or not the Media Access Control (MAC) address can be changed.
	AllowMacChanges pulumi.BoolPtrInput
	// Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port.
	AllowPromiscuous pulumi.BoolPtrInput
	// Enable beacon probing. Requires that the vSwitch has been configured to use a beacon. If disabled, link status is used
	// only.
	CheckBeacon pulumi.BoolPtrInput
	// If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.
	Failback pulumi.BoolPtrInput
	// The [managed object ID][docs-about-morefs] of
	// the host to set the port group up on. Forces a new resource if changed.
	HostSystemId pulumi.StringInput
	// The name of the port group.  Forces a new resource if
	// changed.
	Name pulumi.StringPtrInput
	// If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.
	NotifySwitches pulumi.BoolPtrInput
	// The average bandwidth in bits per second if traffic shaping is enabled.
	ShapingAverageBandwidth pulumi.IntPtrInput
	// The maximum burst size allowed in bytes if traffic shaping is enabled.
	ShapingBurstSize pulumi.IntPtrInput
	// Enable traffic shaping on this virtual switch or port group.
	ShapingEnabled pulumi.BoolPtrInput
	// The peak bandwidth during bursts in bits per second if traffic shaping is enabled.
	ShapingPeakBandwidth pulumi.IntPtrInput
	// List of standby network adapters used for failover.
	StandbyNics pulumi.StringArrayInput
	// The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, or
	// failover_explicit.
	TeamingPolicy pulumi.StringPtrInput
	// The name of the virtual switch to bind
	// this port group to. Forces a new resource if changed.
	VirtualSwitchName pulumi.StringInput
	// The VLAN ID/trunk mode for this port group.  An ID of
	// `0` denotes no tagging, an ID of `1`-`4094` tags with the specific ID, and an
	// ID of `4095` enables trunk mode, allowing the guest to manage its own
	// tagging. Default: `0`.
	VlanId pulumi.IntPtrInput
}

func (HostPortGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*hostPortGroupArgs)(nil)).Elem()
}

