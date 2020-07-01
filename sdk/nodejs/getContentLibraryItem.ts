// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * The `vsphere.ContentLibraryItem` data source can be used to discover the ID of a Content Library item.
 *
 * > **NOTE:** This resource requires vCenter and is not available on direct ESXi
 * connections.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as vsphere from "@pulumi/vsphere";
 *
 * const library = vsphere.getContentLibrary({
 *     name: "Content Library Test",
 * });
 * const item = library.then(library => vsphere.getContentLibraryItem({
 *     name: "Ubuntu Bionic 18.04",
 *     libraryId: library.id,
 * }));
 * ```
 */
export function getContentLibraryItem(args: GetContentLibraryItemArgs, opts?: pulumi.InvokeOptions): Promise<GetContentLibraryItemResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("vsphere:index/getContentLibraryItem:getContentLibraryItem", {
        "libraryId": args.libraryId,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getContentLibraryItem.
 */
export interface GetContentLibraryItemArgs {
    /**
     * The ID of the Content Library the item exists in.
     */
    readonly libraryId: string;
    /**
     * The name of the Content Library.
     */
    readonly name: string;
}

/**
 * A collection of values returned by getContentLibraryItem.
 */
export interface GetContentLibraryItemResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly libraryId: string;
    readonly name: string;
}
