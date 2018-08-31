// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package vsphere

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// The `vsphere_virtual_machine_snapshot` resource can be used to manage snapshots
// for a virtual machine.
// 
// For more information on managing snapshots and how they work in VMware, see
// [here][ext-vm-snapshot-management].
// 
// [ext-vm-snapshot-management]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-CA948C69-7F58-4519-AEB1-739545EA94E5.html
// 
// ~> **NOTE:** A snapshot in VMware differs from traditional disk snapshots, and
// can contain the actual running state of the virtual machine, data for all disks
// that have not been set to be independent from the snapshot (including ones that
// have been attached via the [attach][docs-vsphere-virtual-machine-disk-attach]
// parameter to the `vsphere_virtual_machine` `disk` block), and even the
// configuration of the virtual machine at the time of the snapshot. Virtual
// machine, disk activity, and configuration changes post-snapshot are not
// included in the original state. Use this resource with care! Neither VMware nor
// HashiCorp recommends retaining snapshots for a extended period of time and does
// NOT recommend using them as as backup feature. For more information on the
// limitation of virtual machine snapshots, see [here][ext-vm-snap-limitations].
// 
// [docs-vsphere-virtual-machine-disk-attach]: /docs/providers/vsphere/r/virtual_machine.html#attach
// [ext-vm-snap-limitations]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-53F65726-A23B-4CF0-A7D5-48E584B88613.html
type VirtualMachineSnapshot struct {
	s *pulumi.ResourceState
}

// NewVirtualMachineSnapshot registers a new resource with the given unique name, arguments, and options.
func NewVirtualMachineSnapshot(ctx *pulumi.Context,
	name string, args *VirtualMachineSnapshotArgs, opts ...pulumi.ResourceOpt) (*VirtualMachineSnapshot, error) {
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
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["consolidate"] = nil
		inputs["description"] = nil
		inputs["memory"] = nil
		inputs["quiesce"] = nil
		inputs["removeChildren"] = nil
		inputs["snapshotName"] = nil
		inputs["virtualMachineUuid"] = nil
	} else {
		inputs["consolidate"] = args.Consolidate
		inputs["description"] = args.Description
		inputs["memory"] = args.Memory
		inputs["quiesce"] = args.Quiesce
		inputs["removeChildren"] = args.RemoveChildren
		inputs["snapshotName"] = args.SnapshotName
		inputs["virtualMachineUuid"] = args.VirtualMachineUuid
	}
	s, err := ctx.RegisterResource("vsphere:index/virtualMachineSnapshot:VirtualMachineSnapshot", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &VirtualMachineSnapshot{s: s}, nil
}

// GetVirtualMachineSnapshot gets an existing VirtualMachineSnapshot resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVirtualMachineSnapshot(ctx *pulumi.Context,
	name string, id pulumi.ID, state *VirtualMachineSnapshotState, opts ...pulumi.ResourceOpt) (*VirtualMachineSnapshot, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["consolidate"] = state.Consolidate
		inputs["description"] = state.Description
		inputs["memory"] = state.Memory
		inputs["quiesce"] = state.Quiesce
		inputs["removeChildren"] = state.RemoveChildren
		inputs["snapshotName"] = state.SnapshotName
		inputs["virtualMachineUuid"] = state.VirtualMachineUuid
	}
	s, err := ctx.ReadResource("vsphere:index/virtualMachineSnapshot:VirtualMachineSnapshot", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &VirtualMachineSnapshot{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *VirtualMachineSnapshot) URN() *pulumi.URNOutput {
	return r.s.URN
}

// ID is this resource's unique identifier assigned by its provider.
func (r *VirtualMachineSnapshot) ID() *pulumi.IDOutput {
	return r.s.ID
}

// If set to `true`, the delta disks involved in this
// snapshot will be consolidated into the parent when this resource is
// destroyed.
func (r *VirtualMachineSnapshot) Consolidate() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["consolidate"])
}

// A description for the snapshot.
func (r *VirtualMachineSnapshot) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// If set to `true`, a dump of the internal state of the
// virtual machine is included in the snapshot.
func (r *VirtualMachineSnapshot) Memory() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["memory"])
}

// If set to `true`, and the virtual machine is powered
// on when the snapshot is taken, VMware Tools is used to quiesce the file
// system in the virtual machine.
func (r *VirtualMachineSnapshot) Quiesce() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["quiesce"])
}

// If set to `true`, the entire snapshot subtree
// is removed when this resource is destroyed.
func (r *VirtualMachineSnapshot) RemoveChildren() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["removeChildren"])
}

// The name of the snapshot.
func (r *VirtualMachineSnapshot) SnapshotName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["snapshotName"])
}

// The virtual machine UUID.
func (r *VirtualMachineSnapshot) VirtualMachineUuid() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["virtualMachineUuid"])
}

// Input properties used for looking up and filtering VirtualMachineSnapshot resources.
type VirtualMachineSnapshotState struct {
	// If set to `true`, the delta disks involved in this
	// snapshot will be consolidated into the parent when this resource is
	// destroyed.
	Consolidate interface{}
	// A description for the snapshot.
	Description interface{}
	// If set to `true`, a dump of the internal state of the
	// virtual machine is included in the snapshot.
	Memory interface{}
	// If set to `true`, and the virtual machine is powered
	// on when the snapshot is taken, VMware Tools is used to quiesce the file
	// system in the virtual machine.
	Quiesce interface{}
	// If set to `true`, the entire snapshot subtree
	// is removed when this resource is destroyed.
	RemoveChildren interface{}
	// The name of the snapshot.
	SnapshotName interface{}
	// The virtual machine UUID.
	VirtualMachineUuid interface{}
}

// The set of arguments for constructing a VirtualMachineSnapshot resource.
type VirtualMachineSnapshotArgs struct {
	// If set to `true`, the delta disks involved in this
	// snapshot will be consolidated into the parent when this resource is
	// destroyed.
	Consolidate interface{}
	// A description for the snapshot.
	Description interface{}
	// If set to `true`, a dump of the internal state of the
	// virtual machine is included in the snapshot.
	Memory interface{}
	// If set to `true`, and the virtual machine is powered
	// on when the snapshot is taken, VMware Tools is used to quiesce the file
	// system in the virtual machine.
	Quiesce interface{}
	// If set to `true`, the entire snapshot subtree
	// is removed when this resource is destroyed.
	RemoveChildren interface{}
	// The name of the snapshot.
	SnapshotName interface{}
	// The virtual machine UUID.
	VirtualMachineUuid interface{}
}
