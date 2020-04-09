// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package vsphere

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// The `.Host` data source can be used to discover the ID of a vSphere
// host. This can then be used with resources or data sources that require a host
// managed object reference ID.
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/d/host.html.markdown.
func LookupHost(ctx *pulumi.Context, args *LookupHostArgs, opts ...pulumi.InvokeOption) (*LookupHostResult, error) {
	var rv LookupHostResult
	err := ctx.Invoke("vsphere:index/getHost:getHost", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getHost.
type LookupHostArgs struct {
	// The [managed object reference
	// ID][docs-about-morefs] of a datacenter.
	DatacenterId string `pulumi:"datacenterId"`
	// The name of the host. This can be a name or path. Can be
	// omitted if there is only one host in your inventory.
	Name *string `pulumi:"name"`
}

// A collection of values returned by getHost.
type LookupHostResult struct {
	DatacenterId string `pulumi:"datacenterId"`
	// id is the provider-assigned unique ID for this managed resource.
	Id   string  `pulumi:"id"`
	Name *string `pulumi:"name"`
	// The [managed object ID][docs-about-morefs] of the host's
	// root resource pool.
	ResourcePoolId string `pulumi:"resourcePoolId"`
}
