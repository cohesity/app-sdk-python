# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class ProtectionJobRun(object):

    """Implementation of the 'ProtectionJobRun' model.

    Identification of a protection job run.

    Attributes:
        job_id (int): Id of the protection job unique within the cohesity
            cluster.
        run_id (int): Id of a run of the protection job.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "job_id":'jobId',
        "run_id":'runId'
    }

    def __init__(self,
                 job_id=None,
                 run_id=None):
        """Constructor for the ProtectionJobRun class"""

        # Initialize members of the class
        self.job_id = job_id
        self.run_id = run_id


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
        job_id = dictionary.get('jobId')
        run_id = dictionary.get('runId')

        # Return an object of this model
        return cls(job_id,
                   run_id)


