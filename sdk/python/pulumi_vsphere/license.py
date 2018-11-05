# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from . import utilities

class License(pulumi.CustomResource):
    """
    Provides a VMware vSphere license resource. This can be used to add and remove license keys.
    """
    def __init__(__self__, __name__, __opts__=None, labels=None, license_key=None):
        """Create a License resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['labels'] = labels

        if not license_key:
            raise TypeError('Missing required property license_key')
        __props__['licenseKey'] = license_key

        __props__['edition_key'] = None
        __props__['name'] = None
        __props__['total'] = None
        __props__['used'] = None

        super(License, __self__).__init__(
            'vsphere:index/license:License',
            __name__,
            __props__,
            __opts__)

