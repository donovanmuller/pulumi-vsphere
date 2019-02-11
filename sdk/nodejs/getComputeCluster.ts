// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The `vsphere_compute_cluster` data source can be used to discover the ID of a
 * cluster in vSphere. This is useful to fetch the ID of a cluster that you want
 * to use for virtual machine placement via the
 * [`vsphere_virtual_machine`][docs-virtual-machine-resource] resource, allowing
 * you to specify the cluster's root resource pool directly versus using the alias
 * available through the [`vsphere_resource_pool`][docs-resource-pool-data-source]
 * data source.
 * 
 * [docs-virtual-machine-resource]: /docs/providers/vsphere/r/virtual_machine.html
 * [docs-resource-pool-data-source]: /docs/providers/vsphere/d/resource_pool.html
 * 
 * > You may also wish to see the
 * [`vsphere_compute_cluster`][docs-compute-cluster-resource] resource for further
 * details about clusters or how to work with them in Terraform.
 * 
 * [docs-compute-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as vsphere from "@pulumi/vsphere";
 * 
 * const computeCluster = pulumi.output(vsphere.getComputeCluster({
 *     datacenterId: vsphere_datacenter_dc.id.apply(id => id),
 *     name: "compute-cluster1",
 * }));
 * const datacenter = pulumi.output(vsphere.getDatacenter({
 *     name: "dc1",
 * }));
 * ```
 */
export function getComputeCluster(args: GetComputeClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetComputeClusterResult> {
    return pulumi.runtime.invoke("vsphere:index/getComputeCluster:getComputeCluster", {
        "datacenterId": args.datacenterId,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getComputeCluster.
 */
export interface GetComputeClusterArgs {
    /**
     * The [managed object reference
     * ID][docs-about-morefs] of the datacenter the cluster is located in.  This can
     * be omitted if the search path used in `name` is an absolute path.  For
     * default datacenters, use the id attribute from an empty `vsphere_datacenter`
     * data source.
     */
    readonly datacenterId?: string;
    /**
     * The name or absolute path to the cluster.
     */
    readonly name: string;
}

/**
 * A collection of values returned by getComputeCluster.
 */
export interface GetComputeClusterResult {
    readonly resourcePoolId: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
