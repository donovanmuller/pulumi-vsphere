# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class DatastoreCluster(pulumi.CustomResource):
    """
    The `vsphere_datastore_cluster` resource can be used to create and manage
    datastore clusters. This can be used to create groups of datastores with a
    shared management interface, allowing for resource control and load balancing
    through Storage DRS.
    
    For more information on vSphere datastore clusters and Storage DRS, see [this
    page][ref-vsphere-datastore-clusters].
    
    [ref-vsphere-datastore-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-598DF695-107E-406B-9C95-0AF961FC227A.html
    
    ~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
    connections.
    
    ~> **NOTE:** Storage DRS requires a vSphere Enterprise Plus license.
    """
    def __init__(__self__, __name__, __opts__=None, custom_attributes=None, datacenter_id=None, folder=None, name=None, sdrs_advanced_options=None, sdrs_automation_level=None, sdrs_default_intra_vm_affinity=None, sdrs_enabled=None, sdrs_free_space_threshold=None, sdrs_free_space_threshold_mode=None, sdrs_free_space_utilization_difference=None, sdrs_io_balance_automation_level=None, sdrs_io_latency_threshold=None, sdrs_io_load_balance_enabled=None, sdrs_io_load_imbalance_threshold=None, sdrs_io_reservable_iops_threshold=None, sdrs_io_reservable_percent_threshold=None, sdrs_io_reservable_threshold_mode=None, sdrs_load_balance_interval=None, sdrs_policy_enforcement_automation_level=None, sdrs_rule_enforcement_automation_level=None, sdrs_space_balance_automation_level=None, sdrs_space_utilization_threshold=None, sdrs_vm_evacuation_automation_level=None, tags=None):
        """Create a DatastoreCluster resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if custom_attributes and not isinstance(custom_attributes, dict):
            raise TypeError('Expected property custom_attributes to be a dict')
        __self__.custom_attributes = custom_attributes
        """
        A map of custom attribute ids to attribute
        value strings to set for the datastore cluster. See
        [here][docs-setting-custom-attributes] for a reference on how to set values
        for custom attributes.
        """
        __props__['customAttributes'] = custom_attributes

        if not datacenter_id:
            raise TypeError('Missing required property datacenter_id')
        elif not isinstance(datacenter_id, basestring):
            raise TypeError('Expected property datacenter_id to be a basestring')
        __self__.datacenter_id = datacenter_id
        """
        The [managed object ID][docs-about-morefs] of
        the datacenter to create the datastore cluster in. Forces a new resource if
        changed.
        """
        __props__['datacenterId'] = datacenter_id

        if folder and not isinstance(folder, basestring):
            raise TypeError('Expected property folder to be a basestring')
        __self__.folder = folder
        """
        The relative path to a folder to put this datastore
        cluster in.  This is a path relative to the datacenter you are deploying the
        datastore to.  Example: for the `dc1` datacenter, and a provided `folder` of
        `foo/bar`, Terraform will place a datastore cluster named
        `terraform-datastore-cluster-test` in a datastore folder located at
        `/dc1/datastore/foo/bar`, with the final inventory path being
        `/dc1/datastore/foo/bar/terraform-datastore-cluster-test`.
        """
        __props__['folder'] = folder

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the datastore cluster.
        """
        __props__['name'] = name

        if sdrs_advanced_options and not isinstance(sdrs_advanced_options, dict):
            raise TypeError('Expected property sdrs_advanced_options to be a dict')
        __self__.sdrs_advanced_options = sdrs_advanced_options
        """
        A key/value map of advanced Storage DRS
        settings that are not exposed via Terraform or the vSphere client.
        """
        __props__['sdrsAdvancedOptions'] = sdrs_advanced_options

        if sdrs_automation_level and not isinstance(sdrs_automation_level, basestring):
            raise TypeError('Expected property sdrs_automation_level to be a basestring')
        __self__.sdrs_automation_level = sdrs_automation_level
        """
        The global automation level for all
        virtual machines in this datastore cluster. Default: `manual`.
        """
        __props__['sdrsAutomationLevel'] = sdrs_automation_level

        if sdrs_default_intra_vm_affinity and not isinstance(sdrs_default_intra_vm_affinity, bool):
            raise TypeError('Expected property sdrs_default_intra_vm_affinity to be a bool')
        __self__.sdrs_default_intra_vm_affinity = sdrs_default_intra_vm_affinity
        """
        When `true`, all disks in a
        single virtual machine will be kept on the same datastore. Default: `true`.
        """
        __props__['sdrsDefaultIntraVmAffinity'] = sdrs_default_intra_vm_affinity

        if sdrs_enabled and not isinstance(sdrs_enabled, bool):
            raise TypeError('Expected property sdrs_enabled to be a bool')
        __self__.sdrs_enabled = sdrs_enabled
        """
        Enable Storage DRS for this datastore cluster.
        Default: `false`.
        """
        __props__['sdrsEnabled'] = sdrs_enabled

        if sdrs_free_space_threshold and not isinstance(sdrs_free_space_threshold, int):
            raise TypeError('Expected property sdrs_free_space_threshold to be a int')
        __self__.sdrs_free_space_threshold = sdrs_free_space_threshold
        """
        The free space threshold to use.
        When set to `utilization`, `drs_space_utilization_threshold` is used, and
        when set to `freeSpace`, `drs_free_space_threshold` is used. Default:
        `utilization`.
        """
        __props__['sdrsFreeSpaceThreshold'] = sdrs_free_space_threshold

        if sdrs_free_space_threshold_mode and not isinstance(sdrs_free_space_threshold_mode, basestring):
            raise TypeError('Expected property sdrs_free_space_threshold_mode to be a basestring')
        __self__.sdrs_free_space_threshold_mode = sdrs_free_space_threshold_mode
        """
        The free space threshold to use. When set to utilization, drs_space_utilization_threshold is used, and when set
        to freeSpace, drs_free_space_threshold is used.
        """
        __props__['sdrsFreeSpaceThresholdMode'] = sdrs_free_space_threshold_mode

        if sdrs_free_space_utilization_difference and not isinstance(sdrs_free_space_utilization_difference, int):
            raise TypeError('Expected property sdrs_free_space_utilization_difference to be a int')
        __self__.sdrs_free_space_utilization_difference = sdrs_free_space_utilization_difference
        """
        The threshold, in
        percent, of difference between space utilization in datastores before storage
        DRS makes decisions to balance the space. Default: `5` percent.
        """
        __props__['sdrsFreeSpaceUtilizationDifference'] = sdrs_free_space_utilization_difference

        if sdrs_io_balance_automation_level and not isinstance(sdrs_io_balance_automation_level, basestring):
            raise TypeError('Expected property sdrs_io_balance_automation_level to be a basestring')
        __self__.sdrs_io_balance_automation_level = sdrs_io_balance_automation_level
        """
        Overrides the default
        automation settings when correcting I/O load imbalances.
        """
        __props__['sdrsIoBalanceAutomationLevel'] = sdrs_io_balance_automation_level

        if sdrs_io_latency_threshold and not isinstance(sdrs_io_latency_threshold, int):
            raise TypeError('Expected property sdrs_io_latency_threshold to be a int')
        __self__.sdrs_io_latency_threshold = sdrs_io_latency_threshold
        """
        The I/O latency threshold, in
        milliseconds, that storage DRS uses to make recommendations to move disks
        from this datastore. Default: `15` seconds.
        """
        __props__['sdrsIoLatencyThreshold'] = sdrs_io_latency_threshold

        if sdrs_io_load_balance_enabled and not isinstance(sdrs_io_load_balance_enabled, bool):
            raise TypeError('Expected property sdrs_io_load_balance_enabled to be a bool')
        __self__.sdrs_io_load_balance_enabled = sdrs_io_load_balance_enabled
        """
        Enable I/O load balancing for
        this datastore cluster. Default: `true`.
        """
        __props__['sdrsIoLoadBalanceEnabled'] = sdrs_io_load_balance_enabled

        if sdrs_io_load_imbalance_threshold and not isinstance(sdrs_io_load_imbalance_threshold, int):
            raise TypeError('Expected property sdrs_io_load_imbalance_threshold to be a int')
        __self__.sdrs_io_load_imbalance_threshold = sdrs_io_load_imbalance_threshold
        """
        The difference between load
        in datastores in the cluster before storage DRS makes recommendations to
        balance the load. Default: `5` percent.
        """
        __props__['sdrsIoLoadImbalanceThreshold'] = sdrs_io_load_imbalance_threshold

        if sdrs_io_reservable_iops_threshold and not isinstance(sdrs_io_reservable_iops_threshold, int):
            raise TypeError('Expected property sdrs_io_reservable_iops_threshold to be a int')
        __self__.sdrs_io_reservable_iops_threshold = sdrs_io_reservable_iops_threshold
        """
        The threshold of reservable
        IOPS of all virtual machines on the datastore before storage DRS makes
        recommendations to move VMs off of a datastore. Note that this setting should
        only be set if `sdrs_io_reservable_percent_threshold` cannot make an accurate
        estimate of the capacity of the datastores in your cluster, and should be set
        to roughly 50-60% of the worst case peak performance of the backing LUNs.
        """
        __props__['sdrsIoReservableIopsThreshold'] = sdrs_io_reservable_iops_threshold

        if sdrs_io_reservable_percent_threshold and not isinstance(sdrs_io_reservable_percent_threshold, int):
            raise TypeError('Expected property sdrs_io_reservable_percent_threshold to be a int')
        __self__.sdrs_io_reservable_percent_threshold = sdrs_io_reservable_percent_threshold
        """
        The threshold, in
        percent, of actual estimated performance of the datastore (in IOPS) that
        storage DRS uses to make recommendations to move VMs off of a datastore when
        the total reservable IOPS exceeds the threshold. Default: `60` percent.
        """
        __props__['sdrsIoReservablePercentThreshold'] = sdrs_io_reservable_percent_threshold

        if sdrs_io_reservable_threshold_mode and not isinstance(sdrs_io_reservable_threshold_mode, basestring):
            raise TypeError('Expected property sdrs_io_reservable_threshold_mode to be a basestring')
        __self__.sdrs_io_reservable_threshold_mode = sdrs_io_reservable_threshold_mode
        """
        The reservable IOPS
        threshold setting to use, `sdrs_io_reservable_percent_threshold` in the event
        of `automatic`, or `sdrs_io_reservable_iops_threshold` in the event of
        `manual`. Default: `automatic`.
        """
        __props__['sdrsIoReservableThresholdMode'] = sdrs_io_reservable_threshold_mode

        if sdrs_load_balance_interval and not isinstance(sdrs_load_balance_interval, int):
            raise TypeError('Expected property sdrs_load_balance_interval to be a int')
        __self__.sdrs_load_balance_interval = sdrs_load_balance_interval
        """
        The storage DRS poll interval, in
        minutes. Default: `480` minutes.
        """
        __props__['sdrsLoadBalanceInterval'] = sdrs_load_balance_interval

        if sdrs_policy_enforcement_automation_level and not isinstance(sdrs_policy_enforcement_automation_level, basestring):
            raise TypeError('Expected property sdrs_policy_enforcement_automation_level to be a basestring')
        __self__.sdrs_policy_enforcement_automation_level = sdrs_policy_enforcement_automation_level
        """
        Overrides the default
        automation settings when correcting storage and VM policy violations.
        """
        __props__['sdrsPolicyEnforcementAutomationLevel'] = sdrs_policy_enforcement_automation_level

        if sdrs_rule_enforcement_automation_level and not isinstance(sdrs_rule_enforcement_automation_level, basestring):
            raise TypeError('Expected property sdrs_rule_enforcement_automation_level to be a basestring')
        __self__.sdrs_rule_enforcement_automation_level = sdrs_rule_enforcement_automation_level
        """
        Overrides the default
        automation settings when correcting affinity rule violations.
        """
        __props__['sdrsRuleEnforcementAutomationLevel'] = sdrs_rule_enforcement_automation_level

        if sdrs_space_balance_automation_level and not isinstance(sdrs_space_balance_automation_level, basestring):
            raise TypeError('Expected property sdrs_space_balance_automation_level to be a basestring')
        __self__.sdrs_space_balance_automation_level = sdrs_space_balance_automation_level
        """
        Overrides the default
        automation settings when correcting disk space imbalances.
        """
        __props__['sdrsSpaceBalanceAutomationLevel'] = sdrs_space_balance_automation_level

        if sdrs_space_utilization_threshold and not isinstance(sdrs_space_utilization_threshold, int):
            raise TypeError('Expected property sdrs_space_utilization_threshold to be a int')
        __self__.sdrs_space_utilization_threshold = sdrs_space_utilization_threshold
        """
        The threshold, in percent of used space, that storage DRS uses to make decisions to migrate VMs out of a
        datastore.
        """
        __props__['sdrsSpaceUtilizationThreshold'] = sdrs_space_utilization_threshold

        if sdrs_vm_evacuation_automation_level and not isinstance(sdrs_vm_evacuation_automation_level, basestring):
            raise TypeError('Expected property sdrs_vm_evacuation_automation_level to be a basestring')
        __self__.sdrs_vm_evacuation_automation_level = sdrs_vm_evacuation_automation_level
        """
        Overrides the default
        automation settings when generating recommendations for datastore evacuation.
        """
        __props__['sdrsVmEvacuationAutomationLevel'] = sdrs_vm_evacuation_automation_level

        if tags and not isinstance(tags, list):
            raise TypeError('Expected property tags to be a list')
        __self__.tags = tags
        """
        The IDs of any tags to attach to this resource. See
        [here][docs-applying-tags] for a reference on how to apply tags.
        """
        __props__['tags'] = tags

        super(DatastoreCluster, __self__).__init__(
            'vsphere:index/datastoreCluster:DatastoreCluster',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'customAttributes' in outs:
            self.custom_attributes = outs['customAttributes']
        if 'datacenterId' in outs:
            self.datacenter_id = outs['datacenterId']
        if 'folder' in outs:
            self.folder = outs['folder']
        if 'name' in outs:
            self.name = outs['name']
        if 'sdrsAdvancedOptions' in outs:
            self.sdrs_advanced_options = outs['sdrsAdvancedOptions']
        if 'sdrsAutomationLevel' in outs:
            self.sdrs_automation_level = outs['sdrsAutomationLevel']
        if 'sdrsDefaultIntraVmAffinity' in outs:
            self.sdrs_default_intra_vm_affinity = outs['sdrsDefaultIntraVmAffinity']
        if 'sdrsEnabled' in outs:
            self.sdrs_enabled = outs['sdrsEnabled']
        if 'sdrsFreeSpaceThreshold' in outs:
            self.sdrs_free_space_threshold = outs['sdrsFreeSpaceThreshold']
        if 'sdrsFreeSpaceThresholdMode' in outs:
            self.sdrs_free_space_threshold_mode = outs['sdrsFreeSpaceThresholdMode']
        if 'sdrsFreeSpaceUtilizationDifference' in outs:
            self.sdrs_free_space_utilization_difference = outs['sdrsFreeSpaceUtilizationDifference']
        if 'sdrsIoBalanceAutomationLevel' in outs:
            self.sdrs_io_balance_automation_level = outs['sdrsIoBalanceAutomationLevel']
        if 'sdrsIoLatencyThreshold' in outs:
            self.sdrs_io_latency_threshold = outs['sdrsIoLatencyThreshold']
        if 'sdrsIoLoadBalanceEnabled' in outs:
            self.sdrs_io_load_balance_enabled = outs['sdrsIoLoadBalanceEnabled']
        if 'sdrsIoLoadImbalanceThreshold' in outs:
            self.sdrs_io_load_imbalance_threshold = outs['sdrsIoLoadImbalanceThreshold']
        if 'sdrsIoReservableIopsThreshold' in outs:
            self.sdrs_io_reservable_iops_threshold = outs['sdrsIoReservableIopsThreshold']
        if 'sdrsIoReservablePercentThreshold' in outs:
            self.sdrs_io_reservable_percent_threshold = outs['sdrsIoReservablePercentThreshold']
        if 'sdrsIoReservableThresholdMode' in outs:
            self.sdrs_io_reservable_threshold_mode = outs['sdrsIoReservableThresholdMode']
        if 'sdrsLoadBalanceInterval' in outs:
            self.sdrs_load_balance_interval = outs['sdrsLoadBalanceInterval']
        if 'sdrsPolicyEnforcementAutomationLevel' in outs:
            self.sdrs_policy_enforcement_automation_level = outs['sdrsPolicyEnforcementAutomationLevel']
        if 'sdrsRuleEnforcementAutomationLevel' in outs:
            self.sdrs_rule_enforcement_automation_level = outs['sdrsRuleEnforcementAutomationLevel']
        if 'sdrsSpaceBalanceAutomationLevel' in outs:
            self.sdrs_space_balance_automation_level = outs['sdrsSpaceBalanceAutomationLevel']
        if 'sdrsSpaceUtilizationThreshold' in outs:
            self.sdrs_space_utilization_threshold = outs['sdrsSpaceUtilizationThreshold']
        if 'sdrsVmEvacuationAutomationLevel' in outs:
            self.sdrs_vm_evacuation_automation_level = outs['sdrsVmEvacuationAutomationLevel']
        if 'tags' in outs:
            self.tags = outs['tags']