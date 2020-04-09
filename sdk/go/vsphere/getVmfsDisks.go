// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package vsphere

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// The `.getVmfsDisks` data source can be used to discover the storage
// devices available on an ESXi host. This data source can be combined with the
// [`.VmfsDatastore`][data-source-vmfs-datastore] resource to create VMFS
// datastores based off a set of discovered disks.
//
// [data-source-vmfs-datastore]: /docs/providers/vsphere/r/vmfs_datastore.html
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/d/vmfs_disks.html.markdown.
func GetVmfsDisks(ctx *pulumi.Context, args *GetVmfsDisksArgs, opts ...pulumi.InvokeOption) (*GetVmfsDisksResult, error) {
	var rv GetVmfsDisksResult
	err := ctx.Invoke("vsphere:index/getVmfsDisks:getVmfsDisks", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getVmfsDisks.
type GetVmfsDisksArgs struct {
	// A regular expression to filter the disks against. Only
	// disks with canonical names that match will be included.
	Filter *string `pulumi:"filter"`
	// The [managed object ID][docs-about-morefs] of
	// the host to look for disks on.
	HostSystemId string `pulumi:"hostSystemId"`
	// Whether or not to rescan storage adapters before
	// searching for disks. This may lengthen the time it takes to perform the
	// search. Default: `false`.
	Rescan *bool `pulumi:"rescan"`
}

// A collection of values returned by getVmfsDisks.
type GetVmfsDisksResult struct {
	// A lexicographically sorted list of devices discovered by the
	// operation, matching the supplied `filter`, if provided.
	Disks        []string `pulumi:"disks"`
	Filter       *string  `pulumi:"filter"`
	HostSystemId string   `pulumi:"hostSystemId"`
	// id is the provider-assigned unique ID for this managed resource.
	Id     string `pulumi:"id"`
	Rescan *bool  `pulumi:"rescan"`
}
