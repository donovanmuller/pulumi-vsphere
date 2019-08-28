# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class DatastoreCluster(pulumi.CustomResource):
    custom_attributes: pulumi.Output[dict]
    """
    A map of custom attribute ids to attribute
    value strings to set for the datastore cluster. See
    [here][docs-setting-custom-attributes] for a reference on how to set values
    for custom attributes.
    """
    datacenter_id: pulumi.Output[str]
    """
    The [managed object ID][docs-about-morefs] of
    the datacenter to create the datastore cluster in. Forces a new resource if
    changed.
    """
    folder: pulumi.Output[str]
    name: pulumi.Output[str]
    """
    The name of the datastore cluster.
    """
    sdrs_advanced_options: pulumi.Output[dict]
    sdrs_automation_level: pulumi.Output[str]
    """
    The global automation level for all
    virtual machines in this datastore cluster. Default: `manual`.
    """
    sdrs_default_intra_vm_affinity: pulumi.Output[bool]
    """
    When `true`, all disks in a
    single virtual machine will be kept on the same datastore. Default: `true`.
    """
    sdrs_enabled: pulumi.Output[bool]
    """
    Enable Storage DRS for this datastore cluster.
    Default: `false`.
    """
    sdrs_free_space_threshold: pulumi.Output[float]
    """
    The free space threshold to use.
    When set to `utilization`, `drs_space_utilization_threshold` is used, and
    when set to `freeSpace`, `drs_free_space_threshold` is used. Default:
    `utilization`.
    """
    sdrs_free_space_threshold_mode: pulumi.Output[str]
    sdrs_free_space_utilization_difference: pulumi.Output[float]
    """
    The threshold, in
    percent, of difference between space utilization in datastores before storage
    DRS makes decisions to balance the space. Default: `5` percent.
    """
    sdrs_io_balance_automation_level: pulumi.Output[str]
    """
    Overrides the default
    automation settings when correcting I/O load imbalances.
    """
    sdrs_io_latency_threshold: pulumi.Output[float]
    """
    The I/O latency threshold, in
    milliseconds, that storage DRS uses to make recommendations to move disks
    from this datastore. Default: `15` seconds.
    """
    sdrs_io_load_balance_enabled: pulumi.Output[bool]
    """
    Enable I/O load balancing for
    this datastore cluster. Default: `true`.
    """
    sdrs_io_load_imbalance_threshold: pulumi.Output[float]
    """
    The difference between load
    in datastores in the cluster before storage DRS makes recommendations to
    balance the load. Default: `5` percent.
    """
    sdrs_io_reservable_iops_threshold: pulumi.Output[float]
    """
    The threshold of reservable
    IOPS of all virtual machines on the datastore before storage DRS makes
    recommendations to move VMs off of a datastore. Note that this setting should
    only be set if `sdrs_io_reservable_percent_threshold` cannot make an accurate
    estimate of the capacity of the datastores in your cluster, and should be set
    to roughly 50-60% of the worst case peak performance of the backing LUNs.
    """
    sdrs_io_reservable_percent_threshold: pulumi.Output[float]
    """
    The threshold, in
    percent, of actual estimated performance of the datastore (in IOPS) that
    storage DRS uses to make recommendations to move VMs off of a datastore when
    the total reservable IOPS exceeds the threshold. Default: `60` percent.
    """
    sdrs_io_reservable_threshold_mode: pulumi.Output[str]
    """
    The reservable IOPS
    threshold setting to use, `sdrs_io_reservable_percent_threshold` in the event
    of `automatic`, or `sdrs_io_reservable_iops_threshold` in the event of
    `manual`. Default: `automatic`.
    """
    sdrs_load_balance_interval: pulumi.Output[float]
    """
    The storage DRS poll interval, in
    minutes. Default: `480` minutes.
    """
    sdrs_policy_enforcement_automation_level: pulumi.Output[str]
    """
    Overrides the default
    automation settings when correcting storage and VM policy violations.
    """
    sdrs_rule_enforcement_automation_level: pulumi.Output[str]
    """
    Overrides the default
    automation settings when correcting affinity rule violations.
    """
    sdrs_space_balance_automation_level: pulumi.Output[str]
    """
    Overrides the default
    automation settings when correcting disk space imbalances.
    """
    sdrs_space_utilization_threshold: pulumi.Output[float]
    sdrs_vm_evacuation_automation_level: pulumi.Output[str]
    """
    Overrides the default
    automation settings when generating recommendations for datastore evacuation.
    """
    tags: pulumi.Output[list]
    """
    The IDs of any tags to attach to this resource. See
    [here][docs-applying-tags] for a reference on how to apply tags.
    """
    def __init__(__self__, resource_name, opts=None, custom_attributes=None, datacenter_id=None, folder=None, name=None, sdrs_advanced_options=None, sdrs_automation_level=None, sdrs_default_intra_vm_affinity=None, sdrs_enabled=None, sdrs_free_space_threshold=None, sdrs_free_space_threshold_mode=None, sdrs_free_space_utilization_difference=None, sdrs_io_balance_automation_level=None, sdrs_io_latency_threshold=None, sdrs_io_load_balance_enabled=None, sdrs_io_load_imbalance_threshold=None, sdrs_io_reservable_iops_threshold=None, sdrs_io_reservable_percent_threshold=None, sdrs_io_reservable_threshold_mode=None, sdrs_load_balance_interval=None, sdrs_policy_enforcement_automation_level=None, sdrs_rule_enforcement_automation_level=None, sdrs_space_balance_automation_level=None, sdrs_space_utilization_threshold=None, sdrs_vm_evacuation_automation_level=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        The `.DatastoreCluster` resource can be used to create and manage
        datastore clusters. This can be used to create groups of datastores with a
        shared management interface, allowing for resource control and load balancing
        through Storage DRS.
        
        For more information on vSphere datastore clusters and Storage DRS, see [this
        page][ref-vsphere-datastore-clusters].
        
        [ref-vsphere-datastore-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-598DF695-107E-406B-9C95-0AF961FC227A.html
        
        > **NOTE:** This resource requires vCenter and is not available on direct ESXi
        connections.
        
        > **NOTE:** Storage DRS requires a vSphere Enterprise Plus license.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] custom_attributes: A map of custom attribute ids to attribute
               value strings to set for the datastore cluster. See
               [here][docs-setting-custom-attributes] for a reference on how to set values
               for custom attributes.
        :param pulumi.Input[str] datacenter_id: The [managed object ID][docs-about-morefs] of
               the datacenter to create the datastore cluster in. Forces a new resource if
               changed.
        :param pulumi.Input[str] name: The name of the datastore cluster.
        :param pulumi.Input[str] sdrs_automation_level: The global automation level for all
               virtual machines in this datastore cluster. Default: `manual`.
        :param pulumi.Input[bool] sdrs_default_intra_vm_affinity: When `true`, all disks in a
               single virtual machine will be kept on the same datastore. Default: `true`.
        :param pulumi.Input[bool] sdrs_enabled: Enable Storage DRS for this datastore cluster.
               Default: `false`.
        :param pulumi.Input[float] sdrs_free_space_threshold: The free space threshold to use.
               When set to `utilization`, `drs_space_utilization_threshold` is used, and
               when set to `freeSpace`, `drs_free_space_threshold` is used. Default:
               `utilization`.
        :param pulumi.Input[float] sdrs_free_space_utilization_difference: The threshold, in
               percent, of difference between space utilization in datastores before storage
               DRS makes decisions to balance the space. Default: `5` percent.
        :param pulumi.Input[str] sdrs_io_balance_automation_level: Overrides the default
               automation settings when correcting I/O load imbalances.
        :param pulumi.Input[float] sdrs_io_latency_threshold: The I/O latency threshold, in
               milliseconds, that storage DRS uses to make recommendations to move disks
               from this datastore. Default: `15` seconds.
        :param pulumi.Input[bool] sdrs_io_load_balance_enabled: Enable I/O load balancing for
               this datastore cluster. Default: `true`.
        :param pulumi.Input[float] sdrs_io_load_imbalance_threshold: The difference between load
               in datastores in the cluster before storage DRS makes recommendations to
               balance the load. Default: `5` percent.
        :param pulumi.Input[float] sdrs_io_reservable_iops_threshold: The threshold of reservable
               IOPS of all virtual machines on the datastore before storage DRS makes
               recommendations to move VMs off of a datastore. Note that this setting should
               only be set if `sdrs_io_reservable_percent_threshold` cannot make an accurate
               estimate of the capacity of the datastores in your cluster, and should be set
               to roughly 50-60% of the worst case peak performance of the backing LUNs.
        :param pulumi.Input[float] sdrs_io_reservable_percent_threshold: The threshold, in
               percent, of actual estimated performance of the datastore (in IOPS) that
               storage DRS uses to make recommendations to move VMs off of a datastore when
               the total reservable IOPS exceeds the threshold. Default: `60` percent.
        :param pulumi.Input[str] sdrs_io_reservable_threshold_mode: The reservable IOPS
               threshold setting to use, `sdrs_io_reservable_percent_threshold` in the event
               of `automatic`, or `sdrs_io_reservable_iops_threshold` in the event of
               `manual`. Default: `automatic`.
        :param pulumi.Input[float] sdrs_load_balance_interval: The storage DRS poll interval, in
               minutes. Default: `480` minutes.
        :param pulumi.Input[str] sdrs_policy_enforcement_automation_level: Overrides the default
               automation settings when correcting storage and VM policy violations.
        :param pulumi.Input[str] sdrs_rule_enforcement_automation_level: Overrides the default
               automation settings when correcting affinity rule violations.
        :param pulumi.Input[str] sdrs_space_balance_automation_level: Overrides the default
               automation settings when correcting disk space imbalances.
        :param pulumi.Input[str] sdrs_vm_evacuation_automation_level: Overrides the default
               automation settings when generating recommendations for datastore evacuation.
        :param pulumi.Input[list] tags: The IDs of any tags to attach to this resource. See
               [here][docs-applying-tags] for a reference on how to apply tags.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/r/datastore_cluster.html.markdown.
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

            __props__['custom_attributes'] = custom_attributes
            if datacenter_id is None:
                raise TypeError("Missing required property 'datacenter_id'")
            __props__['datacenter_id'] = datacenter_id
            __props__['folder'] = folder
            __props__['name'] = name
            __props__['sdrs_advanced_options'] = sdrs_advanced_options
            __props__['sdrs_automation_level'] = sdrs_automation_level
            __props__['sdrs_default_intra_vm_affinity'] = sdrs_default_intra_vm_affinity
            __props__['sdrs_enabled'] = sdrs_enabled
            __props__['sdrs_free_space_threshold'] = sdrs_free_space_threshold
            __props__['sdrs_free_space_threshold_mode'] = sdrs_free_space_threshold_mode
            __props__['sdrs_free_space_utilization_difference'] = sdrs_free_space_utilization_difference
            __props__['sdrs_io_balance_automation_level'] = sdrs_io_balance_automation_level
            __props__['sdrs_io_latency_threshold'] = sdrs_io_latency_threshold
            __props__['sdrs_io_load_balance_enabled'] = sdrs_io_load_balance_enabled
            __props__['sdrs_io_load_imbalance_threshold'] = sdrs_io_load_imbalance_threshold
            __props__['sdrs_io_reservable_iops_threshold'] = sdrs_io_reservable_iops_threshold
            __props__['sdrs_io_reservable_percent_threshold'] = sdrs_io_reservable_percent_threshold
            __props__['sdrs_io_reservable_threshold_mode'] = sdrs_io_reservable_threshold_mode
            __props__['sdrs_load_balance_interval'] = sdrs_load_balance_interval
            __props__['sdrs_policy_enforcement_automation_level'] = sdrs_policy_enforcement_automation_level
            __props__['sdrs_rule_enforcement_automation_level'] = sdrs_rule_enforcement_automation_level
            __props__['sdrs_space_balance_automation_level'] = sdrs_space_balance_automation_level
            __props__['sdrs_space_utilization_threshold'] = sdrs_space_utilization_threshold
            __props__['sdrs_vm_evacuation_automation_level'] = sdrs_vm_evacuation_automation_level
            __props__['tags'] = tags
        super(DatastoreCluster, __self__).__init__(
            'vsphere:index/datastoreCluster:DatastoreCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, custom_attributes=None, datacenter_id=None, folder=None, name=None, sdrs_advanced_options=None, sdrs_automation_level=None, sdrs_default_intra_vm_affinity=None, sdrs_enabled=None, sdrs_free_space_threshold=None, sdrs_free_space_threshold_mode=None, sdrs_free_space_utilization_difference=None, sdrs_io_balance_automation_level=None, sdrs_io_latency_threshold=None, sdrs_io_load_balance_enabled=None, sdrs_io_load_imbalance_threshold=None, sdrs_io_reservable_iops_threshold=None, sdrs_io_reservable_percent_threshold=None, sdrs_io_reservable_threshold_mode=None, sdrs_load_balance_interval=None, sdrs_policy_enforcement_automation_level=None, sdrs_rule_enforcement_automation_level=None, sdrs_space_balance_automation_level=None, sdrs_space_utilization_threshold=None, sdrs_vm_evacuation_automation_level=None, tags=None):
        """
        Get an existing DatastoreCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] custom_attributes: A map of custom attribute ids to attribute
               value strings to set for the datastore cluster. See
               [here][docs-setting-custom-attributes] for a reference on how to set values
               for custom attributes.
        :param pulumi.Input[str] datacenter_id: The [managed object ID][docs-about-morefs] of
               the datacenter to create the datastore cluster in. Forces a new resource if
               changed.
        :param pulumi.Input[str] name: The name of the datastore cluster.
        :param pulumi.Input[str] sdrs_automation_level: The global automation level for all
               virtual machines in this datastore cluster. Default: `manual`.
        :param pulumi.Input[bool] sdrs_default_intra_vm_affinity: When `true`, all disks in a
               single virtual machine will be kept on the same datastore. Default: `true`.
        :param pulumi.Input[bool] sdrs_enabled: Enable Storage DRS for this datastore cluster.
               Default: `false`.
        :param pulumi.Input[float] sdrs_free_space_threshold: The free space threshold to use.
               When set to `utilization`, `drs_space_utilization_threshold` is used, and
               when set to `freeSpace`, `drs_free_space_threshold` is used. Default:
               `utilization`.
        :param pulumi.Input[float] sdrs_free_space_utilization_difference: The threshold, in
               percent, of difference between space utilization in datastores before storage
               DRS makes decisions to balance the space. Default: `5` percent.
        :param pulumi.Input[str] sdrs_io_balance_automation_level: Overrides the default
               automation settings when correcting I/O load imbalances.
        :param pulumi.Input[float] sdrs_io_latency_threshold: The I/O latency threshold, in
               milliseconds, that storage DRS uses to make recommendations to move disks
               from this datastore. Default: `15` seconds.
        :param pulumi.Input[bool] sdrs_io_load_balance_enabled: Enable I/O load balancing for
               this datastore cluster. Default: `true`.
        :param pulumi.Input[float] sdrs_io_load_imbalance_threshold: The difference between load
               in datastores in the cluster before storage DRS makes recommendations to
               balance the load. Default: `5` percent.
        :param pulumi.Input[float] sdrs_io_reservable_iops_threshold: The threshold of reservable
               IOPS of all virtual machines on the datastore before storage DRS makes
               recommendations to move VMs off of a datastore. Note that this setting should
               only be set if `sdrs_io_reservable_percent_threshold` cannot make an accurate
               estimate of the capacity of the datastores in your cluster, and should be set
               to roughly 50-60% of the worst case peak performance of the backing LUNs.
        :param pulumi.Input[float] sdrs_io_reservable_percent_threshold: The threshold, in
               percent, of actual estimated performance of the datastore (in IOPS) that
               storage DRS uses to make recommendations to move VMs off of a datastore when
               the total reservable IOPS exceeds the threshold. Default: `60` percent.
        :param pulumi.Input[str] sdrs_io_reservable_threshold_mode: The reservable IOPS
               threshold setting to use, `sdrs_io_reservable_percent_threshold` in the event
               of `automatic`, or `sdrs_io_reservable_iops_threshold` in the event of
               `manual`. Default: `automatic`.
        :param pulumi.Input[float] sdrs_load_balance_interval: The storage DRS poll interval, in
               minutes. Default: `480` minutes.
        :param pulumi.Input[str] sdrs_policy_enforcement_automation_level: Overrides the default
               automation settings when correcting storage and VM policy violations.
        :param pulumi.Input[str] sdrs_rule_enforcement_automation_level: Overrides the default
               automation settings when correcting affinity rule violations.
        :param pulumi.Input[str] sdrs_space_balance_automation_level: Overrides the default
               automation settings when correcting disk space imbalances.
        :param pulumi.Input[str] sdrs_vm_evacuation_automation_level: Overrides the default
               automation settings when generating recommendations for datastore evacuation.
        :param pulumi.Input[list] tags: The IDs of any tags to attach to this resource. See
               [here][docs-applying-tags] for a reference on how to apply tags.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/r/datastore_cluster.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["custom_attributes"] = custom_attributes
        __props__["datacenter_id"] = datacenter_id
        __props__["folder"] = folder
        __props__["name"] = name
        __props__["sdrs_advanced_options"] = sdrs_advanced_options
        __props__["sdrs_automation_level"] = sdrs_automation_level
        __props__["sdrs_default_intra_vm_affinity"] = sdrs_default_intra_vm_affinity
        __props__["sdrs_enabled"] = sdrs_enabled
        __props__["sdrs_free_space_threshold"] = sdrs_free_space_threshold
        __props__["sdrs_free_space_threshold_mode"] = sdrs_free_space_threshold_mode
        __props__["sdrs_free_space_utilization_difference"] = sdrs_free_space_utilization_difference
        __props__["sdrs_io_balance_automation_level"] = sdrs_io_balance_automation_level
        __props__["sdrs_io_latency_threshold"] = sdrs_io_latency_threshold
        __props__["sdrs_io_load_balance_enabled"] = sdrs_io_load_balance_enabled
        __props__["sdrs_io_load_imbalance_threshold"] = sdrs_io_load_imbalance_threshold
        __props__["sdrs_io_reservable_iops_threshold"] = sdrs_io_reservable_iops_threshold
        __props__["sdrs_io_reservable_percent_threshold"] = sdrs_io_reservable_percent_threshold
        __props__["sdrs_io_reservable_threshold_mode"] = sdrs_io_reservable_threshold_mode
        __props__["sdrs_load_balance_interval"] = sdrs_load_balance_interval
        __props__["sdrs_policy_enforcement_automation_level"] = sdrs_policy_enforcement_automation_level
        __props__["sdrs_rule_enforcement_automation_level"] = sdrs_rule_enforcement_automation_level
        __props__["sdrs_space_balance_automation_level"] = sdrs_space_balance_automation_level
        __props__["sdrs_space_utilization_threshold"] = sdrs_space_utilization_threshold
        __props__["sdrs_vm_evacuation_automation_level"] = sdrs_vm_evacuation_automation_level
        __props__["tags"] = tags
        return DatastoreCluster(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

