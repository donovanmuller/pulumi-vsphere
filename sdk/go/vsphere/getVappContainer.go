// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package vsphere

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// The `.VappContainer` data source can be used to discover the ID of a
// vApp container in vSphere. This is useful to fetch the ID of a vApp container
// that you want to use to create virtual machines in using the
// [`.VirtualMachine`][docs-virtual-machine-resource] resource.
//
// [docs-virtual-machine-resource]: /docs/providers/vsphere/r/virtual_machine.html
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/d/vapp_container.html.markdown.
func LookupVappContainer(ctx *pulumi.Context, args *LookupVappContainerArgs, opts ...pulumi.InvokeOption) (*LookupVappContainerResult, error) {
	var rv LookupVappContainerResult
	err := ctx.Invoke("vsphere:index/getVappContainer:getVappContainer", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getVappContainer.
type LookupVappContainerArgs struct {
	// The [managed object reference
	// ID][docs-about-morefs] of the datacenter the vApp container is located in.
	DatacenterId string `pulumi:"datacenterId"`
	// The name of the vApp container. This can be a name or
	// path.
	Name string `pulumi:"name"`
}

// A collection of values returned by getVappContainer.
type LookupVappContainerResult struct {
	DatacenterId string `pulumi:"datacenterId"`
	// id is the provider-assigned unique ID for this managed resource.
	Id   string `pulumi:"id"`
	Name string `pulumi:"name"`
}
