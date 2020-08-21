// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface ComputeClusterVsanDiskGroup {
    cache?: string;
    storages?: string[];
}

export interface DistributedPortGroupVlanRange {
    maxVlan: number;
    minVlan: number;
}

export interface DistributedVirtualSwitchHost {
    /**
     * The list of NIC devices to map to uplinks on the DVS,
     * added in order they are specified.
     */
    devices: string[];
    /**
     * The host system ID of the host to add to the
     * DVS.
     */
    hostSystemId: string;
}

export interface DistributedVirtualSwitchVlanRange {
    maxVlan: number;
    minVlan: number;
}

export interface EntityPermissionsPermission {
    /**
     * Whether userOrGroup field refers to a user or a group. True for a group and false for a user.
     */
    isGroup: boolean;
    /**
     * Whether or not this permission propagates down the hierarchy to sub-entities.
     */
    propagate: boolean;
    /**
     * The role id of the role to be given to the user on the specified entity.
     */
    roleId: string;
    /**
     * The user/group getting the permission.
     */
    userOrGroup: string;
}

export interface GetVirtualMachineDisk {
    /**
     * Set to `true` if the disk has been eager zeroed.
     */
    eagerlyScrub: boolean;
    /**
     * The label for the disk.
     */
    label: string;
    /**
     * The size of the disk, in GIB.
     */
    size: number;
    /**
     * Set to `true` if the disk has been thin provisioned.
     */
    thinProvisioned: boolean;
    /**
     * The disk number on the storage bus.
     */
    unitNumber: number;
}

export interface GetVirtualMachineVapp {
    properties?: {[key: string]: string};
}

export interface HostPortGroupPorts {
    /**
     * The key for this port group as returned from the vSphere API.
     */
    key: string;
    macAddresses: string[];
    type: string;
}

export interface VirtualMachineCdrom {
    /**
     * Indicates whether the device should be backed by
     * remote client device. Conflicts with `datastoreId` and `path`.
     */
    clientDevice?: boolean;
    /**
     * The datastore ID that the ISO is located in.
     * Requried for using a datastore ISO. Conflicts with `clientDevice`.
     */
    datastoreId?: string;
    /**
     * An address internal to this provider that helps locate the
     * device when `key` is unavailable. This follows a convention of
     * `CONTROLLER_TYPE:BUS_NUMBER:UNIT_NUMBER`. Example: `scsi:0:1` means device
     * unit 1 on SCSI bus 0.
     */
    deviceAddress: string;
    /**
     * The ID of the device within the virtual machine.
     */
    key: number;
    /**
     * The path to the ISO file. Required for using a datastore
     * ISO. Conflicts with `clientDevice`.
     */
    path?: string;
}

export interface VirtualMachineClone {
    customize?: outputs.VirtualMachineCloneCustomize;
    linkedClone?: boolean;
    ovfNetworkMap?: {[key: string]: string};
    ovfStorageMap?: {[key: string]: string};
    templateUuid: string;
    timeout?: number;
}

export interface VirtualMachineCloneCustomize {
    dnsServerLists?: string[];
    dnsSuffixLists?: string[];
    ipv4Gateway?: string;
    ipv6Gateway?: string;
    linuxOptions?: outputs.VirtualMachineCloneCustomizeLinuxOptions;
    /**
     * A specification for a virtual NIC on this
     * virtual machine. See network interface options
     * below.
     */
    networkInterfaces?: outputs.VirtualMachineCloneCustomizeNetworkInterface[];
    timeout?: number;
    windowsOptions?: outputs.VirtualMachineCloneCustomizeWindowsOptions;
    windowsSysprepText?: string;
}

export interface VirtualMachineCloneCustomizeLinuxOptions {
    domain: string;
    hostName: string;
    hwClockUtc?: boolean;
    timeZone?: string;
}

export interface VirtualMachineCloneCustomizeNetworkInterface {
    dnsDomain?: string;
    dnsServerLists?: string[];
    ipv4Address?: string;
    ipv4Netmask?: number;
    ipv6Address?: string;
    ipv6Netmask?: number;
}

