# Copyright 2019 Cohesity Inc.
#
# Python example to list recent user_configurable unresolved alert unresolved Alerts.
#
# Usage: python list_unresolved_alerts.py --max_alerts 10

import os
import argparse
import datetime

from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.models.alert_state_list_enum import AlertStateListEnum
from cohesity_app_sdk.app_client import AppClient

MAX_ALERTS = 100

class Alerts(object):
    """
    Class to display Alerts.
    """
    def display_alerts(self, cohesity_client, max_alerts):
        """
        Method to display the list of Unresolved Alerts
        :param cohesity_client(object): Cohesity client object.
        :return:
        """
        alerts = cohesity_client.alerts
        alerts_list = alerts.get_alerts(max_alerts=max_alerts,
                                        alert_state_list=[AlertStateListEnum.KOPEN])
        for alert in alerts_list:
            print ('{0:<10}\t\t{1:>8}\t{2:>10}'.format(self.epoch_to_date(alert.first_timestamp_usecs),
                                                       alert.alert_category,
                                                       alert.severity))

    @staticmethod
    def epoch_to_date(epoch):
        """
        Method to convert epoch time in usec to date format
        :param epoch(int): Epoch time of the job run.
        :return: date(str): Date format of the job run.
        """
        date_string = datetime.datetime.fromtimestamp(epoch/10**6).strftime('%m-%d-%Y %H:%M:%S')
        return date_string

def get_mgnt_token():
    """
    To get the management access token from athena to authenticate
    :return: mgmt_auth_token
    """
    # Get the Environment variables from App Container.
    app_auth_token = os.getenv('APP_AUTHENTICATION_TOKEN')
    app_endpoint_ip = os.getenv('APPS_API_ENDPOINT_IP')
    app_endpoint_port = os.getenv('APPS_API_ENDPOINT_PORT')


    # Initialize the client.
    app_cli = AppClient(app_auth_token, app_endpoint_ip, app_endpoint_port)
    app_cli.config.disable_logging()


    # Get the settings information.
    settings = app_cli.settings
    print(settings.get_app_settings())


    # Get the management access token.
    token = app_cli.token_management
    mgmt_auth_token = token.create_management_access_token()
    return mgmt_auth_token

def main(args):

    # Login to the cluster
    host_ip = os.getenv('HOST_IP')
    mgmt_auth_token = get_mgnt_token()
    cohesity_client = CohesityClient(cluster_vip=host_ip,
                                         auth_token=mgmt_auth_token)

    alerts = Alerts()
    alerts.display_alerts(cohesity_client, args.max_alerts)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Arguments needed to run this python process.")
    parser.add_argument("--max_alerts", help="Number of Alerts.", default=MAX_ALERTS)
    args = parser.parse_args()
    main(args)
