# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetPolicyResult:
    """
    A collection of values returned by getPolicy.
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
class AwaitableGetPolicyResult(GetPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPolicyResult(
            id=self.id,
            name=self.name)

def get_policy(name=None,opts=None):
    """
    The `.getPolicy` data source can be used to discover the UUID of a
    vSphere storage policy. This can then be used with resources or data sources that
    require a storage policy.

    > **NOTE:** Storage policy support is unsupported on direct ESXi connections and
    requires vCenter 6.0 or higher.



    > This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/d/storage_policy.html.markdown.


    :param str name: The name of the storage policy.
    """
    __args__ = dict()


    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('vsphere:index/getPolicy:getPolicy', __args__, opts=opts).value

    return AwaitableGetPolicyResult(
        id=__ret__.get('id'),
        name=__ret__.get('name'))
