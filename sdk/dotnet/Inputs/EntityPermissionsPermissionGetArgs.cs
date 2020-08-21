// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.VSphere.Inputs
{

    public sealed class EntityPermissionsPermissionGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether user_or_group field refers to a user or a group. True for a group and false for a user.
        /// </summary>
        [Input("isGroup", required: true)]
        public Input<bool> IsGroup { get; set; } = null!;

        /// <summary>
        /// Whether or not this permission propagates down the hierarchy to sub-entities.
        /// </summary>
        [Input("propagate", required: true)]
        public Input<bool> Propagate { get; set; } = null!;

        /// <summary>
        /// The role id of the role to be given to the user on the specified entity.
        /// </summary>
        [Input("roleId", required: true)]
        public Input<string> RoleId { get; set; } = null!;

        /// <summary>
        /// The user/group getting the permission.
        /// </summary>
        [Input("userOrGroup", required: true)]
        public Input<string> UserOrGroup { get; set; } = null!;

        public EntityPermissionsPermissionGetArgs()
        {
        }
    }
}
