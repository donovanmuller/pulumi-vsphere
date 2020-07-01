// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package vsphere

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// The `Host` data source can be used to discover the ID of a vSphere
// host. This can then be used with resources or data sources that require a host
// managed object reference ID.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		opt0 := "dc1"
// 		datacenter, err := vsphere.LookupDatacenter(ctx, &vsphere.LookupDatacenterArgs{
// 			Name: &opt0,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		opt1 := "esxi1"
// 		_, err = vsphere.LookupHost(ctx, &vsphere.LookupHostArgs{
// 			DatacenterId: datacenter.Id,
// 			Name:         &opt1,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
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
	// The managed object reference
	// ID of a datacenter.
	DatacenterId string `pulumi:"datacenterId"`
	// The name of the host. This can be a name or path. Can be
	// omitted if there is only one host in your inventory.
	Name *string `pulumi:"name"`
}

// A collection of values returned by getHost.
type LookupHostResult struct {
	DatacenterId string `pulumi:"datacenterId"`
	// The provider-assigned unique ID for this managed resource.
	Id   string  `pulumi:"id"`
	Name *string `pulumi:"name"`
	// The managed object ID of the host's
	// root resource pool.
	ResourcePoolId string `pulumi:"resourcePoolId"`
}
