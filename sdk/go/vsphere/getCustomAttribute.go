// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package vsphere

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func LookupCustomAttribute(ctx *pulumi.Context, args *LookupCustomAttributeArgs, opts ...pulumi.InvokeOption) (*LookupCustomAttributeResult, error) {
	var rv LookupCustomAttributeResult
	err := ctx.Invoke("vsphere:index/getCustomAttribute:getCustomAttribute", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getCustomAttribute.
type LookupCustomAttributeArgs struct {
	// The name of the custom attribute.
	Name string `pulumi:"name"`
}

// A collection of values returned by getCustomAttribute.
type LookupCustomAttributeResult struct {
	// id is the provider-assigned unique ID for this managed resource.
	Id                string `pulumi:"id"`
	ManagedObjectType string `pulumi:"managedObjectType"`
	Name              string `pulumi:"name"`
}
