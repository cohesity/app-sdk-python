# -*- coding: utf-8 -*-

from cohesity_app_sdk.decorators import lazy_property
from cohesity_app_sdk.configuration import Configuration
from cohesity_app_sdk.controllers.mount_controller import MountController
from cohesity_app_sdk.controllers.settings import Settings
from cohesity_app_sdk.controllers.token_management import TokenManagement


class AppClient(object):

    config = Configuration

    @lazy_property
    def mount(self):
        return MountController()

    @lazy_property
    def settings(self):
        return Settings()

    @lazy_property
    def token_management(self):
        return TokenManagement()

    #CohesityPatch
    def __init__(self, app_auth_token=None, app_endpoint_ip=None,
                 app_endpoint_port=None):
        if app_auth_token != None and app_auth_token !=None and \
                app_endpoint_port != None:
            Configuration.app_auth_token = app_auth_token
            Configuration.app_endpoint_ip = app_endpoint_ip
            Configuration.app_endpoint_port = app_endpoint_port
        else:
            raise Exception("Specify all the above parameters: "
                            "app_auth_token, app_endpoint_ip, "
                            "app_endpoint_port")


