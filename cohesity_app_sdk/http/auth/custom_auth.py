# -*- coding: utf-8 -*-

from cohesity_app_sdk.configuration import Configuration


class CustomAuth:

    @classmethod
    def apply(cls, http_request):
        """ Add CustomAuth authentication to the request.

        Args:
            http_request (HttpRequest): The HttpRequest object to which
                authentication header will be added.

        """
        token = Configuration.app_auth_token
        http_request.headers['Authorization'] = "Bearer {}".format(token)
