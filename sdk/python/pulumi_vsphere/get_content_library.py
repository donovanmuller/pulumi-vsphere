# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetContentLibraryResult:
    """
    A collection of values returned by getContentLibrary.
    """
    def __init__(__self__, id=None, name=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
class AwaitableGetContentLibraryResult(GetContentLibraryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContentLibraryResult(
            id=self.id,
            name=self.name)

def get_content_library(name=None,opts=None):
    """
    The `.ContentLibrary` data source can be used to discover the ID of a Content Library.

    > **NOTE:** This resource requires vCenter and is not available on direct ESXi
    connections.




    :param str name: The name of the Content Library.
    """
    __args__ = dict()


    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('vsphere:index/getContentLibrary:getContentLibrary', __args__, opts=opts).value

    return AwaitableGetContentLibraryResult(
        id=__ret__.get('id'),
        name=__ret__.get('name'))
