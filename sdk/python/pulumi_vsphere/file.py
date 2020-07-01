# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables


class File(pulumi.CustomResource):
    create_directories: pulumi.Output[bool]
    """
    Create directories in `destination_file`
    path parameter if any missing for copy operation.
    """
    datacenter: pulumi.Output[str]
    """
    The name of a datacenter in which the file will be
    uploaded to.
    """
    datastore: pulumi.Output[str]
    """
    The name of the datastore in which to upload the
    file to.
    """
    destination_file: pulumi.Output[str]
    """
    The path to where the file should be uploaded
    or copied to on vSphere.
    """
    source_datacenter: pulumi.Output[str]
    """
    The name of a datacenter in which the file
    will be copied from. Forces a new resource if changed.
    """
    source_datastore: pulumi.Output[str]
    """
    The name of the datastore in which file will
    be copied from. Forces a new resource if changed.
    """
    source_file: pulumi.Output[str]
    """
    The path to the file being uploaded from the
    host to vSphere or copied within vSphere. Forces a new resource if
    changed.
    """
    def __init__(__self__, resource_name, opts=None, create_directories=None, datacenter=None, datastore=None, destination_file=None, source_datacenter=None, source_datastore=None, source_file=None, __props__=None, __name__=None, __opts__=None):
        """
        The `File` resource can be used to upload files (such as virtual disk
        files) from the host machine that this provider is running on to a target
        datastore.  The resource can also be used to copy files between datastores, or
        from one location to another on the same datastore.

        Updates to destination parameters such as `datacenter`, `datastore`, or
        `destination_file` will move the managed file a new destination based on the
        values of the new settings.  If any source parameter is changed, such as
        `source_datastore`, `source_datacenter` or `source_file`), the resource will be
        re-created. Depending on if destination parameters are being changed as well,
        this may result in the destination file either being overwritten or deleted at
        the old location.

        ## Example Usage
        ### Uploading a file

        ```python
        import pulumi
        import pulumi_vsphere as vsphere

        ubuntu_disk_upload = vsphere.File("ubuntuDiskUpload",
            datacenter="my_datacenter",
            datastore="local",
            destination_file="/my_path/disks/custom_ubuntu.vmdk",
            source_file="/home/ubuntu/my_disks/custom_ubuntu.vmdk")
        ```
        ### Copying a file

        ```python
        import pulumi
        import pulumi_vsphere as vsphere

        ubuntu_disk_copy = vsphere.File("ubuntuDiskCopy",
            datacenter="my_datacenter",
            datastore="local",
            destination_file="/my_path/custom_ubuntu_id.vmdk",
            source_datacenter="my_datacenter",
            source_datastore="local",
            source_file="/my_path/disks/custom_ubuntu.vmdk")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] create_directories: Create directories in `destination_file`
               path parameter if any missing for copy operation.
        :param pulumi.Input[str] datacenter: The name of a datacenter in which the file will be
               uploaded to.
        :param pulumi.Input[str] datastore: The name of the datastore in which to upload the
               file to.
        :param pulumi.Input[str] destination_file: The path to where the file should be uploaded
               or copied to on vSphere.
        :param pulumi.Input[str] source_datacenter: The name of a datacenter in which the file
               will be copied from. Forces a new resource if changed.
        :param pulumi.Input[str] source_datastore: The name of the datastore in which file will
               be copied from. Forces a new resource if changed.
        :param pulumi.Input[str] source_file: The path to the file being uploaded from the
               host to vSphere or copied within vSphere. Forces a new resource if
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

            __props__['create_directories'] = create_directories
            __props__['datacenter'] = datacenter
            if datastore is None:
                raise TypeError("Missing required property 'datastore'")
            __props__['datastore'] = datastore
            if destination_file is None:
                raise TypeError("Missing required property 'destination_file'")
            __props__['destination_file'] = destination_file
            __props__['source_datacenter'] = source_datacenter
            __props__['source_datastore'] = source_datastore
            if source_file is None:
                raise TypeError("Missing required property 'source_file'")
            __props__['source_file'] = source_file
        super(File, __self__).__init__(
            'vsphere:index/file:File',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, create_directories=None, datacenter=None, datastore=None, destination_file=None, source_datacenter=None, source_datastore=None, source_file=None):
        """
        Get an existing File resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] create_directories: Create directories in `destination_file`
               path parameter if any missing for copy operation.
        :param pulumi.Input[str] datacenter: The name of a datacenter in which the file will be
               uploaded to.
        :param pulumi.Input[str] datastore: The name of the datastore in which to upload the
               file to.
        :param pulumi.Input[str] destination_file: The path to where the file should be uploaded
               or copied to on vSphere.
        :param pulumi.Input[str] source_datacenter: The name of a datacenter in which the file
               will be copied from. Forces a new resource if changed.
        :param pulumi.Input[str] source_datastore: The name of the datastore in which file will
               be copied from. Forces a new resource if changed.
        :param pulumi.Input[str] source_file: The path to the file being uploaded from the
               host to vSphere or copied within vSphere. Forces a new resource if
               changed.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["create_directories"] = create_directories
        __props__["datacenter"] = datacenter
        __props__["datastore"] = datastore
        __props__["destination_file"] = destination_file
        __props__["source_datacenter"] = source_datacenter
        __props__["source_datastore"] = source_datastore
        __props__["source_file"] = source_file
        return File(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
