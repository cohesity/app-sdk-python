# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import logging
from cohesity_app_sdk.api_helper import APIHelper
from cohesity_app_sdk.configuration import Configuration
from cohesity_app_sdk.controllers.base_controller import BaseController
from cohesity_app_sdk.http.auth.o_auth_2 import OAuth2
from cohesity_app_sdk.exceptions.api_exception import APIException
from cohesity_app_sdk.exceptions.error_error_exception import ErrorErrorException

class MountController(BaseController):

    """A Controller to access Endpoints in the cohesity_app_sdk API."""

    def __init__(self, client=None, call_back=None):
        super(MountController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def delete_unmount(self,
                       dir_name):
        """Does a DELETE request to /mounts/{dirName}.

        Unmount previously mounted view/namespace or volume of a protected
        entity.

        Args:
            dir_name (string): Name of the mount directory.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_unmount called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for delete_unmount.')
            _url_path = '/mounts/{dirName}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'dirName': dir_name
            })
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare and execute request
            self.logger.info('Preparing and executing request for delete_unmount.')
            _request = self.http_client.delete(_query_url)
            OAuth2.apply(_request)
            _context = self.execute_request(_request, name = 'delete_unmount')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_unmount.')
            if _context.response.status_code == 400:
                raise APIException('Invalid parameters.', _context)
            elif _context.response.status_code == 401:
                raise APIException('Invalid token.', _context)
            elif _context.response.status_code == 404:
                raise APIException('Directory doesn\'t exist.', _context)
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

    def create_mount(self,
                     mount_options):
        """Does a POST request to /mounts.

        Allows you to mount a cohesity external view or snapshots of a
        protected object (VM volumes or NAS).

        Args:
            mount_options (MountOptions): TODO: type description here.
                Example:

        Returns:
            void: Response from the API. Mount operation is in progress.
                Client should retry the mount call with same arguments till it
                gets success before using the mount.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_mount called.')

            # Prepare query URL
            self.logger.info('Preparing query URL for create_mount.')
            _url_path = '/mounts'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)

            # Prepare headers
            self.logger.info('Preparing headers for create_mount.')
            _headers = {
                'content-type': 'application/json; charset=utf-8'
            }

            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_mount.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(mount_options))
            OAuth2.apply(_request)
            _context = self.execute_request(_request, name = 'create_mount')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_mount.')
            if _context.response.status_code == 400:
                raise APIException('Validation errors.', _context)
            elif _context.response.status_code == 401:
                raise APIException('Invalid token.', _context)
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
