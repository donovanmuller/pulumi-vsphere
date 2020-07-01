// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a VMware vSphere host resource. This represents an ESXi host that
 * can be used either as part of a Compute Cluster or Standalone.
 *
 * ## Example Usage
 * ### Create a standalone host
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as vsphere from "@pulumi/vsphere";
 *
 * const dc = vsphere.getDatacenter({
 *     name: "my-datacenter",
 * });
 * const h1 = new vsphere.Host("h1", {
 *     hostname: "10.10.10.1",
 *     username: "root",
 *     password: "password",
 *     license: "00000-00000-00000-00000i-00000",
 *     datacenter: dc.then(dc => dc.id),
 * });
 * ```
 * ### Create host in a compute cluster
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as vsphere from "@pulumi/vsphere";
 *
 * const dc = vsphere.getDatacenter({
 *     name: "TfDatacenter",
 * });
 * const c1 = dc.then(dc => vsphere.getComputeCluster({
 *     name: "DC0_C0",
 *     datacenterId: dc.id,
 * }));
 * const h1 = new vsphere.Host("h1", {
 *     hostname: "10.10.10.1",
 *     username: "root",
 *     password: "password",
 *     license: "00000-00000-00000-00000i-00000",
 *     cluster: c1.then(c1 => c1.id),
 * });
 * ```
 * ## Importing
 *
 * An existing host can be [imported][docs-import] into this resource
 * via supplying the host's ID. An example is below:
 *
 * [docs-import]: /docs/import/index.html
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * ```
 *
 * The above would import the host with ID `host-123`.
 */
export class Host extends pulumi.CustomResource {
    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: HostState, opts?: pulumi.CustomResourceOptions): Host {
        return new Host(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'vsphere:index/host:Host';

    /**
     * Returns true if the given object is an instance of Host.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Host {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Host.__pulumiType;
    }

    /**
     * The ID of the Compute Cluster this host should
     * be added to. This should not be set if `datacenter` is set. Conflicts with:
     * `cluster`.
     */
    public readonly cluster!: pulumi.Output<string | undefined>;
    /**
     * Can be set to `true` if compute cluster
     * membership will be managed through the `computeCluster` resource rather
     * than the`host` resource. Conflicts with: `cluster`.
     */
    public readonly clusterManaged!: pulumi.Output<boolean | undefined>;
    /**
     * If set to false then the host will be disconected.
     * Default is `false`.
     */
    public readonly connected!: pulumi.Output<boolean | undefined>;
    /**
     * The ID of the datacenter this host should
     * be added to. This should not be set if `cluster` is set.
     */
    public readonly datacenter!: pulumi.Output<string | undefined>;
    /**
     * If set to true then it will force the host to be added, even
     * if the host is already connected to a different vSphere instance. Default is `false`
     */
    public readonly force!: pulumi.Output<boolean | undefined>;
    /**
     * FQDN or IP address of the host to be added.
     */
    public readonly hostname!: pulumi.Output<string>;
    /**
     * The license key that will be applied to the host.
     * The license key is expected to be present in vSphere.
     */
    public readonly license!: pulumi.Output<string | undefined>;
    /**
     * Set the lockdown state of the host. Valid options are
     * `disabled`, `normal`, and `strict`. Default is `disabled`.
     */
    public readonly lockdown!: pulumi.Output<string | undefined>;
    /**
     * Set the management state of the host. Default is `false`.
     */
    public readonly maintenance!: pulumi.Output<boolean | undefined>;
    /**
     * Password that will be used by vSphere to authenticate
     * to the host.
     */
    public readonly password!: pulumi.Output<string>;
    /**
     * Host's certificate SHA-1 thumbprint. If not set the the
     * CA that signed the host's certificate should be trusted. If the CA is not trusted
     * and no thumbprint is set then the operation will fail.
     */
    public readonly thumbprint!: pulumi.Output<string | undefined>;
    /**
     * Username that will be used by vSphere to authenticate
     * to the host.
     */
    public readonly username!: pulumi.Output<string>;

    /**
     * Create a Host resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: HostArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: HostArgs | HostState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as HostState | undefined;
            inputs["cluster"] = state ? state.cluster : undefined;
            inputs["clusterManaged"] = state ? state.clusterManaged : undefined;
            inputs["connected"] = state ? state.connected : undefined;
            inputs["datacenter"] = state ? state.datacenter : undefined;
            inputs["force"] = state ? state.force : undefined;
            inputs["hostname"] = state ? state.hostname : undefined;
            inputs["license"] = state ? state.license : undefined;
            inputs["lockdown"] = state ? state.lockdown : undefined;
            inputs["maintenance"] = state ? state.maintenance : undefined;
            inputs["password"] = state ? state.password : undefined;
            inputs["thumbprint"] = state ? state.thumbprint : undefined;
            inputs["username"] = state ? state.username : undefined;
        } else {
            const args = argsOrState as HostArgs | undefined;
            if (!args || args.hostname === undefined) {
                throw new Error("Missing required property 'hostname'");
            }
            if (!args || args.password === undefined) {
                throw new Error("Missing required property 'password'");
            }
            if (!args || args.username === undefined) {
                throw new Error("Missing required property 'username'");
            }
            inputs["cluster"] = args ? args.cluster : undefined;
            inputs["clusterManaged"] = args ? args.clusterManaged : undefined;
            inputs["connected"] = args ? args.connected : undefined;
            inputs["datacenter"] = args ? args.datacenter : undefined;
            inputs["force"] = args ? args.force : undefined;
            inputs["hostname"] = args ? args.hostname : undefined;
            inputs["license"] = args ? args.license : undefined;
            inputs["lockdown"] = args ? args.lockdown : undefined;
            inputs["maintenance"] = args ? args.maintenance : undefined;
            inputs["password"] = args ? args.password : undefined;
            inputs["thumbprint"] = args ? args.thumbprint : undefined;
            inputs["username"] = args ? args.username : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Host.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Host resources.
 */
export interface HostState {
    /**
     * The ID of the Compute Cluster this host should
     * be added to. This should not be set if `datacenter` is set. Conflicts with:
     * `cluster`.
     */
    readonly cluster?: pulumi.Input<string>;
    /**
     * Can be set to `true` if compute cluster
     * membership will be managed through the `computeCluster` resource rather
     * than the`host` resource. Conflicts with: `cluster`.
     */
    readonly clusterManaged?: pulumi.Input<boolean>;
    /**
     * If set to false then the host will be disconected.
     * Default is `false`.
     */
    readonly connected?: pulumi.Input<boolean>;
    /**
     * The ID of the datacenter this host should
     * be added to. This should not be set if `cluster` is set.
     */
    readonly datacenter?: pulumi.Input<string>;
    /**
     * If set to true then it will force the host to be added, even
     * if the host is already connected to a different vSphere instance. Default is `false`
     */
    readonly force?: pulumi.Input<boolean>;
    /**
     * FQDN or IP address of the host to be added.
     */
    readonly hostname?: pulumi.Input<string>;
    /**
     * The license key that will be applied to the host.
     * The license key is expected to be present in vSphere.
     */
    readonly license?: pulumi.Input<string>;
    /**
     * Set the lockdown state of the host. Valid options are
     * `disabled`, `normal`, and `strict`. Default is `disabled`.
     */
    readonly lockdown?: pulumi.Input<string>;
    /**
     * Set the management state of the host. Default is `false`.
     */
    readonly maintenance?: pulumi.Input<boolean>;
    /**
     * Password that will be used by vSphere to authenticate
     * to the host.
     */
    readonly password?: pulumi.Input<string>;
    /**
     * Host's certificate SHA-1 thumbprint. If not set the the
     * CA that signed the host's certificate should be trusted. If the CA is not trusted
     * and no thumbprint is set then the operation will fail.
     */
    readonly thumbprint?: pulumi.Input<string>;
    /**
     * Username that will be used by vSphere to authenticate
     * to the host.
     */
    readonly username?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Host resource.
 */
export interface HostArgs {
    /**
     * The ID of the Compute Cluster this host should
     * be added to. This should not be set if `datacenter` is set. Conflicts with:
     * `cluster`.
     */
    readonly cluster?: pulumi.Input<string>;
    /**
     * Can be set to `true` if compute cluster
     * membership will be managed through the `computeCluster` resource rather
     * than the`host` resource. Conflicts with: `cluster`.
     */
    readonly clusterManaged?: pulumi.Input<boolean>;
    /**
     * If set to false then the host will be disconected.
     * Default is `false`.
     */
    readonly connected?: pulumi.Input<boolean>;
    /**
     * The ID of the datacenter this host should
     * be added to. This should not be set if `cluster` is set.
     */
    readonly datacenter?: pulumi.Input<string>;
    /**
     * If set to true then it will force the host to be added, even
     * if the host is already connected to a different vSphere instance. Default is `false`
     */
    readonly force?: pulumi.Input<boolean>;
    /**
     * FQDN or IP address of the host to be added.
     */
    readonly hostname: pulumi.Input<string>;
    /**
     * The license key that will be applied to the host.
     * The license key is expected to be present in vSphere.
     */
    readonly license?: pulumi.Input<string>;
    /**
     * Set the lockdown state of the host. Valid options are
     * `disabled`, `normal`, and `strict`. Default is `disabled`.
     */
    readonly lockdown?: pulumi.Input<string>;
    /**
     * Set the management state of the host. Default is `false`.
     */
    readonly maintenance?: pulumi.Input<boolean>;
    /**
     * Password that will be used by vSphere to authenticate
     * to the host.
     */
    readonly password: pulumi.Input<string>;
    /**
     * Host's certificate SHA-1 thumbprint. If not set the the
     * CA that signed the host's certificate should be trusted. If the CA is not trusted
     * and no thumbprint is set then the operation will fail.
     */
    readonly thumbprint?: pulumi.Input<string>;
    /**
     * Username that will be used by vSphere to authenticate
     * to the host.
     */
    readonly username: pulumi.Input<string>;
}
