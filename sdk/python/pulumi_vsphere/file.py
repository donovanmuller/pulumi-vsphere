# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from . import utilities, tables

class File(pulumi.CustomResource):
    """
    The `vsphere_file` resource can be used to upload files (such as virtual disk
    files) from the host machine that Terraform is running on to a target
    datastore.  The resource can also be used to copy files between datastores, or
    from one location to another on the same datastore.
    
    Updates to destination parameters such as `datacenter`, `datastore`, or
    `destination_file` will move the managed file a new destination based on the
    values of the new settings.  If any source parameter is changed, such as
    `source_datastore`, `source_datacenter` or `source_file`), the resource will be
    re-created. Depending on if destination parameters are being changed as well,
    this may result in the destination file either being overwritten or deleted at
    the old location.
    """
    def __init__(__self__, __name__, __opts__=None, create_directories=None, datacenter=None, datastore=None, destination_file=None, source_datacenter=None, source_datastore=None, source_file=None):
        """Create a File resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['create_directories'] = create_directories

        __props__['datacenter'] = datacenter

        if not datastore:
            raise TypeError('Missing required property datastore')
        __props__['datastore'] = datastore

        if not destination_file:
            raise TypeError('Missing required property destination_file')
        __props__['destination_file'] = destination_file

        __props__['source_datacenter'] = source_datacenter

        __props__['source_datastore'] = source_datastore

        if not source_file:
            raise TypeError('Missing required property source_file')
        __props__['source_file'] = source_file

        super(File, __self__).__init__(
            'vsphere:index/file:File',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

