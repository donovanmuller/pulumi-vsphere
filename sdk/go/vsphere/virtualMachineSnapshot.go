// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package vsphere

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// The `.VirtualMachineSnapshot` resource can be used to manage snapshots
// for a virtual machine.
//
// For more information on managing snapshots and how they work in VMware, see
// [here][ext-vm-snapshot-management].
//
// [ext-vm-snapshot-management]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-CA948C69-7F58-4519-AEB1-739545EA94E5.html
//
// > **NOTE:** A snapshot in VMware differs from traditional disk snapshots, and
// can contain the actual running state of the virtual machine, data for all disks
// that have not been set to be independent from the snapshot (including ones that
// have been attached via the [attach][docs-vsphere-virtual-machine-disk-attach]
// parameter to the `.VirtualMachine` `disk` block), and even the
// configuration of the virtual machine at the time of the snapshot. Virtual
// machine, disk activity, and configuration changes post-snapshot are not
// included in the original state. Use this resource with care! Neither VMware nor
// HashiCorp recommends retaining snapshots for a extended period of time and does
// NOT recommend using them as as backup feature. For more information on the
// limitation of virtual machine snapshots, see [here][ext-vm-snap-limitations].
//
// [docs-vsphere-virtual-machine-disk-attach]: /docs/providers/vsphere/r/virtual_machine.html#attach
// [ext-vm-snap-limitations]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-53F65726-A23B-4CF0-A7D5-48E584B88613.html
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/r/virtual_machine_snapshot.html.markdown.
type VirtualMachineSnapshot struct {
	pulumi.CustomResourceState

	// If set to `true`, the delta disks involved in this
	// snapshot will be consolidated into the parent when this resource is
	// destroyed.
	Consolidate pulumi.BoolPtrOutput `pulumi:"consolidate"`
	// A description for the snapshot.
	Description pulumi.StringOutput `pulumi:"description"`
	// If set to `true`, a dump of the internal state of the
	// virtual machine is included in the snapshot.
	Memory pulumi.BoolOutput `pulumi:"memory"`
	// If set to `true`, and the virtual machine is powered
	// on when the snapshot is taken, VMware Tools is used to quiesce the file
	// system in the virtual machine.
	Quiesce pulumi.BoolOutput `pulumi:"quiesce"`
	// If set to `true`, the entire snapshot subtree
	// is removed when this resource is destroyed.
	RemoveChildren pulumi.BoolPtrOutput `pulumi:"removeChildren"`
	// The name of the snapshot.
	SnapshotName pulumi.StringOutput `pulumi:"snapshotName"`
	// The virtual machine UUID.
	VirtualMachineUuid pulumi.StringOutput `pulumi:"virtualMachineUuid"`
}

