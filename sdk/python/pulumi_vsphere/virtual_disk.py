# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from . import utilities, tables

class VirtualDisk(pulumi.CustomResource):
    adapter_type: pulumi.Output[str]
    """
    The adapter type for this virtual disk. Can be
    one of `ide`, `lsiLogic`, or `busLogic`.  Default: `lsiLogic`.
    """
    create_directories: pulumi.Output[bool]
    """
    Tells the resource to create any
    directories that are a part of the `vmdk_path` parameter if they are missing.
    Default: `false`.
    """
    datacenter: pulumi.Output[str]
    """
    The name of the datacenter in which to create the
    disk. Can be omitted when when ESXi or if there is only one datacenter in
    your infrastructure.
    """
    datastore: pulumi.Output[str]
    """
    The name of the datastore in which to create the
    disk.
    """
    size: pulumi.Output[int]
    """
    Size of the disk (in GB).
    """
    type: pulumi.Output[str]
    """
    The type of disk to create. Can be one of
    `eagerZeroedThick`, `lazy`, or `thin`. Default: `eagerZeroedThick`. For
    information on what each kind of disk provisioning policy means, click
    [here][docs-vmware-vm-disk-provisioning].
    """
    vmdk_path: pulumi.Output[str]
    """
    The path, including filename, of the virtual disk to
    be created.  This needs to end in `.vmdk`.
    """
    def __init__(__self__, __name__, __opts__=None, adapter_type=None, create_directories=None, datacenter=None, datastore=None, size=None, type=None, vmdk_path=None):
        """
        The `vsphere_virtual_disk` resource can be used to create virtual disks outside
        of any given [`vsphere_virtual_machine`][docs-vsphere-virtual-machine]
        resource. These disks can be attached to a virtual machine by creating a disk
        block with the [`attach`][docs-vsphere-virtual-machine-disk-attach] parameter.
        
        [docs-vsphere-virtual-machine]: /docs/providers/vsphere/r/virtual_machine.html
        [docs-vsphere-virtual-machine-disk-attach]: /docs/providers/vsphere/r/virtual_machine.html#attach
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] adapter_type: The adapter type for this virtual disk. Can be
               one of `ide`, `lsiLogic`, or `busLogic`.  Default: `lsiLogic`.
        :param pulumi.Input[bool] create_directories: Tells the resource to create any
               directories that are a part of the `vmdk_path` parameter if they are missing.
               Default: `false`.
        :param pulumi.Input[str] datacenter: The name of the datacenter in which to create the
               disk. Can be omitted when when ESXi or if there is only one datacenter in
               your infrastructure.
        :param pulumi.Input[str] datastore: The name of the datastore in which to create the
               disk.
        :param pulumi.Input[int] size: Size of the disk (in GB).
        :param pulumi.Input[str] type: The type of disk to create. Can be one of
               `eagerZeroedThick`, `lazy`, or `thin`. Default: `eagerZeroedThick`. For
               information on what each kind of disk provisioning policy means, click
               [here][docs-vmware-vm-disk-provisioning].
        :param pulumi.Input[str] vmdk_path: The path, including filename, of the virtual disk to
               be created.  This needs to end in `.vmdk`.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['adapter_type'] = adapter_type

        __props__['create_directories'] = create_directories

        __props__['datacenter'] = datacenter

        if not datastore:
            raise TypeError('Missing required property datastore')
        __props__['datastore'] = datastore

        if not size:
            raise TypeError('Missing required property size')
        __props__['size'] = size

        __props__['type'] = type

        if not vmdk_path:
            raise TypeError('Missing required property vmdk_path')
        __props__['vmdk_path'] = vmdk_path

        super(VirtualDisk, __self__).__init__(
            'vsphere:index/virtualDisk:VirtualDisk',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

