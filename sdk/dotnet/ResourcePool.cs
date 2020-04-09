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
    /// The `vsphere..ResourcePool` resource can be used to create and manage
    /// resource pools in standalone hosts or on compute clusters.
    /// 
    /// For more information on vSphere resource pools, see [this
    /// page][ref-vsphere-resource_pools].
    /// 
    /// [ref-vsphere-resource_pools]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-60077B40-66FF-4625-934A-641703ED7601.html
    /// 
    /// 
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/r/resource_pool.html.markdown.
    /// </summary>
    public partial class ResourcePool : Pulumi.CustomResource
    {
        /// <summary>
        /// Determines if the reservation on a resource
        /// pool can grow beyond the specified value if the parent resource pool has
        /// unreserved resources. Default: `true`
        /// </summary>
        [Output("cpuExpandable")]
        public Output<bool?> CpuExpandable { get; private set; } = null!;

        /// <summary>
        /// The CPU utilization of a resource pool will not exceed
        /// this limit, even if there are available resources. Set to `-1` for unlimited.
        /// Default: `-1`
        /// </summary>
        [Output("cpuLimit")]
        public Output<int?> CpuLimit { get; private set; } = null!;

        /// <summary>
        /// Amount of CPU (MHz) that is guaranteed
        /// available to the resource pool. Default: `0`
        /// </summary>
        [Output("cpuReservation")]
        public Output<int?> CpuReservation { get; private set; } = null!;

        /// <summary>
        /// The CPU allocation level. The level is a
        /// simplified view of shares. Levels map to a pre-determined set of numeric
        /// values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
        /// `low`, `normal`, or `high` are specified values in `cpu_shares` will be
        /// ignored.  Default: `normal`
        /// </summary>
        [Output("cpuShareLevel")]
        public Output<string?> CpuShareLevel { get; private set; } = null!;

        /// <summary>
        /// The number of shares allocated for CPU. Used to
        /// determine resource allocation in case of resource contention. If this is set,
        /// `cpu_share_level` must be `custom`.
        /// </summary>
        [Output("cpuShares")]
        public Output<int> CpuShares { get; private set; } = null!;

        /// <summary>
        /// A list of custom attributes to set on this resource.
        /// </summary>
        [Output("customAttributes")]
        public Output<ImmutableDictionary<string, string>?> CustomAttributes { get; private set; } = null!;

        /// <summary>
        /// Determines if the reservation on a resource
        /// pool can grow beyond the specified value if the parent resource pool has
        /// unreserved resources. Default: `true`
        /// </summary>
        [Output("memoryExpandable")]
        public Output<bool?> MemoryExpandable { get; private set; } = null!;

        /// <summary>
        /// The CPU utilization of a resource pool will not exceed
        /// this limit, even if there are available resources. Set to `-1` for unlimited.
        /// Default: `-1`
        /// </summary>
        [Output("memoryLimit")]
        public Output<int?> MemoryLimit { get; private set; } = null!;

        /// <summary>
        /// Amount of CPU (MHz) that is guaranteed
        /// available to the resource pool. Default: `0`
        /// </summary>
        [Output("memoryReservation")]
        public Output<int?> MemoryReservation { get; private set; } = null!;

        /// <summary>
        /// The CPU allocation level. The level is a
        /// simplified view of shares. Levels map to a pre-determined set of numeric
        /// values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
        /// `low`, `normal`, or `high` are specified values in `memory_shares` will be
        /// ignored.  Default: `normal`
        /// </summary>
        [Output("memoryShareLevel")]
        public Output<string?> MemoryShareLevel { get; private set; } = null!;

        /// <summary>
        /// The number of shares allocated for CPU. Used to
        /// determine resource allocation in case of resource contention. If this is set,
        /// `memory_share_level` must be `custom`.
        /// </summary>
        [Output("memoryShares")]
        public Output<int> MemoryShares { get; private set; } = null!;

        /// <summary>
        /// The name of the resource pool.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The [managed object ID][docs-about-morefs]
        /// of the parent resource pool. This can be the root resource pool for a cluster
        /// or standalone host, or a resource pool itself. When moving a resource pool
        /// from one parent resource pool to another, both must share a common root
        /// resource pool or the move will fail.
        /// </summary>
        [Output("parentResourcePoolId")]
        public Output<string> ParentResourcePoolId { get; private set; } = null!;

        /// <summary>
        /// The IDs of any tags to attach to this resource. See
        /// [here][docs-applying-tags] for a reference on how to apply tags.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<string>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a ResourcePool resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ResourcePool(string name, ResourcePoolArgs args, CustomResourceOptions? options = null)
            : base("vsphere:index/resourcePool:ResourcePool", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private ResourcePool(string name, Input<string> id, ResourcePoolState? state = null, CustomResourceOptions? options = null)
            : base("vsphere:index/resourcePool:ResourcePool", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ResourcePool resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ResourcePool Get(string name, Input<string> id, ResourcePoolState? state = null, CustomResourceOptions? options = null)
        {
            return new ResourcePool(name, id, state, options);
        }
    }

    public sealed class ResourcePoolArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Determines if the reservation on a resource
        /// pool can grow beyond the specified value if the parent resource pool has
        /// unreserved resources. Default: `true`
        /// </summary>
        [Input("cpuExpandable")]
        public Input<bool>? CpuExpandable { get; set; }

        /// <summary>
        /// The CPU utilization of a resource pool will not exceed
        /// this limit, even if there are available resources. Set to `-1` for unlimited.
        /// Default: `-1`
        /// </summary>
        [Input("cpuLimit")]
        public Input<int>? CpuLimit { get; set; }

        /// <summary>
        /// Amount of CPU (MHz) that is guaranteed
        /// available to the resource pool. Default: `0`
        /// </summary>
        [Input("cpuReservation")]
        public Input<int>? CpuReservation { get; set; }

        /// <summary>
        /// The CPU allocation level. The level is a
        /// simplified view of shares. Levels map to a pre-determined set of numeric
        /// values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
        /// `low`, `normal`, or `high` are specified values in `cpu_shares` will be
        /// ignored.  Default: `normal`
        /// </summary>
        [Input("cpuShareLevel")]
        public Input<string>? CpuShareLevel { get; set; }

        /// <summary>
        /// The number of shares allocated for CPU. Used to
        /// determine resource allocation in case of resource contention. If this is set,
        /// `cpu_share_level` must be `custom`.
        /// </summary>
        [Input("cpuShares")]
        public Input<int>? CpuShares { get; set; }

        [Input("customAttributes")]
        private InputMap<string>? _customAttributes;

        /// <summary>
        /// A list of custom attributes to set on this resource.
        /// </summary>
        public InputMap<string> CustomAttributes
        {
            get => _customAttributes ?? (_customAttributes = new InputMap<string>());
            set => _customAttributes = value;
        }

        /// <summary>
        /// Determines if the reservation on a resource
        /// pool can grow beyond the specified value if the parent resource pool has
        /// unreserved resources. Default: `true`
        /// </summary>
        [Input("memoryExpandable")]
        public Input<bool>? MemoryExpandable { get; set; }

        /// <summary>
        /// The CPU utilization of a resource pool will not exceed
        /// this limit, even if there are available resources. Set to `-1` for unlimited.
        /// Default: `-1`
        /// </summary>
        [Input("memoryLimit")]
        public Input<int>? MemoryLimit { get; set; }

        /// <summary>
        /// Amount of CPU (MHz) that is guaranteed
        /// available to the resource pool. Default: `0`
        /// </summary>
        [Input("memoryReservation")]
        public Input<int>? MemoryReservation { get; set; }

        /// <summary>
        /// The CPU allocation level. The level is a
        /// simplified view of shares. Levels map to a pre-determined set of numeric
        /// values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
        /// `low`, `normal`, or `high` are specified values in `memory_shares` will be
        /// ignored.  Default: `normal`
        /// </summary>
        [Input("memoryShareLevel")]
        public Input<string>? MemoryShareLevel { get; set; }

        /// <summary>
        /// The number of shares allocated for CPU. Used to
        /// determine resource allocation in case of resource contention. If this is set,
        /// `memory_share_level` must be `custom`.
        /// </summary>
        [Input("memoryShares")]
        public Input<int>? MemoryShares { get; set; }

        /// <summary>
        /// The name of the resource pool.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The [managed object ID][docs-about-morefs]
        /// of the parent resource pool. This can be the root resource pool for a cluster
        /// or standalone host, or a resource pool itself. When moving a resource pool
        /// from one parent resource pool to another, both must share a common root
        /// resource pool or the move will fail.
        /// </summary>
        [Input("parentResourcePoolId", required: true)]
        public Input<string> ParentResourcePoolId { get; set; } = null!;

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// The IDs of any tags to attach to this resource. See
        /// [here][docs-applying-tags] for a reference on how to apply tags.
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        public ResourcePoolArgs()
        {
        }
    }

    public sealed class ResourcePoolState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Determines if the reservation on a resource
        /// pool can grow beyond the specified value if the parent resource pool has
        /// unreserved resources. Default: `true`
        /// </summary>
        [Input("cpuExpandable")]
        public Input<bool>? CpuExpandable { get; set; }

        /// <summary>
        /// The CPU utilization of a resource pool will not exceed
        /// this limit, even if there are available resources. Set to `-1` for unlimited.
        /// Default: `-1`
        /// </summary>
        [Input("cpuLimit")]
        public Input<int>? CpuLimit { get; set; }

        /// <summary>
        /// Amount of CPU (MHz) that is guaranteed
        /// available to the resource pool. Default: `0`
        /// </summary>
        [Input("cpuReservation")]
        public Input<int>? CpuReservation { get; set; }

        /// <summary>
        /// The CPU allocation level. The level is a
        /// simplified view of shares. Levels map to a pre-determined set of numeric
        /// values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
        /// `low`, `normal`, or `high` are specified values in `cpu_shares` will be
        /// ignored.  Default: `normal`
        /// </summary>
        [Input("cpuShareLevel")]
        public Input<string>? CpuShareLevel { get; set; }

        /// <summary>
        /// The number of shares allocated for CPU. Used to
        /// determine resource allocation in case of resource contention. If this is set,
        /// `cpu_share_level` must be `custom`.
        /// </summary>
        [Input("cpuShares")]
        public Input<int>? CpuShares { get; set; }

        [Input("customAttributes")]
        private InputMap<string>? _customAttributes;

        /// <summary>
        /// A list of custom attributes to set on this resource.
        /// </summary>
        public InputMap<string> CustomAttributes
        {
            get => _customAttributes ?? (_customAttributes = new InputMap<string>());
            set => _customAttributes = value;
        }

        /// <summary>
        /// Determines if the reservation on a resource
        /// pool can grow beyond the specified value if the parent resource pool has
        /// unreserved resources. Default: `true`
        /// </summary>
        [Input("memoryExpandable")]
        public Input<bool>? MemoryExpandable { get; set; }

        /// <summary>
        /// The CPU utilization of a resource pool will not exceed
        /// this limit, even if there are available resources. Set to `-1` for unlimited.
        /// Default: `-1`
        /// </summary>
        [Input("memoryLimit")]
        public Input<int>? MemoryLimit { get; set; }

        /// <summary>
        /// Amount of CPU (MHz) that is guaranteed
        /// available to the resource pool. Default: `0`
        /// </summary>
        [Input("memoryReservation")]
        public Input<int>? MemoryReservation { get; set; }

        /// <summary>
        /// The CPU allocation level. The level is a
        /// simplified view of shares. Levels map to a pre-determined set of numeric
        /// values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
        /// `low`, `normal`, or `high` are specified values in `memory_shares` will be
        /// ignored.  Default: `normal`
        /// </summary>
        [Input("memoryShareLevel")]
        public Input<string>? MemoryShareLevel { get; set; }

        /// <summary>
        /// The number of shares allocated for CPU. Used to
        /// determine resource allocation in case of resource contention. If this is set,
        /// `memory_share_level` must be `custom`.
        /// </summary>
        [Input("memoryShares")]
        public Input<int>? MemoryShares { get; set; }

        /// <summary>
        /// The name of the resource pool.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The [managed object ID][docs-about-morefs]
        /// of the parent resource pool. This can be the root resource pool for a cluster
        /// or standalone host, or a resource pool itself. When moving a resource pool
        /// from one parent resource pool to another, both must share a common root
        /// resource pool or the move will fail.
        /// </summary>
        [Input("parentResourcePoolId")]
        public Input<string>? ParentResourcePoolId { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// The IDs of any tags to attach to this resource. See
        /// [here][docs-applying-tags] for a reference on how to apply tags.
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        public ResourcePoolState()
        {
        }
    }
}
