# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

_SNAKE_TO_CAMEL_CASE_TABLE = {
    "access_mode": "accessMode",
    "active_nics": "activeNics",
    "active_uplinks": "activeUplinks",
    "adapter_type": "adapterType",
    "affinity_host_group_name": "affinityHostGroupName",
    "allow_forged_transmits": "allowForgedTransmits",
    "allow_mac_changes": "allowMacChanges",
    "allow_promiscuous": "allowPromiscuous",
    "alternate_guest_name": "alternateGuestName",
    "anti_affinity_host_group_name": "antiAffinityHostGroupName",
    "associable_types": "associableTypes",
    "auto_expand": "autoExpand",
    "beacon_interval": "beaconInterval",
    "block_all_ports": "blockAllPorts",
    "block_override_allowed": "blockOverrideAllowed",
    "boot_delay": "bootDelay",
    "boot_retry_delay": "bootRetryDelay",
    "boot_retry_enabled": "bootRetryEnabled",
    "category_id": "categoryId",
    "change_version": "changeVersion",
    "check_beacon": "checkBeacon",
    "cluster_managed": "clusterManaged",
    "compute_cluster_id": "computeClusterId",
    "computed_policy": "computedPolicy",
    "config_version": "configVersion",
    "contact_detail": "contactDetail",
    "contact_name": "contactName",
    "container_id": "containerId",
    "cpu_expandable": "cpuExpandable",
    "cpu_hot_add_enabled": "cpuHotAddEnabled",
    "cpu_hot_remove_enabled": "cpuHotRemoveEnabled",
    "cpu_limit": "cpuLimit",
    "cpu_performance_counters_enabled": "cpuPerformanceCountersEnabled",
    "cpu_reservation": "cpuReservation",
    "cpu_share_count": "cpuShareCount",
    "cpu_share_level": "cpuShareLevel",
    "cpu_shares": "cpuShares",
    "create_directories": "createDirectories",
    "custom_attributes": "customAttributes",
    "datacenter_id": "datacenterId",
    "datastore_cluster_id": "datastoreClusterId",
    "datastore_id": "datastoreId",
    "default_ip_address": "defaultIpAddress",
    "dependency_vm_group_name": "dependencyVmGroupName",
    "destination_file": "destinationFile",
    "directpath_gen2_allowed": "directpathGen2Allowed",
    "distributed_port_group": "distributedPortGroup",
    "distributed_switch_port": "distributedSwitchPort",
    "distributed_virtual_switch_uuid": "distributedVirtualSwitchUuid",
    "dpm_automation_level": "dpmAutomationLevel",
    "dpm_enabled": "dpmEnabled",
    "dpm_threshold": "dpmThreshold",
    "drs_advanced_options": "drsAdvancedOptions",
    "drs_automation_level": "drsAutomationLevel",
    "drs_enable_predictive_drs": "drsEnablePredictiveDrs",
    "drs_enable_vm_overrides": "drsEnableVmOverrides",
    "drs_enabled": "drsEnabled",
    "drs_migration_threshold": "drsMigrationThreshold",
    "edition_key": "editionKey",
    "efi_secure_boot_enabled": "efiSecureBootEnabled",
    "egress_shaping_average_bandwidth": "egressShapingAverageBandwidth",
    "egress_shaping_burst_size": "egressShapingBurstSize",
    "egress_shaping_enabled": "egressShapingEnabled",
    "egress_shaping_peak_bandwidth": "egressShapingPeakBandwidth",
    "enable_disk_uuid": "enableDiskUuid",
    "enable_logging": "enableLogging",
    "ept_rvi_mode": "eptRviMode",
    "extra_config": "extraConfig",
    "faulttolerance_maximum_mbit": "faulttoleranceMaximumMbit",
    "faulttolerance_reservation_mbit": "faulttoleranceReservationMbit",
    "faulttolerance_share_count": "faulttoleranceShareCount",
    "faulttolerance_share_level": "faulttoleranceShareLevel",
    "file_urls": "fileUrls",
    "force_evacuate_on_destroy": "forceEvacuateOnDestroy",
    "force_power_off": "forcePowerOff",
    "free_space": "freeSpace",
    "guest_id": "guestId",
    "guest_ip_addresses": "guestIpAddresses",
    "ha_admission_control_failover_host_system_ids": "haAdmissionControlFailoverHostSystemIds",
    "ha_admission_control_host_failure_tolerance": "haAdmissionControlHostFailureTolerance",
    "ha_admission_control_performance_tolerance": "haAdmissionControlPerformanceTolerance",
    "ha_admission_control_policy": "haAdmissionControlPolicy",
    "ha_admission_control_resource_percentage_auto_compute": "haAdmissionControlResourcePercentageAutoCompute",
    "ha_admission_control_resource_percentage_cpu": "haAdmissionControlResourcePercentageCpu",
    "ha_admission_control_resource_percentage_memory": "haAdmissionControlResourcePercentageMemory",
    "ha_admission_control_slot_policy_explicit_cpu": "haAdmissionControlSlotPolicyExplicitCpu",
    "ha_admission_control_slot_policy_explicit_memory": "haAdmissionControlSlotPolicyExplicitMemory",
    "ha_admission_control_slot_policy_use_explicit_size": "haAdmissionControlSlotPolicyUseExplicitSize",
    "ha_advanced_options": "haAdvancedOptions",
    "ha_datastore_apd_recovery_action": "haDatastoreApdRecoveryAction",
    "ha_datastore_apd_response": "haDatastoreApdResponse",
    "ha_datastore_apd_response_delay": "haDatastoreApdResponseDelay",
    "ha_datastore_pdl_response": "haDatastorePdlResponse",
    "ha_enabled": "haEnabled",
    "ha_heartbeat_datastore_ids": "haHeartbeatDatastoreIds",
    "ha_heartbeat_datastore_policy": "haHeartbeatDatastorePolicy",
    "ha_host_isolation_response": "haHostIsolationResponse",
    "ha_host_monitoring": "haHostMonitoring",
    "ha_vm_component_protection": "haVmComponentProtection",
    "ha_vm_dependency_restart_condition": "haVmDependencyRestartCondition",
    "ha_vm_failure_interval": "haVmFailureInterval",
    "ha_vm_maximum_failure_window": "haVmMaximumFailureWindow",
    "ha_vm_maximum_resets": "haVmMaximumResets",
    "ha_vm_minimum_uptime": "haVmMinimumUptime",
    "ha_vm_monitoring": "haVmMonitoring",
    "ha_vm_monitoring_use_cluster_defaults": "haVmMonitoringUseClusterDefaults",
    "ha_vm_restart_additional_delay": "haVmRestartAdditionalDelay",
    "ha_vm_restart_priority": "haVmRestartPriority",
    "ha_vm_restart_timeout": "haVmRestartTimeout",
    "hardware_version": "hardwareVersion",
    "hbr_maximum_mbit": "hbrMaximumMbit",
    "hbr_reservation_mbit": "hbrReservationMbit",
    "hbr_share_count": "hbrShareCount",
    "hbr_share_level": "hbrShareLevel",
    "host_cluster_exit_timeout": "hostClusterExitTimeout",
    "host_managed": "hostManaged",
    "host_system_id": "hostSystemId",
    "host_system_ids": "hostSystemIds",
    "hv_mode": "hvMode",
    "ide_controller_count": "ideControllerCount",
    "ignored_guest_ips": "ignoredGuestIps",
    "ingress_shaping_average_bandwidth": "ingressShapingAverageBandwidth",
    "ingress_shaping_burst_size": "ingressShapingBurstSize",
    "ingress_shaping_enabled": "ingressShapingEnabled",
    "ingress_shaping_peak_bandwidth": "ingressShapingPeakBandwidth",
    "ipv4_address": "ipv4Address",
    "iscsi_maximum_mbit": "iscsiMaximumMbit",
    "iscsi_reservation_mbit": "iscsiReservationMbit",
    "iscsi_share_count": "iscsiShareCount",
    "iscsi_share_level": "iscsiShareLevel",
    "lacp_api_version": "lacpApiVersion",
    "lacp_enabled": "lacpEnabled",
    "lacp_mode": "lacpMode",
    "latency_sensitivity": "latencySensitivity",
    "library_id": "libraryId",
    "license_key": "licenseKey",
    "link_discovery_operation": "linkDiscoveryOperation",
    "link_discovery_protocol": "linkDiscoveryProtocol",
    "live_port_moving_allowed": "livePortMovingAllowed",
    "maintenance_mode": "maintenanceMode",
    "managed_object_type": "managedObjectType",
    "management_maximum_mbit": "managementMaximumMbit",
    "management_reservation_mbit": "managementReservationMbit",
    "management_share_count": "managementShareCount",
    "management_share_level": "managementShareLevel",
    "max_mtu": "maxMtu",
    "memory_expandable": "memoryExpandable",
    "memory_hot_add_enabled": "memoryHotAddEnabled",
    "memory_limit": "memoryLimit",
    "memory_reservation": "memoryReservation",
    "memory_share_count": "memoryShareCount",
    "memory_share_level": "memoryShareLevel",
    "memory_shares": "memoryShares",
    "migrate_wait_timeout": "migrateWaitTimeout",
    "multicast_filtering_mode": "multicastFilteringMode",
    "multiple_host_access": "multipleHostAccess",
    "nested_hv_enabled": "nestedHvEnabled",
    "netflow_active_flow_timeout": "netflowActiveFlowTimeout",
    "netflow_collector_ip_address": "netflowCollectorIpAddress",
    "netflow_collector_port": "netflowCollectorPort",
    "netflow_enabled": "netflowEnabled",
    "netflow_idle_flow_timeout": "netflowIdleFlowTimeout",
    "netflow_internal_flows_only": "netflowInternalFlowsOnly",
    "netflow_observation_domain_id": "netflowObservationDomainId",
    "netflow_override_allowed": "netflowOverrideAllowed",
    "netflow_sampling_rate": "netflowSamplingRate",
    "network_adapters": "networkAdapters",
    "network_interfaces": "networkInterfaces",
    "network_resource_control_enabled": "networkResourceControlEnabled",
    "network_resource_control_version": "networkResourceControlVersion",
    "network_resource_pool_key": "networkResourcePoolKey",
    "network_resource_pool_override_allowed": "networkResourcePoolOverrideAllowed",
    "nfs_maximum_mbit": "nfsMaximumMbit",
    "nfs_reservation_mbit": "nfsReservationMbit",
    "nfs_share_count": "nfsShareCount",
    "nfs_share_level": "nfsShareLevel",
    "notify_switches": "notifySwitches",
    "num_cores_per_socket": "numCoresPerSocket",
    "num_cpus": "numCpus",
    "number_of_ports": "numberOfPorts",
    "ovf_deploy": "ovfDeploy",
    "parent_folder_id": "parentFolderId",
    "parent_resource_pool_id": "parentResourcePoolId",
    "pci_device_ids": "pciDeviceIds",
    "port_config_reset_at_disconnect": "portConfigResetAtDisconnect",
    "port_name_format": "portNameFormat",
    "port_private_secondary_vlan_id": "portPrivateSecondaryVlanId",
    "poweron_timeout": "poweronTimeout",
    "proactive_ha_automation_level": "proactiveHaAutomationLevel",
    "proactive_ha_enabled": "proactiveHaEnabled",
    "proactive_ha_moderate_remediation": "proactiveHaModerateRemediation",
    "proactive_ha_provider_ids": "proactiveHaProviderIds",
    "proactive_ha_severe_remediation": "proactiveHaSevereRemediation",
    "protocol_endpoint": "protocolEndpoint",
    "reboot_required": "rebootRequired",
    "remote_hosts": "remoteHosts",
    "remote_path": "remotePath",
    "remove_children": "removeChildren",
    "resource_pool_id": "resourcePoolId",
    "run_tools_scripts_after_power_on": "runToolsScriptsAfterPowerOn",
    "run_tools_scripts_after_resume": "runToolsScriptsAfterResume",
    "run_tools_scripts_before_guest_reboot": "runToolsScriptsBeforeGuestReboot",
    "run_tools_scripts_before_guest_shutdown": "runToolsScriptsBeforeGuestShutdown",
    "run_tools_scripts_before_guest_standby": "runToolsScriptsBeforeGuestStandby",
    "sata_controller_count": "sataControllerCount",
    "scsi_bus_sharing": "scsiBusSharing",
    "scsi_controller_count": "scsiControllerCount",
    "scsi_type": "scsiType",
    "sdrs_advanced_options": "sdrsAdvancedOptions",
    "sdrs_automation_level": "sdrsAutomationLevel",
    "sdrs_default_intra_vm_affinity": "sdrsDefaultIntraVmAffinity",
    "sdrs_enabled": "sdrsEnabled",
    "sdrs_free_space_threshold": "sdrsFreeSpaceThreshold",
    "sdrs_free_space_threshold_mode": "sdrsFreeSpaceThresholdMode",
    "sdrs_free_space_utilization_difference": "sdrsFreeSpaceUtilizationDifference",
    "sdrs_intra_vm_affinity": "sdrsIntraVmAffinity",
    "sdrs_io_balance_automation_level": "sdrsIoBalanceAutomationLevel",
    "sdrs_io_latency_threshold": "sdrsIoLatencyThreshold",
    "sdrs_io_load_balance_enabled": "sdrsIoLoadBalanceEnabled",
    "sdrs_io_load_imbalance_threshold": "sdrsIoLoadImbalanceThreshold",
    "sdrs_io_reservable_iops_threshold": "sdrsIoReservableIopsThreshold",
    "sdrs_io_reservable_percent_threshold": "sdrsIoReservablePercentThreshold",
    "sdrs_io_reservable_threshold_mode": "sdrsIoReservableThresholdMode",
    "sdrs_load_balance_interval": "sdrsLoadBalanceInterval",
    "sdrs_policy_enforcement_automation_level": "sdrsPolicyEnforcementAutomationLevel",
    "sdrs_rule_enforcement_automation_level": "sdrsRuleEnforcementAutomationLevel",
    "sdrs_space_balance_automation_level": "sdrsSpaceBalanceAutomationLevel",
    "sdrs_space_utilization_threshold": "sdrsSpaceUtilizationThreshold",
    "sdrs_vm_evacuation_automation_level": "sdrsVmEvacuationAutomationLevel",
    "security_policy_override_allowed": "securityPolicyOverrideAllowed",
    "security_type": "securityType",
    "shaping_average_bandwidth": "shapingAverageBandwidth",
    "shaping_burst_size": "shapingBurstSize",
    "shaping_enabled": "shapingEnabled",
    "shaping_override_allowed": "shapingOverrideAllowed",
    "shaping_peak_bandwidth": "shapingPeakBandwidth",
    "shutdown_wait_timeout": "shutdownWaitTimeout",
    "snapshot_name": "snapshotName",
    "source_datacenter": "sourceDatacenter",
    "source_datastore": "sourceDatastore",
    "source_file": "sourceFile",
    "standby_nics": "standbyNics",
    "standby_uplinks": "standbyUplinks",
    "start_action": "startAction",
    "start_delay": "startDelay",
    "start_order": "startOrder",
    "stop_action": "stopAction",
    "stop_delay": "stopDelay",
    "storage_backings": "storageBackings",
    "storage_policy_id": "storagePolicyId",
    "swap_placement_policy": "swapPlacementPolicy",
    "sync_time_with_host": "syncTimeWithHost",
    "tag_rules": "tagRules",
    "target_id": "targetId",
    "teaming_policy": "teamingPolicy",
    "traffic_filter_override_allowed": "trafficFilterOverrideAllowed",
    "tx_uplink": "txUplink",
    "uncommitted_space": "uncommittedSpace",
    "uplink_teaming_override_allowed": "uplinkTeamingOverrideAllowed",
    "vapp_transports": "vappTransports",
    "vdp_maximum_mbit": "vdpMaximumMbit",
    "vdp_reservation_mbit": "vdpReservationMbit",
    "vdp_share_count": "vdpShareCount",
    "vdp_share_level": "vdpShareLevel",
    "virtual_machine_id": "virtualMachineId",
    "virtual_machine_ids": "virtualMachineIds",
    "virtual_machine_uuid": "virtualMachineUuid",
    "virtual_switch_name": "virtualSwitchName",
    "virtualmachine_maximum_mbit": "virtualmachineMaximumMbit",
    "virtualmachine_reservation_mbit": "virtualmachineReservationMbit",
    "virtualmachine_share_count": "virtualmachineShareCount",
    "virtualmachine_share_level": "virtualmachineShareLevel",
    "vlan_id": "vlanId",
    "vlan_override_allowed": "vlanOverrideAllowed",
    "vlan_ranges": "vlanRanges",
    "vm_group_name": "vmGroupName",
    "vmdk_path": "vmdkPath",
    "vmotion_maximum_mbit": "vmotionMaximumMbit",
    "vmotion_reservation_mbit": "vmotionReservationMbit",
    "vmotion_share_count": "vmotionShareCount",
    "vmotion_share_level": "vmotionShareLevel",
    "vmware_tools_status": "vmwareToolsStatus",
    "vmx_path": "vmxPath",
    "vsan_maximum_mbit": "vsanMaximumMbit",
    "vsan_reservation_mbit": "vsanReservationMbit",
    "vsan_share_count": "vsanShareCount",
    "vsan_share_level": "vsanShareLevel",
    "wait_for_guest": "waitForGuest",
    "wait_for_guest_ip_timeout": "waitForGuestIpTimeout",
    "wait_for_guest_net_routable": "waitForGuestNetRoutable",
    "wait_for_guest_net_timeout": "waitForGuestNetTimeout",
}

