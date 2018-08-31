"use strict";
// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***
Object.defineProperty(exports, "__esModule", { value: true });
const pulumi = require("@pulumi/pulumi");
/**
 * The `vsphere_resource_pool` resource can be used to create and manage
 * resource pools in standalone hosts or on compute clusters.
 *
 * For more information on vSphere resource pools, see [this
 * page][ref-vsphere-resource_pools].
 *
 * [ref-vsphere-resource_pools]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-60077B40-66FF-4625-934A-641703ED7601.html
 */
class ResourcePool extends pulumi.CustomResource {
    /**
     * Get an existing ResourcePool resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    static get(name, id, state) {
        return new ResourcePool(name, state, { id });
    }
    constructor(name, argsOrState, opts) {
        let inputs = {};
        if (opts && opts.id) {
            const state = argsOrState;
            inputs["cpuExpandable"] = state ? state.cpuExpandable : undefined;
            inputs["cpuLimit"] = state ? state.cpuLimit : undefined;
            inputs["cpuReservation"] = state ? state.cpuReservation : undefined;
            inputs["cpuShareLevel"] = state ? state.cpuShareLevel : undefined;
            inputs["cpuShares"] = state ? state.cpuShares : undefined;
            inputs["customAttributes"] = state ? state.customAttributes : undefined;
            inputs["memoryExpandable"] = state ? state.memoryExpandable : undefined;
            inputs["memoryLimit"] = state ? state.memoryLimit : undefined;
            inputs["memoryReservation"] = state ? state.memoryReservation : undefined;
            inputs["memoryShareLevel"] = state ? state.memoryShareLevel : undefined;
            inputs["memoryShares"] = state ? state.memoryShares : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["parentResourcePoolId"] = state ? state.parentResourcePoolId : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        }
        else {
            const args = argsOrState;
            if (!args || args.parentResourcePoolId === undefined) {
                throw new Error("Missing required property 'parentResourcePoolId'");
            }
            inputs["cpuExpandable"] = args ? args.cpuExpandable : undefined;
            inputs["cpuLimit"] = args ? args.cpuLimit : undefined;
            inputs["cpuReservation"] = args ? args.cpuReservation : undefined;
            inputs["cpuShareLevel"] = args ? args.cpuShareLevel : undefined;
            inputs["cpuShares"] = args ? args.cpuShares : undefined;
            inputs["customAttributes"] = args ? args.customAttributes : undefined;
            inputs["memoryExpandable"] = args ? args.memoryExpandable : undefined;
            inputs["memoryLimit"] = args ? args.memoryLimit : undefined;
            inputs["memoryReservation"] = args ? args.memoryReservation : undefined;
            inputs["memoryShareLevel"] = args ? args.memoryShareLevel : undefined;
            inputs["memoryShares"] = args ? args.memoryShares : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["parentResourcePoolId"] = args ? args.parentResourcePoolId : undefined;
            inputs["tags"] = args ? args.tags : undefined;
        }
        super("vsphere:index/resourcePool:ResourcePool", name, inputs, opts);
    }
}
exports.ResourcePool = ResourcePool;
//# sourceMappingURL=resourcePool.js.map