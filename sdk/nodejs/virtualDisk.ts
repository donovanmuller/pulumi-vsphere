// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The `vsphere_virtual_disk` resource can be used to create virtual disks outside
 * of any given [`vsphere_virtual_machine`][docs-vsphere-virtual-machine]
 * resource. These disks can be attached to a virtual machine by creating a disk
 * block with the [`attach`][docs-vsphere-virtual-machine-disk-attach] parameter.
 * 
 * [docs-vsphere-virtual-machine]: /docs/providers/vsphere/r/virtual_machine.html
 * [docs-vsphere-virtual-machine-disk-attach]: /docs/providers/vsphere/r/virtual_machine.html#attach
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as vsphere from "@pulumi/vsphere";
 * 
 * const myDisk = new vsphere.VirtualDisk("myDisk", {
 *     datacenter: "Datacenter",
 *     datastore: "local",
 *     size: 2,
 *     type: "thin",
 *     vmdkPath: "myDisk.vmdk",
 * });
 * ```
 */
export class VirtualDisk extends pulumi.CustomResource {
    /**
     * Get an existing VirtualDisk resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VirtualDiskState, opts?: pulumi.CustomResourceOptions): VirtualDisk {
        return new VirtualDisk(name, <any>state, { ...opts, id: id });
    }

    /**
     * The adapter type for this virtual disk. Can be
     * one of `ide`, `lsiLogic`, or `busLogic`.  Default: `lsiLogic`.
     */
    public readonly adapterType: pulumi.Output<string | undefined>;
    /**
     * Tells the resource to create any
     * directories that are a part of the `vmdk_path` parameter if they are missing.
     * Default: `false`.
     */
    public readonly createDirectories: pulumi.Output<boolean | undefined>;
    /**
     * The name of the datacenter in which to create the
     * disk. Can be omitted when when ESXi or if there is only one datacenter in
     * your infrastructure.
     */
    public readonly datacenter: pulumi.Output<string | undefined>;
    /**
     * The name of the datastore in which to create the
     * disk.
     */
    public readonly datastore: pulumi.Output<string>;
    /**
     * Size of the disk (in GB).
     */
    public readonly size: pulumi.Output<number>;
    /**
     * The type of disk to create. Can be one of
     * `eagerZeroedThick`, `lazy`, or `thin`. Default: `eagerZeroedThick`. For
     * information on what each kind of disk provisioning policy means, click
     * [here][docs-vmware-vm-disk-provisioning].
     */
    public readonly type: pulumi.Output<string | undefined>;
    /**
     * The path, including filename, of the virtual disk to
     * be created.  This needs to end in `.vmdk`.
     */
    public readonly vmdkPath: pulumi.Output<string>;

    /**
     * Create a VirtualDisk resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VirtualDiskArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VirtualDiskArgs | VirtualDiskState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: VirtualDiskState = argsOrState as VirtualDiskState | undefined;
            inputs["adapterType"] = state ? state.adapterType : undefined;
            inputs["createDirectories"] = state ? state.createDirectories : undefined;
            inputs["datacenter"] = state ? state.datacenter : undefined;
            inputs["datastore"] = state ? state.datastore : undefined;
            inputs["size"] = state ? state.size : undefined;
            inputs["type"] = state ? state.type : undefined;
            inputs["vmdkPath"] = state ? state.vmdkPath : undefined;
        } else {
            const args = argsOrState as VirtualDiskArgs | undefined;
            if (!args || args.datastore === undefined) {
                throw new Error("Missing required property 'datastore'");
            }
            if (!args || args.size === undefined) {
                throw new Error("Missing required property 'size'");
            }
            if (!args || args.vmdkPath === undefined) {
                throw new Error("Missing required property 'vmdkPath'");
            }
            inputs["adapterType"] = args ? args.adapterType : undefined;
            inputs["createDirectories"] = args ? args.createDirectories : undefined;
            inputs["datacenter"] = args ? args.datacenter : undefined;
            inputs["datastore"] = args ? args.datastore : undefined;
            inputs["size"] = args ? args.size : undefined;
            inputs["type"] = args ? args.type : undefined;
            inputs["vmdkPath"] = args ? args.vmdkPath : undefined;
        }
        super("vsphere:index/virtualDisk:VirtualDisk", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering VirtualDisk resources.
 */
export interface VirtualDiskState {
    /**
     * The adapter type for this virtual disk. Can be
     * one of `ide`, `lsiLogic`, or `busLogic`.  Default: `lsiLogic`.
     */
    readonly adapterType?: pulumi.Input<string>;
    /**
     * Tells the resource to create any
     * directories that are a part of the `vmdk_path` parameter if they are missing.
     * Default: `false`.
     */
    readonly createDirectories?: pulumi.Input<boolean>;
    /**
     * The name of the datacenter in which to create the
     * disk. Can be omitted when when ESXi or if there is only one datacenter in
     * your infrastructure.
     */
    readonly datacenter?: pulumi.Input<string>;
    /**
     * The name of the datastore in which to create the
     * disk.
     */
    readonly datastore?: pulumi.Input<string>;
    /**
     * Size of the disk (in GB).
     */
    readonly size?: pulumi.Input<number>;
    /**
     * The type of disk to create. Can be one of
     * `eagerZeroedThick`, `lazy`, or `thin`. Default: `eagerZeroedThick`. For
     * information on what each kind of disk provisioning policy means, click
     * [here][docs-vmware-vm-disk-provisioning].
     */
    readonly type?: pulumi.Input<string>;
    /**
     * The path, including filename, of the virtual disk to
     * be created.  This needs to end in `.vmdk`.
     */
    readonly vmdkPath?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a VirtualDisk resource.
 */
export interface VirtualDiskArgs {
    /**
     * The adapter type for this virtual disk. Can be
     * one of `ide`, `lsiLogic`, or `busLogic`.  Default: `lsiLogic`.
     */
    readonly adapterType?: pulumi.Input<string>;
    /**
     * Tells the resource to create any
     * directories that are a part of the `vmdk_path` parameter if they are missing.
     * Default: `false`.
     */
    readonly createDirectories?: pulumi.Input<boolean>;
    /**
     * The name of the datacenter in which to create the
     * disk. Can be omitted when when ESXi or if there is only one datacenter in
     * your infrastructure.
     */
    readonly datacenter?: pulumi.Input<string>;
    /**
     * The name of the datastore in which to create the
     * disk.
     */
    readonly datastore: pulumi.Input<string>;
    /**
     * Size of the disk (in GB).
     */
    readonly size: pulumi.Input<number>;
    /**
     * The type of disk to create. Can be one of
     * `eagerZeroedThick`, `lazy`, or `thin`. Default: `eagerZeroedThick`. For
     * information on what each kind of disk provisioning policy means, click
     * [here][docs-vmware-vm-disk-provisioning].
     */
    readonly type?: pulumi.Input<string>;
    /**
     * The path, including filename, of the virtual disk to
     * be created.  This needs to end in `.vmdk`.
     */
    readonly vmdkPath: pulumi.Input<string>;
}
