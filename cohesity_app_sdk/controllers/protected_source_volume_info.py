# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import logging
from cohesity_app_sdk.api_helper import APIHelper
from cohesity_app_sdk.configuration import Configuration
from cohesity_app_sdk.controllers.base_controller import BaseController
from cohesity_app_sdk.http.auth.o_auth_2 import OAuth2
from cohesity_app_sdk.models.protected_source_volume_info import ProtectedSourceVolumeInfo
from cohesity_app_sdk.exceptions.api_exception import APIException
from cohesity_app_sdk.exceptions.error_error_exception import ErrorErrorException

class ProtectedSourceVolumeInfo(BaseController):

    """A Controller to access Endpoints in the cohesity_app_sdk API."""

    def __init__(self, client=None, call_back=None):
        super(ProtectedSourceVolumeInfo, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def get_protected_source_volume_info(self,
                                         source_id):
        """Does a GET request to /protectedSourceVolumeInfo/{sourceId}.

        Gets the list of volumes for a snapshot of a protected source.

        Args:
            source_id (int): Unique ID of the protected source.

        Returns:
            ProtectedSourceVolumeInfo: Response from the API. Successful
                operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_protected_source_volume_info called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_protected_source_volume_info.')
            _url_path = '/protectedSourceVolumeInfo/{sourceId}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'sourceId': source_id
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_protected_source_volume_info.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_protected_source_volume_info.')
            _request = self.http_client.get(_query_url, headers=_headers)
            OAuth2.apply(_request)
            _context = self.execute_request(_request, name = 'get_protected_source_volume_info')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_protected_source_volume_info.')
            if _context.response.status_code == 401:
                raise APIException('Unauthorized', _context)
            elif _context.response.status_code == 404:
                raise APIException('Snapshot does not exist.', _context)
            elif _context.response.status_code == 500:
                raise ErrorErrorException('Unexpected error', _context)
            elif _context.response.status_code == 502:
                raise APIException('Bad Gateway.', _context)
            elif _context.response.status_code == 504:
                raise APIException('Gateway Timeout.', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, ProtectedSourceVolumeInfo.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
