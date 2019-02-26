# -*- coding: utf-8 -*-


class ManagementAccessToken(object):

    """Implementation of the 'ManagementAccessToken' model.

    TODO: type model description here.

    Attributes:
        access_token (string): Token which can be used to call Iris Management
            apis.
        token_type (string): Type of the token returned. E.g. Bearer.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access_token":'accessToken',
        "token_type":'tokenType'
    }

    def __init__(self,
                 access_token=None,
                 token_type=None):
        """Constructor for the ManagementAccessToken class"""

        # Initialize members of the class
        self.access_token = access_token
        self.token_type = token_type


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
        access_token = dictionary.get('accessToken')
        token_type = dictionary.get('tokenType')

        # Return an object of this model
        return cls(access_token,
                   token_type)


