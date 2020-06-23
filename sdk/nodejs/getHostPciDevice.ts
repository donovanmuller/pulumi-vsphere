// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * The `vsphere..getHostPciDevice` data source can be used to discover the DeviceID
 * of a vSphere host's PCI device. This can then be used with 
 * `vsphere..VirtualMachine`'s `pciDeviceId`.
 *
 * ## Example Usage With Vendor ID and Class ID
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as vsphere from "@pulumi/vsphere";
 *
 * const datacenter = vsphere.getDatacenter({
 *     name: "dc1",
 * });
 * const host = datacenter.then(datacenter => vsphere.getHost({
 *     name: "esxi1",
 *     datacenterId: datacenter.id,
 * }));
 * const dev = host.then(host => vsphere.getHostPciDevice({
 *     hostId: host.id,
 *     classId: 123,
 *     vendorId: 456,
 * }));
 * ```
 * ## Example Usage With Name Regular Expression
 *  
 *  ```hcl
 *  data "vsphere..Datacenter" "datacenter" {
 *    name = "dc1"
 *  }
 *  
 *  data "vsphere..Host" "host" {
 *    name          = "esxi1"
 *    datacenterId = data.vsphere_datacenter.datacenter.id
 *  }
 *  
 *  data "vsphere..getHostPciDevice" "dev" {
 *    hostId    = data.vsphere_host.host.id
 *    nameRegex = "MMC"
 *  }
 *  ```
 */
export function getHostPciDevice(args: GetHostPciDeviceArgs, opts?: pulumi.InvokeOptions): Promise<GetHostPciDeviceResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("vsphere:index/getHostPciDevice:getHostPciDevice", {
        "classId": args.classId,
        "hostId": args.hostId,
        "nameRegex": args.nameRegex,
        "vendorId": args.vendorId,
    }, opts);
}

/**
 * A collection of arguments for invoking getHostPciDevice.
 */
export interface GetHostPciDeviceArgs {
    /**
     * The hexadecimal PCI device class ID
     */
    readonly classId?: string;
    /**
     * The [managed object reference
     * ID][docs-about-morefs] of a host.
     */
    readonly hostId: string;
    /**
     * A regular expression that will be used to match
     * the host PCI device name.
     */
    readonly nameRegex?: string;
    /**
     * The hexadecimal PCI device vendor ID.
     */
    readonly vendorId?: string;
}

/**
 * A collection of values returned by getHostPciDevice.
 */
export interface GetHostPciDeviceResult {
    readonly classId?: string;
    readonly hostId: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The name of the PCI device.
     */
    readonly name: string;
    readonly nameRegex?: string;
    readonly vendorId?: string;
}
