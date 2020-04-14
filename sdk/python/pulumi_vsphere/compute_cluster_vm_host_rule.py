# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class ComputeClusterVmHostRule(pulumi.CustomResource):
    affinity_host_group_name: pulumi.Output[str]
    """
    When this field is used, the virtual
    machines defined in `vm_group_name` will be run on the
    hosts defined in this host group.
    """
    anti_affinity_host_group_name: pulumi.Output[str]
    """
    When this field is used, the
    virtual machines defined in `vm_group_name` will _not_ be
    run on the hosts defined in this host group.
    """
    compute_cluster_id: pulumi.Output[str]
    """
    The [managed object reference
    ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
    resource if changed.
    """
    enabled: pulumi.Output[bool]
    """
    Enable this rule in the cluster. Default: `true`.
    """
    mandatory: pulumi.Output[bool]
    """
    When this value is `true`, prevents any virtual
    machine operations that may violate this rule. Default: `false`.
    """
    name: pulumi.Output[str]
    """
    The name of the rule. This must be unique in the
    cluster.
    """
    vm_group_name: pulumi.Output[str]
    """
    The name of the virtual machine group to use
    with this rule.
    """
    def __init__(__self__, resource_name, opts=None, affinity_host_group_name=None, anti_affinity_host_group_name=None, compute_cluster_id=None, enabled=None, mandatory=None, name=None, vm_group_name=None, __props__=None, __name__=None, __opts__=None):
        """
        The `.ComputeClusterVmHostRule` resource can be used to manage
        VM-to-host rules in a cluster, either created by the
        [`.ComputeCluster`][tf-vsphere-cluster-resource] resource or looked up
        by the [`.ComputeCluster`][tf-vsphere-cluster-data-source] data source.

        [tf-vsphere-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
        [tf-vsphere-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html

        This resource can create both _affinity rules_, where virtual machines run on
        specified hosts, or _anti-affinity_ rules, where virtual machines run on hosts
        outside of the ones specified in the rule. Virtual machines and hosts are
        supplied via groups, which can be managed via the
        [`.ComputeClusterVmGroup`][tf-vsphere-cluster-vm-group-resource] and
        [`.ComputeClusterHostGroup`][tf-vsphere-cluster-host-group-resource]
        resources.

        [tf-vsphere-cluster-vm-group-resource]: /docs/providers/vsphere/r/compute_cluster_vm_group.html
        [tf-vsphere-cluster-host-group-resource]: /docs/providers/vsphere/r/compute_cluster_host_group.html

        > **NOTE:** This resource requires vCenter and is not available on direct ESXi
        connections.

        > **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.



        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] affinity_host_group_name: When this field is used, the virtual
               machines defined in `vm_group_name` will be run on the
               hosts defined in this host group.
        :param pulumi.Input[str] anti_affinity_host_group_name: When this field is used, the
               virtual machines defined in `vm_group_name` will _not_ be
               run on the hosts defined in this host group.
        :param pulumi.Input[str] compute_cluster_id: The [managed object reference
               ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
               resource if changed.
        :param pulumi.Input[bool] enabled: Enable this rule in the cluster. Default: `true`.
        :param pulumi.Input[bool] mandatory: When this value is `true`, prevents any virtual
               machine operations that may violate this rule. Default: `false`.
        :param pulumi.Input[str] name: The name of the rule. This must be unique in the
               cluster.
        :param pulumi.Input[str] vm_group_name: The name of the virtual machine group to use
               with this rule.
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

            __props__['affinity_host_group_name'] = affinity_host_group_name
            __props__['anti_affinity_host_group_name'] = anti_affinity_host_group_name
            if compute_cluster_id is None:
                raise TypeError("Missing required property 'compute_cluster_id'")
            __props__['compute_cluster_id'] = compute_cluster_id
            __props__['enabled'] = enabled
            __props__['mandatory'] = mandatory
            __props__['name'] = name
            if vm_group_name is None:
                raise TypeError("Missing required property 'vm_group_name'")
            __props__['vm_group_name'] = vm_group_name
        super(ComputeClusterVmHostRule, __self__).__init__(
            'vsphere:index/computeClusterVmHostRule:ComputeClusterVmHostRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, affinity_host_group_name=None, anti_affinity_host_group_name=None, compute_cluster_id=None, enabled=None, mandatory=None, name=None, vm_group_name=None):
        """
        Get an existing ComputeClusterVmHostRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] affinity_host_group_name: When this field is used, the virtual
               machines defined in `vm_group_name` will be run on the
               hosts defined in this host group.
        :param pulumi.Input[str] anti_affinity_host_group_name: When this field is used, the
               virtual machines defined in `vm_group_name` will _not_ be
               run on the hosts defined in this host group.
        :param pulumi.Input[str] compute_cluster_id: The [managed object reference
               ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
               resource if changed.
        :param pulumi.Input[bool] enabled: Enable this rule in the cluster. Default: `true`.
        :param pulumi.Input[bool] mandatory: When this value is `true`, prevents any virtual
               machine operations that may violate this rule. Default: `false`.
        :param pulumi.Input[str] name: The name of the rule. This must be unique in the
               cluster.
        :param pulumi.Input[str] vm_group_name: The name of the virtual machine group to use
               with this rule.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["affinity_host_group_name"] = affinity_host_group_name
        __props__["anti_affinity_host_group_name"] = anti_affinity_host_group_name
        __props__["compute_cluster_id"] = compute_cluster_id
        __props__["enabled"] = enabled
        __props__["mandatory"] = mandatory
        __props__["name"] = name
        __props__["vm_group_name"] = vm_group_name
        return ComputeClusterVmHostRule(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

