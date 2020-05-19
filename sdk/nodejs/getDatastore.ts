// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * The `vsphere..getDatastore` data source can be used to discover the ID of a
 * datastore in vSphere. This is useful to fetch the ID of a datastore that you
 * want to use to create virtual machines in using the
 * `vsphere..VirtualMachine` resource. 
 *
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
 * const datastore = datacenter.apply(datacenter => vsphere.getDatastore({
 *     datacenterId: datacenter.id,
 *     name: "datastore1",
 * }, { async: true }));
 * ```
 */
export function getDatastore(args: GetDatastoreArgs, opts?: pulumi.InvokeOptions): Promise<GetDatastoreResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("vsphere:index/getDatastore:getDatastore", {
        "datacenterId": args.datacenterId,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getDatastore.
 */
export interface GetDatastoreArgs {
    /**
     * The managed object reference
     * ID of the datacenter the datastore is located in. This
     * can be omitted if the search path used in `name` is an absolute path. For
     * default datacenters, use the id attribute from an empty `vsphere..Datacenter`
     * data source.
     */
    readonly datacenterId?: string;
    /**
     * The name of the datastore. This can be a name or path.
     */
    readonly name: string;
}

/**
 * A collection of values returned by getDatastore.
 */
export interface GetDatastoreResult {
    readonly datacenterId?: string;
    readonly name: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
