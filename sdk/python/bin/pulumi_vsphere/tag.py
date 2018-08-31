# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class Tag(pulumi.CustomResource):
    """
    The `vsphere_tag` resource can be used to create and manage tags, which allow
    you to attach metadata to objects in the vSphere inventory to make these
    objects more sortable and searchable.
    
    For more information about tags, click [here][ext-tags-general].
    
    [ext-tags-general]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vcenterhost.doc/GUID-E8E854DD-AA97-4E0C-8419-CE84F93C4058.html
    
    ~> **NOTE:** Tagging support is unsupported on direct ESXi connections and
    requires vCenter 6.0 or higher.
    """
    def __init__(__self__, __name__, __opts__=None, category_id=None, description=None, name=None):
        """Create a Tag resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not category_id:
            raise TypeError('Missing required property category_id')
        elif not isinstance(category_id, basestring):
            raise TypeError('Expected property category_id to be a basestring')
        __self__.category_id = category_id
        """
        The unique identifier of the parent category in
        which this tag will be created. Forces a new resource if changed.
        """
        __props__['categoryId'] = category_id

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        A description for the tag.
        """
        __props__['description'] = description

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The display name of the tag. The name must be unique
        within its category.
        """
        __props__['name'] = name

        super(Tag, __self__).__init__(
            'vsphere:index/tag:Tag',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'categoryId' in outs:
            self.category_id = outs['categoryId']
        if 'description' in outs:
            self.description = outs['description']
        if 'name' in outs:
            self.name = outs['name']
