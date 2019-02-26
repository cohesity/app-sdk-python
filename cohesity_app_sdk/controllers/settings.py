# -*- coding: utf-8 -*-

import logging
from cohesity_app_sdk.api_helper import APIHelper
from cohesity_app_sdk.configuration import Configuration
from cohesity_app_sdk.controllers.base_controller import BaseController
from cohesity_app_sdk.http.auth.custom_auth import CustomAuth
from cohesity_app_sdk.models.app_settings import AppSettings
from cohesity_app_sdk.exceptions.api_exception import APIException
from cohesity_app_sdk.exceptions.error_exception import ErrorException

class Settings(BaseController):

    """A Controller to access Endpoints in the cohesity_app_sdk API."""

    def __init__(self, client=None, call_back=None):
        super(Settings, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def get_app_settings(self):
        """Does a GET request to /appSettings.

        Returns app settings object.

        Returns:
            AppSettings: Response from the API. Successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_app_settings called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for get_app_settings.')
            _url_path = '/appSettings'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for get_app_settings.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_app_settings.')
            _request = self.http_client.get(_query_url, headers=_headers)
            CustomAuth.apply(_request)
            _context = self.execute_request(_request, name = 'get_app_settings')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_app_settings.')
            if _context.response.status_code == 401:
                raise APIException('Invalid token', _context)
            elif _context.response.status_code == 500:
                raise ErrorException('Unexpected error', _context)
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, AppSettings.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
