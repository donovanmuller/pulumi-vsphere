// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package vsphere

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// The `.HaVmOverride` resource can be used to add an override for
// vSphere HA settings on a cluster for a specific virtual machine. With this
// resource, one can control specific HA settings so that they are different than
// the cluster default, accommodating the needs of that specific virtual machine,
// while not affecting the rest of the cluster.
//
// For more information on vSphere HA, see [this page][ref-vsphere-ha-clusters].
//
// [ref-vsphere-ha-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.avail.doc/GUID-5432CA24-14F1-44E3-87FB-61D937831CF6.html
//
// > **NOTE:** This resource requires vCenter and is not available on direct ESXi
// connections.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/r/ha_vm_override.html.markdown.
type HaVmOverride struct {
	pulumi.CustomResourceState

	// The [managed object reference
	// ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
	// resource if changed.
	ComputeClusterId pulumi.StringOutput `pulumi:"computeClusterId"`
	// Controls the action to take
	// on this virtual machine if an APD status on an affected datastore clears in
	// the middle of an APD event. Can be one of `useClusterDefault`, `none` or
	// `reset`.  Default: `useClusterDefault`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaDatastoreApdRecoveryAction pulumi.StringPtrOutput `pulumi:"haDatastoreApdRecoveryAction"`
	// Controls the action to take on this
	// virtual machine when the cluster has detected loss to all paths to a relevant
	// datastore. Can be one of `clusterDefault`, `disabled`, `warning`,
	// `restartConservative`, or `restartAggressive`.  Default: `clusterDefault`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaDatastoreApdResponse pulumi.StringPtrOutput `pulumi:"haDatastoreApdResponse"`
	// Controls the delay in minutes
	// to wait after an APD timeout event to execute the response action defined in
	// `haDatastoreApdResponse`. Use `-1` to use
	// the cluster default. Default: `-1`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaDatastoreApdResponseDelay pulumi.IntPtrOutput `pulumi:"haDatastoreApdResponseDelay"`
	// Controls the action to take on this
	// virtual machine when the cluster has detected a permanent device loss to a
	// relevant datastore. Can be one of `clusterDefault`, `disabled`, `warning`, or
	// `restartAggressive`. Default: `clusterDefault`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaDatastorePdlResponse pulumi.StringPtrOutput `pulumi:"haDatastorePdlResponse"`
	// The action to take on this virtual
	// machine when a host has detected that it has been isolated from the rest of
	// the cluster. Can be one of `clusterIsolationResponse`, `none`, `powerOff`, or
	// `shutdown`. Default: `clusterIsolationResponse`.
	HaHostIsolationResponse pulumi.StringPtrOutput `pulumi:"haHostIsolationResponse"`
	// If a heartbeat from this virtual
	// machine is not received within this configured interval, the virtual machine
	// is marked as failed. The value is in seconds. Default: `30`.
	HaVmFailureInterval pulumi.IntPtrOutput `pulumi:"haVmFailureInterval"`
	// The length of the reset window in
	// which `haVmMaximumResets` can operate. When this
	// window expires, no more resets are attempted regardless of the setting
	// configured in `haVmMaximumResets`. `-1` means no window, meaning an
	// unlimited reset time is allotted. The value is specified in seconds. Default:
	// `-1` (no window).
	HaVmMaximumFailureWindow pulumi.IntPtrOutput `pulumi:"haVmMaximumFailureWindow"`
	// The maximum number of resets that HA will
	// perform to this virtual machine when responding to a failure event. Default:
	// `3`
	HaVmMaximumResets pulumi.IntPtrOutput `pulumi:"haVmMaximumResets"`
	// The time, in seconds, that HA waits after
	// powering on this virtual machine before monitoring for heartbeats. Default:
	// `120` (2 minutes).
	HaVmMinimumUptime pulumi.IntPtrOutput `pulumi:"haVmMinimumUptime"`
	// The type of virtual machine monitoring to use
	// when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
	// `vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.
	HaVmMonitoring pulumi.StringPtrOutput `pulumi:"haVmMonitoring"`
	// Determines whether or
	// not the cluster's default settings or the VM override settings specified in
	// this resource are used for virtual machine monitoring. The default is `true`
	// (use cluster defaults) - set to `false` to have overrides take effect.
	HaVmMonitoringUseClusterDefaults pulumi.BoolPtrOutput `pulumi:"haVmMonitoringUseClusterDefaults"`
	// The restart priority for the virtual
	// machine when vSphere detects a host failure. Can be one of
	// `clusterRestartPriority`, `lowest`, `low`, `medium`, `high`, or `highest`.
	// Default: `clusterRestartPriority`.
	HaVmRestartPriority pulumi.StringPtrOutput `pulumi:"haVmRestartPriority"`
	// The maximum time, in seconds, that
	// vSphere HA will wait for this virtual machine to be ready. Use `-1` to
	// specify the cluster default.  Default: `-1`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaVmRestartTimeout pulumi.IntPtrOutput `pulumi:"haVmRestartTimeout"`
	// The UUID of the virtual machine to create
	// the override for.  Forces a new resource if changed.
	VirtualMachineId pulumi.StringOutput `pulumi:"virtualMachineId"`
}

