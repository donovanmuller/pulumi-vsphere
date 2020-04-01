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
        [Obsolete("Use GetTagCategory.InvokeAsync() instead")]
        public static Task<GetTagCategoryResult> GetTagCategory(GetTagCategoryArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetTagCategoryResult>("vsphere:index/getTagCategory:getTagCategory", args ?? InvokeArgs.Empty, options.WithVersion());
    }
    public static class GetTagCategory
    {
        public static Task<GetTagCategoryResult> InvokeAsync(GetTagCategoryArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetTagCategoryResult>("vsphere:index/getTagCategory:getTagCategory", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetTagCategoryArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the tag category.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetTagCategoryArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetTagCategoryResult
    {
        public readonly ImmutableArray<string> AssociableTypes;
        public readonly string Cardinality;
        public readonly string Description;
        public readonly string Name;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetTagCategoryResult(
            ImmutableArray<string> associableTypes,
            string cardinality,
            string description,
            string name,
            string id)
        {
            AssociableTypes = associableTypes;
            Cardinality = cardinality;
            Description = description;
            Name = name;
            Id = id;
        }
    }
}
