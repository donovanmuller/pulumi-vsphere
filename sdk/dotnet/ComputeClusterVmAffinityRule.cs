// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Vsphere
{
    /// <summary>
    /// The `vsphere..ComputeClusterVmAffinityRule` resource can be used to manage
    /// VM affinity rules in a cluster, either created by the
    /// [`vsphere..ComputeCluster`][tf-vsphere-cluster-resource] resource or looked up
    /// by the [`vsphere..ComputeCluster`][tf-vsphere-cluster-data-source] data source.
    /// 
    /// [tf-vsphere-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
    /// [tf-vsphere-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html
    /// 
    /// This rule can be used to tell a set to virtual machines to run together on a
    /// single host within a cluster. When configured, DRS will make a best effort to
    /// ensure that the virtual machines run on the same host, or prevent any operation
    /// that would keep that from happening, depending on the value of the
    /// `mandatory` flag.
    /// 
    /// &gt; Keep in mind that this rule can only be used to tell VMs to run together on
    /// a _non-specific_ host - it can't be used to pin VMs to a host. For that, see
    /// the
    /// [`vsphere..ComputeClusterVmHostRule`][tf-vsphere-cluster-vm-host-rule-resource]
    /// resource.
    /// 
    /// [tf-vsphere-cluster-vm-host-rule-resource]: /docs/providers/vsphere/r/compute_cluster_vm_host_rule.html
    /// 
    /// &gt; **NOTE:** This resource requires vCenter and is not available on direct ESXi
    /// connections.
    /// 
    /// &gt; **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/r/compute_cluster_vm_affinity_rule.html.markdown.
    /// </summary>
    public partial class ComputeClusterVmAffinityRule : Pulumi.CustomResource
    {
        /// <summary>
        /// The [managed object reference
        /// ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
        /// resource if changed.
        /// </summary>
        [Output("computeClusterId")]
        public Output<string> ComputeClusterId { get; private set; } = null!;

        /// <summary>
        /// Enable this rule in the cluster. Default: `true`.
        /// </summary>
        [Output("enabled")]
        public Output<bool?> Enabled { get; private set; } = null!;

        /// <summary>
        /// When this value is `true`, prevents any virtual
        /// machine operations that may violate this rule. Default: `false`.
        /// </summary>
        [Output("mandatory")]
        public Output<bool?> Mandatory { get; private set; } = null!;

        /// <summary>
        /// The name of the rule. This must be unique in the cluster.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The UUIDs of the virtual machines to run
        /// on the same host together.
        /// </summary>
        [Output("virtualMachineIds")]
        public Output<ImmutableArray<string>> VirtualMachineIds { get; private set; } = null!;


        /// <summary>
        /// Create a ComputeClusterVmAffinityRule resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ComputeClusterVmAffinityRule(string name, ComputeClusterVmAffinityRuleArgs args, CustomResourceOptions? options = null)
            : base("vsphere:index/computeClusterVmAffinityRule:ComputeClusterVmAffinityRule", name, args, MakeResourceOptions(options, ""))
        {
        }

        private ComputeClusterVmAffinityRule(string name, Input<string> id, ComputeClusterVmAffinityRuleState? state = null, CustomResourceOptions? options = null)
            : base("vsphere:index/computeClusterVmAffinityRule:ComputeClusterVmAffinityRule", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ComputeClusterVmAffinityRule resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ComputeClusterVmAffinityRule Get(string name, Input<string> id, ComputeClusterVmAffinityRuleState? state = null, CustomResourceOptions? options = null)
        {
            return new ComputeClusterVmAffinityRule(name, id, state, options);
        }
    }

    public sealed class ComputeClusterVmAffinityRuleArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The [managed object reference
        /// ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
        /// resource if changed.
        /// </summary>
        [Input("computeClusterId", required: true)]
        public Input<string> ComputeClusterId { get; set; } = null!;

        /// <summary>
        /// Enable this rule in the cluster. Default: `true`.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// When this value is `true`, prevents any virtual
        /// machine operations that may violate this rule. Default: `false`.
        /// </summary>
        [Input("mandatory")]
        public Input<bool>? Mandatory { get; set; }

        /// <summary>
        /// The name of the rule. This must be unique in the cluster.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("virtualMachineIds", required: true)]
        private InputList<string>? _virtualMachineIds;

        /// <summary>
        /// The UUIDs of the virtual machines to run
        /// on the same host together.
        /// </summary>
        public InputList<string> VirtualMachineIds
        {
            get => _virtualMachineIds ?? (_virtualMachineIds = new InputList<string>());
            set => _virtualMachineIds = value;
        }

        public ComputeClusterVmAffinityRuleArgs()
        {
        }
    }

    public sealed class ComputeClusterVmAffinityRuleState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The [managed object reference
        /// ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
        /// resource if changed.
        /// </summary>
        [Input("computeClusterId")]
        public Input<string>? ComputeClusterId { get; set; }

        /// <summary>
        /// Enable this rule in the cluster. Default: `true`.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// When this value is `true`, prevents any virtual
        /// machine operations that may violate this rule. Default: `false`.
        /// </summary>
        [Input("mandatory")]
        public Input<bool>? Mandatory { get; set; }

        /// <summary>
        /// The name of the rule. This must be unique in the cluster.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("virtualMachineIds")]
        private InputList<string>? _virtualMachineIds;

        /// <summary>
        /// The UUIDs of the virtual machines to run
        /// on the same host together.
        /// </summary>
        public InputList<string> VirtualMachineIds
        {
            get => _virtualMachineIds ?? (_virtualMachineIds = new InputList<string>());
            set => _virtualMachineIds = value;
        }

        public ComputeClusterVmAffinityRuleState()
        {
        }
    }
}