// NewVirtualMachineSnapshot registers a new resource with the given unique name, arguments, and options.
func NewVirtualMachineSnapshot(ctx *pulumi.Context,
	name string, args *VirtualMachineSnapshotArgs, opts ...pulumi.ResourceOption) (*VirtualMachineSnapshot, error) {
	if args == nil || args.Description == nil {
		return nil, errors.New("missing required argument 'Description'")
	}
	if args == nil || args.Memory == nil {
		return nil, errors.New("missing required argument 'Memory'")
	}
	if args == nil || args.Quiesce == nil {
		return nil, errors.New("missing required argument 'Quiesce'")
	}
	if args == nil || args.SnapshotName == nil {
		return nil, errors.New("missing required argument 'SnapshotName'")
	}
	if args == nil || args.VirtualMachineUuid == nil {
		return nil, errors.New("missing required argument 'VirtualMachineUuid'")
	}
	if args == nil {
		args = &VirtualMachineSnapshotArgs{}
	}
	var resource VirtualMachineSnapshot
	err := ctx.RegisterResource("vsphere:index/virtualMachineSnapshot:VirtualMachineSnapshot", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVirtualMachineSnapshot gets an existing VirtualMachineSnapshot resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVirtualMachineSnapshot(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VirtualMachineSnapshotState, opts ...pulumi.ResourceOption) (*VirtualMachineSnapshot, error) {
	var resource VirtualMachineSnapshot
	err := ctx.ReadResource("vsphere:index/virtualMachineSnapshot:VirtualMachineSnapshot", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VirtualMachineSnapshot resources.
type virtualMachineSnapshotState struct {
	// If set to `true`, the delta disks involved in this
	// snapshot will be consolidated into the parent when this resource is
	// destroyed.
	Consolidate *bool `pulumi:"consolidate"`
	// A description for the snapshot.
	Description *string `pulumi:"description"`
	// If set to `true`, a dump of the internal state of the
	// virtual machine is included in the snapshot.
	Memory *bool `pulumi:"memory"`
	// If set to `true`, and the virtual machine is powered
	// on when the snapshot is taken, VMware Tools is used to quiesce the file
	// system in the virtual machine.
	Quiesce *bool `pulumi:"quiesce"`
	// If set to `true`, the entire snapshot subtree
	// is removed when this resource is destroyed.
	RemoveChildren *bool `pulumi:"removeChildren"`
	// The name of the snapshot.
	SnapshotName *string `pulumi:"snapshotName"`
	// The virtual machine UUID.
	VirtualMachineUuid *string `pulumi:"virtualMachineUuid"`
}

type VirtualMachineSnapshotState struct {
	// If set to `true`, the delta disks involved in this
	// snapshot will be consolidated into the parent when this resource is
	// destroyed.
	Consolidate pulumi.BoolPtrInput
	// A description for the snapshot.
	Description pulumi.StringPtrInput
	// If set to `true`, a dump of the internal state of the
	// virtual machine is included in the snapshot.
	Memory pulumi.BoolPtrInput
	// If set to `true`, and the virtual machine is powered
	// on when the snapshot is taken, VMware Tools is used to quiesce the file
	// system in the virtual machine.
	Quiesce pulumi.BoolPtrInput
	// If set to `true`, the entire snapshot subtree
	// is removed when this resource is destroyed.
	RemoveChildren pulumi.BoolPtrInput
	// The name of the snapshot.
	SnapshotName pulumi.StringPtrInput
	// The virtual machine UUID.
	VirtualMachineUuid pulumi.StringPtrInput
}

func (VirtualMachineSnapshotState) ElementType() reflect.Type {
	return reflect.TypeOf((*virtualMachineSnapshotState)(nil)).Elem()
}

type virtualMachineSnapshotArgs struct {
	// If set to `true`, the delta disks involved in this
	// snapshot will be consolidated into the parent when this resource is
	// destroyed.
	Consolidate *bool `pulumi:"consolidate"`
	// A description for the snapshot.
	Description string `pulumi:"description"`
	// If set to `true`, a dump of the internal state of the
	// virtual machine is included in the snapshot.
	Memory bool `pulumi:"memory"`
	// If set to `true`, and the virtual machine is powered
	// on when the snapshot is taken, VMware Tools is used to quiesce the file
	// system in the virtual machine.
	Quiesce bool `pulumi:"quiesce"`
	// If set to `true`, the entire snapshot subtree
	// is removed when this resource is destroyed.
	RemoveChildren *bool `pulumi:"removeChildren"`
	// The name of the snapshot.
	SnapshotName string `pulumi:"snapshotName"`
	// The virtual machine UUID.
	VirtualMachineUuid string `pulumi:"virtualMachineUuid"`
}

// The set of arguments for constructing a VirtualMachineSnapshot resource.
type VirtualMachineSnapshotArgs struct {
	// If set to `true`, the delta disks involved in this
	// snapshot will be consolidated into the parent when this resource is
	// destroyed.
	Consolidate pulumi.BoolPtrInput
	// A description for the snapshot.
	Description pulumi.StringInput
	// If set to `true`, a dump of the internal state of the
	// virtual machine is included in the snapshot.
	Memory pulumi.BoolInput
	// If set to `true`, and the virtual machine is powered
	// on when the snapshot is taken, VMware Tools is used to quiesce the file
	// system in the virtual machine.
	Quiesce pulumi.BoolInput
	// If set to `true`, the entire snapshot subtree
	// is removed when this resource is destroyed.
	RemoveChildren pulumi.BoolPtrInput
	// The name of the snapshot.
	SnapshotName pulumi.StringInput
	// The virtual machine UUID.
	VirtualMachineUuid pulumi.StringInput
}

func (VirtualMachineSnapshotArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*virtualMachineSnapshotArgs)(nil)).Elem()
}
