import * as pulumi from "@pulumi/pulumi";
/**
 * The `vsphere_network` data source can be used to discover the ID of a network
 * in vSphere. This can be any network that can be used as the backing for a
 * network interface for `vsphere_virtual_machine` or any other vSphere resource
 * that requires a network. This includes standard (host-based) port groups, DVS
 * port groups, or opaque networks such as those managed by NSX.
 */
export declare function getNetwork(args: GetNetworkArgs, opts?: pulumi.InvokeOptions): Promise<GetNetworkResult>;
/**
 * A collection of arguments for invoking getNetwork.
 */
export interface GetNetworkArgs {
    /**
     * The [managed object reference
     * ID][docs-about-morefs] of the datacenter the network is located in. This can
     * be omitted if the search path used in `name` is an absolute path. For default
     * datacenters, use the id attribute from an empty `vsphere_datacenter` data
     * source.
     */
    readonly datacenterId?: string;
    /**
     * The name of the network. This can be a name or path.
     */
    readonly name: string;
}
/**
 * A collection of values returned by getNetwork.
 */
export interface GetNetworkResult {
    readonly type: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
