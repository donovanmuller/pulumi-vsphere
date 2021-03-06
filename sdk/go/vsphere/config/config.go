// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi/config"
)

// If set, VMware vSphere client will permit unverifiable SSL certificates.
func GetAllowUnverifiedSsl(ctx *pulumi.Context) bool {
	v, err := config.TryBool(ctx, "vsphere:allowUnverifiedSsl")
	if err == nil {
		return v
	}
	return getEnvOrDefault(false, parseEnvBool, "VSPHERE_ALLOW_UNVERIFIED_SSL").(bool)
}

// govmomi debug
func GetClientDebug(ctx *pulumi.Context) bool {
	v, err := config.TryBool(ctx, "vsphere:clientDebug")
	if err == nil {
		return v
	}
	return getEnvOrDefault(false, parseEnvBool, "VSPHERE_CLIENT_DEBUG").(bool)
}

// govmomi debug path for debug
func GetClientDebugPath(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "vsphere:clientDebugPath")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "VSPHERE_CLIENT_DEBUG_PATH").(string)
}

// govmomi debug path for a single run
func GetClientDebugPathRun(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "vsphere:clientDebugPathRun")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "VSPHERE_CLIENT_DEBUG_PATH_RUN").(string)
}

// The user password for vSphere API operations.
func GetPassword(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "vsphere:password")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "VSPHERE_PASSWORD").(string)
}

// Persist vSphere client sessions to disk
func GetPersistSession(ctx *pulumi.Context) bool {
	v, err := config.TryBool(ctx, "vsphere:persistSession")
	if err == nil {
		return v
	}
	return getEnvOrDefault(false, parseEnvBool, "VSPHERE_PERSIST_SESSION").(bool)
}

// The directory to save vSphere REST API sessions to
func GetRestSessionPath(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "vsphere:restSessionPath")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "VSPHERE_REST_SESSION_PATH").(string)
}

// The user name for vSphere API operations.
func GetUser(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "vsphere:user")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "VSPHERE_USER").(string)
}

// Deprecated: This field has been renamed to vsphere_server.
func GetVcenterServer(ctx *pulumi.Context) string {
	return config.Get(ctx, "vsphere:vcenterServer")
}

// Keep alive interval for the VIM session in minutes
func GetVimKeepAlive(ctx *pulumi.Context) int {
	v, err := config.TryInt(ctx, "vsphere:vimKeepAlive")
	if err == nil {
		return v
	}
	return getEnvOrDefault(0, parseEnvInt, "VSPHERE_VIM_KEEP_ALIVE").(int)
}

// The directory to save vSphere SOAP API sessions to
func GetVimSessionPath(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "vsphere:vimSessionPath")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "VSPHERE_VIM_SESSION_PATH").(string)
}

// The vSphere Server name for vSphere API operations.
func GetVsphereServer(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "vsphere:vsphereServer")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "VSPHERE_SERVER").(string)
}
