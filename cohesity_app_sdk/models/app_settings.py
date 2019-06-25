# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_app_sdk.models.user
import cohesity_app_sdk.models.app_instance_settings

class AppSettings(object):

    """Implementation of the 'AppSettings' model.

    TODO: type model description here.

    Attributes:
        user (User): Specifies user information who launched the given app
            instance.
        app_instance_settings (AppInstanceSettings): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "user":'user',
        "app_instance_settings":'appInstanceSettings'
    }

    def __init__(self,
                 user=None,
                 app_instance_settings=None):
        """Constructor for the AppSettings class"""

        # Initialize members of the class
        self.user = user
        self.app_instance_settings = app_instance_settings


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
        user = cohesity_app_sdk.models.user.User.from_dictionary(dictionary.get('user')) if dictionary.get('user') else None
        app_instance_settings = cohesity_app_sdk.models.app_instance_settings.AppInstanceSettings.from_dictionary(dictionary.get('appInstanceSettings')) if dictionary.get('appInstanceSettings') else None

        # Return an object of this model
        return cls(user,
                   app_instance_settings)


