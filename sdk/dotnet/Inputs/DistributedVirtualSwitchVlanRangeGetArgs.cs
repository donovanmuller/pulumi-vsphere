// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.VSphere.Inputs
{

    public sealed class DistributedVirtualSwitchVlanRangeGetArgs : Pulumi.ResourceArgs
    {
        [Input("maxVlan", required: true)]
        public Input<int> MaxVlan { get; set; } = null!;

        [Input("minVlan", required: true)]
        public Input<int> MinVlan { get; set; } = null!;

        public DistributedVirtualSwitchVlanRangeGetArgs()
        {
        }
    }
}