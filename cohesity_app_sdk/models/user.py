# -*- coding: utf-8 -*-


class User(object):

    """Implementation of the 'User' model.

    Specifies user information who launched the given app instance.

    Attributes:
        domain (string): Domain of the user who launched the app instance.
        user_name (string): Username of the user who launched the app
            instance.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "domain":'domain',
        "user_name":'userName'
    }

    def __init__(self,
                 domain=None,
                 user_name=None):
        """Constructor for the User class"""

        # Initialize members of the class
        self.domain = domain
        self.user_name = user_name


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
        domain = dictionary.get('domain')
        user_name = dictionary.get('userName')

        # Return an object of this model
        return cls(domain,
                   user_name)


