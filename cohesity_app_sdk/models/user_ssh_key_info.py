# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class UserSshKeyInfo(object):

    """Implementation of the 'UserSshKeyInfo' model.

    Username and the ssh key for the user.

    Attributes:
        username (string): Username.
        ssh_key (string): Ssh key for the user.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "username":'username',
        "ssh_key":'sshKey'
    }

    def __init__(self,
                 username=None,
                 ssh_key=None):
        """Constructor for the UserSshKeyInfo class"""

        # Initialize members of the class
        self.username = username
        self.ssh_key = ssh_key


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
        username = dictionary.get('username')
        ssh_key = dictionary.get('sshKey')

        # Return an object of this model
        return cls(username,
                   ssh_key)