_CAMEL_TO_SNAKE_CASE_TABLE = {
    "accessMode": "access_mode",
    "activeNics": "active_nics",
    "activeUplinks": "active_uplinks",
    "adapterType": "adapter_type",
    "affinityHostGroupName": "affinity_host_group_name",
    "allowForgedTransmits": "allow_forged_transmits",
    "allowMacChanges": "allow_mac_changes",
    "allowPromiscuous": "allow_promiscuous",
    "alternateGuestName": "alternate_guest_name",
    "antiAffinityHostGroupName": "anti_affinity_host_group_name",
    "associableTypes": "associable_types",
    "autoExpand": "auto_expand",
    "beaconInterval": "beacon_interval",
    "blockAllPorts": "block_all_ports",
    "blockOverrideAllowed": "block_override_allowed",
    "bootDelay": "boot_delay",
    "bootRetryDelay": "boot_retry_delay",
    "bootRetryEnabled": "boot_retry_enabled",
    "categoryId": "category_id",
    "changeVersion": "change_version",
    "checkBeacon": "check_beacon",
    "clusterManaged": "cluster_managed",
    "computeClusterId": "compute_cluster_id",
    "computedPolicy": "computed_policy",
    "configVersion": "config_version",
    "contactDetail": "contact_detail",
    "contactName": "contact_name",
    "containerId": "container_id",
    "cpuExpandable": "cpu_expandable",
    "cpuHotAddEnabled": "cpu_hot_add_enabled",
    "cpuHotRemoveEnabled": "cpu_hot_remove_enabled",
    "cpuLimit": "cpu_limit",
    "cpuPerformanceCountersEnabled": "cpu_performance_counters_enabled",
    "cpuReservation": "cpu_reservation",
    "cpuShareCount": "cpu_share_count",
    "cpuShareLevel": "cpu_share_level",
    "cpuShares": "cpu_shares",
    "createDirectories": "create_directories",
    "customAttributes": "custom_attributes",
    "datacenterId": "datacenter_id",
    "datastoreClusterId": "datastore_cluster_id",
    "datastoreId": "datastore_id",
    "defaultIpAddress": "default_ip_address",
    "dependencyVmGroupName": "dependency_vm_group_name",
    "destinationFile": "destination_file",
    "directpathGen2Allowed": "directpath_gen2_allowed",
    "distributedPortGroup": "distributed_port_group",
    "distributedSwitchPort": "distributed_switch_port",
    "distributedVirtualSwitchUuid": "distributed_virtual_switch_uuid",
    "dpmAutomationLevel": "dpm_automation_level",
    "dpmEnabled": "dpm_enabled",
    "dpmThreshold": "dpm_threshold",
    "drsAdvancedOptions": "drs_advanced_options",
    "drsAutomationLevel": "drs_automation_level",
    "drsEnablePredictiveDrs": "drs_enable_predictive_drs",
    "drsEnableVmOverrides": "drs_enable_vm_overrides",
    "drsEnabled": "drs_enabled",
    "drsMigrationThreshold": "drs_migration_threshold",
    "editionKey": "edition_key",
    "efiSecureBootEnabled": "efi_secure_boot_enabled",
    "egressShapingAverageBandwidth": "egress_shaping_average_bandwidth",
    "egressShapingBurstSize": "egress_shaping_burst_size",
    "egressShapingEnabled": "egress_shaping_enabled",
    "egressShapingPeakBandwidth": "egress_shaping_peak_bandwidth",
    "enableDiskUuid": "enable_disk_uuid",
    "enableLogging": "enable_logging",
    "eptRviMode": "ept_rvi_mode",
    "extraConfig": "extra_config",
    "faulttoleranceMaximumMbit": "faulttolerance_maximum_mbit",
    "faulttoleranceReservationMbit": "faulttolerance_reservation_mbit",
    "faulttoleranceShareCount": "faulttolerance_share_count",
    "faulttoleranceShareLevel": "faulttolerance_share_level",
    "fileUrls": "file_urls",
    "forceEvacuateOnDestroy": "force_evacuate_on_destroy",
    "forcePowerOff": "force_power_off",
    "freeSpace": "free_space",
    "guestId": "guest_id",
    "guestIpAddresses": "guest_ip_addresses",
    "haAdmissionControlFailoverHostSystemIds": "ha_admission_control_failover_host_system_ids",
    "haAdmissionControlHostFailureTolerance": "ha_admission_control_host_failure_tolerance",
    "haAdmissionControlPerformanceTolerance": "ha_admission_control_performance_tolerance",
    "haAdmissionControlPolicy": "ha_admission_control_policy",
    "haAdmissionControlResourcePercentageAutoCompute": "ha_admission_control_resource_percentage_auto_compute",
    "haAdmissionControlResourcePercentageCpu": "ha_admission_control_resource_percentage_cpu",
    "haAdmissionControlResourcePercentageMemory": "ha_admission_control_resource_percentage_memory",
    "haAdmissionControlSlotPolicyExplicitCpu": "ha_admission_control_slot_policy_explicit_cpu",
    "haAdmissionControlSlotPolicyExplicitMemory": "ha_admission_control_slot_policy_explicit_memory",
    "haAdmissionControlSlotPolicyUseExplicitSize": "ha_admission_control_slot_policy_use_explicit_size",
    "haAdvancedOptions": "ha_advanced_options",
    "haDatastoreApdRecoveryAction": "ha_datastore_apd_recovery_action",
    "haDatastoreApdResponse": "ha_datastore_apd_response",
    "haDatastoreApdResponseDelay": "ha_datastore_apd_response_delay",
    "haDatastorePdlResponse": "ha_datastore_pdl_response",
    "haEnabled": "ha_enabled",
    "haHeartbeatDatastoreIds": "ha_heartbeat_datastore_ids",
    "haHeartbeatDatastorePolicy": "ha_heartbeat_datastore_policy",
    "haHostIsolationResponse": "ha_host_isolation_response",
    "haHostMonitoring": "ha_host_monitoring",
    "haVmComponentProtection": "ha_vm_component_protection",
    "haVmDependencyRestartCondition": "ha_vm_dependency_restart_condition",
    "haVmFailureInterval": "ha_vm_failure_interval",
    "haVmMaximumFailureWindow": "ha_vm_maximum_failure_window",
    "haVmMaximumResets": "ha_vm_maximum_resets",
    "haVmMinimumUptime": "ha_vm_minimum_uptime",
    "haVmMonitoring": "ha_vm_monitoring",
    "haVmMonitoringUseClusterDefaults": "ha_vm_monitoring_use_cluster_defaults",
    "haVmRestartAdditionalDelay": "ha_vm_restart_additional_delay",
    "haVmRestartPriority": "ha_vm_restart_priority",
    "haVmRestartTimeout": "ha_vm_restart_timeout",
    "hardwareVersion": "hardware_version",
    "hbrMaximumMbit": "hbr_maximum_mbit",
    "hbrReservationMbit": "hbr_reservation_mbit",
    "hbrShareCount": "hbr_share_count",
    "hbrShareLevel": "hbr_share_level",
    "hostClusterExitTimeout": "host_cluster_exit_timeout",
    "hostManaged": "host_managed",
    "hostSystemId": "host_system_id",
    "hostSystemIds": "host_system_ids",
    "hvMode": "hv_mode",
    "ideControllerCount": "ide_controller_count",
    "ignoredGuestIps": "ignored_guest_ips",
    "ingressShapingAverageBandwidth": "ingress_shaping_average_bandwidth",
    "ingressShapingBurstSize": "ingress_shaping_burst_size",
    "ingressShapingEnabled": "ingress_shaping_enabled",
    "ingressShapingPeakBandwidth": "ingress_shaping_peak_bandwidth",
    "ipv4Address": "ipv4_address",
    "iscsiMaximumMbit": "iscsi_maximum_mbit",
    "iscsiReservationMbit": "iscsi_reservation_mbit",
    "iscsiShareCount": "iscsi_share_count",
    "iscsiShareLevel": "iscsi_share_level",
    "lacpApiVersion": "lacp_api_version",
    "lacpEnabled": "lacp_enabled",
    "lacpMode": "lacp_mode",
    "latencySensitivity": "latency_sensitivity",
    "libraryId": "library_id",
    "licenseKey": "license_key",
    "linkDiscoveryOperation": "link_discovery_operation",
    "linkDiscoveryProtocol": "link_discovery_protocol",
    "livePortMovingAllowed": "live_port_moving_allowed",
    "maintenanceMode": "maintenance_mode",
    "managedObjectType": "managed_object_type",
    "managementMaximumMbit": "management_maximum_mbit",
    "managementReservationMbit": "management_reservation_mbit",
    "managementShareCount": "management_share_count",
    "managementShareLevel": "management_share_level",
    "maxMtu": "max_mtu",
    "memoryExpandable": "memory_expandable",
    "memoryHotAddEnabled": "memory_hot_add_enabled",
    "memoryLimit": "memory_limit",
    "memoryReservation": "memory_reservation",
    "memoryShareCount": "memory_share_count",
    "memoryShareLevel": "memory_share_level",
    "memoryShares": "memory_shares",
    "migrateWaitTimeout": "migrate_wait_timeout",
    "multicastFilteringMode": "multicast_filtering_mode",
    "multipleHostAccess": "multiple_host_access",
    "nestedHvEnabled": "nested_hv_enabled",
    "netflowActiveFlowTimeout": "netflow_active_flow_timeout",
    "netflowCollectorIpAddress": "netflow_collector_ip_address",
    "netflowCollectorPort": "netflow_collector_port",
    "netflowEnabled": "netflow_enabled",
    "netflowIdleFlowTimeout": "netflow_idle_flow_timeout",
    "netflowInternalFlowsOnly": "netflow_internal_flows_only",
    "netflowObservationDomainId": "netflow_observation_domain_id",
    "netflowOverrideAllowed": "netflow_override_allowed",
    "netflowSamplingRate": "netflow_sampling_rate",
    "networkAdapters": "network_adapters",
    "networkInterfaces": "network_interfaces",
    "networkResourceControlEnabled": "network_resource_control_enabled",
    "networkResourceControlVersion": "network_resource_control_version",
    "networkResourcePoolKey": "network_resource_pool_key",
    "networkResourcePoolOverrideAllowed": "network_resource_pool_override_allowed",
    "nfsMaximumMbit": "nfs_maximum_mbit",
    "nfsReservationMbit": "nfs_reservation_mbit",
    "nfsShareCount": "nfs_share_count",
    "nfsShareLevel": "nfs_share_level",
    "notifySwitches": "notify_switches",
    "numCoresPerSocket": "num_cores_per_socket",
    "numCpus": "num_cpus",
    "numberOfPorts": "number_of_ports",
    "ovfDeploy": "ovf_deploy",
    "parentFolderId": "parent_folder_id",
    "parentResourcePoolId": "parent_resource_pool_id",
    "pciDeviceIds": "pci_device_ids",
    "portConfigResetAtDisconnect": "port_config_reset_at_disconnect",
    "portNameFormat": "port_name_format",
    "portPrivateSecondaryVlanId": "port_private_secondary_vlan_id",
    "poweronTimeout": "poweron_timeout",
    "proactiveHaAutomationLevel": "proactive_ha_automation_level",
    "proactiveHaEnabled": "proactive_ha_enabled",
    "proactiveHaModerateRemediation": "proactive_ha_moderate_remediation",
    "proactiveHaProviderIds": "proactive_ha_provider_ids",
    "proactiveHaSevereRemediation": "proactive_ha_severe_remediation",
    "protocolEndpoint": "protocol_endpoint",
    "rebootRequired": "reboot_required",
    "remoteHosts": "remote_hosts",
    "remotePath": "remote_path",
    "removeChildren": "remove_children",
    "resourcePoolId": "resource_pool_id",
    "runToolsScriptsAfterPowerOn": "run_tools_scripts_after_power_on",
    "runToolsScriptsAfterResume": "run_tools_scripts_after_resume",
    "runToolsScriptsBeforeGuestReboot": "run_tools_scripts_before_guest_reboot",
    "runToolsScriptsBeforeGuestShutdown": "run_tools_scripts_before_guest_shutdown",
    "runToolsScriptsBeforeGuestStandby": "run_tools_scripts_before_guest_standby",
    "sataControllerCount": "sata_controller_count",
    "scsiBusSharing": "scsi_bus_sharing",
    "scsiControllerCount": "scsi_controller_count",
    "scsiType": "scsi_type",
    "sdrsAdvancedOptions": "sdrs_advanced_options",
    "sdrsAutomationLevel": "sdrs_automation_level",
    "sdrsDefaultIntraVmAffinity": "sdrs_default_intra_vm_affinity",
    "sdrsEnabled": "sdrs_enabled",
    "sdrsFreeSpaceThreshold": "sdrs_free_space_threshold",
    "sdrsFreeSpaceThresholdMode": "sdrs_free_space_threshold_mode",
    "sdrsFreeSpaceUtilizationDifference": "sdrs_free_space_utilization_difference",
    "sdrsIntraVmAffinity": "sdrs_intra_vm_affinity",
    "sdrsIoBalanceAutomationLevel": "sdrs_io_balance_automation_level",
    "sdrsIoLatencyThreshold": "sdrs_io_latency_threshold",
    "sdrsIoLoadBalanceEnabled": "sdrs_io_load_balance_enabled",
    "sdrsIoLoadImbalanceThreshold": "sdrs_io_load_imbalance_threshold",
    "sdrsIoReservableIopsThreshold": "sdrs_io_reservable_iops_threshold",
    "sdrsIoReservablePercentThreshold": "sdrs_io_reservable_percent_threshold",
    "sdrsIoReservableThresholdMode": "sdrs_io_reservable_threshold_mode",
    "sdrsLoadBalanceInterval": "sdrs_load_balance_interval",
    "sdrsPolicyEnforcementAutomationLevel": "sdrs_policy_enforcement_automation_level",
    "sdrsRuleEnforcementAutomationLevel": "sdrs_rule_enforcement_automation_level",
    "sdrsSpaceBalanceAutomationLevel": "sdrs_space_balance_automation_level",
    "sdrsSpaceUtilizationThreshold": "sdrs_space_utilization_threshold",
    "sdrsVmEvacuationAutomationLevel": "sdrs_vm_evacuation_automation_level",
    "securityPolicyOverrideAllowed": "security_policy_override_allowed",
    "securityType": "security_type",
    "shapingAverageBandwidth": "shaping_average_bandwidth",
    "shapingBurstSize": "shaping_burst_size",
    "shapingEnabled": "shaping_enabled",
    "shapingOverrideAllowed": "shaping_override_allowed",
    "shapingPeakBandwidth": "shaping_peak_bandwidth",
    "shutdownWaitTimeout": "shutdown_wait_timeout",
    "snapshotName": "snapshot_name",
    "sourceDatacenter": "source_datacenter",
    "sourceDatastore": "source_datastore",
    "sourceFile": "source_file",
    "standbyNics": "standby_nics",
    "standbyUplinks": "standby_uplinks",
    "startAction": "start_action",
    "startDelay": "start_delay",
    "startOrder": "start_order",
    "stopAction": "stop_action",
    "stopDelay": "stop_delay",
    "storageBackings": "storage_backings",
    "storagePolicyId": "storage_policy_id",
    "swapPlacementPolicy": "swap_placement_policy",
    "syncTimeWithHost": "sync_time_with_host",
    "tagRules": "tag_rules",
    "targetId": "target_id",
    "teamingPolicy": "teaming_policy",
    "trafficFilterOverrideAllowed": "traffic_filter_override_allowed",
    "txUplink": "tx_uplink",
    "uncommittedSpace": "uncommitted_space",
    "uplinkTeamingOverrideAllowed": "uplink_teaming_override_allowed",
    "vappTransports": "vapp_transports",
    "vdpMaximumMbit": "vdp_maximum_mbit",
    "vdpReservationMbit": "vdp_reservation_mbit",
    "vdpShareCount": "vdp_share_count",
    "vdpShareLevel": "vdp_share_level",
    "virtualMachineId": "virtual_machine_id",
    "virtualMachineIds": "virtual_machine_ids",
    "virtualMachineUuid": "virtual_machine_uuid",
    "virtualSwitchName": "virtual_switch_name",
    "virtualmachineMaximumMbit": "virtualmachine_maximum_mbit",
    "virtualmachineReservationMbit": "virtualmachine_reservation_mbit",
    "virtualmachineShareCount": "virtualmachine_share_count",
    "virtualmachineShareLevel": "virtualmachine_share_level",
    "vlanId": "vlan_id",
    "vlanOverrideAllowed": "vlan_override_allowed",
    "vlanRanges": "vlan_ranges",
    "vmGroupName": "vm_group_name",
    "vmdkPath": "vmdk_path",
    "vmotionMaximumMbit": "vmotion_maximum_mbit",
    "vmotionReservationMbit": "vmotion_reservation_mbit",
    "vmotionShareCount": "vmotion_share_count",
    "vmotionShareLevel": "vmotion_share_level",
    "vmwareToolsStatus": "vmware_tools_status",
    "vmxPath": "vmx_path",
    "vsanMaximumMbit": "vsan_maximum_mbit",
    "vsanReservationMbit": "vsan_reservation_mbit",
    "vsanShareCount": "vsan_share_count",
    "vsanShareLevel": "vsan_share_level",
    "waitForGuest": "wait_for_guest",
    "waitForGuestIpTimeout": "wait_for_guest_ip_timeout",
    "waitForGuestNetRoutable": "wait_for_guest_net_routable",
    "waitForGuestNetTimeout": "wait_for_guest_net_timeout",
}
