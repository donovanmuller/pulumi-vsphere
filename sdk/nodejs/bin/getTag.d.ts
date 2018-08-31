import * as pulumi from "@pulumi/pulumi";
/**
 * The `vsphere_tag` data source can be used to reference tags that are not
 * managed by Terraform. Its attributes are exactly the same as the [`vsphere_tag`
 * resource][resource-tag], and, like importing, the data source takes a name and
 * category to search on. The `id` and other attributes are then populated with
 * the data found by the search.
 *
 * [resource-tag]: /docs/providers/vsphere/r/tag.html
 *
 * ~> **NOTE:** Tagging support is unsupported on direct ESXi connections and
 * requires vCenter 6.0 or higher.
 */
export declare function getTag(args: GetTagArgs, opts?: pulumi.InvokeOptions): Promise<GetTagResult>;
/**
 * A collection of arguments for invoking getTag.
 */
export interface GetTagArgs {
    /**
     * The ID of the tag category the tag is located in.
     */
    readonly categoryId: string;
    /**
     * The name of the tag.
     */
    readonly name: string;
}
/**
 * A collection of values returned by getTag.
 */
export interface GetTagResult {
    readonly description: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
