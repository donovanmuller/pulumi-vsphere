# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class ComputeClusterHostGroup(pulumi.CustomResource):
    """
    The `vsphere_compute_cluster_host_group` resource can be used to manage groups
    of hosts in a cluster, either created by the
    [`vsphere_compute_cluster`][tf-vsphere-cluster-resource] resource or looked up
    by the [`vsphere_compute_cluster`][tf-vsphere-cluster-data-source] data source.
    
    [tf-vsphere-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
    [tf-vsphere-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html
    
    This resource mainly serves as an input to the
    [`vsphere_compute_cluster_vm_host_rule`][tf-vsphere-cluster-vm-host-rule-resource]
    resource - see the documentation for that resource for further details on how
    to use host groups.
    
    [tf-vsphere-cluster-vm-host-rule-resource]: /docs/providers/vsphere/r/compute_cluster_vm_host_rule.html
    
    ~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
    connections.
    
    ~> **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.
    """
    def __init__(__self__, __name__, __opts__=None, compute_cluster_id=None, host_system_ids=None, name=None):
        """Create a ComputeClusterHostGroup resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not compute_cluster_id:
            raise TypeError('Missing required property compute_cluster_id')
        elif not isinstance(compute_cluster_id, basestring):
            raise TypeError('Expected property compute_cluster_id to be a basestring')
        __self__.compute_cluster_id = compute_cluster_id
        """
        The [managed object reference
        ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
        resource if changed.
        """
        __props__['computeClusterId'] = compute_cluster_id

        if host_system_ids and not isinstance(host_system_ids, list):
            raise TypeError('Expected property host_system_ids to be a list')
        __self__.host_system_ids = host_system_ids
        """
        The [managed object IDs][docs-about-morefs] of
        the hosts to put in the cluster.
        """
        __props__['hostSystemIds'] = host_system_ids

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the host group. This must be unique in the
        cluster. Forces a new resource if changed.
        """
        __props__['name'] = name

        super(ComputeClusterHostGroup, __self__).__init__(
            'vsphere:index/computeClusterHostGroup:ComputeClusterHostGroup',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'computeClusterId' in outs:
            self.compute_cluster_id = outs['computeClusterId']
        if 'hostSystemIds' in outs:
            self.host_system_ids = outs['hostSystemIds']
        if 'name' in outs:
            self.name = outs['name']
