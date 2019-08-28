// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/d/tag_category.html.markdown.
 */
export function getTagCategory(args: GetTagCategoryArgs, opts?: pulumi.InvokeOptions): Promise<GetTagCategoryResult> & GetTagCategoryResult {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetTagCategoryResult> = pulumi.runtime.invoke("vsphere:index/getTagCategory:getTagCategory", {
        "name": args.name,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getTagCategory.
 */
export interface GetTagCategoryArgs {
    /**
     * The name of the tag category.
     */
    readonly name: string;
}

/**
 * A collection of values returned by getTagCategory.
 */
export interface GetTagCategoryResult {
    readonly associableTypes: string[];
    readonly cardinality: string;
    readonly description: string;
    readonly name: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
