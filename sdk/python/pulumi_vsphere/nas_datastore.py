# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from . import utilities

class NasDatastore(pulumi.CustomResource):
    """
    The `vsphere_nas_datastore` resource can be used to create and manage NAS
    datastores on an ESXi host or a set of hosts. The resource supports mounting
    NFS v3 and v4.1 shares to be used as datastores.
    
    ~> **NOTE:** Unlike [`vsphere_vmfs_datastore`][resource-vmfs-datastore], a NAS
    datastore is only mounted on the hosts you choose to mount it on. To mount on
    multiple hosts, you must specify each host that you want to add in the
    `host_system_ids` argument.
    
    [resource-vmfs-datastore]: /docs/providers/vsphere/r/vmfs_datastore.html
    """
    def __init__(__self__, __name__, __opts__=None, access_mode=None, custom_attributes=None, datastore_cluster_id=None, folder=None, host_system_ids=None, name=None, remote_hosts=None, remote_path=None, security_type=None, tags=None, type=None):
        """Create a NasDatastore resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['accessMode'] = access_mode

        __props__['customAttributes'] = custom_attributes

        __props__['datastoreClusterId'] = datastore_cluster_id

        __props__['folder'] = folder

        if not host_system_ids:
            raise TypeError('Missing required property host_system_ids')
        __props__['hostSystemIds'] = host_system_ids

        __props__['name'] = name

        if not remote_hosts:
            raise TypeError('Missing required property remote_hosts')
        __props__['remoteHosts'] = remote_hosts

        if not remote_path:
            raise TypeError('Missing required property remote_path')
        __props__['remotePath'] = remote_path

        __props__['securityType'] = security_type

        __props__['tags'] = tags

        __props__['type'] = type

        __props__['accessible'] = None
        __props__['capacity'] = None
        __props__['free_space'] = None
        __props__['maintenance_mode'] = None
        __props__['multiple_host_access'] = None
        __props__['protocol_endpoint'] = None
        __props__['uncommitted_space'] = None
        __props__['url'] = None

        super(NasDatastore, __self__).__init__(
            'vsphere:index/nasDatastore:NasDatastore',
            __name__,
            __props__,
            __opts__)

