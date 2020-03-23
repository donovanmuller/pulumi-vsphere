// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package vsphere

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// The `.Folder` data source can be used to get the general attributes of a
// vSphere inventory folder. Paths are absolute and include must include the
// datacenter.  
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/d/folder.html.markdown.
func LookupFolder(ctx *pulumi.Context, args *LookupFolderArgs, opts ...pulumi.InvokeOption) (*LookupFolderResult, error) {
	var rv LookupFolderResult
	err := ctx.Invoke("vsphere:index/getFolder:getFolder", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getFolder.
type LookupFolderArgs struct {
	Path string `pulumi:"path"`
}


// A collection of values returned by getFolder.
type LookupFolderResult struct {
	// id is the provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	Path string `pulumi:"path"`
}

