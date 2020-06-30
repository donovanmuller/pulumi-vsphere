# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetVirtualMachineResult:
    """
    A collection of values returned by getVirtualMachine.
    """
    def __init__(__self__, alternate_guest_name=None, datacenter_id=None, disks=None, firmware=None, guest_id=None, guest_ip_addresses=None, id=None, ide_controller_scan_count=None, name=None, network_interface_types=None, sata_controller_scan_count=None, scsi_bus_sharing=None, scsi_controller_scan_count=None, scsi_type=None):
        if alternate_guest_name and not isinstance(alternate_guest_name, str):
            raise TypeError("Expected argument 'alternate_guest_name' to be a str")
        __self__.alternate_guest_name = alternate_guest_name
        """
        The alternate guest name of the virtual machine when
        guest_id is a non-specific operating system, like `otherGuest`.
        """
        if datacenter_id and not isinstance(datacenter_id, str):
            raise TypeError("Expected argument 'datacenter_id' to be a str")
        __self__.datacenter_id = datacenter_id
        if disks and not isinstance(disks, list):
            raise TypeError("Expected argument 'disks' to be a list")
        __self__.disks = disks
        """
        Information about each of the disks on this virtual machine or
        template. These are sorted by bus and unit number so that they can be applied
        to a `.VirtualMachine` resource in the order the resource expects
        while cloning. This is useful for discovering certain disk settings while
        performing a linked clone, as all settings that are output by this data
        source must be the same on the destination virtual machine as the source.
        Only the first number of controllers defined by `scsi_controller_scan_count`
        are scanned for disks. The sub-attributes are:
        """
        if firmware and not isinstance(firmware, str):
            raise TypeError("Expected argument 'firmware' to be a str")
        __self__.firmware = firmware
        """
        The firmware type for this virtual machine. Can be `bios` or `efi`.
        """
        if guest_id and not isinstance(guest_id, str):
            raise TypeError("Expected argument 'guest_id' to be a str")
        __self__.guest_id = guest_id
        """
        The guest ID of the virtual machine or template.
        """
        if guest_ip_addresses and not isinstance(guest_ip_addresses, list):
            raise TypeError("Expected argument 'guest_ip_addresses' to be a list")
        __self__.guest_ip_addresses = guest_ip_addresses
        """
        A list of IP addresses as reported by VMWare tools.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if ide_controller_scan_count and not isinstance(ide_controller_scan_count, float):
            raise TypeError("Expected argument 'ide_controller_scan_count' to be a float")
        __self__.ide_controller_scan_count = ide_controller_scan_count
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if network_interface_types and not isinstance(network_interface_types, list):
            raise TypeError("Expected argument 'network_interface_types' to be a list")
        __self__.network_interface_types = network_interface_types
        """
        The network interface types for each network
        interface found on the virtual machine, in device bus order. Will be one of
        `e1000`, `e1000e`, `pcnet32`, `sriov`, `vmxnet2`, or `vmxnet3`.
        """
        if sata_controller_scan_count and not isinstance(sata_controller_scan_count, float):
            raise TypeError("Expected argument 'sata_controller_scan_count' to be a float")
        __self__.sata_controller_scan_count = sata_controller_scan_count
        if scsi_bus_sharing and not isinstance(scsi_bus_sharing, str):
            raise TypeError("Expected argument 'scsi_bus_sharing' to be a str")
        __self__.scsi_bus_sharing = scsi_bus_sharing
        """
        Mode for sharing the SCSI bus. The modes are
        physicalSharing, virtualSharing, and noSharing. Only the first number of
        controllers defined by `scsi_controller_scan_count` are scanned.
        """
        if scsi_controller_scan_count and not isinstance(scsi_controller_scan_count, float):
            raise TypeError("Expected argument 'scsi_controller_scan_count' to be a float")
        __self__.scsi_controller_scan_count = scsi_controller_scan_count
        if scsi_type and not isinstance(scsi_type, str):
            raise TypeError("Expected argument 'scsi_type' to be a str")
        __self__.scsi_type = scsi_type
        """
        The common type of all SCSI controllers on this virtual machine.
        Will be one of `lsilogic` (LSI Logic Parallel), `lsilogic-sas` (LSI Logic
        SAS), `pvscsi` (VMware Paravirtual), `buslogic` (BusLogic), or `mixed` when
        there are multiple controller types. Only the first number of controllers
        defined by `scsi_controller_scan_count` are scanned.
        """
class AwaitableGetVirtualMachineResult(GetVirtualMachineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualMachineResult(
            alternate_guest_name=self.alternate_guest_name,
            datacenter_id=self.datacenter_id,
            disks=self.disks,
            firmware=self.firmware,
            guest_id=self.guest_id,
            guest_ip_addresses=self.guest_ip_addresses,
            id=self.id,
            ide_controller_scan_count=self.ide_controller_scan_count,
            name=self.name,
            network_interface_types=self.network_interface_types,
            sata_controller_scan_count=self.sata_controller_scan_count,
            scsi_bus_sharing=self.scsi_bus_sharing,
            scsi_controller_scan_count=self.scsi_controller_scan_count,
            scsi_type=self.scsi_type)

def get_virtual_machine(datacenter_id=None,ide_controller_scan_count=None,name=None,sata_controller_scan_count=None,scsi_controller_scan_count=None,opts=None):
    """
    The `.VirtualMachine` data source can be used to find the UUID of an
    existing virtual machine or template. Its most relevant purpose is for finding
    the UUID of a template to be used as the source for cloning into a new
    `.VirtualMachine` resource. It also
    reads the guest ID so that can be supplied as well.

    ## Example Usage



    ```python
    import pulumi
    import pulumi_vsphere as vsphere

    datacenter = vsphere.get_datacenter(name="dc1")
    template = vsphere.get_virtual_machine(datacenter_id=datacenter.id,
        name="test-vm-template")
    ```



    :param str datacenter_id: The managed object reference
           ID of the datacenter the virtual machine is located in.
           This can be omitted if the search path used in `name` is an absolute path.
           For default datacenters, use the `id` attribute from an empty
           `.Datacenter` data source.
    :param str name: The name of the virtual machine. This can be a name or
           path.
    :param float scsi_controller_scan_count: The number of SCSI controllers to
           scan for disk attributes and controller types on. Default: `1`.
    """
    __args__ = dict()


    __args__['datacenterId'] = datacenter_id
    __args__['ideControllerScanCount'] = ide_controller_scan_count
    __args__['name'] = name
    __args__['sataControllerScanCount'] = sata_controller_scan_count
    __args__['scsiControllerScanCount'] = scsi_controller_scan_count
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('vsphere:index/getVirtualMachine:getVirtualMachine', __args__, opts=opts).value

    return AwaitableGetVirtualMachineResult(
        alternate_guest_name=__ret__.get('alternateGuestName'),
        datacenter_id=__ret__.get('datacenterId'),
        disks=__ret__.get('disks'),
        firmware=__ret__.get('firmware'),
        guest_id=__ret__.get('guestId'),
        guest_ip_addresses=__ret__.get('guestIpAddresses'),
        id=__ret__.get('id'),
        ide_controller_scan_count=__ret__.get('ideControllerScanCount'),
        name=__ret__.get('name'),
        network_interface_types=__ret__.get('networkInterfaceTypes'),
        sata_controller_scan_count=__ret__.get('sataControllerScanCount'),
        scsi_bus_sharing=__ret__.get('scsiBusSharing'),
        scsi_controller_scan_count=__ret__.get('scsiControllerScanCount'),
        scsi_type=__ret__.get('scsiType'))
