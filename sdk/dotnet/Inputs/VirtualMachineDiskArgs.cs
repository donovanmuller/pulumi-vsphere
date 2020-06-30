// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.VSphere.Inputs
{

    public sealed class VirtualMachineDiskArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Attach an external disk instead of creating a new one.
        /// Implies and conflicts with `keep_on_remove`. If set, you cannot set `size`,
        /// `eagerly_scrub`, or `thin_provisioned`. Must set `path` if used.
        /// </summary>
        [Input("attach")]
        public Input<bool>? Attach { get; set; }

        /// <summary>
        /// The type of storage controller to attach the
        /// disk to. Can be `scsi`, `sata`, or `ide`. You must have the appropriate
        /// number of controllers enabled for the selected type. Default `scsi`.
        /// </summary>
        [Input("controllerType")]
        public Input<string>? ControllerType { get; set; }

        /// <summary>
        /// The datastore ID that the ISO is located in.
        /// Requried for using a datastore ISO. Conflicts with `client_device`.
        /// </summary>
        [Input("datastoreId")]
        public Input<string>? DatastoreId { get; set; }

        /// <summary>
        /// An address internal to this provider that helps locate the
        /// device when `key` is unavailable. This follows a convention of
        /// `CONTROLLER_TYPE:BUS_NUMBER:UNIT_NUMBER`. Example: `scsi:0:1` means device
        /// unit 1 on SCSI bus 0.
        /// </summary>
        [Input("deviceAddress")]
        public Input<string>? DeviceAddress { get; set; }

        /// <summary>
        /// The mode of this this virtual disk for purposes of
        /// writes and snapshotting. Can be one of `append`, `independent_nonpersistent`,
        /// `independent_persistent`, `nonpersistent`, `persistent`, or `undoable`.
        /// Default: `persistent`. For an explanation of options, click
        /// [here][vmware-docs-disk-mode].
        /// </summary>
        [Input("diskMode")]
        public Input<string>? DiskMode { get; set; }

        /// <summary>
        /// The sharing mode of this virtual disk. Can be one
        /// of `sharingMultiWriter` or `sharingNone`. Default: `sharingNone`.
        /// </summary>
        [Input("diskSharing")]
        public Input<string>? DiskSharing { get; set; }

        /// <summary>
        /// If set to `true`, the disk space is zeroed out
        /// on VM creation. This will delay the creation of the disk or virtual machine.
        /// Cannot be set to `true` when `thin_provisioned` is `true`.  See the section
        /// on picking a disk type.  Default: `false`.
        /// </summary>
        [Input("eagerlyScrub")]
        public Input<bool>? EagerlyScrub { get; set; }

        /// <summary>
        /// The upper limit of IOPS that this disk can use. The
        /// default is no limit.
        /// </summary>
        [Input("ioLimit")]
        public Input<int>? IoLimit { get; set; }

        /// <summary>
        /// The I/O reservation (guarantee) that this disk
        /// has, in IOPS.  The default is no reservation.
        /// </summary>
        [Input("ioReservation")]
        public Input<int>? IoReservation { get; set; }

        /// <summary>
        /// The share count for this disk when the share
        /// level is `custom`.
        /// </summary>
        [Input("ioShareCount")]
        public Input<int>? IoShareCount { get; set; }

        /// <summary>
        /// The share allocation level for this disk. Can
        /// be one of `low`, `normal`, `high`, or `custom`. Default: `normal`.
        /// </summary>
        [Input("ioShareLevel")]
        public Input<string>? IoShareLevel { get; set; }

        /// <summary>
        /// Keep this disk when removing the device or
        /// destroying the virtual machine. Default: `false`.
        /// </summary>
        [Input("keepOnRemove")]
        public Input<bool>? KeepOnRemove { get; set; }

        /// <summary>
        /// The ID of the device within the virtual machine.
        /// </summary>
        [Input("key")]
        public Input<int>? Key { get; set; }

        /// <summary>
        /// A label for the disk. Forces a new disk if changed.
        /// </summary>
        [Input("label")]
        public Input<string>? Label { get; set; }

        /// <summary>
        /// An alias for both `label` and `path`, the latter when
        /// using `attach`. Required if not using `label`.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The path to the ISO file. Required for using a datastore
        /// ISO. Conflicts with `client_device`.
        /// </summary>
        [Input("path")]
        public Input<string>? Path { get; set; }

        /// <summary>
        /// The size of the disk, in GB.
        /// </summary>
        [Input("size")]
        public Input<int>? Size { get; set; }

        /// <summary>
        /// The UUID of the storage policy to assign to this disk.
        /// </summary>
        [Input("storagePolicyId")]
        public Input<string>? StoragePolicyId { get; set; }

        /// <summary>
        /// If `true`, this disk is thin provisioned,
        /// with space for the file being allocated on an as-needed basis. Cannot be set
        /// to `true` when `eagerly_scrub` is `true`. See the section on picking a disk
        /// type. Default: `true`.
        /// </summary>
        [Input("thinProvisioned")]
        public Input<bool>? ThinProvisioned { get; set; }

        /// <summary>
        /// The disk number on the storage bus. The maximum
        /// value for this setting is the value of the controller count times the
        /// controller capacity (15 for SCSI, 30 for SATA, and 2 for IDE).
        /// The default is `0`, for which one disk must be set to. Duplicate unit numbers
        /// are not allowed.
        /// </summary>
        [Input("unitNumber")]
        public Input<int>? UnitNumber { get; set; }

        /// <summary>
        /// The UUID of the virtual disk's VMDK file. This is used to track the
        /// virtual disk on the virtual machine.
        /// </summary>
        [Input("uuid")]
        public Input<string>? Uuid { get; set; }

        /// <summary>
        /// If `true`, writes for this disk are sent
        /// directly to the filesystem immediately instead of being buffered. Default:
        /// `false`.
        /// </summary>
        [Input("writeThrough")]
        public Input<bool>? WriteThrough { get; set; }

        public VirtualMachineDiskArgs()
        {
        }
    }
}
