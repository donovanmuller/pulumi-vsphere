# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from . import utilities, tables

class StorageDrsVmOverride(pulumi.CustomResource):
    """
    The `vsphere_storage_drs_vm_override` resource can be used to add a Storage DRS
    override to a datastore cluster for a specific virtual machine. With this
    resource, one can enable or disable Storage DRS, and control the automation
    level and disk affinity for a single virtual machine without affecting the rest
    of the datastore cluster.
    
    For more information on vSphere datastore clusters and Storage DRS, see [this
    page][ref-vsphere-datastore-clusters].
    
    [ref-vsphere-datastore-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-598DF695-107E-406B-9C95-0AF961FC227A.html
    """
    def __init__(__self__, __name__, __opts__=None, datastore_cluster_id=None, sdrs_automation_level=None, sdrs_enabled=None, sdrs_intra_vm_affinity=None, virtual_machine_id=None):
        """Create a StorageDrsVmOverride resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not datastore_cluster_id:
            raise TypeError('Missing required property datastore_cluster_id')
        __props__['datastore_cluster_id'] = datastore_cluster_id

        __props__['sdrs_automation_level'] = sdrs_automation_level

        __props__['sdrs_enabled'] = sdrs_enabled

        __props__['sdrs_intra_vm_affinity'] = sdrs_intra_vm_affinity

        if not virtual_machine_id:
            raise TypeError('Missing required property virtual_machine_id')
        __props__['virtual_machine_id'] = virtual_machine_id

        super(StorageDrsVmOverride, __self__).__init__(
            'vsphere:index/storageDrsVmOverride:StorageDrsVmOverride',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

