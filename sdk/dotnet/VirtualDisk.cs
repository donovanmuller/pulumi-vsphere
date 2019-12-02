// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Vsphere
{
    /// <summary>
    /// The `vsphere..VirtualDisk` resource can be used to create virtual disks outside
    /// of any given [`vsphere..VirtualMachine`][docs-vsphere-virtual-machine]
    /// resource. These disks can be attached to a virtual machine by creating a disk
    /// block with the [`attach`][docs-vsphere-virtual-machine-disk-attach] parameter.
    /// 
    /// [docs-vsphere-virtual-machine]: /docs/providers/vsphere/r/virtual_machine.html
    /// [docs-vsphere-virtual-machine-disk-attach]: /docs/providers/vsphere/r/virtual_machine.html#attach
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/r/virtual_disk.html.markdown.
    /// </summary>
    public partial class VirtualDisk : Pulumi.CustomResource
    {
        /// <summary>
        /// The adapter type for this virtual disk. Can be
        /// one of `ide`, `lsiLogic`, or `busLogic`.  Default: `lsiLogic`.
        /// </summary>
        [Output("adapterType")]
        public Output<string?> AdapterType { get; private set; } = null!;

        /// <summary>
        /// Tells the resource to create any
        /// directories that are a part of the `vmdk_path` parameter if they are missing.
        /// Default: `false`.
        /// </summary>
        [Output("createDirectories")]
        public Output<bool?> CreateDirectories { get; private set; } = null!;

        /// <summary>
        /// The name of the datacenter in which to create the
        /// disk. Can be omitted when when ESXi or if there is only one datacenter in
        /// your infrastructure.
        /// </summary>
        [Output("datacenter")]
        public Output<string?> Datacenter { get; private set; } = null!;

        /// <summary>
        /// The name of the datastore in which to create the
        /// disk.
        /// </summary>
        [Output("datastore")]
        public Output<string> Datastore { get; private set; } = null!;

        /// <summary>
        /// Size of the disk (in GB).
        /// </summary>
        [Output("size")]
        public Output<int> Size { get; private set; } = null!;

        /// <summary>
        /// The type of disk to create. Can be one of
        /// `eagerZeroedThick`, `lazy`, or `thin`. Default: `eagerZeroedThick`. For
        /// information on what each kind of disk provisioning policy means, click
        /// [here][docs-vmware-vm-disk-provisioning].
        /// </summary>
        [Output("type")]
        public Output<string?> Type { get; private set; } = null!;

        /// <summary>
        /// The path, including filename, of the virtual disk to
        /// be created.  This needs to end in `.vmdk`.
        /// </summary>
        [Output("vmdkPath")]
        public Output<string> VmdkPath { get; private set; } = null!;


        /// <summary>
        /// Create a VirtualDisk resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public VirtualDisk(string name, VirtualDiskArgs args, CustomResourceOptions? options = null)
            : base("vsphere:index/virtualDisk:VirtualDisk", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private VirtualDisk(string name, Input<string> id, VirtualDiskState? state = null, CustomResourceOptions? options = null)
            : base("vsphere:index/virtualDisk:VirtualDisk", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing VirtualDisk resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static VirtualDisk Get(string name, Input<string> id, VirtualDiskState? state = null, CustomResourceOptions? options = null)
        {
            return new VirtualDisk(name, id, state, options);
        }
    }

    public sealed class VirtualDiskArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The adapter type for this virtual disk. Can be
        /// one of `ide`, `lsiLogic`, or `busLogic`.  Default: `lsiLogic`.
        /// </summary>
        [Input("adapterType")]
        public Input<string>? AdapterType { get; set; }

        /// <summary>
        /// Tells the resource to create any
        /// directories that are a part of the `vmdk_path` parameter if they are missing.
        /// Default: `false`.
        /// </summary>
        [Input("createDirectories")]
        public Input<bool>? CreateDirectories { get; set; }

        /// <summary>
        /// The name of the datacenter in which to create the
        /// disk. Can be omitted when when ESXi or if there is only one datacenter in
        /// your infrastructure.
        /// </summary>
        [Input("datacenter")]
        public Input<string>? Datacenter { get; set; }

        /// <summary>
        /// The name of the datastore in which to create the
        /// disk.
        /// </summary>
        [Input("datastore", required: true)]
        public Input<string> Datastore { get; set; } = null!;

        /// <summary>
        /// Size of the disk (in GB).
        /// </summary>
        [Input("size", required: true)]
        public Input<int> Size { get; set; } = null!;

        /// <summary>
        /// The type of disk to create. Can be one of
        /// `eagerZeroedThick`, `lazy`, or `thin`. Default: `eagerZeroedThick`. For
        /// information on what each kind of disk provisioning policy means, click
        /// [here][docs-vmware-vm-disk-provisioning].
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        /// <summary>
        /// The path, including filename, of the virtual disk to
        /// be created.  This needs to end in `.vmdk`.
        /// </summary>
        [Input("vmdkPath", required: true)]
        public Input<string> VmdkPath { get; set; } = null!;

        public VirtualDiskArgs()
        {
        }
    }

    public sealed class VirtualDiskState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The adapter type for this virtual disk. Can be
        /// one of `ide`, `lsiLogic`, or `busLogic`.  Default: `lsiLogic`.
        /// </summary>
        [Input("adapterType")]
        public Input<string>? AdapterType { get; set; }

        /// <summary>
        /// Tells the resource to create any
        /// directories that are a part of the `vmdk_path` parameter if they are missing.
        /// Default: `false`.
        /// </summary>
        [Input("createDirectories")]
        public Input<bool>? CreateDirectories { get; set; }

        /// <summary>
        /// The name of the datacenter in which to create the
        /// disk. Can be omitted when when ESXi or if there is only one datacenter in
        /// your infrastructure.
        /// </summary>
        [Input("datacenter")]
        public Input<string>? Datacenter { get; set; }

        /// <summary>
        /// The name of the datastore in which to create the
        /// disk.
        /// </summary>
        [Input("datastore")]
        public Input<string>? Datastore { get; set; }

        /// <summary>
        /// Size of the disk (in GB).
        /// </summary>
        [Input("size")]
        public Input<int>? Size { get; set; }

        /// <summary>
        /// The type of disk to create. Can be one of
        /// `eagerZeroedThick`, `lazy`, or `thin`. Default: `eagerZeroedThick`. For
        /// information on what each kind of disk provisioning policy means, click
        /// [here][docs-vmware-vm-disk-provisioning].
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        /// <summary>
        /// The path, including filename, of the virtual disk to
        /// be created.  This needs to end in `.vmdk`.
        /// </summary>
        [Input("vmdkPath")]
        public Input<string>? VmdkPath { get; set; }

        public VirtualDiskState()
        {
        }
    }
}
