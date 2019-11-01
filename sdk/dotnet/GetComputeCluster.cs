// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Vsphere
{
    public static partial class Invokes
    {
        /// <summary>
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/d/compute_cluster.html.markdown.
        /// </summary>
        public static Task<GetComputeClusterResult> GetComputeCluster(GetComputeClusterArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetComputeClusterResult>("vsphere:index/getComputeCluster:getComputeCluster", args, options.WithVersion());
    }

    public sealed class GetComputeClusterArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The [managed object reference
        /// ID][docs-about-morefs] of the datacenter the cluster is located in.  This can
        /// be omitted if the search path used in `name` is an absolute path.  For
        /// default datacenters, use the id attribute from an empty `vsphere..Datacenter`
        /// data source.
        /// </summary>
        [Input("datacenterId")]
        public Input<string>? DatacenterId { get; set; }

        /// <summary>
        /// The name or absolute path to the cluster.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetComputeClusterArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetComputeClusterResult
    {
        public readonly string? DatacenterId;
        public readonly string Name;
        public readonly string ResourcePoolId;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetComputeClusterResult(
            string? datacenterId,
            string name,
            string resourcePoolId,
            string id)
        {
            DatacenterId = datacenterId;
            Name = name;
            ResourcePoolId = resourcePoolId;
            Id = id;
        }
    }
}
