# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class CustomAttribute(pulumi.CustomResource):
    """
    The `vsphere_custom_attribute` resource can be used to create and manage custom
    attributes, which allow users to associate user-specific meta-information with 
    vSphere managed objects. Custom attribute values must be strings and are stored 
    on the vCenter Server and not the managed object.
    
    For more information about custom attributes, click [here][ext-custom-attributes].
    
    [ext-custom-attributes]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vcenterhost.doc/GUID-73606C4C-763C-4E27-A1DA-032E4C46219D.html
    
    ~> **NOTE:** Custom attributes are unsupported on direct ESXi connections 
    and require vCenter.
    """
    def __init__(__self__, __name__, __opts__=None, managed_object_type=None, name=None):
        """Create a CustomAttribute resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if managed_object_type and not isinstance(managed_object_type, basestring):
            raise TypeError('Expected property managed_object_type to be a basestring')
        __self__.managed_object_type = managed_object_type
        """
        The object type that this attribute may be
        applied to. If not set, the custom attribute may be applied to any object
        type. For a full list, click here. Forces a new
        resource if changed.
        """
        __props__['managedObjectType'] = managed_object_type

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the custom attribute.
        """
        __props__['name'] = name

        super(CustomAttribute, __self__).__init__(
            'vsphere:index/customAttribute:CustomAttribute',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'managedObjectType' in outs:
            self.managed_object_type = outs['managedObjectType']
        if 'name' in outs:
            self.name = outs['name']
