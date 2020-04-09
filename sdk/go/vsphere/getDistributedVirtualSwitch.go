// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package vsphere

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// The `.DistributedVirtualSwitch` data source can be used to discover
// the ID and uplink data of a of a vSphere distributed virtual switch (DVS). This
// can then be used with resources or data sources that require a DVS, such as the
// [`.DistributedPortGroup`][distributed-port-group] resource, for which
// an example is shown below.
//
// [distributed-port-group]: /docs/providers/vsphere/r/distributed_port_group.html
//
// > **NOTE:** This data source requires vCenter and is not available on direct
// ESXi connections.
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/d/distributed_virtual_switch.html.markdown.
func LookupDistributedVirtualSwitch(ctx *pulumi.Context, args *LookupDistributedVirtualSwitchArgs, opts ...pulumi.InvokeOption) (*LookupDistributedVirtualSwitchResult, error) {
	var rv LookupDistributedVirtualSwitchResult
	err := ctx.Invoke("vsphere:index/getDistributedVirtualSwitch:getDistributedVirtualSwitch", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getDistributedVirtualSwitch.
type LookupDistributedVirtualSwitchArgs struct {
	// The [managed object reference
	// ID][docs-about-morefs] of the datacenter the DVS is located in. This can be
	// omitted if the search path used in `name` is an absolute path. For default
	// datacenters, use the id attribute from an empty `.Datacenter` data
	// source.
	DatacenterId *string `pulumi:"datacenterId"`
	// The name of the distributed virtual switch. This can be a
	// name or path.
	Name string `pulumi:"name"`
}

// A collection of values returned by getDistributedVirtualSwitch.
type LookupDistributedVirtualSwitchResult struct {
	DatacenterId *string `pulumi:"datacenterId"`
	// id is the provider-assigned unique ID for this managed resource.
	Id      string   `pulumi:"id"`
	Name    string   `pulumi:"name"`
	Uplinks []string `pulumi:"uplinks"`
}