export interface VirtualMachineCloneCustomizeWindowsOptions {
    adminPassword?: string;
    autoLogon?: boolean;
    autoLogonCount?: number;
    computerName: string;
    domainAdminPassword?: string;
    domainAdminUser?: string;
    fullName?: string;
    joinDomain?: string;
    organizationName?: string;
    productKey?: string;
    runOnceCommandLists?: string[];
    timeZone?: number;
    workgroup?: string;
}

export interface VirtualMachineDisk {
    /**
     * Attach an external disk instead of creating a new one.
     * Implies and conflicts with `keepOnRemove`. If set, you cannot set `size`,
     * `eagerlyScrub`, or `thinProvisioned`. Must set `path` if used.
     */
    attach?: boolean;
    /**
     * The type of storage controller to attach the
     * disk to. Can be `scsi`, `sata`, or `ide`. You must have the appropriate
     * number of controllers enabled for the selected type. Default `scsi`.
     */
    controllerType?: string;
    /**
     * The datastore ID that the ISO is located in.
     * Requried for using a datastore ISO. Conflicts with `clientDevice`.
     */
    datastoreId?: string;
    /**
     * An address internal to this provider that helps locate the
     * device when `key` is unavailable. This follows a convention of
     * `CONTROLLER_TYPE:BUS_NUMBER:UNIT_NUMBER`. Example: `scsi:0:1` means device
     * unit 1 on SCSI bus 0.
     */
    deviceAddress: string;
    /**
     * The mode of this this virtual disk for purposes of
     * writes and snapshotting. Can be one of `append`, `independentNonpersistent`,
     * `independentPersistent`, `nonpersistent`, `persistent`, or `undoable`.
     * Default: `persistent`. For an explanation of options, click
     * [here][vmware-docs-disk-mode].
     */
    diskMode?: string;
    /**
     * The sharing mode of this virtual disk. Can be one
     * of `sharingMultiWriter` or `sharingNone`. Default: `sharingNone`.
     */
    diskSharing?: string;
    /**
     * If set to `true`, the disk space is zeroed out
     * on VM creation. This will delay the creation of the disk or virtual machine.
     * Cannot be set to `true` when `thinProvisioned` is `true`.  See the section
     * on picking a disk type.  Default: `false`.
     */
    eagerlyScrub?: boolean;
    /**
     * The upper limit of IOPS that this disk can use. The
     * default is no limit.
     */
    ioLimit?: number;
    /**
     * The I/O reservation (guarantee) that this disk
     * has, in IOPS.  The default is no reservation.
     */
    ioReservation?: number;
    /**
     * The share count for this disk when the share
     * level is `custom`.
     */
    ioShareCount?: number;
    /**
     * The share allocation level for this disk. Can
     * be one of `low`, `normal`, `high`, or `custom`. Default: `normal`.
     */
    ioShareLevel?: string;
    /**
     * Keep this disk when removing the device or
     * destroying the virtual machine. Default: `false`.
     */
    keepOnRemove?: boolean;
    /**
     * The ID of the device within the virtual machine.
     */
    key: number;
    /**
     * A label for the disk. Forces a new disk if changed.
     */
    label?: string;
    /**
     * An alias for both `label` and `path`, the latter when
     * using `attach`. Required if not using `label`.
     *
     * @deprecated 
The name attribute for virtual disks will be removed in favor of "label" in
future releases. To transition existing disks, rename the "name" attribute to
"label". When doing so, ensure the value of the attribute stays the same.

Note that "label" does not control the name of a VMDK and does not need to bear
the name of one on new disks or virtual machines. For more information, see the
documentation for the label attribute at: 

https://www.terraform.io/docs/providers/vsphere/r/virtual_machine.html#label

     */
    name?: string;
    /**
     * The path to the ISO file. Required for using a datastore
     * ISO. Conflicts with `clientDevice`.
     */
    path: string;
    /**
     * The size of the disk, in GB.
     */
    size?: number;
    /**
     * The UUID of the storage policy to assign to this disk.
     */
    storagePolicyId?: string;
    /**
     * If `true`, this disk is thin provisioned,
     * with space for the file being allocated on an as-needed basis. Cannot be set
     * to `true` when `eagerlyScrub` is `true`. See the section on picking a disk
     * type. Default: `true`.
     */
    thinProvisioned?: boolean;
    /**
     * The disk number on the storage bus. The maximum
     * value for this setting is the value of the controller count times the
     * controller capacity (15 for SCSI, 30 for SATA, and 2 for IDE).
     * The default is `0`, for which one disk must be set to. Duplicate unit numbers
     * are not allowed.
     */
    unitNumber?: number;
    /**
     * The UUID of the virtual disk's VMDK file. This is used to track the
     * virtual disk on the virtual machine.
     */
    uuid: string;
    /**
     * If `true`, writes for this disk are sent
     * directly to the filesystem immediately instead of being buffered. Default:
     * `false`.
     */
    writeThrough?: boolean;
}

