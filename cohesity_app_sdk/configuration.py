# -*- coding: utf-8 -*-

import sys
import logging

from cohesity_app_sdk.api_helper import APIHelper

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


class Configuration(object):

    """A class used for configuring the SDK by a user.

    This class need not be instantiated and all properties and methods
    are accessible without instance creation.

    """

    # Set the array parameter serialization method
    # (allowed: indexed, unindexed, plain, csv, tsv, psv)
    array_serialization = "indexed"

    # True if the client should skip verification of SSL certificates
    skip_ssl_verification = False

    # An enum for SDK environments
    class Environment(object):
        PRODUCTION = 0

    # An enum for API servers
    class Server(object):
        DEFAULT = 0

    # The environment in which the SDK is running
    environment = Environment.PRODUCTION

    # TODO: Set an appropriate value
    app_endpoint_ip = 'athena-server.cohesity.com'

    # TODO: Set an appropriate value
    app_endpoint_port = '25694'

    # App Authentication Token
    # TODO: Set an appropriate value
    app_auth_token = None


    # All the environments the SDK can run in
    environments = {
        Environment.PRODUCTION: {
            Server.DEFAULT: 'http://{app_endpoint_ip}:{app_endpoint_port}/athenaservices/api/v1/public',
        },
    }

    @classmethod
    def get_base_uri(cls, server=Server.DEFAULT):
        """Generates the appropriate base URI for the environment and the server.

        Args:
            server (Configuration.Server): The server enum for which the base URI is required.

        Returns:
            String: The base URI.

        """
        parameters = {
            "app_endpoint_ip": cls.app_endpoint_ip,
            "app_endpoint_port": cls.app_endpoint_port,
        }
        return APIHelper.append_url_with_template_parameters(
            cls.environments[cls.environment][server], parameters, False)

    @classmethod
    def disable_logging(cls):
        """Disable all logging in the SDK
        """
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

    @classmethod
    def enable_logging(cls, filename=None, filemode='a',
                       stream=sys.stdout, level=logging.INFO):
        """Enable logging in the SDK

        Args:
            filename: Specifies that a FileHandler be created, using the specified
                filename, rather than a StreamHandler.
            filemode: If filename is specified, open the file in this mode.
                Defaults to 'a'.
            stream: Use the specified stream to initialize the StreamHandler.
            level: Set the root logger level to the specified level.
        """

        cls.disable_logging()   # clear previously set logging info

        if filename is None:
            logging.basicConfig(stream=stream, level=level)
        else:
            logging.basicConfig(filename=filename, filemode=filemode,
                                level=level)
