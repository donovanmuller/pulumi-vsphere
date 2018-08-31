import * as pulumi from "@pulumi/pulumi";
/**
 * The `vsphere_tag` resource can be used to create and manage tags, which allow
 * you to attach metadata to objects in the vSphere inventory to make these
 * objects more sortable and searchable.
 *
 * For more information about tags, click [here][ext-tags-general].
 *
 * [ext-tags-general]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vcenterhost.doc/GUID-E8E854DD-AA97-4E0C-8419-CE84F93C4058.html
 *
 * ~> **NOTE:** Tagging support is unsupported on direct ESXi connections and
 * requires vCenter 6.0 or higher.
 */
export declare class Tag extends pulumi.CustomResource {
    /**
     * Get an existing Tag resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TagState): Tag;
    /**
     * The unique identifier of the parent category in
     * which this tag will be created. Forces a new resource if changed.
     */
    readonly categoryId: pulumi.Output<string>;
    /**
     * A description for the tag.
     */
    readonly description: pulumi.Output<string | undefined>;
    /**
     * The display name of the tag. The name must be unique
     * within its category.
     */
    readonly name: pulumi.Output<string>;
    /**
     * Create a Tag resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TagArgs, opts?: pulumi.CustomResourceOptions);
}
/**
 * Input properties used for looking up and filtering Tag resources.
 */
export interface TagState {
    /**
     * The unique identifier of the parent category in
     * which this tag will be created. Forces a new resource if changed.
     */
    readonly categoryId?: pulumi.Input<string>;
    /**
     * A description for the tag.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The display name of the tag. The name must be unique
     * within its category.
     */
    readonly name?: pulumi.Input<string>;
}
/**
 * The set of arguments for constructing a Tag resource.
 */
export interface TagArgs {
    /**
     * The unique identifier of the parent category in
     * which this tag will be created. Forces a new resource if changed.
     */
    readonly categoryId: pulumi.Input<string>;
    /**
     * A description for the tag.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The display name of the tag. The name must be unique
     * within its category.
     */
    readonly name?: pulumi.Input<string>;
}
