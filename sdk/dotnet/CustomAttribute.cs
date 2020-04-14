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
    /// The `vsphere..CustomAttribute` resource can be used to create and manage custom
    /// attributes, which allow users to associate user-specific meta-information with 
    /// vSphere managed objects. Custom attribute values must be strings and are stored 
    /// on the vCenter Server and not the managed object.
    /// 
    /// For more information about custom attributes, click [here][ext-custom-attributes].
    /// 
    /// [ext-custom-attributes]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vcenterhost.doc/GUID-73606C4C-763C-4E27-A1DA-032E4C46219D.html
    /// 
    /// &gt; **NOTE:** Custom attributes are unsupported on direct ESXi connections 
    /// and require vCenter.
    /// 
    /// 
    /// ## Managed Object Types
    /// 
    /// The following table will help you determine what value you need to enter for 
    /// the managed object type you want the attribute to apply to.
    /// 
    /// Note that if you want a attribute to apply to all objects, leave the type 
    /// unspecified.
    /// 
    /// &lt;table&gt;
    /// &lt;tr&gt;&lt;th&gt;Type&lt;/th&gt;&lt;th&gt;Value&lt;/th&gt;&lt;/tr&gt;
    /// &lt;tr&gt;&lt;td&gt;Folders&lt;/td&gt;&lt;td&gt;`Folder`&lt;/td&gt;&lt;/tr&gt;
    /// &lt;tr&gt;&lt;td&gt;Clusters&lt;/td&gt;&lt;td&gt;`ClusterComputeResource`&lt;/td&gt;&lt;/tr&gt;
    /// &lt;tr&gt;&lt;td&gt;Datacenters&lt;/td&gt;&lt;td&gt;`Datacenter`&lt;/td&gt;&lt;/tr&gt;
    /// &lt;tr&gt;&lt;td&gt;Datastores&lt;/td&gt;&lt;td&gt;`Datastore`&lt;/td&gt;&lt;/tr&gt;
    /// &lt;tr&gt;&lt;td&gt;Datastore Clusters&lt;/td&gt;&lt;td&gt;`StoragePod`&lt;/td&gt;&lt;/tr&gt;
    /// &lt;tr&gt;&lt;td&gt;DVS Portgroups&lt;/td&gt;&lt;td&gt;`DistributedVirtualPortgroup`&lt;/td&gt;&lt;/tr&gt;
    /// &lt;tr&gt;&lt;td&gt;Distributed vSwitches&lt;/td&gt;&lt;td&gt;`DistributedVirtualSwitch`&lt;br&gt;`VmwareDistributedVirtualSwitch`&lt;/td&gt;&lt;/tr&gt;
    /// &lt;tr&gt;&lt;td&gt;Hosts&lt;/td&gt;&lt;td&gt;`HostSystem`&lt;/td&gt;&lt;/tr&gt;
    /// &lt;tr&gt;&lt;td&gt;Content Libraries&lt;/td&gt;&lt;td&gt;`com.vmware.content.Library`&lt;/td&gt;&lt;/tr&gt;
    /// &lt;tr&gt;&lt;td&gt;Content Library Items&lt;/td&gt;&lt;td&gt;`com.vmware.content.library.Item`&lt;/td&gt;&lt;/tr&gt;
    /// &lt;tr&gt;&lt;td&gt;Networks&lt;/td&gt;&lt;td&gt;`HostNetwork`&lt;br&gt;`Network`&lt;br&gt;`OpaqueNetwork`&lt;/td&gt;&lt;/tr&gt;
    /// &lt;tr&gt;&lt;td&gt;Resource Pools&lt;/td&gt;&lt;td&gt;`ResourcePool`&lt;/td&gt;&lt;/tr&gt;
    /// &lt;tr&gt;&lt;td&gt;vApps&lt;/td&gt;&lt;td&gt;`VirtualApp`&lt;/td&gt;&lt;/tr&gt;
    /// &lt;tr&gt;&lt;td&gt;Virtual Machines&lt;/td&gt;&lt;td&gt;`VirtualMachine`&lt;/td&gt;&lt;/tr&gt;
    /// &lt;/table&gt;
    /// </summary>
    public partial class CustomAttribute : Pulumi.CustomResource
    {
        /// <summary>
        /// The object type that this attribute may be
        /// applied to. If not set, the custom attribute may be applied to any object
        /// type. For a full list, click here. Forces a new
        /// resource if changed.
        /// </summary>
        [Output("managedObjectType")]
        public Output<string?> ManagedObjectType { get; private set; } = null!;

        /// <summary>
        /// The name of the custom attribute.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a CustomAttribute resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public CustomAttribute(string name, CustomAttributeArgs? args = null, CustomResourceOptions? options = null)
            : base("vsphere:index/customAttribute:CustomAttribute", name, args ?? new CustomAttributeArgs(), MakeResourceOptions(options, ""))
        {
        }

        private CustomAttribute(string name, Input<string> id, CustomAttributeState? state = null, CustomResourceOptions? options = null)
            : base("vsphere:index/customAttribute:CustomAttribute", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing CustomAttribute resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static CustomAttribute Get(string name, Input<string> id, CustomAttributeState? state = null, CustomResourceOptions? options = null)
        {
            return new CustomAttribute(name, id, state, options);
        }
    }

    public sealed class CustomAttributeArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The object type that this attribute may be
        /// applied to. If not set, the custom attribute may be applied to any object
        /// type. For a full list, click here. Forces a new
        /// resource if changed.
        /// </summary>
        [Input("managedObjectType")]
        public Input<string>? ManagedObjectType { get; set; }

        /// <summary>
        /// The name of the custom attribute.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public CustomAttributeArgs()
        {
        }
    }

    public sealed class CustomAttributeState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The object type that this attribute may be
        /// applied to. If not set, the custom attribute may be applied to any object
        /// type. For a full list, click here. Forces a new
        /// resource if changed.
        /// </summary>
        [Input("managedObjectType")]
        public Input<string>? ManagedObjectType { get; set; }

        /// <summary>
        /// The name of the custom attribute.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public CustomAttributeState()
        {
        }
    }
}
