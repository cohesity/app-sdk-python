# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_app_sdk.models.user_ssh_key_info

class VolumeSpec(object):

    """Implementation of the 'VolumeSpec' model.

    Spec to create a kubernetes volume backed by cohesity view.

    Attributes:
        volume_type (VolumeTypeEnum): Type of the backing for the volume
        volume_capacity_bytes (int): volume capacity
        volume_claim_ref (string): The specific persistent volume claim that
            will claim this volume.
        disk_image_location (string): Path for disk image from which to create
            volume. Can either be an absolute path or relative path in the
            app's output view.
        disk_type (DiskTypeEnum): Disk type
        sysprep_operations (list of SysprepOperationEnum): Sequence of sysprep
            operations to be done on the disk
        user_ssh_keys (list of UserSshKeyInfo): Ssh keys for some users to be
            inserted into the VM.
        swap_mount_point (string): Swap mount point to be inserted.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "volume_type":'volumeType',
        "volume_capacity_bytes":'volumeCapacityBytes',
        "volume_claim_ref":'volumeClaimRef',
        "disk_image_location":'diskImageLocation',
        "disk_type":'diskType',
        "sysprep_operations":'sysprepOperations',
        "user_ssh_keys":'userSshKeys',
        "swap_mount_point":'swapMountPoint'
    }

    def __init__(self,
                 volume_type=None,
                 volume_capacity_bytes=None,
                 volume_claim_ref=None,
                 disk_image_location=None,
                 disk_type=None,
                 sysprep_operations=None,
                 user_ssh_keys=None,
                 swap_mount_point=None):
        """Constructor for the VolumeSpec class"""

        # Initialize members of the class
        self.volume_type = volume_type
        self.volume_capacity_bytes = volume_capacity_bytes
        self.volume_claim_ref = volume_claim_ref
        self.disk_image_location = disk_image_location
        self.disk_type = disk_type
        self.sysprep_operations = sysprep_operations
        self.user_ssh_keys = user_ssh_keys
        self.swap_mount_point = swap_mount_point


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        volume_type = dictionary.get('volumeType')
        volume_capacity_bytes = dictionary.get('volumeCapacityBytes')
        volume_claim_ref = dictionary.get('volumeClaimRef')
        disk_image_location = dictionary.get('diskImageLocation')
        disk_type = dictionary.get('diskType')
        sysprep_operations = dictionary.get('sysprepOperations')
        user_ssh_keys = None
        if dictionary.get('userSshKeys') != None:
            user_ssh_keys = list()
            for structure in dictionary.get('userSshKeys'):
                user_ssh_keys.append(cohesity_app_sdk.models.user_ssh_key_info.UserSshKeyInfo.from_dictionary(structure))
        swap_mount_point = dictionary.get('swapMountPoint')

        # Return an object of this model
        return cls(volume_type,
                   volume_capacity_bytes,
                   volume_claim_ref,
                   disk_image_location,
                   disk_type,
                   sysprep_operations,
                   user_ssh_keys,
                   swap_mount_point)


