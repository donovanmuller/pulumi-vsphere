// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The `vsphere..ComputeClusterVmAffinityRule` resource can be used to manage
 * VM affinity rules in a cluster, either created by the
 * `vsphere..ComputeCluster` resource or looked up
 * by the `vsphere..ComputeCluster` data source.
 *
 * This rule can be used to tell a set to virtual machines to run together on a
 * single host within a cluster. When configured, DRS will make a best effort to
 * ensure that the virtual machines run on the same host, or prevent any operation
 * that would keep that from happening, depending on the value of the
 * `mandatory` flag.
 *
 * > Keep in mind that this rule can only be used to tell VMs to run together on
 * a _non-specific_ host - it can't be used to pin VMs to a host. For that, see
 * the
 * `vsphere..ComputeClusterVmHostRule`
 * resource.
 *
 * > **NOTE:** This resource requires vCenter and is not available on direct ESXi
 * connections.
 *
 * > **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.
 *
 * ## Example Usage
 *
 *
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as vsphere from "@pulumi/vsphere";
 *
 * const dc = pulumi.output(vsphere.getDatacenter({
 *     name: "dc1",
 * }, { async: true }));
 * const datastore = dc.apply(dc => vsphere.getDatastore({
 *     datacenterId: dc.id,
 *     name: "datastore1",
 * }, { async: true }));
 * const cluster = dc.apply(dc => vsphere.getComputeCluster({
 *     datacenterId: dc.id,
 *     name: "cluster1",
 * }, { async: true }));
 * const network = dc.apply(dc => vsphere.getNetwork({
 *     datacenterId: dc.id,
 *     name: "network1",
 * }, { async: true }));
 * const vm: vsphere.VirtualMachine[] = [];
 * for (let i = 0; i < 2; i++) {
 *     vm.push(new vsphere.VirtualMachine(`vm-${i}`, {
 *         datastoreId: datastore.id,
 *         disks: [{
 *             label: "disk0",
 *             size: 20,
 *         }],
 *         guestId: "other3xLinux64Guest",
 *         memory: 2048,
 *         networkInterfaces: [{
 *             networkId: network.id,
 *         }],
 *         numCpus: 2,
 *         resourcePoolId: cluster.resourcePoolId,
 *     }));
 * }
 * const clusterVmAffinityRule = new vsphere.ComputeClusterVmAffinityRule("clusterVmAffinityRule", {
 *     computeClusterId: cluster.id,
 *     virtualMachineIds: vm.map(v => v.id),
 * });
 * ```
 */
export class ComputeClusterVmAffinityRule extends pulumi.CustomResource {
    /**
     * Get an existing ComputeClusterVmAffinityRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ComputeClusterVmAffinityRuleState, opts?: pulumi.CustomResourceOptions): ComputeClusterVmAffinityRule {
        return new ComputeClusterVmAffinityRule(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'vsphere:index/computeClusterVmAffinityRule:ComputeClusterVmAffinityRule';

    /**
     * Returns true if the given object is an instance of ComputeClusterVmAffinityRule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ComputeClusterVmAffinityRule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ComputeClusterVmAffinityRule.__pulumiType;
    }

    /**
     * The managed object reference
     * ID of the cluster to put the group in.  Forces a new
     * resource if changed.
     */
    public readonly computeClusterId!: pulumi.Output<string>;
    /**
     * Enable this rule in the cluster. Default: `true`.
     */
    public readonly enabled!: pulumi.Output<boolean | undefined>;
    /**
     * When this value is `true`, prevents any virtual
     * machine operations that may violate this rule. Default: `false`.
     */
    public readonly mandatory!: pulumi.Output<boolean | undefined>;
    /**
     * The name of the rule. This must be unique in the cluster.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The UUIDs of the virtual machines to run
     * on the same host together.
     */
    public readonly virtualMachineIds!: pulumi.Output<string[]>;

    /**
     * Create a ComputeClusterVmAffinityRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ComputeClusterVmAffinityRuleArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ComputeClusterVmAffinityRuleArgs | ComputeClusterVmAffinityRuleState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ComputeClusterVmAffinityRuleState | undefined;
            inputs["computeClusterId"] = state ? state.computeClusterId : undefined;
            inputs["enabled"] = state ? state.enabled : undefined;
            inputs["mandatory"] = state ? state.mandatory : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["virtualMachineIds"] = state ? state.virtualMachineIds : undefined;
        } else {
            const args = argsOrState as ComputeClusterVmAffinityRuleArgs | undefined;
            if (!args || args.computeClusterId === undefined) {
                throw new Error("Missing required property 'computeClusterId'");
            }
            if (!args || args.virtualMachineIds === undefined) {
                throw new Error("Missing required property 'virtualMachineIds'");
            }
            inputs["computeClusterId"] = args ? args.computeClusterId : undefined;
            inputs["enabled"] = args ? args.enabled : undefined;
            inputs["mandatory"] = args ? args.mandatory : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["virtualMachineIds"] = args ? args.virtualMachineIds : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(ComputeClusterVmAffinityRule.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ComputeClusterVmAffinityRule resources.
 */
export interface ComputeClusterVmAffinityRuleState {
    /**
     * The managed object reference
     * ID of the cluster to put the group in.  Forces a new
     * resource if changed.
     */
    readonly computeClusterId?: pulumi.Input<string>;
    /**
     * Enable this rule in the cluster. Default: `true`.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * When this value is `true`, prevents any virtual
     * machine operations that may violate this rule. Default: `false`.
     */
    readonly mandatory?: pulumi.Input<boolean>;
    /**
     * The name of the rule. This must be unique in the cluster.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The UUIDs of the virtual machines to run
     * on the same host together.
     */
    readonly virtualMachineIds?: pulumi.Input<pulumi.Input<string>[]>;
}

/**
 * The set of arguments for constructing a ComputeClusterVmAffinityRule resource.
 */
export interface ComputeClusterVmAffinityRuleArgs {
    /**
     * The managed object reference
     * ID of the cluster to put the group in.  Forces a new
     * resource if changed.
     */
    readonly computeClusterId: pulumi.Input<string>;
    /**
     * Enable this rule in the cluster. Default: `true`.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * When this value is `true`, prevents any virtual
     * machine operations that may violate this rule. Default: `false`.
     */
    readonly mandatory?: pulumi.Input<boolean>;
    /**
     * The name of the rule. This must be unique in the cluster.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The UUIDs of the virtual machines to run
     * on the same host together.
     */
    readonly virtualMachineIds: pulumi.Input<pulumi.Input<string>[]>;
}
