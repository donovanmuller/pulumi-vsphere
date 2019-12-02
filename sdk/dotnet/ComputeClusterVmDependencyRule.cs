// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Vsphere
{
    /// <summary>
    /// The `vsphere..ComputeClusterVmDependencyRule` resource can be used to manage
    /// VM dependency rules in a cluster, either created by the
    /// [`vsphere..ComputeCluster`][tf-vsphere-cluster-resource] resource or looked up
    /// by the [`vsphere..ComputeCluster`][tf-vsphere-cluster-data-source] data source.
    /// 
    /// [tf-vsphere-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
    /// [tf-vsphere-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html
    /// 
    /// A virtual machine dependency rule applies to vSphere HA, and allows
    /// user-defined startup orders for virtual machines in the case of host failure.
    /// Virtual machines are supplied via groups, which can be managed via the
    /// [`vsphere..ComputeClusterVmGroup`][tf-vsphere-cluster-vm-group-resource]
    /// resource.
    /// 
    /// [tf-vsphere-cluster-vm-group-resource]: /docs/providers/vsphere/r/compute_cluster_vm_group.html
    /// 
    /// &gt; **NOTE:** This resource requires vCenter and is not available on direct ESXi
    /// connections.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/r/compute_cluster_vm_dependency_rule.html.markdown.
    /// </summary>
    public partial class ComputeClusterVmDependencyRule : Pulumi.CustomResource
    {
        /// <summary>
        /// The [managed object reference
        /// ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
        /// resource if changed.
        /// </summary>
        [Output("computeClusterId")]
        public Output<string> ComputeClusterId { get; private set; } = null!;

        /// <summary>
        /// The name of the VM group that this
        /// rule depends on. The VMs defined in the group specified by
        /// `vm_group_name` will not be started until the VMs in this
        /// group are started.
        /// </summary>
        [Output("dependencyVmGroupName")]
        public Output<string> DependencyVmGroupName { get; private set; } = null!;

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
        /// The name of the rule. This must be unique in the
        /// cluster.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The name of the VM group that is the subject of
        /// this rule. The VMs defined in this group will not be started until the VMs in
        /// the group specified by
        /// `dependency_vm_group_name` are started.
        /// </summary>
        [Output("vmGroupName")]
        public Output<string> VmGroupName { get; private set; } = null!;


        /// <summary>
        /// Create a ComputeClusterVmDependencyRule resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ComputeClusterVmDependencyRule(string name, ComputeClusterVmDependencyRuleArgs args, CustomResourceOptions? options = null)
            : base("vsphere:index/computeClusterVmDependencyRule:ComputeClusterVmDependencyRule", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private ComputeClusterVmDependencyRule(string name, Input<string> id, ComputeClusterVmDependencyRuleState? state = null, CustomResourceOptions? options = null)
            : base("vsphere:index/computeClusterVmDependencyRule:ComputeClusterVmDependencyRule", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ComputeClusterVmDependencyRule resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ComputeClusterVmDependencyRule Get(string name, Input<string> id, ComputeClusterVmDependencyRuleState? state = null, CustomResourceOptions? options = null)
        {
            return new ComputeClusterVmDependencyRule(name, id, state, options);
        }
    }

    public sealed class ComputeClusterVmDependencyRuleArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The [managed object reference
        /// ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
        /// resource if changed.
        /// </summary>
        [Input("computeClusterId", required: true)]
        public Input<string> ComputeClusterId { get; set; } = null!;

        /// <summary>
        /// The name of the VM group that this
        /// rule depends on. The VMs defined in the group specified by
        /// `vm_group_name` will not be started until the VMs in this
        /// group are started.
        /// </summary>
        [Input("dependencyVmGroupName", required: true)]
        public Input<string> DependencyVmGroupName { get; set; } = null!;

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
        /// The name of the rule. This must be unique in the
        /// cluster.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the VM group that is the subject of
        /// this rule. The VMs defined in this group will not be started until the VMs in
        /// the group specified by
        /// `dependency_vm_group_name` are started.
        /// </summary>
        [Input("vmGroupName", required: true)]
        public Input<string> VmGroupName { get; set; } = null!;

        public ComputeClusterVmDependencyRuleArgs()
        {
        }
    }

    public sealed class ComputeClusterVmDependencyRuleState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The [managed object reference
        /// ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
        /// resource if changed.
        /// </summary>
        [Input("computeClusterId")]
        public Input<string>? ComputeClusterId { get; set; }

        /// <summary>
        /// The name of the VM group that this
        /// rule depends on. The VMs defined in the group specified by
        /// `vm_group_name` will not be started until the VMs in this
        /// group are started.
        /// </summary>
        [Input("dependencyVmGroupName")]
        public Input<string>? DependencyVmGroupName { get; set; }

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
        /// The name of the rule. This must be unique in the
        /// cluster.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the VM group that is the subject of
        /// this rule. The VMs defined in this group will not be started until the VMs in
        /// the group specified by
        /// `dependency_vm_group_name` are started.
        /// </summary>
        [Input("vmGroupName")]
        public Input<string>? VmGroupName { get; set; }

        public ComputeClusterVmDependencyRuleState()
        {
        }
    }
}
