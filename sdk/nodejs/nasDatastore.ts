// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class NasDatastore extends pulumi.CustomResource {
    /**
     * Get an existing NasDatastore resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NasDatastoreState, opts?: pulumi.CustomResourceOptions): NasDatastore {
        return new NasDatastore(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'vsphere:index/nasDatastore:NasDatastore';

    /**
     * Returns true if the given object is an instance of NasDatastore.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is NasDatastore {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === NasDatastore.__pulumiType;
    }

    /**
     * Access mode for the mount point. Can be one of
     * `readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
     * that the datastore will be read-write depending on the permissions of the
     * actual share. Default: `readWrite`. Forces a new resource if changed.
     */
    public readonly accessMode!: pulumi.Output<string | undefined>;
    /**
     * The connectivity status of the datastore. If this is `false`,
     * some other computed attributes may be out of date.
     */
    public /*out*/ readonly accessible!: pulumi.Output<boolean>;
    /**
     * Maximum capacity of the datastore, in megabytes.
     */
    public /*out*/ readonly capacity!: pulumi.Output<number>;
    /**
     * Map of custom attribute ids to attribute 
     * value strings to set on datasource resource.
     */
    public readonly customAttributes!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * The managed object
     * ID of a datastore cluster to put this datastore in.
     * Conflicts with `folder`.
     */
    public readonly datastoreClusterId!: pulumi.Output<string | undefined>;
    /**
     * The relative path to a folder to put this datastore in.
     * This is a path relative to the datacenter you are deploying the datastore to.
     * Example: for the `dc1` datacenter, and a provided `folder` of `foo/bar`,
     * The provider will place a datastore named `test` in a datastore folder
     * located at `/dc1/datastore/foo/bar`, with the final inventory path being
     * `/dc1/datastore/foo/bar/test`. Conflicts with
     * `datastoreClusterId`.
     */
    public readonly folder!: pulumi.Output<string | undefined>;
    /**
     * Available space of this datastore, in megabytes.
     */
    public /*out*/ readonly freeSpace!: pulumi.Output<number>;
    /**
     * The managed object IDs of
     * the hosts to mount the datastore on.
     */
    public readonly hostSystemIds!: pulumi.Output<string[]>;
    /**
     * The current maintenance mode state of the datastore.
     */
    public /*out*/ readonly maintenanceMode!: pulumi.Output<string>;
    /**
     * If `true`, more than one host in the datacenter has
     * been configured with access to the datastore.
     */
    public /*out*/ readonly multipleHostAccess!: pulumi.Output<boolean>;
    /**
     * The name of the datastore. Forces a new resource if
     * changed.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Indicates that this NAS volume is a protocol endpoint.
     * This field is only populated if the host supports virtual datastores.
     */
    public /*out*/ readonly protocolEndpoint!: pulumi.Output<string>;
    /**
     * The hostnames or IP addresses of the remote
     * server or servers. Only one element should be present for NFS v3 but multiple
     * can be present for NFS v4.1. Forces a new resource if changed.
     */
    public readonly remoteHosts!: pulumi.Output<string[]>;
    /**
     * The remote path of the mount point. Forces a new
     * resource if changed.
     */
    public readonly remotePath!: pulumi.Output<string>;
    /**
     * The security type to use when using NFS v4.1.
     * Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
     * if changed.
     */
    public readonly securityType!: pulumi.Output<string | undefined>;
    /**
     * The IDs of any tags to attach to this resource.
     */
    public readonly tags!: pulumi.Output<string[] | undefined>;
    /**
     * The type of NAS volume. Can be one of `NFS` (to denote
     * v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
     * changed.
     */
    public readonly type!: pulumi.Output<string | undefined>;
    /**
     * Total additional storage space, in megabytes,
     * potentially used by all virtual machines on this datastore.
     */
    public /*out*/ readonly uncommittedSpace!: pulumi.Output<number>;
    /**
     * The unique locator for the datastore.
     */
    public /*out*/ readonly url!: pulumi.Output<string>;

    /**
     * Create a NasDatastore resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NasDatastoreArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: NasDatastoreArgs | NasDatastoreState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as NasDatastoreState | undefined;
            inputs["accessMode"] = state ? state.accessMode : undefined;
            inputs["accessible"] = state ? state.accessible : undefined;
            inputs["capacity"] = state ? state.capacity : undefined;
            inputs["customAttributes"] = state ? state.customAttributes : undefined;
            inputs["datastoreClusterId"] = state ? state.datastoreClusterId : undefined;
            inputs["folder"] = state ? state.folder : undefined;
            inputs["freeSpace"] = state ? state.freeSpace : undefined;
            inputs["hostSystemIds"] = state ? state.hostSystemIds : undefined;
            inputs["maintenanceMode"] = state ? state.maintenanceMode : undefined;
            inputs["multipleHostAccess"] = state ? state.multipleHostAccess : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["protocolEndpoint"] = state ? state.protocolEndpoint : undefined;
            inputs["remoteHosts"] = state ? state.remoteHosts : undefined;
            inputs["remotePath"] = state ? state.remotePath : undefined;
            inputs["securityType"] = state ? state.securityType : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["type"] = state ? state.type : undefined;
            inputs["uncommittedSpace"] = state ? state.uncommittedSpace : undefined;
            inputs["url"] = state ? state.url : undefined;
        } else {
            const args = argsOrState as NasDatastoreArgs | undefined;
            if (!args || args.hostSystemIds === undefined) {
                throw new Error("Missing required property 'hostSystemIds'");
            }
            if (!args || args.remoteHosts === undefined) {
                throw new Error("Missing required property 'remoteHosts'");
            }
            if (!args || args.remotePath === undefined) {
                throw new Error("Missing required property 'remotePath'");
            }
            inputs["accessMode"] = args ? args.accessMode : undefined;
            inputs["customAttributes"] = args ? args.customAttributes : undefined;
            inputs["datastoreClusterId"] = args ? args.datastoreClusterId : undefined;
            inputs["folder"] = args ? args.folder : undefined;
            inputs["hostSystemIds"] = args ? args.hostSystemIds : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["remoteHosts"] = args ? args.remoteHosts : undefined;
            inputs["remotePath"] = args ? args.remotePath : undefined;
            inputs["securityType"] = args ? args.securityType : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["type"] = args ? args.type : undefined;
            inputs["accessible"] = undefined /*out*/;
            inputs["capacity"] = undefined /*out*/;
            inputs["freeSpace"] = undefined /*out*/;
            inputs["maintenanceMode"] = undefined /*out*/;
            inputs["multipleHostAccess"] = undefined /*out*/;
            inputs["protocolEndpoint"] = undefined /*out*/;
            inputs["uncommittedSpace"] = undefined /*out*/;
            inputs["url"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(NasDatastore.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering NasDatastore resources.
 */
export interface NasDatastoreState {
    /**
     * Access mode for the mount point. Can be one of
     * `readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
     * that the datastore will be read-write depending on the permissions of the
     * actual share. Default: `readWrite`. Forces a new resource if changed.
     */
    readonly accessMode?: pulumi.Input<string>;
    /**
     * The connectivity status of the datastore. If this is `false`,
     * some other computed attributes may be out of date.
     */
    readonly accessible?: pulumi.Input<boolean>;
    /**
     * Maximum capacity of the datastore, in megabytes.
     */
    readonly capacity?: pulumi.Input<number>;
    /**
     * Map of custom attribute ids to attribute 
     * value strings to set on datasource resource.
     */
    readonly customAttributes?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The managed object
     * ID of a datastore cluster to put this datastore in.
     * Conflicts with `folder`.
     */
    readonly datastoreClusterId?: pulumi.Input<string>;
    /**
     * The relative path to a folder to put this datastore in.
     * This is a path relative to the datacenter you are deploying the datastore to.
     * Example: for the `dc1` datacenter, and a provided `folder` of `foo/bar`,
     * The provider will place a datastore named `test` in a datastore folder
     * located at `/dc1/datastore/foo/bar`, with the final inventory path being
     * `/dc1/datastore/foo/bar/test`. Conflicts with
     * `datastoreClusterId`.
     */
    readonly folder?: pulumi.Input<string>;
    /**
     * Available space of this datastore, in megabytes.
     */
    readonly freeSpace?: pulumi.Input<number>;
    /**
     * The managed object IDs of
     * the hosts to mount the datastore on.
     */
    readonly hostSystemIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The current maintenance mode state of the datastore.
     */
    readonly maintenanceMode?: pulumi.Input<string>;
    /**
     * If `true`, more than one host in the datacenter has
     * been configured with access to the datastore.
     */
    readonly multipleHostAccess?: pulumi.Input<boolean>;
    /**
     * The name of the datastore. Forces a new resource if
     * changed.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Indicates that this NAS volume is a protocol endpoint.
     * This field is only populated if the host supports virtual datastores.
     */
    readonly protocolEndpoint?: pulumi.Input<string>;
    /**
     * The hostnames or IP addresses of the remote
     * server or servers. Only one element should be present for NFS v3 but multiple
     * can be present for NFS v4.1. Forces a new resource if changed.
     */
    readonly remoteHosts?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The remote path of the mount point. Forces a new
     * resource if changed.
     */
    readonly remotePath?: pulumi.Input<string>;
    /**
     * The security type to use when using NFS v4.1.
     * Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
     * if changed.
     */
    readonly securityType?: pulumi.Input<string>;
    /**
     * The IDs of any tags to attach to this resource.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The type of NAS volume. Can be one of `NFS` (to denote
     * v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
     * changed.
     */
    readonly type?: pulumi.Input<string>;
    /**
     * Total additional storage space, in megabytes,
     * potentially used by all virtual machines on this datastore.
     */
    readonly uncommittedSpace?: pulumi.Input<number>;
    /**
     * The unique locator for the datastore.
     */
    readonly url?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a NasDatastore resource.
 */
export interface NasDatastoreArgs {
    /**
     * Access mode for the mount point. Can be one of
     * `readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
     * that the datastore will be read-write depending on the permissions of the
     * actual share. Default: `readWrite`. Forces a new resource if changed.
     */
    readonly accessMode?: pulumi.Input<string>;
    /**
     * Map of custom attribute ids to attribute 
     * value strings to set on datasource resource.
     */
    readonly customAttributes?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The managed object
     * ID of a datastore cluster to put this datastore in.
     * Conflicts with `folder`.
     */
    readonly datastoreClusterId?: pulumi.Input<string>;
    /**
     * The relative path to a folder to put this datastore in.
     * This is a path relative to the datacenter you are deploying the datastore to.
     * Example: for the `dc1` datacenter, and a provided `folder` of `foo/bar`,
     * The provider will place a datastore named `test` in a datastore folder
     * located at `/dc1/datastore/foo/bar`, with the final inventory path being
     * `/dc1/datastore/foo/bar/test`. Conflicts with
     * `datastoreClusterId`.
     */
    readonly folder?: pulumi.Input<string>;
    /**
     * The managed object IDs of
     * the hosts to mount the datastore on.
     */
    readonly hostSystemIds: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of the datastore. Forces a new resource if
     * changed.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The hostnames or IP addresses of the remote
     * server or servers. Only one element should be present for NFS v3 but multiple
     * can be present for NFS v4.1. Forces a new resource if changed.
     */
    readonly remoteHosts: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The remote path of the mount point. Forces a new
     * resource if changed.
     */
    readonly remotePath: pulumi.Input<string>;
    /**
     * The security type to use when using NFS v4.1.
     * Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
     * if changed.
     */
    readonly securityType?: pulumi.Input<string>;
    /**
     * The IDs of any tags to attach to this resource.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The type of NAS volume. Can be one of `NFS` (to denote
     * v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
     * changed.
     */
    readonly type?: pulumi.Input<string>;
}
