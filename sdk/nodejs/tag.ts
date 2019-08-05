// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/r/tag.html.markdown.
 */
export class Tag extends pulumi.CustomResource {
    /**
     * Get an existing Tag resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TagState, opts?: pulumi.CustomResourceOptions): Tag {
        return new Tag(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'vsphere:index/tag:Tag';

    /**
     * Returns true if the given object is an instance of Tag.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Tag {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Tag.__pulumiType;
    }

    /**
     * The unique identifier of the parent category in
     * which this tag will be created. Forces a new resource if changed.
     */
    public readonly categoryId!: pulumi.Output<string>;
    /**
     * A description for the tag.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The display name of the tag. The name must be unique
     * within its category.
     */
    public readonly name!: pulumi.Output<string>;

    /**
     * Create a Tag resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TagArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TagArgs | TagState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as TagState | undefined;
            inputs["categoryId"] = state ? state.categoryId : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["name"] = state ? state.name : undefined;
        } else {
            const args = argsOrState as TagArgs | undefined;
            if (!args || args.categoryId === undefined) {
                throw new Error("Missing required property 'categoryId'");
            }
            inputs["categoryId"] = args ? args.categoryId : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Tag.__pulumiType, name, inputs, opts);
    }
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
