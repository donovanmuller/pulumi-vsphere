// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The provider type for the vsphere package. By default, resources use package-wide configuration
 * settings, however an explicit `Provider` instance may be created and passed during resource
 * construction to achieve fine-grained programmatic control over provider settings. See the
 * [documentation](https://pulumi.io/reference/programming-model.html#providers) for more information.
 */
export class Provider extends pulumi.ProviderResource {

    /**
     * Create a Provider resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ProviderArgs, opts?: pulumi.ResourceOptions) {
        let inputs: pulumi.Inputs = {};
        {
            if (!args || args.password === undefined) {
                throw new Error("Missing required property 'password'");
            }
            if (!args || args.user === undefined) {
                throw new Error("Missing required property 'user'");
            }
            inputs["allowUnverifiedSsl"] = pulumi.output(args ? args.allowUnverifiedSsl : undefined).apply(JSON.stringify);
            inputs["clientDebug"] = pulumi.output(args ? args.clientDebug : undefined).apply(JSON.stringify);
            inputs["clientDebugPath"] = args ? args.clientDebugPath : undefined;
            inputs["clientDebugPathRun"] = args ? args.clientDebugPathRun : undefined;
            inputs["password"] = args ? args.password : undefined;
            inputs["persistSession"] = pulumi.output(args ? args.persistSession : undefined).apply(JSON.stringify);
            inputs["restSessionPath"] = args ? args.restSessionPath : undefined;
            inputs["user"] = args ? args.user : undefined;
            inputs["vcenterServer"] = args ? args.vcenterServer : undefined;
            inputs["vimSessionPath"] = args ? args.vimSessionPath : undefined;
            inputs["vsphereServer"] = args ? args.vsphereServer : undefined;
        }
        super("vsphere", name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Provider resource.
 */
export interface ProviderArgs {
    /**
     * If set, VMware vSphere client will permit unverifiable SSL certificates.
     */
    readonly allowUnverifiedSsl?: pulumi.Input<boolean>;
    /**
     * govmomi debug
     */
    readonly clientDebug?: pulumi.Input<boolean>;
    /**
     * govmomi debug path for debug
     */
    readonly clientDebugPath?: pulumi.Input<string>;
    /**
     * govmomi debug path for a single run
     */
    readonly clientDebugPathRun?: pulumi.Input<string>;
    /**
     * The user password for vSphere API operations.
     */
    readonly password: pulumi.Input<string>;
    /**
     * Persist vSphere client sessions to disk
     */
    readonly persistSession?: pulumi.Input<boolean>;
    /**
     * The directory to save vSphere REST API sessions to
     */
    readonly restSessionPath?: pulumi.Input<string>;
    /**
     * The user name for vSphere API operations.
     */
    readonly user: pulumi.Input<string>;
    readonly vcenterServer?: pulumi.Input<string>;
    /**
     * The directory to save vSphere SOAP API sessions to
     */
    readonly vimSessionPath?: pulumi.Input<string>;
    /**
     * The vSphere Server name for vSphere API operations.
     */
    readonly vsphereServer?: pulumi.Input<string>;
}
