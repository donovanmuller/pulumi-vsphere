// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package vsphere

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// The `File` resource can be used to upload files (such as virtual disk
// files) from the host machine that this provider is running on to a target
// datastore.  The resource can also be used to copy files between datastores, or
// from one location to another on the same datastore.
//
// Updates to destination parameters such as `datacenter`, `datastore`, or
// `destinationFile` will move the managed file a new destination based on the
// values of the new settings.  If any source parameter is changed, such as
// `sourceDatastore`, `sourceDatacenter` or `sourceFile`), the resource will be
// re-created. Depending on if destination parameters are being changed as well,
// this may result in the destination file either being overwritten or deleted at
// the old location.
//
// ## Example Usage
// ### Uploading a file
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := vsphere.NewFile(ctx, "ubuntuDiskUpload", &vsphere.FileArgs{
// 			Datacenter:      pulumi.String("my_datacenter"),
// 			Datastore:       pulumi.String("local"),
// 			DestinationFile: pulumi.String("/my_path/disks/custom_ubuntu.vmdk"),
// 			SourceFile:      pulumi.String("/home/ubuntu/my_disks/custom_ubuntu.vmdk"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### Copying a file
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := vsphere.NewFile(ctx, "ubuntuDiskCopy", &vsphere.FileArgs{
// 			Datacenter:       pulumi.String("my_datacenter"),
// 			Datastore:        pulumi.String("local"),
// 			DestinationFile:  pulumi.String("/my_path/custom_ubuntu_id.vmdk"),
// 			SourceDatacenter: pulumi.String("my_datacenter"),
// 			SourceDatastore:  pulumi.String("local"),
// 			SourceFile:       pulumi.String("/my_path/disks/custom_ubuntu.vmdk"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type File struct {
	pulumi.CustomResourceState

	// Create directories in `destinationFile`
	// path parameter if any missing for copy operation.
	CreateDirectories pulumi.BoolPtrOutput `pulumi:"createDirectories"`
	// The name of a datacenter in which the file will be
	// uploaded to.
	Datacenter pulumi.StringPtrOutput `pulumi:"datacenter"`
	// The name of the datastore in which to upload the
	// file to.
	Datastore pulumi.StringOutput `pulumi:"datastore"`
	// The path to where the file should be uploaded
	// or copied to on vSphere.
	DestinationFile pulumi.StringOutput `pulumi:"destinationFile"`
	// The name of a datacenter in which the file
	// will be copied from. Forces a new resource if changed.
	SourceDatacenter pulumi.StringPtrOutput `pulumi:"sourceDatacenter"`
	// The name of the datastore in which file will
	// be copied from. Forces a new resource if changed.
	SourceDatastore pulumi.StringPtrOutput `pulumi:"sourceDatastore"`
	// The path to the file being uploaded from the
	// host to vSphere or copied within vSphere. Forces a new resource if
	// changed.
	SourceFile pulumi.StringOutput `pulumi:"sourceFile"`
}

// NewFile registers a new resource with the given unique name, arguments, and options.
func NewFile(ctx *pulumi.Context,
	name string, args *FileArgs, opts ...pulumi.ResourceOption) (*File, error) {
	if args == nil || args.Datastore == nil {
		return nil, errors.New("missing required argument 'Datastore'")
	}
	if args == nil || args.DestinationFile == nil {
		return nil, errors.New("missing required argument 'DestinationFile'")
	}
	if args == nil || args.SourceFile == nil {
		return nil, errors.New("missing required argument 'SourceFile'")
	}
	if args == nil {
		args = &FileArgs{}
	}
	var resource File
	err := ctx.RegisterResource("vsphere:index/file:File", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFile gets an existing File resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFile(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FileState, opts ...pulumi.ResourceOption) (*File, error) {
	var resource File
	err := ctx.ReadResource("vsphere:index/file:File", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering File resources.
type fileState struct {
	// Create directories in `destinationFile`
	// path parameter if any missing for copy operation.
	CreateDirectories *bool `pulumi:"createDirectories"`
	// The name of a datacenter in which the file will be
	// uploaded to.
	Datacenter *string `pulumi:"datacenter"`
	// The name of the datastore in which to upload the
	// file to.
	Datastore *string `pulumi:"datastore"`
	// The path to where the file should be uploaded
	// or copied to on vSphere.
	DestinationFile *string `pulumi:"destinationFile"`
	// The name of a datacenter in which the file
	// will be copied from. Forces a new resource if changed.
	SourceDatacenter *string `pulumi:"sourceDatacenter"`
	// The name of the datastore in which file will
	// be copied from. Forces a new resource if changed.
	SourceDatastore *string `pulumi:"sourceDatastore"`
	// The path to the file being uploaded from the
	// host to vSphere or copied within vSphere. Forces a new resource if
	// changed.
	SourceFile *string `pulumi:"sourceFile"`
}

type FileState struct {
	// Create directories in `destinationFile`
	// path parameter if any missing for copy operation.
	CreateDirectories pulumi.BoolPtrInput
	// The name of a datacenter in which the file will be
	// uploaded to.
	Datacenter pulumi.StringPtrInput
	// The name of the datastore in which to upload the
	// file to.
	Datastore pulumi.StringPtrInput
	// The path to where the file should be uploaded
	// or copied to on vSphere.
	DestinationFile pulumi.StringPtrInput
	// The name of a datacenter in which the file
	// will be copied from. Forces a new resource if changed.
	SourceDatacenter pulumi.StringPtrInput
	// The name of the datastore in which file will
	// be copied from. Forces a new resource if changed.
	SourceDatastore pulumi.StringPtrInput
	// The path to the file being uploaded from the
	// host to vSphere or copied within vSphere. Forces a new resource if
	// changed.
	SourceFile pulumi.StringPtrInput
}

func (FileState) ElementType() reflect.Type {
	return reflect.TypeOf((*fileState)(nil)).Elem()
}

type fileArgs struct {
	// Create directories in `destinationFile`
	// path parameter if any missing for copy operation.
	CreateDirectories *bool `pulumi:"createDirectories"`
	// The name of a datacenter in which the file will be
	// uploaded to.
	Datacenter *string `pulumi:"datacenter"`
	// The name of the datastore in which to upload the
	// file to.
	Datastore string `pulumi:"datastore"`
	// The path to where the file should be uploaded
	// or copied to on vSphere.
	DestinationFile string `pulumi:"destinationFile"`
	// The name of a datacenter in which the file
	// will be copied from. Forces a new resource if changed.
	SourceDatacenter *string `pulumi:"sourceDatacenter"`
	// The name of the datastore in which file will
	// be copied from. Forces a new resource if changed.
	SourceDatastore *string `pulumi:"sourceDatastore"`
	// The path to the file being uploaded from the
	// host to vSphere or copied within vSphere. Forces a new resource if
	// changed.
	SourceFile string `pulumi:"sourceFile"`
}

// The set of arguments for constructing a File resource.
type FileArgs struct {
	// Create directories in `destinationFile`
	// path parameter if any missing for copy operation.
	CreateDirectories pulumi.BoolPtrInput
	// The name of a datacenter in which the file will be
	// uploaded to.
	Datacenter pulumi.StringPtrInput
	// The name of the datastore in which to upload the
	// file to.
	Datastore pulumi.StringInput
	// The path to where the file should be uploaded
	// or copied to on vSphere.
	DestinationFile pulumi.StringInput
	// The name of a datacenter in which the file
	// will be copied from. Forces a new resource if changed.
	SourceDatacenter pulumi.StringPtrInput
	// The name of the datastore in which file will
	// be copied from. Forces a new resource if changed.
	SourceDatastore pulumi.StringPtrInput
	// The path to the file being uploaded from the
	// host to vSphere or copied within vSphere. Forces a new resource if
	// changed.
	SourceFile pulumi.StringInput
}

func (FileArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*fileArgs)(nil)).Elem()
}
