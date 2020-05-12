// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.VSphere
{
    /// <summary>
    /// The `vsphere..HaVmOverride` resource can be used to add an override for
    /// vSphere HA settings on a cluster for a specific virtual machine. With this
    /// resource, one can control specific HA settings so that they are different than
    /// the cluster default, accommodating the needs of that specific virtual machine,
    /// while not affecting the rest of the cluster.
    /// 
    /// For more information on vSphere HA, see [this page][ref-vsphere-ha-clusters].
    /// 
    /// [ref-vsphere-ha-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.avail.doc/GUID-5432CA24-14F1-44E3-87FB-61D937831CF6.html
    /// 
    /// &gt; **NOTE:** This resource requires vCenter and is not available on direct ESXi
    /// connections.
    /// </summary>
    public partial class HaVmOverride : Pulumi.CustomResource
    {
        /// <summary>
        /// The managed object reference
        /// ID of the cluster to put the override in.  Forces a new
        /// resource if changed.
        /// </summary>
        [Output("computeClusterId")]
        public Output<string> ComputeClusterId { get; private set; } = null!;

        /// <summary>
        /// Controls the action to take
        /// on this virtual machine if an APD status on an affected datastore clears in
        /// the middle of an APD event. Can be one of `useClusterDefault`, `none` or
        /// `reset`.  Default: `useClusterDefault`.
        /// </summary>
        [Output("haDatastoreApdRecoveryAction")]
        public Output<string?> HaDatastoreApdRecoveryAction { get; private set; } = null!;

        /// <summary>
        /// Controls the action to take on this
        /// virtual machine when the cluster has detected loss to all paths to a relevant
        /// datastore. Can be one of `clusterDefault`, `disabled`, `warning`,
        /// `restartConservative`, or `restartAggressive`.  Default: `clusterDefault`.
        /// </summary>
        [Output("haDatastoreApdResponse")]
        public Output<string?> HaDatastoreApdResponse { get; private set; } = null!;

        /// <summary>
        /// Controls the delay in minutes
        /// to wait after an APD timeout event to execute the response action defined in
        /// `ha_datastore_apd_response`. Use `-1` to use
        /// the cluster default. Default: `-1`.
        /// </summary>
        [Output("haDatastoreApdResponseDelay")]
        public Output<int?> HaDatastoreApdResponseDelay { get; private set; } = null!;

        /// <summary>
        /// Controls the action to take on this
        /// virtual machine when the cluster has detected a permanent device loss to a
        /// relevant datastore. Can be one of `clusterDefault`, `disabled`, `warning`, or
        /// `restartAggressive`. Default: `clusterDefault`.
        /// </summary>
        [Output("haDatastorePdlResponse")]
        public Output<string?> HaDatastorePdlResponse { get; private set; } = null!;

        /// <summary>
        /// The action to take on this virtual
        /// machine when a host has detected that it has been isolated from the rest of
        /// the cluster. Can be one of `clusterIsolationResponse`, `none`, `powerOff`, or
        /// `shutdown`. Default: `clusterIsolationResponse`.
        /// </summary>
        [Output("haHostIsolationResponse")]
        public Output<string?> HaHostIsolationResponse { get; private set; } = null!;

        /// <summary>
        /// If a heartbeat from this virtual
        /// machine is not received within this configured interval, the virtual machine
        /// is marked as failed. The value is in seconds. Default: `30`.
        /// </summary>
        [Output("haVmFailureInterval")]
        public Output<int?> HaVmFailureInterval { get; private set; } = null!;

        /// <summary>
        /// The length of the reset window in
        /// which `ha_vm_maximum_resets` can operate. When this
        /// window expires, no more resets are attempted regardless of the setting
        /// configured in `ha_vm_maximum_resets`. `-1` means no window, meaning an
        /// unlimited reset time is allotted. The value is specified in seconds. Default:
        /// `-1` (no window).
        /// </summary>
        [Output("haVmMaximumFailureWindow")]
        public Output<int?> HaVmMaximumFailureWindow { get; private set; } = null!;

        /// <summary>
        /// The maximum number of resets that HA will
        /// perform to this virtual machine when responding to a failure event. Default:
        /// `3`
        /// </summary>
        [Output("haVmMaximumResets")]
        public Output<int?> HaVmMaximumResets { get; private set; } = null!;

        /// <summary>
        /// The time, in seconds, that HA waits after
        /// powering on this virtual machine before monitoring for heartbeats. Default:
        /// `120` (2 minutes).
        /// </summary>
        [Output("haVmMinimumUptime")]
        public Output<int?> HaVmMinimumUptime { get; private set; } = null!;

        /// <summary>
        /// The type of virtual machine monitoring to use
        /// when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
        /// `vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.
        /// </summary>
        [Output("haVmMonitoring")]
        public Output<string?> HaVmMonitoring { get; private set; } = null!;

        /// <summary>
        /// Determines whether or
        /// not the cluster's default settings or the VM override settings specified in
        /// this resource are used for virtual machine monitoring. The default is `true`
        /// (use cluster defaults) - set to `false` to have overrides take effect.
        /// </summary>
        [Output("haVmMonitoringUseClusterDefaults")]
        public Output<bool?> HaVmMonitoringUseClusterDefaults { get; private set; } = null!;

        /// <summary>
        /// The restart priority for the virtual
        /// machine when vSphere detects a host failure. Can be one of
        /// `clusterRestartPriority`, `lowest`, `low`, `medium`, `high`, or `highest`.
        /// Default: `clusterRestartPriority`.
        /// </summary>
        [Output("haVmRestartPriority")]
        public Output<string?> HaVmRestartPriority { get; private set; } = null!;

        /// <summary>
        /// The maximum time, in seconds, that
        /// vSphere HA will wait for this virtual machine to be ready. Use `-1` to
        /// specify the cluster default.  Default: `-1`.
        /// </summary>
        [Output("haVmRestartTimeout")]
        public Output<int?> HaVmRestartTimeout { get; private set; } = null!;

        /// <summary>
        /// The UUID of the virtual machine to create
        /// the override for.  Forces a new resource if changed.
        /// </summary>
        [Output("virtualMachineId")]
        public Output<string> VirtualMachineId { get; private set; } = null!;


        /// <summary>
        /// Create a HaVmOverride resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public HaVmOverride(string name, HaVmOverrideArgs args, CustomResourceOptions? options = null)
            : base("vsphere:index/haVmOverride:HaVmOverride", name, args ?? new HaVmOverrideArgs(), MakeResourceOptions(options, ""))
        {
        }

        private HaVmOverride(string name, Input<string> id, HaVmOverrideState? state = null, CustomResourceOptions? options = null)
            : base("vsphere:index/haVmOverride:HaVmOverride", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing HaVmOverride resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static HaVmOverride Get(string name, Input<string> id, HaVmOverrideState? state = null, CustomResourceOptions? options = null)
        {
            return new HaVmOverride(name, id, state, options);
        }
    }

    public sealed class HaVmOverrideArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The managed object reference
        /// ID of the cluster to put the override in.  Forces a new
        /// resource if changed.
        /// </summary>
        [Input("computeClusterId", required: true)]
        public Input<string> ComputeClusterId { get; set; } = null!;

        /// <summary>
        /// Controls the action to take
        /// on this virtual machine if an APD status on an affected datastore clears in
        /// the middle of an APD event. Can be one of `useClusterDefault`, `none` or
        /// `reset`.  Default: `useClusterDefault`.
        /// </summary>
        [Input("haDatastoreApdRecoveryAction")]
        public Input<string>? HaDatastoreApdRecoveryAction { get; set; }

        /// <summary>
        /// Controls the action to take on this
        /// virtual machine when the cluster has detected loss to all paths to a relevant
        /// datastore. Can be one of `clusterDefault`, `disabled`, `warning`,
        /// `restartConservative`, or `restartAggressive`.  Default: `clusterDefault`.
        /// </summary>
        [Input("haDatastoreApdResponse")]
        public Input<string>? HaDatastoreApdResponse { get; set; }

        /// <summary>
        /// Controls the delay in minutes
        /// to wait after an APD timeout event to execute the response action defined in
        /// `ha_datastore_apd_response`. Use `-1` to use
        /// the cluster default. Default: `-1`.
        /// </summary>
        [Input("haDatastoreApdResponseDelay")]
        public Input<int>? HaDatastoreApdResponseDelay { get; set; }

        /// <summary>
        /// Controls the action to take on this
        /// virtual machine when the cluster has detected a permanent device loss to a
        /// relevant datastore. Can be one of `clusterDefault`, `disabled`, `warning`, or
        /// `restartAggressive`. Default: `clusterDefault`.
        /// </summary>
        [Input("haDatastorePdlResponse")]
        public Input<string>? HaDatastorePdlResponse { get; set; }

        /// <summary>
        /// The action to take on this virtual
        /// machine when a host has detected that it has been isolated from the rest of
        /// the cluster. Can be one of `clusterIsolationResponse`, `none`, `powerOff`, or
        /// `shutdown`. Default: `clusterIsolationResponse`.
        /// </summary>
        [Input("haHostIsolationResponse")]
        public Input<string>? HaHostIsolationResponse { get; set; }

        /// <summary>
        /// If a heartbeat from this virtual
        /// machine is not received within this configured interval, the virtual machine
        /// is marked as failed. The value is in seconds. Default: `30`.
        /// </summary>
        [Input("haVmFailureInterval")]
        public Input<int>? HaVmFailureInterval { get; set; }

        /// <summary>
        /// The length of the reset window in
        /// which `ha_vm_maximum_resets` can operate. When this
        /// window expires, no more resets are attempted regardless of the setting
        /// configured in `ha_vm_maximum_resets`. `-1` means no window, meaning an
        /// unlimited reset time is allotted. The value is specified in seconds. Default:
        /// `-1` (no window).
        /// </summary>
        [Input("haVmMaximumFailureWindow")]
        public Input<int>? HaVmMaximumFailureWindow { get; set; }

        /// <summary>
        /// The maximum number of resets that HA will
        /// perform to this virtual machine when responding to a failure event. Default:
        /// `3`
        /// </summary>
        [Input("haVmMaximumResets")]
        public Input<int>? HaVmMaximumResets { get; set; }

        /// <summary>
        /// The time, in seconds, that HA waits after
        /// powering on this virtual machine before monitoring for heartbeats. Default:
        /// `120` (2 minutes).
        /// </summary>
        [Input("haVmMinimumUptime")]
        public Input<int>? HaVmMinimumUptime { get; set; }

        /// <summary>
        /// The type of virtual machine monitoring to use
        /// when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
        /// `vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.
        /// </summary>
        [Input("haVmMonitoring")]
        public Input<string>? HaVmMonitoring { get; set; }

        /// <summary>
        /// Determines whether or
        /// not the cluster's default settings or the VM override settings specified in
        /// this resource are used for virtual machine monitoring. The default is `true`
        /// (use cluster defaults) - set to `false` to have overrides take effect.
        /// </summary>
        [Input("haVmMonitoringUseClusterDefaults")]
        public Input<bool>? HaVmMonitoringUseClusterDefaults { get; set; }

        /// <summary>
        /// The restart priority for the virtual
        /// machine when vSphere detects a host failure. Can be one of
        /// `clusterRestartPriority`, `lowest`, `low`, `medium`, `high`, or `highest`.
        /// Default: `clusterRestartPriority`.
        /// </summary>
        [Input("haVmRestartPriority")]
        public Input<string>? HaVmRestartPriority { get; set; }

        /// <summary>
        /// The maximum time, in seconds, that
        /// vSphere HA will wait for this virtual machine to be ready. Use `-1` to
        /// specify the cluster default.  Default: `-1`.
        /// </summary>
        [Input("haVmRestartTimeout")]
        public Input<int>? HaVmRestartTimeout { get; set; }

        /// <summary>
        /// The UUID of the virtual machine to create
        /// the override for.  Forces a new resource if changed.
        /// </summary>
        [Input("virtualMachineId", required: true)]
        public Input<string> VirtualMachineId { get; set; } = null!;

        public HaVmOverrideArgs()
        {
        }
    }

    public sealed class HaVmOverrideState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The managed object reference
        /// ID of the cluster to put the override in.  Forces a new
        /// resource if changed.
        /// </summary>
        [Input("computeClusterId")]
        public Input<string>? ComputeClusterId { get; set; }

        /// <summary>
        /// Controls the action to take
        /// on this virtual machine if an APD status on an affected datastore clears in
        /// the middle of an APD event. Can be one of `useClusterDefault`, `none` or
        /// `reset`.  Default: `useClusterDefault`.
        /// </summary>
        [Input("haDatastoreApdRecoveryAction")]
        public Input<string>? HaDatastoreApdRecoveryAction { get; set; }

        /// <summary>
        /// Controls the action to take on this
        /// virtual machine when the cluster has detected loss to all paths to a relevant
        /// datastore. Can be one of `clusterDefault`, `disabled`, `warning`,
        /// `restartConservative`, or `restartAggressive`.  Default: `clusterDefault`.
        /// </summary>
        [Input("haDatastoreApdResponse")]
        public Input<string>? HaDatastoreApdResponse { get; set; }

        /// <summary>
        /// Controls the delay in minutes
        /// to wait after an APD timeout event to execute the response action defined in
        /// `ha_datastore_apd_response`. Use `-1` to use
        /// the cluster default. Default: `-1`.
        /// </summary>
        [Input("haDatastoreApdResponseDelay")]
        public Input<int>? HaDatastoreApdResponseDelay { get; set; }

        /// <summary>
        /// Controls the action to take on this
        /// virtual machine when the cluster has detected a permanent device loss to a
        /// relevant datastore. Can be one of `clusterDefault`, `disabled`, `warning`, or
        /// `restartAggressive`. Default: `clusterDefault`.
        /// </summary>
        [Input("haDatastorePdlResponse")]
        public Input<string>? HaDatastorePdlResponse { get; set; }

        /// <summary>
        /// The action to take on this virtual
        /// machine when a host has detected that it has been isolated from the rest of
        /// the cluster. Can be one of `clusterIsolationResponse`, `none`, `powerOff`, or
        /// `shutdown`. Default: `clusterIsolationResponse`.
        /// </summary>
        [Input("haHostIsolationResponse")]
        public Input<string>? HaHostIsolationResponse { get; set; }

        /// <summary>
        /// If a heartbeat from this virtual
        /// machine is not received within this configured interval, the virtual machine
        /// is marked as failed. The value is in seconds. Default: `30`.
        /// </summary>
        [Input("haVmFailureInterval")]
        public Input<int>? HaVmFailureInterval { get; set; }

        /// <summary>
        /// The length of the reset window in
        /// which `ha_vm_maximum_resets` can operate. When this
        /// window expires, no more resets are attempted regardless of the setting
        /// configured in `ha_vm_maximum_resets`. `-1` means no window, meaning an
        /// unlimited reset time is allotted. The value is specified in seconds. Default:
        /// `-1` (no window).
        /// </summary>
        [Input("haVmMaximumFailureWindow")]
        public Input<int>? HaVmMaximumFailureWindow { get; set; }

        /// <summary>
        /// The maximum number of resets that HA will
        /// perform to this virtual machine when responding to a failure event. Default:
        /// `3`
        /// </summary>
        [Input("haVmMaximumResets")]
        public Input<int>? HaVmMaximumResets { get; set; }

        /// <summary>
        /// The time, in seconds, that HA waits after
        /// powering on this virtual machine before monitoring for heartbeats. Default:
        /// `120` (2 minutes).
        /// </summary>
        [Input("haVmMinimumUptime")]
        public Input<int>? HaVmMinimumUptime { get; set; }

        /// <summary>
        /// The type of virtual machine monitoring to use
        /// when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
        /// `vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.
        /// </summary>
        [Input("haVmMonitoring")]
        public Input<string>? HaVmMonitoring { get; set; }

        /// <summary>
        /// Determines whether or
        /// not the cluster's default settings or the VM override settings specified in
        /// this resource are used for virtual machine monitoring. The default is `true`
        /// (use cluster defaults) - set to `false` to have overrides take effect.
        /// </summary>
        [Input("haVmMonitoringUseClusterDefaults")]
        public Input<bool>? HaVmMonitoringUseClusterDefaults { get; set; }

        /// <summary>
        /// The restart priority for the virtual
        /// machine when vSphere detects a host failure. Can be one of
        /// `clusterRestartPriority`, `lowest`, `low`, `medium`, `high`, or `highest`.
        /// Default: `clusterRestartPriority`.
        /// </summary>
        [Input("haVmRestartPriority")]
        public Input<string>? HaVmRestartPriority { get; set; }

        /// <summary>
        /// The maximum time, in seconds, that
        /// vSphere HA will wait for this virtual machine to be ready. Use `-1` to
        /// specify the cluster default.  Default: `-1`.
        /// </summary>
        [Input("haVmRestartTimeout")]
        public Input<int>? HaVmRestartTimeout { get; set; }

        /// <summary>
        /// The UUID of the virtual machine to create
        /// the override for.  Forces a new resource if changed.
        /// </summary>
        [Input("virtualMachineId")]
        public Input<string>? VirtualMachineId { get; set; }

        public HaVmOverrideState()
        {
        }
    }
}
