# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import logging
from cohesity_app_sdk.api_helper import APIHelper
from cohesity_app_sdk.configuration import Configuration
from cohesity_app_sdk.controllers.base_controller import BaseController
from cohesity_app_sdk.http.auth.o_auth_2 import OAuth2
from cohesity_app_sdk.models.volume_info import VolumeInfo
from cohesity_app_sdk.exceptions.api_exception import APIException
from cohesity_app_sdk.exceptions.error_error_exception import ErrorErrorException

class Volume(BaseController):

    """A Controller to access Endpoints in the cohesity_app_sdk API."""

    def __init__(self, client=None, call_back=None):
        super(Volume, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def get_volume(self,
                   volume_name):
        """Does a GET request to /volumes/{volumeName}.

        Gets the status of persistent volume owned by this app.

        Args:
            volume_name (string): Name of the volume unique within the app
                instance.

        Returns:
            VolumeInfo: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_volume called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for get_volume.')
            _url_path = '/volumes/{volumeName}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'volumeName': volume_name
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for get_volume.')
            _headers = {
                'accept': 'application/json'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_volume.')
            _request = self.http_client.get(_query_url, headers=_headers)
            OAuth2.apply(_request)
            _context = self.execute_request(_request, name = 'get_volume')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_volume.')
            if _context.response.status_code == 401:
                raise APIException('Unauthorized', _context)
            elif _context.response.status_code == 404:
                raise APIException('Volume doesn\'t exist.', _context)
            elif _context.response.status_code == 500:
                raise ErrorErrorException('Unexpected error', _context)
            elif _context.response.status_code == 502:
                raise APIException('Bad Gateway.', _context)
            elif _context.response.status_code == 504:
                raise APIException('Gateway Timeout.', _context)
            self.validate_response(_context)

            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, VolumeInfo.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def delete_volume(self,
                      volume_name):
        """Does a DELETE request to /volumes/{volumeName}.

        Delete a previously created persistent volume owned by this app.

        Args:
            volume_name (string): Name of the volume unique within the app
                instance.

        Returns:
            void: Response from the API. Successful Operation.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_volume called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_volume.')
            _url_path = '/volumes/{volumeName}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'volumeName': volume_name
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info('Preparing and executing request for delete_volume.')
            _request = self.http_client.delete(_query_url)
            OAuth2.apply(_request)
            _context = self.execute_request(_request, name = 'delete_volume')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_volume.')
            if _context.response.status_code == 400:
                raise APIException('Invalid parameters.', _context)
            elif _context.response.status_code == 401:
                raise APIException('Unauthorized.', _context)
            elif _context.response.status_code == 404:
                raise APIException('Volume doesn\'t exist.', _context)
            elif _context.response.status_code == 500:
                raise ErrorErrorException('Unexpected error.', _context)
            elif _context.response.status_code == 502:
                raise APIException('Bad Gateway.', _context)
            elif _context.response.status_code == 504:
                raise APIException('Gateway Timeout.', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_volume(self,
                      volume_name,
                      volume_spec):
        """Does a PUT request to /volumes/{volumeName}.

        Use this API to create a new kubernetes persistent volume backed up by
        cohesity view.

        Args:
            volume_name (string): Name of the volume unique within the app
                instance.
            volume_spec (VolumeSpec): TODO: type description here. Example:

        Returns:
            void: Response from the API. Created.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_volume called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for create_volume.')
            _url_path = '/volumes/{volumeName}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'volumeName': volume_name
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_volume.')
            _headers = {
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_volume.')
            _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(volume_spec))
            OAuth2.apply(_request)
            _context = self.execute_request(_request, name = 'create_volume')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_volume.')
            if _context.response.status_code == 401:
                raise APIException('Unauthorized.', _context)
            elif _context.response.status_code == 409:
                raise APIException('Volume already exists with different parameters.', _context)
            elif _context.response.status_code == 500:
                raise ErrorErrorException('Unexpected error.', _context)
            elif _context.response.status_code == 502:
                raise APIException('Bad Gateway.', _context)
            elif _context.response.status_code == 504:
                raise APIException('Gateway Timeout.', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
