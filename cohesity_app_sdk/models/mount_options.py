# -*- coding: utf-8 -*-


class MountOptions(object):

    """Implementation of the 'MountOptions' model.

    TODO: type model description here.

    Attributes:
        dir_name (string): Directory where view/namespace is mounted.
        view_name (string): The name of the view that is to be mounted.
        mount_options (string): Additional options for mount. All options from
            mount command are supported e.g. rw, ro.
        mount_protocol (MountProtocolEnum): Type of the mount.
        user_name (string): Username if the mount type is smb.
        password (string): Password if the mount type is smb.
        namespace_name (string): The namespace within the view that is to be
            mounted.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dir_name":'dirName',
        "view_name":'viewName',
        "mount_options":'mountOptions',
        "mount_protocol":'mountProtocol',
        "user_name":'userName',
        "password":'password',
        "namespace_name":'namespaceName'
    }

    def __init__(self,
                 dir_name=None,
                 view_name=None,
                 mount_options=None,
                 mount_protocol=None,
                 user_name=None,
                 password=None,
                 namespace_name=None):
        """Constructor for the MountOptions class"""

        # Initialize members of the class
        self.dir_name = dir_name
        self.view_name = view_name
        self.mount_options = mount_options
        self.mount_protocol = mount_protocol
        self.user_name = user_name
        self.password = password
        self.namespace_name = namespace_name


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

        # Return an object of this model
        return cls(dir_name,
                   view_name,
                   mount_options,
                   mount_protocol,
                   user_name,
                   password,
                   namespace_name)


