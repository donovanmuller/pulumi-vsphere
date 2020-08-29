# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from . import _utilities, _tables

__all__ = ['ComputeClusterHostGroup']


class ComputeClusterHostGroup(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compute_cluster_id: Optional[pulumi.Input[str]] = None,
                 host_system_ids: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a ComputeClusterHostGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compute_cluster_id: The managed object reference
               ID of the cluster to put the group in.  Forces a new
               resource if changed.
        :param pulumi.Input[List[pulumi.Input[str]]] host_system_ids: The managed object IDs of
               the hosts to put in the cluster.
        :param pulumi.Input[str] name: The name of the host group. This must be unique in the
               cluster. Forces a new resource if changed.
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

            if compute_cluster_id is None:
                raise TypeError("Missing required property 'compute_cluster_id'")
            __props__['compute_cluster_id'] = compute_cluster_id
            __props__['host_system_ids'] = host_system_ids
            __props__['name'] = name
        super(ComputeClusterHostGroup, __self__).__init__(
            'vsphere:index/computeClusterHostGroup:ComputeClusterHostGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compute_cluster_id: Optional[pulumi.Input[str]] = None,
            host_system_ids: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'ComputeClusterHostGroup':
        """
        Get an existing ComputeClusterHostGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compute_cluster_id: The managed object reference
               ID of the cluster to put the group in.  Forces a new
               resource if changed.
        :param pulumi.Input[List[pulumi.Input[str]]] host_system_ids: The managed object IDs of
               the hosts to put in the cluster.
        :param pulumi.Input[str] name: The name of the host group. This must be unique in the
               cluster. Forces a new resource if changed.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["compute_cluster_id"] = compute_cluster_id
        __props__["host_system_ids"] = host_system_ids
        __props__["name"] = name
        return ComputeClusterHostGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="computeClusterId")
    def compute_cluster_id(self) -> pulumi.Output[str]:
        """
        The managed object reference
        ID of the cluster to put the group in.  Forces a new
        resource if changed.
        """
        return pulumi.get(self, "compute_cluster_id")

    @property
    @pulumi.getter(name="hostSystemIds")
    def host_system_ids(self) -> pulumi.Output[Optional[List[str]]]:
        """
        The managed object IDs of
        the hosts to put in the cluster.
        """
        return pulumi.get(self, "host_system_ids")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the host group. This must be unique in the
        cluster. Forces a new resource if changed.
        """
        return pulumi.get(self, "name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

