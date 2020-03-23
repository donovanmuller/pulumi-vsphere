// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.VSphere
{
    public static partial class Invokes
    {
        /// <summary>
        /// The `vsphere..getDatastore` data source can be used to discover the ID of a
        /// datastore in vSphere. This is useful to fetch the ID of a datastore that you
        /// want to use to create virtual machines in using the
        /// [`vsphere..VirtualMachine`][docs-virtual-machine-resource] resource. 
        /// 
        /// [docs-virtual-machine-resource]: /docs/providers/vsphere/r/virtual_machine.html
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/d/datastore.html.markdown.
        /// </summary>
        public static Task<GetDatastoreResult> GetDatastore(GetDatastoreArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetDatastoreResult>("vsphere:index/getDatastore:getDatastore", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetDatastoreArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The [managed object reference
        /// ID][docs-about-morefs] of the datacenter the datastore is located in. This
        /// can be omitted if the search path used in `name` is an absolute path. For
        /// default datacenters, use the id attribute from an empty `vsphere..Datacenter`
        /// data source.
        /// </summary>
        [Input("datacenterId")]
        public string? DatacenterId { get; set; }

        /// <summary>
        /// The name of the datastore. This can be a name or path.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetDatastoreArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetDatastoreResult
    {
        public readonly string? DatacenterId;
        public readonly string Name;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetDatastoreResult(
            string? datacenterId,
            string name,
            string id)
        {
            DatacenterId = datacenterId;
            Name = name;
            Id = id;
        }
    }
}
