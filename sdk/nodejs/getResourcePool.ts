// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The `vsphere_resource_pool` data source can be used to discover the ID of a
 * resource pool in vSphere. This is useful to fetch the ID of a resource pool
 * that you want to use to create virtual machines in using the
 * [`vsphere_virtual_machine`][docs-virtual-machine-resource] resource. 
 * 
 * [docs-virtual-machine-resource]: /docs/providers/vsphere/r/virtual_machine.html
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as vsphere from "@pulumi/vsphere";
 * 
 * const datacenter = pulumi.output(vsphere.getDatacenter({
 *     name: "dc1",
 * }));
 * const pool = datacenter.apply(datacenter => vsphere.getResourcePool({
 *     datacenterId: datacenter.id,
 *     name: "resource-pool-1",
 * }));
 * ```
 * 
 * ### Specifying the root resource pool for a standalone host
 * 
 * > **NOTE:** Fetching the root resource pool for a cluster can now be done
 * directly via the [`vsphere_compute_cluster`][docs-compute-cluster-data-source]
 * data source.
 * 
 * [docs-compute-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html
 * 
 * All compute resources in vSphere (clusters, standalone hosts, and standalone
 * ESXi) have a resource pool, even if one has not been explicitly created. This
 * resource pool is referred to as the _root resource pool_ and can be looked up
 * by specifying the path as per the example below:
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as vsphere from "@pulumi/vsphere";
 * 
 * const pool = vsphere_datacenter_dc.id.apply(id => vsphere.getResourcePool({
 *     datacenterId: id,
 *     name: "esxi1/Resources",
 * }));
 * ```
 * 
 * For more information on the root resource pool, see [Managing Resource
 * Pools][vmware-docs-resource-pools] in the vSphere documentation.
 * 
 * [vmware-docs-resource-pools]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-60077B40-66FF-4625-934A-641703ED7601.html
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/d/resource_pool.html.markdown.
 */
export function getResourcePool(args?: GetResourcePoolArgs, opts?: pulumi.InvokeOptions): Promise<GetResourcePoolResult> & GetResourcePoolResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetResourcePoolResult> = pulumi.runtime.invoke("vsphere:index/getResourcePool:getResourcePool", {
        "datacenterId": args.datacenterId,
        "name": args.name,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getResourcePool.
 */
export interface GetResourcePoolArgs {
    /**
     * The [managed object reference
     * ID][docs-about-morefs] of the datacenter the resource pool is located in.
     * This can be omitted if the search path used in `name` is an absolute path.
     * For default datacenters, use the id attribute from an empty
     * `vsphere_datacenter` data source.
     */
    readonly datacenterId?: string;
    /**
     * The name of the resource pool. This can be a name or
     * path. This is required when using vCenter.
     */
    readonly name?: string;
}

/**
 * A collection of values returned by getResourcePool.
 */
export interface GetResourcePoolResult {
    readonly datacenterId?: string;
    readonly name?: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
