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


    def __init__(self,
                 o_auth_access_token=None):
        if o_auth_access_token != None:
            Configuration.o_auth_access_token = o_auth_access_token


