// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package vsphere

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// The `vsphere_tag` data source can be used to reference tags that are not
// managed by Terraform. Its attributes are exactly the same as the [`vsphere_tag`
// resource][resource-tag], and, like importing, the data source takes a name and
// category to search on. The `id` and other attributes are then populated with
// the data found by the search.
// 
// [resource-tag]: /docs/providers/vsphere/r/tag.html
// 
// ~> **NOTE:** Tagging support is unsupported on direct ESXi connections and
// requires vCenter 6.0 or higher.
func LookupTag(ctx *pulumi.Context, args *GetTagArgs) (*GetTagResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["categoryId"] = args.CategoryId
		inputs["name"] = args.Name
	}
	outputs, err := ctx.Invoke("vsphere:index/getTag:getTag", inputs)
	if err != nil {
		return nil, err
	}
	return &GetTagResult{
		Description: outputs["description"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getTag.
type GetTagArgs struct {
	// The ID of the tag category the tag is located in.
	CategoryId interface{}
	// The name of the tag.
	Name interface{}
}

// A collection of values returned by getTag.
type GetTagResult struct {
	Description interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
