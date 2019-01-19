# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from . import utilities, tables

class CustomAttribute(pulumi.CustomResource):
    managed_object_type: pulumi.Output[str]
    """
    The object type that this attribute may be
    applied to. If not set, the custom attribute may be applied to any object
    type. For a full list, click here. Forces a new
    resource if changed.
    """
    name: pulumi.Output[str]
    """
    The name of the custom attribute.
    """
    def __init__(__self__, __name__, __opts__=None, managed_object_type=None, name=None):
        """
        The `vsphere_custom_attribute` resource can be used to create and manage custom
        attributes, which allow users to associate user-specific meta-information with 
        vSphere managed objects. Custom attribute values must be strings and are stored 
        on the vCenter Server and not the managed object.
        
        For more information about custom attributes, click [here][ext-custom-attributes].
        
        [ext-custom-attributes]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vcenterhost.doc/GUID-73606C4C-763C-4E27-A1DA-032E4C46219D.html
        
        > **NOTE:** Custom attributes are unsupported on direct ESXi connections 
        and require vCenter.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] managed_object_type: The object type that this attribute may be
               applied to. If not set, the custom attribute may be applied to any object
               type. For a full list, click here. Forces a new
               resource if changed.
        :param pulumi.Input[str] name: The name of the custom attribute.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['managed_object_type'] = managed_object_type

        __props__['name'] = name

        super(CustomAttribute, __self__).__init__(
            'vsphere:index/customAttribute:CustomAttribute',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

