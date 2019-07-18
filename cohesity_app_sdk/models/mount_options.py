# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_app_sdk.models.protection_job_run

class MountOptions(object):

    """Implementation of the 'MountOptions' model.

    TODO: type model description here.

    Attributes:
        dir_name (string): Directory where view/namespace or volume of a
            protected source is mounted.
        view_name (string): The name of the external cohesity view that is to
            be mounted.
        mount_options (string): Additional options for mount. All options from
            mount command are supported e.g. rw, ro.
        mount_protocol (MountProtocolEnum): Type of the mount.
        user_name (string): Username if the mount type is smb.
        password (string): Password if the mount type is smb.
        namespace_name (string): If this type of mount is nfs this is the
            namespace within the view that is to be mounted.
        protected_source_id (int): If mounting snapshot of a protected source
            this is the unique ID of the protected source.
        protection_job_run (ProtectionJobRun): Identification of a protection
            job run.
        volume_name (string): Name of the volume of the VM to mount if the
            protected source is of type VM.
        pod_uid (string): The UID of the pod on which the container is
            running.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dir_name":'dirName',
        "view_name":'viewName',
        "mount_options":'mountOptions',
        "mount_protocol":'mountProtocol',
        "user_name":'userName',
        "password":'password',
        "namespace_name":'namespaceName',
        "protected_source_id":'protectedSourceId',
        "protection_job_run":'protectionJobRun',
        "volume_name":'volumeName',
        "pod_uid":'podUid'
    }

    def __init__(self,
                 dir_name=None,
                 view_name=None,
                 mount_options=None,
                 mount_protocol=None,
                 user_name=None,
                 password=None,
                 namespace_name=None,
                 protected_source_id=None,
                 protection_job_run=None,
                 volume_name=None,
                 pod_uid=None):
        """Constructor for the MountOptions class"""

        # Initialize members of the class
        self.dir_name = dir_name
        self.view_name = view_name
        self.mount_options = mount_options
        self.mount_protocol = mount_protocol
        self.user_name = user_name
        self.password = password
        self.namespace_name = namespace_name
        self.protected_source_id = protected_source_id
        self.protection_job_run = protection_job_run
        self.volume_name = volume_name
        self.pod_uid = pod_uid


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
        dir_name = dictionary.get('dirName')
        view_name = dictionary.get('viewName')
        mount_options = dictionary.get('mountOptions')
        mount_protocol = dictionary.get('mountProtocol')
        user_name = dictionary.get('userName')
        password = dictionary.get('password')
        namespace_name = dictionary.get('namespaceName')
        protected_source_id = dictionary.get('protectedSourceId')
        protection_job_run = cohesity_app_sdk.models.protection_job_run.ProtectionJobRun.from_dictionary(dictionary.get('protectionJobRun')) if dictionary.get('protectionJobRun') else None
        volume_name = dictionary.get('volumeName')
        pod_uid = dictionary.get('podUid')

        # Return an object of this model
        return cls(dir_name,
                   view_name,
                   mount_options,
                   mount_protocol,
                   user_name,
                   password,
                   namespace_name,
                   protected_source_id,
                   protection_job_run,
                   volume_name,
                   pod_uid)


