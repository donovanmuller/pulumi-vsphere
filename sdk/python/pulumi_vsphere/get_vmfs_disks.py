# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from . import utilities, tables

class GetVmfsDisksResult(object):
    """
    A collection of values returned by getVmfsDisks.
    """
    def __init__(__self__, disks=None, id=None):
        if disks and not isinstance(disks, list):
            raise TypeError('Expected argument disks to be a list')
        __self__.disks = disks
        """
        A lexicographically sorted list of devices discovered by the
        operation, matching the supplied `filter`, if provided.
        """
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_vmfs_disks(filter=None, host_system_id=None, rescan=None):
    """
    The `vsphere_vmfs_disks` data source can be used to discover the storage
    devices available on an ESXi host. This data source can be combined with the
    [`vsphere_vmfs_datastore`][data-source-vmfs-datastore] resource to create VMFS
    datastores based off a set of discovered disks.
    
    [data-source-vmfs-datastore]: /docs/providers/vsphere/r/vmfs_datastore.html
    """
    __args__ = dict()

    __args__['filter'] = filter
    __args__['hostSystemId'] = host_system_id
    __args__['rescan'] = rescan
    __ret__ = await pulumi.runtime.invoke('vsphere:index/getVmfsDisks:getVmfsDisks', __args__)

    return GetVmfsDisksResult(
        disks=__ret__.get('disks'),
        id=__ret__.get('id'))
