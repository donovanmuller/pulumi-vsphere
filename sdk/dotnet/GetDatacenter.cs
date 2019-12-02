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
        /// The `vsphere..Datacenter` data source can be used to discover the ID of a
        /// vSphere datacenter. This can then be used with resources or data sources that
        /// require a datacenter, such as the [`vsphere..Host`][data-source-vsphere-host]
        /// data source.
        /// 
        /// [data-source-vsphere-host]: /docs/providers/vsphere/d/host.html
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/d/datacenter.html.markdown.
        /// </summary>
        public static Task<GetDatacenterResult> GetDatacenter(GetDatacenterArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetDatacenterResult>("vsphere:index/getDatacenter:getDatacenter", args ?? ResourceArgs.Empty, options.WithVersion());
    }

    public sealed class GetDatacenterArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the datacenter. This can be a name or path.
        /// Can be omitted if there is only one datacenter in your inventory.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetDatacenterArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetDatacenterResult
    {
        public readonly string? Name;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetDatacenterResult(
            string? name,
            string id)
        {
            Name = name;
            Id = id;
        }
    }
}
