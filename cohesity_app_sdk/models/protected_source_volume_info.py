# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class ProtectedSourceVolumeInfo(object):

    """Implementation of the 'ProtectedSourceVolumeInfo' model.

    Information about the logical volumes of a protected source as derived by
    inspecting a snapshot made using a protection run.

    Attributes:
        volumes (list of string): Names of volumes of the protected source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "volumes":'volumes'
    }

    def __init__(self,
                 volumes=None):
        """Constructor for the ProtectedSourceVolumeInfo class"""

        # Initialize members of the class
        self.volumes = volumes


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
        volumes = dictionary.get('volumes')

        # Return an object of this model
        return cls(volumes)


