// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Vsphere
{
    /// <summary>
    /// The provider type for the vsphere package. By default, resources use package-wide configuration
    /// settings, however an explicit `Provider` instance may be created and passed during resource
    /// construction to achieve fine-grained programmatic control over provider settings. See the
    /// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/index.html.markdown.
    /// </summary>
    public partial class Provider : Pulumi.ProviderResource
    {
        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs args, ResourceOptions? options = null)
            : base("vsphere", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private static ResourceOptions MakeResourceOptions(ResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new ResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = ResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class ProviderArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// If set, VMware vSphere client will permit unverifiable SSL certificates.
        /// </summary>
        [Input("allowUnverifiedSsl", json: true)]
        public Input<bool>? AllowUnverifiedSsl { get; set; }

        /// <summary>
        /// govmomi debug
        /// </summary>
        [Input("clientDebug", json: true)]
        public Input<bool>? ClientDebug { get; set; }

        /// <summary>
        /// govmomi debug path for debug
        /// </summary>
        [Input("clientDebugPath")]
        public Input<string>? ClientDebugPath { get; set; }

        /// <summary>
        /// govmomi debug path for a single run
        /// </summary>
        [Input("clientDebugPathRun")]
        public Input<string>? ClientDebugPathRun { get; set; }

        /// <summary>
        /// The user password for vSphere API operations.
        /// </summary>
        [Input("password", required: true)]
        public Input<string> Password { get; set; } = null!;

        /// <summary>
        /// Persist vSphere client sessions to disk
        /// </summary>
        [Input("persistSession", json: true)]
        public Input<bool>? PersistSession { get; set; }

        /// <summary>
        /// The directory to save vSphere REST API sessions to
        /// </summary>
        [Input("restSessionPath")]
        public Input<string>? RestSessionPath { get; set; }

        /// <summary>
        /// The user name for vSphere API operations.
        /// </summary>
        [Input("user", required: true)]
        public Input<string> User { get; set; } = null!;

        [Input("vcenterServer")]
        public Input<string>? VcenterServer { get; set; }

        /// <summary>
        /// Keep alive interval for the VIM session in minutes
        /// </summary>
        [Input("vimKeepAlive", json: true)]
        public Input<int>? VimKeepAlive { get; set; }

        /// <summary>
        /// The directory to save vSphere SOAP API sessions to
        /// </summary>
        [Input("vimSessionPath")]
        public Input<string>? VimSessionPath { get; set; }

        /// <summary>
        /// The vSphere Server name for vSphere API operations.
        /// </summary>
        [Input("vsphereServer")]
        public Input<string>? VsphereServer { get; set; }

        public ProviderArgs()
        {
        }
    }
}
