# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class NasDatastore(pulumi.CustomResource):
    access_mode: pulumi.Output[str]
    """
    Access mode for the mount point. Can be one of
    `readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
    that the datastore will be read-write depending on the permissions of the
    actual share. Default: `readWrite`. Forces a new resource if changed.
    """
    accessible: pulumi.Output[bool]
    """
    The connectivity status of the datastore. If this is `false`,
    some other computed attributes may be out of date.
    """
    capacity: pulumi.Output[float]
    """
    Maximum capacity of the datastore, in megabytes.
    """
    custom_attributes: pulumi.Output[dict]
    """
    Map of custom attribute ids to attribute 
    value strings to set on datasource resource. See
    [here][docs-setting-custom-attributes] for a reference on how to set values
    for custom attributes.
    """
    datastore_cluster_id: pulumi.Output[str]
    """
    The [managed object
    ID][docs-about-morefs] of a datastore cluster to put this datastore in.
    Conflicts with `folder`.
    """
    folder: pulumi.Output[str]
    """
    The path to the datastore folder to put the datastore in.
    """
    free_space: pulumi.Output[float]
    """
    Available space of this datastore, in megabytes.
    """
    host_system_ids: pulumi.Output[list]
    """
    The [managed object IDs][docs-about-morefs] of
    the hosts to mount the datastore on.
    """
    maintenance_mode: pulumi.Output[str]
    """
    The current maintenance mode state of the datastore.
    """
    multiple_host_access: pulumi.Output[bool]
    """
    If `true`, more than one host in the datacenter has
    been configured with access to the datastore.
    """
    name: pulumi.Output[str]
    """
    The name of the datastore. Forces a new resource if
    changed.
    """
    protocol_endpoint: pulumi.Output[str]
    """
    Indicates that this NAS volume is a protocol endpoint.
    This field is only populated if the host supports virtual datastores.
    """
    remote_hosts: pulumi.Output[list]
    """
    The hostnames or IP addresses of the remote
    server or servers. Only one element should be present for NFS v3 but multiple
    can be present for NFS v4.1. Forces a new resource if changed.
    """
    remote_path: pulumi.Output[str]
    """
    The remote path of the mount point. Forces a new
    resource if changed.
    """
    security_type: pulumi.Output[str]
    """
    The security type to use when using NFS v4.1.
    Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
    if changed.
    """
    tags: pulumi.Output[list]
    """
    The IDs of any tags to attach to this resource. See
    [here][docs-applying-tags] for a reference on how to apply tags.
    """
    type: pulumi.Output[str]
    """
    The type of NAS volume. Can be one of `NFS` (to denote
    v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
    changed.
    """
    uncommitted_space: pulumi.Output[float]
    """
    Total additional storage space, in megabytes,
    potentially used by all virtual machines on this datastore.
    """
    url: pulumi.Output[str]
    """
    The unique locator for the datastore.
    """
    def __init__(__self__, resource_name, opts=None, access_mode=None, custom_attributes=None, datastore_cluster_id=None, folder=None, host_system_ids=None, name=None, remote_hosts=None, remote_path=None, security_type=None, tags=None, type=None, __props__=None, __name__=None, __opts__=None):
        """
        The `.NasDatastore` resource can be used to create and manage NAS
        datastores on an ESXi host or a set of hosts. The resource supports mounting
        NFS v3 and v4.1 shares to be used as datastores.

        > **NOTE:** Unlike [`.VmfsDatastore`][resource-vmfs-datastore], a NAS
        datastore is only mounted on the hosts you choose to mount it on. To mount on
        multiple hosts, you must specify each host that you want to add in the
        `host_system_ids` argument.

        [resource-vmfs-datastore]: /docs/providers/vsphere/r/vmfs_datastore.html



        > This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/r/nas_datastore.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_mode: Access mode for the mount point. Can be one of
               `readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
               that the datastore will be read-write depending on the permissions of the
               actual share. Default: `readWrite`. Forces a new resource if changed.
        :param pulumi.Input[dict] custom_attributes: Map of custom attribute ids to attribute 
               value strings to set on datasource resource. See
               [here][docs-setting-custom-attributes] for a reference on how to set values
               for custom attributes.
        :param pulumi.Input[str] datastore_cluster_id: The [managed object
               ID][docs-about-morefs] of a datastore cluster to put this datastore in.
               Conflicts with `folder`.
        :param pulumi.Input[str] folder: The path to the datastore folder to put the datastore in.
        :param pulumi.Input[list] host_system_ids: The [managed object IDs][docs-about-morefs] of
               the hosts to mount the datastore on.
        :param pulumi.Input[str] name: The name of the datastore. Forces a new resource if
               changed.
        :param pulumi.Input[list] remote_hosts: The hostnames or IP addresses of the remote
               server or servers. Only one element should be present for NFS v3 but multiple
               can be present for NFS v4.1. Forces a new resource if changed.
        :param pulumi.Input[str] remote_path: The remote path of the mount point. Forces a new
               resource if changed.
        :param pulumi.Input[str] security_type: The security type to use when using NFS v4.1.
               Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
               if changed.
        :param pulumi.Input[list] tags: The IDs of any tags to attach to this resource. See
               [here][docs-applying-tags] for a reference on how to apply tags.
        :param pulumi.Input[str] type: The type of NAS volume. Can be one of `NFS` (to denote
               v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
               changed.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['access_mode'] = access_mode
            __props__['custom_attributes'] = custom_attributes
            __props__['datastore_cluster_id'] = datastore_cluster_id
            __props__['folder'] = folder
            if host_system_ids is None:
                raise TypeError("Missing required property 'host_system_ids'")
            __props__['host_system_ids'] = host_system_ids
            __props__['name'] = name
            if remote_hosts is None:
                raise TypeError("Missing required property 'remote_hosts'")
            __props__['remote_hosts'] = remote_hosts
            if remote_path is None:
                raise TypeError("Missing required property 'remote_path'")
            __props__['remote_path'] = remote_path
            __props__['security_type'] = security_type
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
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, access_mode=None, accessible=None, capacity=None, custom_attributes=None, datastore_cluster_id=None, folder=None, free_space=None, host_system_ids=None, maintenance_mode=None, multiple_host_access=None, name=None, protocol_endpoint=None, remote_hosts=None, remote_path=None, security_type=None, tags=None, type=None, uncommitted_space=None, url=None):
        """
        Get an existing NasDatastore resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_mode: Access mode for the mount point. Can be one of
               `readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
               that the datastore will be read-write depending on the permissions of the
               actual share. Default: `readWrite`. Forces a new resource if changed.
        :param pulumi.Input[bool] accessible: The connectivity status of the datastore. If this is `false`,
               some other computed attributes may be out of date.
        :param pulumi.Input[float] capacity: Maximum capacity of the datastore, in megabytes.
        :param pulumi.Input[dict] custom_attributes: Map of custom attribute ids to attribute 
               value strings to set on datasource resource. See
               [here][docs-setting-custom-attributes] for a reference on how to set values
               for custom attributes.
        :param pulumi.Input[str] datastore_cluster_id: The [managed object
               ID][docs-about-morefs] of a datastore cluster to put this datastore in.
               Conflicts with `folder`.
        :param pulumi.Input[str] folder: The path to the datastore folder to put the datastore in.
        :param pulumi.Input[float] free_space: Available space of this datastore, in megabytes.
        :param pulumi.Input[list] host_system_ids: The [managed object IDs][docs-about-morefs] of
               the hosts to mount the datastore on.
        :param pulumi.Input[str] maintenance_mode: The current maintenance mode state of the datastore.
        :param pulumi.Input[bool] multiple_host_access: If `true`, more than one host in the datacenter has
               been configured with access to the datastore.
        :param pulumi.Input[str] name: The name of the datastore. Forces a new resource if
               changed.
        :param pulumi.Input[str] protocol_endpoint: Indicates that this NAS volume is a protocol endpoint.
               This field is only populated if the host supports virtual datastores.
        :param pulumi.Input[list] remote_hosts: The hostnames or IP addresses of the remote
               server or servers. Only one element should be present for NFS v3 but multiple
               can be present for NFS v4.1. Forces a new resource if changed.
        :param pulumi.Input[str] remote_path: The remote path of the mount point. Forces a new
               resource if changed.
        :param pulumi.Input[str] security_type: The security type to use when using NFS v4.1.
               Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
               if changed.
        :param pulumi.Input[list] tags: The IDs of any tags to attach to this resource. See
               [here][docs-applying-tags] for a reference on how to apply tags.
        :param pulumi.Input[str] type: The type of NAS volume. Can be one of `NFS` (to denote
               v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
               changed.
        :param pulumi.Input[float] uncommitted_space: Total additional storage space, in megabytes,
               potentially used by all virtual machines on this datastore.
        :param pulumi.Input[str] url: The unique locator for the datastore.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["access_mode"] = access_mode
        __props__["accessible"] = accessible
        __props__["capacity"] = capacity
        __props__["custom_attributes"] = custom_attributes
        __props__["datastore_cluster_id"] = datastore_cluster_id
        __props__["folder"] = folder
        __props__["free_space"] = free_space
        __props__["host_system_ids"] = host_system_ids
        __props__["maintenance_mode"] = maintenance_mode
        __props__["multiple_host_access"] = multiple_host_access
        __props__["name"] = name
        __props__["protocol_endpoint"] = protocol_endpoint
        __props__["remote_hosts"] = remote_hosts
        __props__["remote_path"] = remote_path
        __props__["security_type"] = security_type
        __props__["tags"] = tags
        __props__["type"] = type
        __props__["uncommitted_space"] = uncommitted_space
        __props__["url"] = url
        return NasDatastore(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

