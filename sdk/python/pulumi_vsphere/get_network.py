# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class GetNetworkResult:
    """
    A collection of values returned by getNetwork.
    """
    def __init__(__self__, type=None, id=None):
        if type and not isinstance(type, str):
            raise TypeError('Expected argument type to be a str')
        __self__.type = type
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_network(datacenter_id=None,name=None,opts=None):
    """
    The `vsphere_network` data source can be used to discover the ID of a network
    in vSphere. This can be any network that can be used as the backing for a
    network interface for `vsphere_virtual_machine` or any other vSphere resource
    that requires a network. This includes standard (host-based) port groups, DVS
    port groups, or opaque networks such as those managed by NSX.
    """
    __args__ = dict()

    __args__['datacenterId'] = datacenter_id
    __args__['name'] = name
    __ret__ = await pulumi.runtime.invoke('vsphere:index/getNetwork:getNetwork', __args__, opts=opts)

    return GetNetworkResult(
        type=__ret__.get('type'),
        id=__ret__.get('id'))
