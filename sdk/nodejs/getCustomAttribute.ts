// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * The `vsphere.CustomAttribute` data source can be used to reference custom
 * attributes that are not managed by this provider. Its attributes are exactly the
 * same as the `vsphere.CustomAttribute` resource,
 * and, like importing, the data source takes a name to search on. The `id` and
 * other attributes are then populated with the data found by the search.
 *
 * > **NOTE:** Custom attributes are unsupported on direct ESXi connections
 * and require vCenter.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as vsphere from "@pulumi/vsphere";
 *
 * const attribute = pulumi.output(vsphere.getCustomAttribute({
 *     name: "test-attribute",
 * }, { async: true }));
 * ```
 */
export function getCustomAttribute(args: GetCustomAttributeArgs, opts?: pulumi.InvokeOptions): Promise<GetCustomAttributeResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("vsphere:index/getCustomAttribute:getCustomAttribute", {
        "name": args.name,
    }, opts);
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
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly managedObjectType: string;
    readonly name: string;
}
