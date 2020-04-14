// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.VSphere.Inputs
{

    public sealed class VnicIpv4GetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Use DHCP to configure the interface's IPv4 stack.
        /// </summary>
        [Input("dhcp")]
        public Input<bool>? Dhcp { get; set; }

        /// <summary>
        /// IP address of the default gateway, if DHCP or autoconfig is not set.
        /// </summary>
        [Input("gw")]
        public Input<string>? Gw { get; set; }

        /// <summary>
        /// Address of the interface, if DHCP is not set.
        /// </summary>
        [Input("ip")]
        public Input<string>? Ip { get; set; }

        /// <summary>
        /// Netmask of the interface, if DHCP is not set.
        /// </summary>
        [Input("netmask")]
        public Input<string>? Netmask { get; set; }

        public VnicIpv4GetArgs()
        {
        }
    }
}
