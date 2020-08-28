# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from . import _utilities, _tables

__all__ = ['File']


class File(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 create_directories: Optional[pulumi.Input[bool]] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 datastore: Optional[pulumi.Input[str]] = None,
                 destination_file: Optional[pulumi.Input[str]] = None,
                 source_datacenter: Optional[pulumi.Input[str]] = None,
                 source_datastore: Optional[pulumi.Input[str]] = None,
                 source_file: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
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
            opts.version = _utilities.get_version()
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
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            create_directories: Optional[pulumi.Input[bool]] = None,
            datacenter: Optional[pulumi.Input[str]] = None,
            datastore: Optional[pulumi.Input[str]] = None,
            destination_file: Optional[pulumi.Input[str]] = None,
            source_datacenter: Optional[pulumi.Input[str]] = None,
            source_datastore: Optional[pulumi.Input[str]] = None,
            source_file: Optional[pulumi.Input[str]] = None) -> 'File':
        """
        Get an existing File resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
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

    @property
    @pulumi.getter(name="createDirectories")
    def create_directories(self) -> pulumi.Output[Optional[bool]]:
        """
        Create directories in `destination_file`
        path parameter if any missing for copy operation.
        """
        return pulumi.get(self, "create_directories")

    @property
    @pulumi.getter
    def datacenter(self) -> pulumi.Output[Optional[str]]:
        """
        The name of a datacenter in which the file will be
        uploaded to.
        """
        return pulumi.get(self, "datacenter")

    @property
    @pulumi.getter
    def datastore(self) -> pulumi.Output[str]:
        """
        The name of the datastore in which to upload the
        file to.
        """
        return pulumi.get(self, "datastore")

    @property
    @pulumi.getter(name="destinationFile")
    def destination_file(self) -> pulumi.Output[str]:
        """
        The path to where the file should be uploaded
        or copied to on vSphere.
        """
        return pulumi.get(self, "destination_file")

    @property
    @pulumi.getter(name="sourceDatacenter")
    def source_datacenter(self) -> pulumi.Output[Optional[str]]:
        """
        The name of a datacenter in which the file
        will be copied from. Forces a new resource if changed.
        """
        return pulumi.get(self, "source_datacenter")

    @property
    @pulumi.getter(name="sourceDatastore")
    def source_datastore(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the datastore in which file will
        be copied from. Forces a new resource if changed.
        """
        return pulumi.get(self, "source_datastore")

    @property
    @pulumi.getter(name="sourceFile")
    def source_file(self) -> pulumi.Output[str]:
        """
        The path to the file being uploaded from the
        host to vSphere or copied within vSphere. Forces a new resource if
        changed.
        """
        return pulumi.get(self, "source_file")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