// NewHaVmOverride registers a new resource with the given unique name, arguments, and options.
func NewHaVmOverride(ctx *pulumi.Context,
	name string, args *HaVmOverrideArgs, opts ...pulumi.ResourceOption) (*HaVmOverride, error) {
	if args == nil || args.ComputeClusterId == nil {
		return nil, errors.New("missing required argument 'ComputeClusterId'")
	}
	if args == nil || args.VirtualMachineId == nil {
		return nil, errors.New("missing required argument 'VirtualMachineId'")
	}
	if args == nil {
		args = &HaVmOverrideArgs{}
	}
	var resource HaVmOverride
	err := ctx.RegisterResource("vsphere:index/haVmOverride:HaVmOverride", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetHaVmOverride gets an existing HaVmOverride resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetHaVmOverride(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *HaVmOverrideState, opts ...pulumi.ResourceOption) (*HaVmOverride, error) {
	var resource HaVmOverride
	err := ctx.ReadResource("vsphere:index/haVmOverride:HaVmOverride", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering HaVmOverride resources.
type haVmOverrideState struct {
	// The [managed object reference
	// ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
	// resource if changed.
	ComputeClusterId *string `pulumi:"computeClusterId"`
	// Controls the action to take
	// on this virtual machine if an APD status on an affected datastore clears in
	// the middle of an APD event. Can be one of `useClusterDefault`, `none` or
	// `reset`.  Default: `useClusterDefault`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaDatastoreApdRecoveryAction *string `pulumi:"haDatastoreApdRecoveryAction"`
	// Controls the action to take on this
	// virtual machine when the cluster has detected loss to all paths to a relevant
	// datastore. Can be one of `clusterDefault`, `disabled`, `warning`,
	// `restartConservative`, or `restartAggressive`.  Default: `clusterDefault`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaDatastoreApdResponse *string `pulumi:"haDatastoreApdResponse"`
	// Controls the delay in minutes
	// to wait after an APD timeout event to execute the response action defined in
	// `haDatastoreApdResponse`. Use `-1` to use
	// the cluster default. Default: `-1`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaDatastoreApdResponseDelay *int `pulumi:"haDatastoreApdResponseDelay"`
	// Controls the action to take on this
	// virtual machine when the cluster has detected a permanent device loss to a
	// relevant datastore. Can be one of `clusterDefault`, `disabled`, `warning`, or
	// `restartAggressive`. Default: `clusterDefault`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaDatastorePdlResponse *string `pulumi:"haDatastorePdlResponse"`
	// The action to take on this virtual
	// machine when a host has detected that it has been isolated from the rest of
	// the cluster. Can be one of `clusterIsolationResponse`, `none`, `powerOff`, or
	// `shutdown`. Default: `clusterIsolationResponse`.
	HaHostIsolationResponse *string `pulumi:"haHostIsolationResponse"`
	// If a heartbeat from this virtual
	// machine is not received within this configured interval, the virtual machine
	// is marked as failed. The value is in seconds. Default: `30`.
	HaVmFailureInterval *int `pulumi:"haVmFailureInterval"`
	// The length of the reset window in
	// which `haVmMaximumResets` can operate. When this
	// window expires, no more resets are attempted regardless of the setting
	// configured in `haVmMaximumResets`. `-1` means no window, meaning an
	// unlimited reset time is allotted. The value is specified in seconds. Default:
	// `-1` (no window).
	HaVmMaximumFailureWindow *int `pulumi:"haVmMaximumFailureWindow"`
	// The maximum number of resets that HA will
	// perform to this virtual machine when responding to a failure event. Default:
	// `3`
	HaVmMaximumResets *int `pulumi:"haVmMaximumResets"`
	// The time, in seconds, that HA waits after
	// powering on this virtual machine before monitoring for heartbeats. Default:
	// `120` (2 minutes).
	HaVmMinimumUptime *int `pulumi:"haVmMinimumUptime"`
	// The type of virtual machine monitoring to use
	// when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
	// `vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.
	HaVmMonitoring *string `pulumi:"haVmMonitoring"`
	// Determines whether or
	// not the cluster's default settings or the VM override settings specified in
	// this resource are used for virtual machine monitoring. The default is `true`
	// (use cluster defaults) - set to `false` to have overrides take effect.
	HaVmMonitoringUseClusterDefaults *bool `pulumi:"haVmMonitoringUseClusterDefaults"`
	// The restart priority for the virtual
	// machine when vSphere detects a host failure. Can be one of
	// `clusterRestartPriority`, `lowest`, `low`, `medium`, `high`, or `highest`.
	// Default: `clusterRestartPriority`.
	HaVmRestartPriority *string `pulumi:"haVmRestartPriority"`
	// The maximum time, in seconds, that
	// vSphere HA will wait for this virtual machine to be ready. Use `-1` to
	// specify the cluster default.  Default: `-1`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaVmRestartTimeout *int `pulumi:"haVmRestartTimeout"`
	// The UUID of the virtual machine to create
	// the override for.  Forces a new resource if changed.
	VirtualMachineId *string `pulumi:"virtualMachineId"`
}

type HaVmOverrideState struct {
	// The [managed object reference
	// ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
	// resource if changed.
	ComputeClusterId pulumi.StringPtrInput
	// Controls the action to take
	// on this virtual machine if an APD status on an affected datastore clears in
	// the middle of an APD event. Can be one of `useClusterDefault`, `none` or
	// `reset`.  Default: `useClusterDefault`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaDatastoreApdRecoveryAction pulumi.StringPtrInput
	// Controls the action to take on this
	// virtual machine when the cluster has detected loss to all paths to a relevant
	// datastore. Can be one of `clusterDefault`, `disabled`, `warning`,
	// `restartConservative`, or `restartAggressive`.  Default: `clusterDefault`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaDatastoreApdResponse pulumi.StringPtrInput
	// Controls the delay in minutes
	// to wait after an APD timeout event to execute the response action defined in
	// `haDatastoreApdResponse`. Use `-1` to use
	// the cluster default. Default: `-1`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaDatastoreApdResponseDelay pulumi.IntPtrInput
	// Controls the action to take on this
	// virtual machine when the cluster has detected a permanent device loss to a
	// relevant datastore. Can be one of `clusterDefault`, `disabled`, `warning`, or
	// `restartAggressive`. Default: `clusterDefault`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaDatastorePdlResponse pulumi.StringPtrInput
	// The action to take on this virtual
	// machine when a host has detected that it has been isolated from the rest of
	// the cluster. Can be one of `clusterIsolationResponse`, `none`, `powerOff`, or
	// `shutdown`. Default: `clusterIsolationResponse`.
	HaHostIsolationResponse pulumi.StringPtrInput
	// If a heartbeat from this virtual
	// machine is not received within this configured interval, the virtual machine
	// is marked as failed. The value is in seconds. Default: `30`.
	HaVmFailureInterval pulumi.IntPtrInput
	// The length of the reset window in
	// which `haVmMaximumResets` can operate. When this
	// window expires, no more resets are attempted regardless of the setting
	// configured in `haVmMaximumResets`. `-1` means no window, meaning an
	// unlimited reset time is allotted. The value is specified in seconds. Default:
	// `-1` (no window).
	HaVmMaximumFailureWindow pulumi.IntPtrInput
	// The maximum number of resets that HA will
	// perform to this virtual machine when responding to a failure event. Default:
	// `3`
	HaVmMaximumResets pulumi.IntPtrInput
	// The time, in seconds, that HA waits after
	// powering on this virtual machine before monitoring for heartbeats. Default:
	// `120` (2 minutes).
	HaVmMinimumUptime pulumi.IntPtrInput
	// The type of virtual machine monitoring to use
	// when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
	// `vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.
	HaVmMonitoring pulumi.StringPtrInput
	// Determines whether or
	// not the cluster's default settings or the VM override settings specified in
	// this resource are used for virtual machine monitoring. The default is `true`
	// (use cluster defaults) - set to `false` to have overrides take effect.
	HaVmMonitoringUseClusterDefaults pulumi.BoolPtrInput
	// The restart priority for the virtual
	// machine when vSphere detects a host failure. Can be one of
	// `clusterRestartPriority`, `lowest`, `low`, `medium`, `high`, or `highest`.
	// Default: `clusterRestartPriority`.
	HaVmRestartPriority pulumi.StringPtrInput
	// The maximum time, in seconds, that
	// vSphere HA will wait for this virtual machine to be ready. Use `-1` to
	// specify the cluster default.  Default: `-1`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaVmRestartTimeout pulumi.IntPtrInput
	// The UUID of the virtual machine to create
	// the override for.  Forces a new resource if changed.
	VirtualMachineId pulumi.StringPtrInput
}

func (HaVmOverrideState) ElementType() reflect.Type {
	return reflect.TypeOf((*haVmOverrideState)(nil)).Elem()
}

type haVmOverrideArgs struct {
	// The [managed object reference
	// ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
	// resource if changed.
	ComputeClusterId string `pulumi:"computeClusterId"`
	// Controls the action to take
	// on this virtual machine if an APD status on an affected datastore clears in
	// the middle of an APD event. Can be one of `useClusterDefault`, `none` or
	// `reset`.  Default: `useClusterDefault`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaDatastoreApdRecoveryAction *string `pulumi:"haDatastoreApdRecoveryAction"`
	// Controls the action to take on this
	// virtual machine when the cluster has detected loss to all paths to a relevant
	// datastore. Can be one of `clusterDefault`, `disabled`, `warning`,
	// `restartConservative`, or `restartAggressive`.  Default: `clusterDefault`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaDatastoreApdResponse *string `pulumi:"haDatastoreApdResponse"`
	// Controls the delay in minutes
	// to wait after an APD timeout event to execute the response action defined in
	// `haDatastoreApdResponse`. Use `-1` to use
	// the cluster default. Default: `-1`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaDatastoreApdResponseDelay *int `pulumi:"haDatastoreApdResponseDelay"`
	// Controls the action to take on this
	// virtual machine when the cluster has detected a permanent device loss to a
	// relevant datastore. Can be one of `clusterDefault`, `disabled`, `warning`, or
	// `restartAggressive`. Default: `clusterDefault`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaDatastorePdlResponse *string `pulumi:"haDatastorePdlResponse"`
	// The action to take on this virtual
	// machine when a host has detected that it has been isolated from the rest of
	// the cluster. Can be one of `clusterIsolationResponse`, `none`, `powerOff`, or
	// `shutdown`. Default: `clusterIsolationResponse`.
	HaHostIsolationResponse *string `pulumi:"haHostIsolationResponse"`
	// If a heartbeat from this virtual
	// machine is not received within this configured interval, the virtual machine
	// is marked as failed. The value is in seconds. Default: `30`.
	HaVmFailureInterval *int `pulumi:"haVmFailureInterval"`
	// The length of the reset window in
	// which `haVmMaximumResets` can operate. When this
	// window expires, no more resets are attempted regardless of the setting
	// configured in `haVmMaximumResets`. `-1` means no window, meaning an
	// unlimited reset time is allotted. The value is specified in seconds. Default:
	// `-1` (no window).
	HaVmMaximumFailureWindow *int `pulumi:"haVmMaximumFailureWindow"`
	// The maximum number of resets that HA will
	// perform to this virtual machine when responding to a failure event. Default:
	// `3`
	HaVmMaximumResets *int `pulumi:"haVmMaximumResets"`
	// The time, in seconds, that HA waits after
	// powering on this virtual machine before monitoring for heartbeats. Default:
	// `120` (2 minutes).
	HaVmMinimumUptime *int `pulumi:"haVmMinimumUptime"`
	// The type of virtual machine monitoring to use
	// when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
	// `vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.
	HaVmMonitoring *string `pulumi:"haVmMonitoring"`
	// Determines whether or
	// not the cluster's default settings or the VM override settings specified in
	// this resource are used for virtual machine monitoring. The default is `true`
	// (use cluster defaults) - set to `false` to have overrides take effect.
	HaVmMonitoringUseClusterDefaults *bool `pulumi:"haVmMonitoringUseClusterDefaults"`
	// The restart priority for the virtual
	// machine when vSphere detects a host failure. Can be one of
	// `clusterRestartPriority`, `lowest`, `low`, `medium`, `high`, or `highest`.
	// Default: `clusterRestartPriority`.
	HaVmRestartPriority *string `pulumi:"haVmRestartPriority"`
	// The maximum time, in seconds, that
	// vSphere HA will wait for this virtual machine to be ready. Use `-1` to
	// specify the cluster default.  Default: `-1`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaVmRestartTimeout *int `pulumi:"haVmRestartTimeout"`
	// The UUID of the virtual machine to create
	// the override for.  Forces a new resource if changed.
	VirtualMachineId string `pulumi:"virtualMachineId"`
}

// The set of arguments for constructing a HaVmOverride resource.
type HaVmOverrideArgs struct {
	// The [managed object reference
	// ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
	// resource if changed.
	ComputeClusterId pulumi.StringInput
	// Controls the action to take
	// on this virtual machine if an APD status on an affected datastore clears in
	// the middle of an APD event. Can be one of `useClusterDefault`, `none` or
	// `reset`.  Default: `useClusterDefault`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaDatastoreApdRecoveryAction pulumi.StringPtrInput
	// Controls the action to take on this
	// virtual machine when the cluster has detected loss to all paths to a relevant
	// datastore. Can be one of `clusterDefault`, `disabled`, `warning`,
	// `restartConservative`, or `restartAggressive`.  Default: `clusterDefault`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaDatastoreApdResponse pulumi.StringPtrInput
	// Controls the delay in minutes
	// to wait after an APD timeout event to execute the response action defined in
	// `haDatastoreApdResponse`. Use `-1` to use
	// the cluster default. Default: `-1`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaDatastoreApdResponseDelay pulumi.IntPtrInput
	// Controls the action to take on this
	// virtual machine when the cluster has detected a permanent device loss to a
	// relevant datastore. Can be one of `clusterDefault`, `disabled`, `warning`, or
	// `restartAggressive`. Default: `clusterDefault`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaDatastorePdlResponse pulumi.StringPtrInput
	// The action to take on this virtual
	// machine when a host has detected that it has been isolated from the rest of
	// the cluster. Can be one of `clusterIsolationResponse`, `none`, `powerOff`, or
	// `shutdown`. Default: `clusterIsolationResponse`.
	HaHostIsolationResponse pulumi.StringPtrInput
	// If a heartbeat from this virtual
	// machine is not received within this configured interval, the virtual machine
	// is marked as failed. The value is in seconds. Default: `30`.
	HaVmFailureInterval pulumi.IntPtrInput
	// The length of the reset window in
	// which `haVmMaximumResets` can operate. When this
	// window expires, no more resets are attempted regardless of the setting
	// configured in `haVmMaximumResets`. `-1` means no window, meaning an
	// unlimited reset time is allotted. The value is specified in seconds. Default:
	// `-1` (no window).
	HaVmMaximumFailureWindow pulumi.IntPtrInput
	// The maximum number of resets that HA will
	// perform to this virtual machine when responding to a failure event. Default:
	// `3`
	HaVmMaximumResets pulumi.IntPtrInput
	// The time, in seconds, that HA waits after
	// powering on this virtual machine before monitoring for heartbeats. Default:
	// `120` (2 minutes).
	HaVmMinimumUptime pulumi.IntPtrInput
	// The type of virtual machine monitoring to use
	// when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
	// `vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.
	HaVmMonitoring pulumi.StringPtrInput
	// Determines whether or
	// not the cluster's default settings or the VM override settings specified in
	// this resource are used for virtual machine monitoring. The default is `true`
	// (use cluster defaults) - set to `false` to have overrides take effect.
	HaVmMonitoringUseClusterDefaults pulumi.BoolPtrInput
	// The restart priority for the virtual
	// machine when vSphere detects a host failure. Can be one of
	// `clusterRestartPriority`, `lowest`, `low`, `medium`, `high`, or `highest`.
	// Default: `clusterRestartPriority`.
	HaVmRestartPriority pulumi.StringPtrInput
	// The maximum time, in seconds, that
	// vSphere HA will wait for this virtual machine to be ready. Use `-1` to
	// specify the cluster default.  Default: `-1`.
	// <sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
	HaVmRestartTimeout pulumi.IntPtrInput
	// The UUID of the virtual machine to create
	// the override for.  Forces a new resource if changed.
	VirtualMachineId pulumi.StringInput
}

func (HaVmOverrideArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*haVmOverrideArgs)(nil)).Elem()
}
