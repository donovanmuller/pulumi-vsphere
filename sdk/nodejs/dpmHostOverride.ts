// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The `vsphere_dpm_host_override` resource can be used to add a DPM override to a
 * cluster for a particular host. This allows you to control the power management
 * settings for individual hosts in the cluster while leaving any unspecified ones
 * at the default power management settings.
 * 
 * For more information on DPM within vSphere clusters, see [this
 * page][ref-vsphere-cluster-dpm].
 * 
 * [ref-vsphere-cluster-dpm]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-5E5E349A-4644-4C9C-B434-1C0243EBDC80.html
 * 
 * > **NOTE:** This resource requires vCenter and is not available on direct ESXi
 * connections.
 * 
 * > **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.
 * 
 * ## Example Usage
 * 
 * The following example creates a compute cluster comprised of three hosts,
 * making use of the
 * [`vsphere_compute_cluster`][tf-vsphere-compute-cluster-resource] resource. DPM
 * will be disabled in the cluster as it is the default setting, but we override
 * the setting of the first host referenced by the
 * [`vsphere_host`][tf-vsphere-host-data-source] data source (`esxi1`) by using
 * the `vsphere_dpm_host_override` resource so it will be powered off when the
 * cluster does not need it to service virtual machines.
 * 
 * [tf-vsphere-compute-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
 * [tf-vsphere-host-data-source]: /docs/providers/vsphere/d/host.html
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as vsphere from "@pulumi/vsphere";
 * 
 * const config = new pulumi.Config();
 * const datacenter = config.get("datacenter") || "dc1";
 * const hosts = config.get("hosts") || [
 *     "esxi1",
 *     "esxi2",
 *     "esxi3",
 * ];
 * 
 * const dc = pulumi.output(vsphere.getDatacenter({
 *     name: datacenter,
 * }));
 * const hostsHost: Output<vsphere.GETHOSTResult>[] = [];
 * for (let i = 0; i < hosts.length; i++) {
 *     hostsHost.push(vsphere.getHost);
 * %!(EXTRA string=dc.apply(dc => vsphere.getHost({
 *         datacenterId: dc.id,
 *         name: hosts[i],
 *     })))}
 * const computeCluster = new vsphere.ComputeCluster("compute_cluster", {
 *     datacenterId: dc.id,
 *     drsAutomationLevel: "fullyAutomated",
 *     drsEnabled: true,
 *     hostSystemIds: hostsHost.map(v => v.id),
 * });
 * const dpmHostOverride = new vsphere.DpmHostOverride("dpm_host_override", {
 *     computeClusterId: computeCluster.id,
 *     dpmAutomationLevel: "automated",
 *     dpmEnabled: true,
 *     hostSystemId: hostsHost[0].id,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/r/dpm_host_override.html.markdown.
 */
export class DpmHostOverride extends pulumi.CustomResource {
    /**
     * Get an existing DpmHostOverride resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DpmHostOverrideState, opts?: pulumi.CustomResourceOptions): DpmHostOverride {
        return new DpmHostOverride(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'vsphere:index/dpmHostOverride:DpmHostOverride';

    /**
     * Returns true if the given object is an instance of DpmHostOverride.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DpmHostOverride {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DpmHostOverride.__pulumiType;
    }

    /**
     * The [managed object reference
     * ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
     * resource if changed.
     */
    public readonly computeClusterId!: pulumi.Output<string>;
    /**
     * The automation level for host power
     * operations on this host. Can be one of `manual` or `automated`. Default:
     * `manual`.
     */
    public readonly dpmAutomationLevel!: pulumi.Output<string | undefined>;
    /**
     * Enable DPM support for this host. Default:
     * `false`.
     */
    public readonly dpmEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * The managed object ID of the host.
     */
    public readonly hostSystemId!: pulumi.Output<string>;

    /**
     * Create a DpmHostOverride resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DpmHostOverrideArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DpmHostOverrideArgs | DpmHostOverrideState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as DpmHostOverrideState | undefined;
            inputs["computeClusterId"] = state ? state.computeClusterId : undefined;
            inputs["dpmAutomationLevel"] = state ? state.dpmAutomationLevel : undefined;
            inputs["dpmEnabled"] = state ? state.dpmEnabled : undefined;
            inputs["hostSystemId"] = state ? state.hostSystemId : undefined;
        } else {
            const args = argsOrState as DpmHostOverrideArgs | undefined;
            if (!args || args.computeClusterId === undefined) {
                throw new Error("Missing required property 'computeClusterId'");
            }
            if (!args || args.hostSystemId === undefined) {
                throw new Error("Missing required property 'hostSystemId'");
            }
            inputs["computeClusterId"] = args ? args.computeClusterId : undefined;
            inputs["dpmAutomationLevel"] = args ? args.dpmAutomationLevel : undefined;
            inputs["dpmEnabled"] = args ? args.dpmEnabled : undefined;
            inputs["hostSystemId"] = args ? args.hostSystemId : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(DpmHostOverride.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DpmHostOverride resources.
 */
export interface DpmHostOverrideState {
    /**
     * The [managed object reference
     * ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
     * resource if changed.
     */
    readonly computeClusterId?: pulumi.Input<string>;
    /**
     * The automation level for host power
     * operations on this host. Can be one of `manual` or `automated`. Default:
     * `manual`.
     */
    readonly dpmAutomationLevel?: pulumi.Input<string>;
    /**
     * Enable DPM support for this host. Default:
     * `false`.
     */
    readonly dpmEnabled?: pulumi.Input<boolean>;
    /**
     * The managed object ID of the host.
     */
    readonly hostSystemId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DpmHostOverride resource.
 */
export interface DpmHostOverrideArgs {
    /**
     * The [managed object reference
     * ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
     * resource if changed.
     */
    readonly computeClusterId: pulumi.Input<string>;
    /**
     * The automation level for host power
     * operations on this host. Can be one of `manual` or `automated`. Default:
     * `manual`.
     */
    readonly dpmAutomationLevel?: pulumi.Input<string>;
    /**
     * Enable DPM support for this host. Default:
     * `false`.
     */
    readonly dpmEnabled?: pulumi.Input<boolean>;
    /**
     * The managed object ID of the host.
     */
    readonly hostSystemId: pulumi.Input<string>;
}
