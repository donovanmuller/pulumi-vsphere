# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class ComputeClusterVmDependencyRule(pulumi.CustomResource):
    compute_cluster_id: pulumi.Output[str]
    """
    The [managed object reference
    ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
    resource if changed.
    """
    dependency_vm_group_name: pulumi.Output[str]
    """
    The name of the VM group that this
    rule depends on. The VMs defined in the group specified by
    `vm_group_name` will not be started until the VMs in this
    group are started.
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
    The name of the VM group that is the subject of
    this rule. The VMs defined in this group will not be started until the VMs in
    the group specified by
    `dependency_vm_group_name` are started.
    """
    def __init__(__self__, resource_name, opts=None, compute_cluster_id=None, dependency_vm_group_name=None, enabled=None, mandatory=None, name=None, vm_group_name=None, __props__=None, __name__=None, __opts__=None):
        """
        The `.ComputeClusterVmDependencyRule` resource can be used to manage
        VM dependency rules in a cluster, either created by the
        [`.ComputeCluster`][tf-vsphere-cluster-resource] resource or looked up
        by the [`.ComputeCluster`][tf-vsphere-cluster-data-source] data source.

        [tf-vsphere-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
        [tf-vsphere-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html

        A virtual machine dependency rule applies to vSphere HA, and allows
        user-defined startup orders for virtual machines in the case of host failure.
        Virtual machines are supplied via groups, which can be managed via the
        [`.ComputeClusterVmGroup`][tf-vsphere-cluster-vm-group-resource]
        resource.

        [tf-vsphere-cluster-vm-group-resource]: /docs/providers/vsphere/r/compute_cluster_vm_group.html

        > **NOTE:** This resource requires vCenter and is not available on direct ESXi
        connections.

        ## Example Usage



        ```python
        import pulumi
        import pulumi_vsphere as vsphere

        dc = vsphere.get_datacenter(name="dc1")
        datastore = vsphere.get_datastore(datacenter_id=dc.id,
            name="datastore1")
        cluster = vsphere.get_compute_cluster(datacenter_id=dc.id,
            name="cluster1")
        network = vsphere.get_network(datacenter_id=dc.id,
            name="network1")
        vm1 = vsphere.VirtualMachine("vm1",
            datastore_id=datastore.id,
            disks=[{
                "label": "disk0",
                "size": 20,
            }],
            guest_id="other3xLinux64Guest",
            memory=2048,
            network_interfaces=[{
                "networkId": network.id,
            }],
            num_cpus=2,
            resource_pool_id=cluster.resource_pool_id)
        vm2 = vsphere.VirtualMachine("vm2",
            datastore_id=datastore.id,
            disks=[{
                "label": "disk0",
                "size": 20,
            }],
            guest_id="other3xLinux64Guest",
            memory=2048,
            network_interfaces=[{
                "networkId": network.id,
            }],
            num_cpus=2,
            resource_pool_id=cluster.resource_pool_id)
        cluster_vm_group1 = vsphere.ComputeClusterVmGroup("clusterVmGroup1",
            compute_cluster_id=cluster.id,
            virtual_machine_ids=[vm1.id])
        cluster_vm_group2 = vsphere.ComputeClusterVmGroup("clusterVmGroup2",
            compute_cluster_id=cluster.id,
            virtual_machine_ids=[vm2.id])
        cluster_vm_dependency_rule = vsphere.ComputeClusterVmDependencyRule("clusterVmDependencyRule",
            compute_cluster_id=cluster.id,
            dependency_vm_group_name=cluster_vm_group1.name,
            vm_group_name=cluster_vm_group2.name)
        ```


        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compute_cluster_id: The [managed object reference
               ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
               resource if changed.
        :param pulumi.Input[str] dependency_vm_group_name: The name of the VM group that this
               rule depends on. The VMs defined in the group specified by
               `vm_group_name` will not be started until the VMs in this
               group are started.
        :param pulumi.Input[bool] enabled: Enable this rule in the cluster. Default: `true`.
        :param pulumi.Input[bool] mandatory: When this value is `true`, prevents any virtual
               machine operations that may violate this rule. Default: `false`.
        :param pulumi.Input[str] name: The name of the rule. This must be unique in the
               cluster.
        :param pulumi.Input[str] vm_group_name: The name of the VM group that is the subject of
               this rule. The VMs defined in this group will not be started until the VMs in
               the group specified by
               `dependency_vm_group_name` are started.
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

            if compute_cluster_id is None:
                raise TypeError("Missing required property 'compute_cluster_id'")
            __props__['compute_cluster_id'] = compute_cluster_id
            if dependency_vm_group_name is None:
                raise TypeError("Missing required property 'dependency_vm_group_name'")
            __props__['dependency_vm_group_name'] = dependency_vm_group_name
            __props__['enabled'] = enabled
            __props__['mandatory'] = mandatory
            __props__['name'] = name
            if vm_group_name is None:
                raise TypeError("Missing required property 'vm_group_name'")
            __props__['vm_group_name'] = vm_group_name
        super(ComputeClusterVmDependencyRule, __self__).__init__(
            'vsphere:index/computeClusterVmDependencyRule:ComputeClusterVmDependencyRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, compute_cluster_id=None, dependency_vm_group_name=None, enabled=None, mandatory=None, name=None, vm_group_name=None):
        """
        Get an existing ComputeClusterVmDependencyRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compute_cluster_id: The [managed object reference
               ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
               resource if changed.
        :param pulumi.Input[str] dependency_vm_group_name: The name of the VM group that this
               rule depends on. The VMs defined in the group specified by
               `vm_group_name` will not be started until the VMs in this
               group are started.
        :param pulumi.Input[bool] enabled: Enable this rule in the cluster. Default: `true`.
        :param pulumi.Input[bool] mandatory: When this value is `true`, prevents any virtual
               machine operations that may violate this rule. Default: `false`.
        :param pulumi.Input[str] name: The name of the rule. This must be unique in the
               cluster.
        :param pulumi.Input[str] vm_group_name: The name of the VM group that is the subject of
               this rule. The VMs defined in this group will not be started until the VMs in
               the group specified by
               `dependency_vm_group_name` are started.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["compute_cluster_id"] = compute_cluster_id
        __props__["dependency_vm_group_name"] = dependency_vm_group_name
        __props__["enabled"] = enabled
        __props__["mandatory"] = mandatory
        __props__["name"] = name
        __props__["vm_group_name"] = vm_group_name
        return ComputeClusterVmDependencyRule(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

