// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.VSphere.Inputs
{

    public sealed class ContentLibrarySubscriptionGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Method to log into remote Content Library. Must be `NONE` or `BASIC`.
        /// </summary>
        [Input("authenticationMethod")]
        public Input<string>? AuthenticationMethod { get; set; }

        /// <summary>
        /// Enable automatic synchronization with the external content library.
        /// </summary>
        [Input("automaticSync")]
        public Input<bool>? AutomaticSync { get; set; }

        /// <summary>
        /// Download all library content immediately.
        /// </summary>
        [Input("onDemand")]
        public Input<bool>? OnDemand { get; set; }

        /// <summary>
        /// Password to log in with.
        /// </summary>
        [Input("password")]
        public Input<string>? Password { get; set; }

        /// <summary>
        /// URL of remote Content Library.
        /// </summary>
        [Input("subscriptionUrl")]
        public Input<string>? SubscriptionUrl { get; set; }

        /// <summary>
        /// User name to log in with.
        /// </summary>
        [Input("username")]
        public Input<string>? Username { get; set; }

        public ContentLibrarySubscriptionGetArgs()
        {
        }
    }
}
