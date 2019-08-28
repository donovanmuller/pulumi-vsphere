// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/d/custom_attribute.html.markdown.
 */
export function getCustomAttribute(args: GetCustomAttributeArgs, opts?: pulumi.InvokeOptions): Promise<GetCustomAttributeResult> & GetCustomAttributeResult {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetCustomAttributeResult> = pulumi.runtime.invoke("vsphere:index/getCustomAttribute:getCustomAttribute", {
        "name": args.name,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getCustomAttribute.
 */
export interface GetCustomAttributeArgs {
    /**
     * The name of the custom attribute.
     */
    readonly name: string;
}

/**
 * A collection of values returned by getCustomAttribute.
 */
export interface GetCustomAttributeResult {
    readonly managedObjectType: string;
    readonly name: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