export interface VirtualMachineNetworkInterface {
    /**
     * The network interface type. Can be one of
     * `e1000`, `e1000e`, or `vmxnet3`. Default: `vmxnet3`.
     */
    adapterType?: string;
    /**
     * The upper bandwidth limit of this network
     * interface, in Mbits/sec. The default is no limit.
     */
    bandwidthLimit?: number;
    /**
     * The bandwidth reservation of this
     * network interface, in Mbits/sec. The default is no reservation.
     */
    bandwidthReservation?: number;
    /**
     * The share count for this network
     * interface when the share level is `custom`.
     */
    bandwidthShareCount: number;
    /**
     * The bandwidth share allocation level for
     * this interface. Can be one of `low`, `normal`, `high`, or `custom`. Default:
     * `normal`.
     */
    bandwidthShareLevel?: string;
    /**
     * An address internal to this provider that helps locate the
     * device when `key` is unavailable. This follows a convention of
     * `CONTROLLER_TYPE:BUS_NUMBER:UNIT_NUMBER`. Example: `scsi:0:1` means device
     * unit 1 on SCSI bus 0.
     */
    deviceAddress: string;
    /**
     * The ID of the device within the virtual machine.
     */
    key: number;
    /**
     * The MAC address of this network interface. Can
     * only be manually set if `useStaticMac` is true, otherwise this is a
     * computed value that gives the current MAC address of this interface.
     */
    macAddress: string;
    /**
     * The managed object reference
     * ID of the network to connect this interface to.
     */
    networkId: string;
    /**
     * Specifies which OVF NIC the `networkInterface`
     * should be associated with. Only applies at creation and only when deploying
     * from an OVF source.
     */
    ovfMapping?: string;
    /**
     * If true, the `macAddress` field is treated as
     * a static MAC address and set accordingly. Setting this to `true` requires
     * `macAddress` to be set. Default: `false`.
     */
    useStaticMac?: boolean;
}

export interface VirtualMachineOvfDeploy {
    allowUnverifiedSslCert?: boolean;
    diskProvisioning?: string;
    ipAllocationPolicy?: string;
    ipProtocol?: string;
    localOvfPath?: string;
    ovfNetworkMap?: {[key: string]: string};
    remoteOvfUrl?: string;
}

export interface VirtualMachineVapp {
    properties?: {[key: string]: string};
}

export interface VmStoragePolicyTagRule {
    /**
     * Whether to include datastores with the given tags or exclude. Default 
     * value is true i.e. include datastores with the given tags.
     */
    includeDatastoresWithTags?: boolean;
    /**
     * Name of the tag category.
     */
    tagCategory: string;
    /**
     * List of Name of tags to select from the given category.
     */
    tags: string[];
}

export interface VnicIpv4 {
    /**
     * Use DHCP to configure the interface's IPv4 stack.
     */
    dhcp?: boolean;
    /**
     * IP address of the default gateway, if DHCP or autoconfig is not set.
     */
    gw?: string;
    /**
     * Address of the interface, if DHCP is not set.
     */
    ip?: string;
    /**
     * Netmask of the interface, if DHCP is not set.
     */
    netmask?: string;
}

export interface VnicIpv6 {
    /**
     * List of IPv6 addresses
     */
    addresses?: string[];
    /**
     * Use IPv6 Autoconfiguration (RFC2462).
     */
    autoconfig?: boolean;
    /**
     * Use DHCP to configure the interface's IPv4 stack.
     */
    dhcp?: boolean;
    /**
     * IP address of the default gateway, if DHCP or autoconfig is not set.
     */
    gw?: string;
}
