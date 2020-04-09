# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class License(pulumi.CustomResource):
    edition_key: pulumi.Output[str]
    """
    The product edition of the license key.
    """
    labels: pulumi.Output[dict]
    """
    A map of key/value pairs to be attached as labels (tags) to the license key.
    """
    license_key: pulumi.Output[str]
    """
    The license key to add.
    """
    name: pulumi.Output[str]
    """
    The display name for the license.
    """
    total: pulumi.Output[float]
    """
    Total number of units (example: CPUs) contained in the license.
    """
    used: pulumi.Output[float]
    """
    The number of units (example: CPUs) assigned to this license.
    """
    def __init__(__self__, resource_name, opts=None, labels=None, license_key=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a VMware vSphere license resource. This can be used to add and remove license keys.



        > This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/r/license.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] labels: A map of key/value pairs to be attached as labels (tags) to the license key.
        :param pulumi.Input[str] license_key: The license key to add.
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

            __props__['labels'] = labels
            if license_key is None:
                raise TypeError("Missing required property 'license_key'")
            __props__['license_key'] = license_key
            __props__['edition_key'] = None
            __props__['name'] = None
            __props__['total'] = None
            __props__['used'] = None
        super(License, __self__).__init__(
            'vsphere:index/license:License',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, edition_key=None, labels=None, license_key=None, name=None, total=None, used=None):
        """
        Get an existing License resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] edition_key: The product edition of the license key.
        :param pulumi.Input[dict] labels: A map of key/value pairs to be attached as labels (tags) to the license key.
        :param pulumi.Input[str] license_key: The license key to add.
        :param pulumi.Input[str] name: The display name for the license.
        :param pulumi.Input[float] total: Total number of units (example: CPUs) contained in the license.
        :param pulumi.Input[float] used: The number of units (example: CPUs) assigned to this license.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["edition_key"] = edition_key
        __props__["labels"] = labels
        __props__["license_key"] = license_key
        __props__["name"] = name
        __props__["total"] = total
        __props__["used"] = used
        return License(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

