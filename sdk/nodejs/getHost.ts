// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * The `vsphere..Host` data source can be used to discover the ID of a vSphere
 * host. This can then be used with resources or data sources that require a host
 * managed object reference ID.
 *
 * ## Example Usage
 *
 *
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as vsphere from "@pulumi/vsphere";
 *
 * const datacenter = pulumi.output(vsphere.getDatacenter({
 *     name: "dc1",
 * }, { async: true }));
 * const host = datacenter.apply(datacenter => vsphere.getHost({
 *     datacenterId: datacenter.id,
 *     name: "esxi1",
 * }, { async: true }));
 * ```
 */
export function getHost(args: GetHostArgs, opts?: pulumi.InvokeOptions): Promise<GetHostResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("vsphere:index/getHost:getHost", {
        "datacenterId": args.datacenterId,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getHost.
 */
export interface GetHostArgs {
    /**
     * The managed object reference
     * ID of a datacenter.
     */
    readonly datacenterId: string;
    /**
     * The name of the host. This can be a name or path. Can be
     * omitted if there is only one host in your inventory.
     */
    readonly name?: string;
}

/**
 * A collection of values returned by getHost.
 */
export interface GetHostResult {
    readonly datacenterId: string;
    readonly name?: string;
    /**
     * The managed object ID of the host's
     * root resource pool.
     */
    readonly resourcePoolId: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
