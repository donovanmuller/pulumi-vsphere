// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.VSphere.Inputs
{

    public sealed class DistributedVirtualSwitchHostGetArgs : Pulumi.ResourceArgs
    {
        [Input("devices", required: true)]
        private InputList<string>? _devices;

        /// <summary>
        /// The list of NIC devices to map to uplinks on the DVS,
        /// added in order they are specified.
        /// </summary>
        public InputList<string> Devices
        {
            get => _devices ?? (_devices = new InputList<string>());
            set => _devices = value;
        }

        /// <summary>
        /// The host system ID of the host to add to the
        /// DVS.
        /// </summary>
        [Input("hostSystemId", required: true)]
        public Input<string> HostSystemId { get; set; } = null!;

        public DistributedVirtualSwitchHostGetArgs()
        {
        }
    }
}
