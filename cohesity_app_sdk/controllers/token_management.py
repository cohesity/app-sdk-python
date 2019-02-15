# -*- coding: utf-8 -*-

import logging
from cohesity_app_sdk.api_helper import APIHelper
from cohesity_app_sdk.configuration import Configuration
from cohesity_app_sdk.controllers.base_controller import BaseController
from cohesity_app_sdk.http.auth.o_auth_2 import OAuth2
from cohesity_app_sdk.models.management_access_token import ManagementAccessToken
from cohesity_app_sdk.exceptions.api_exception import APIException
from cohesity_app_sdk.exceptions.error_exception import ErrorException

class TokenManagement(BaseController):

    """A Controller to access Endpoints in the cohesity_app_sdk API."""

    def __init__(self, client=None, call_back=None):
        super(TokenManagement, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def create_management_access_token(self):
        """Does a POST request to /managementTokens.

        Use this api to get a new management api token.

        Returns:
            ManagementAccessToken: Response from the API. Successfully created
                new token.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_management_access_token called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for create_management_access_token.')
            _url_path = '/managementTokens'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for create_management_access_token.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_management_access_token.')
            _request = self.http_client.post(_query_url, headers=_headers)
            OAuth2.apply(_request)
            _context = self.execute_request(_request, name = 'create_management_access_token')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_management_access_token.')
            if _context.response.status_code == 401:
                raise APIException('Invalid token.', _context)
            elif _context.response.status_code == 500:
                raise ErrorException('Unexpected error.', _context)
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, ManagementAccessToken.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
