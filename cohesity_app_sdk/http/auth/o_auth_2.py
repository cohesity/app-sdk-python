# -*- coding: utf-8 -*-

from cohesity_app_sdk.configuration import Configuration


class OAuth2:

    @classmethod
    def apply(cls, http_request):
        """ Add OAuth2 authentication to the request.

        Args:
            http_request (HttpRequest): The HttpRequest object to which
                authentication header will be added.

        """
        token = Configuration.o_auth_access_token
        http_request.headers['Authorization'] = "Bearer {}".format(token)
