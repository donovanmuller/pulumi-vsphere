// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.VSphere.Inputs
{

    public sealed class VirtualMachineNetworkInterfaceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The network interface type. Can be one of
        /// `e1000`, `e1000e`, or `vmxnet3`. Default: `vmxnet3`.
        /// </summary>
        [Input("adapterType")]
        public Input<string>? AdapterType { get; set; }

        /// <summary>
        /// The upper bandwidth limit of this network
        /// interface, in Mbits/sec. The default is no limit.
        /// </summary>
        [Input("bandwidthLimit")]
        public Input<int>? BandwidthLimit { get; set; }

        /// <summary>
        /// The bandwidth reservation of this
        /// network interface, in Mbits/sec. The default is no reservation.
        /// </summary>
        [Input("bandwidthReservation")]
        public Input<int>? BandwidthReservation { get; set; }

        /// <summary>
        /// The share count for this network
        /// interface when the share level is `custom`.
        /// </summary>
        [Input("bandwidthShareCount")]
        public Input<int>? BandwidthShareCount { get; set; }

        /// <summary>
        /// The bandwidth share allocation level for
        /// this interface. Can be one of `low`, `normal`, `high`, or `custom`. Default:
        /// `normal`.
        /// </summary>
        [Input("bandwidthShareLevel")]
        public Input<string>? BandwidthShareLevel { get; set; }

        /// <summary>
        /// An address internal to this provider that helps locate the
        /// device when `key` is unavailable. This follows a convention of
        /// `CONTROLLER_TYPE:BUS_NUMBER:UNIT_NUMBER`. Example: `scsi:0:1` means device
        /// unit 1 on SCSI bus 0.
        /// </summary>
        [Input("deviceAddress")]
        public Input<string>? DeviceAddress { get; set; }

        /// <summary>
        /// The ID of the device within the virtual machine.
        /// </summary>
        [Input("key")]
        public Input<int>? Key { get; set; }

        /// <summary>
        /// The MAC address of this network interface. Can
        /// only be manually set if `use_static_mac` is true, otherwise this is a
        /// computed value that gives the current MAC address of this interface.
        /// </summary>
        [Input("macAddress")]
        public Input<string>? MacAddress { get; set; }

        /// <summary>
        /// The managed object reference
        /// ID of the network to connect this interface to.
        /// </summary>
        [Input("networkId", required: true)]
        public Input<string> NetworkId { get; set; } = null!;

        /// <summary>
        /// Specifies which OVF NIC the `network_interface`
        /// should be associated with. Only applies at creation and only when deploying
        /// from an OVF source.
        /// </summary>
        [Input("ovfMapping")]
        public Input<string>? OvfMapping { get; set; }

        /// <summary>
        /// If true, the `mac_address` field is treated as
        /// a static MAC address and set accordingly. Setting this to `true` requires
        /// `mac_address` to be set. Default: `false`.
        /// </summary>
        [Input("useStaticMac")]
        public Input<bool>? UseStaticMac { get; set; }

        public VirtualMachineNetworkInterfaceArgs()
        {
        }
    }
}
