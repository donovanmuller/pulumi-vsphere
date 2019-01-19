# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from . import utilities, tables

class GetHostResult(object):
    """
    A collection of values returned by getHost.
    """
    def __init__(__self__, resource_pool_id=None, id=None):
        if resource_pool_id and not isinstance(resource_pool_id, str):
            raise TypeError('Expected argument resource_pool_id to be a str')
        __self__.resource_pool_id = resource_pool_id
        """
        The [managed object ID][docs-about-morefs] of the host's
        root resource pool.
        """
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_host(datacenter_id=None, name=None):
    """
    The `vsphere_host` data source can be used to discover the ID of a vSphere
    host. This can then be used with resources or data sources that require a host
    managed object reference ID.
    """
    __args__ = dict()

    __args__['datacenterId'] = datacenter_id
    __args__['name'] = name
    __ret__ = await pulumi.runtime.invoke('vsphere:index/getHost:getHost', __args__)

    return GetHostResult(
        resource_pool_id=__ret__.get('resourcePoolId'),
        id=__ret__.get('id'))
