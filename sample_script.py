# Copyright 2019 Cohesity Inc.
#
# Python example to use Cohesity App Python SDK along with Cohesity
# Management SDK. This sample script get's app settings , gets management
# access token and passes it to Cohesity Management client to extract cluster
# name.
# Usage: python sample_script.py

import os
from cohesity_app_sdk.app_client import AppClient
from cohesity_management_sdk.cohesity_client import CohesityClient

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

# Initialize the Cohesity Client.
cluster_ip = os.getenv('HOST_IP')
cohesity_client = CohesityClient(cluster_vip=cluster_ip, auth_token=mgmt_auth_token)
cohesity_client.config.skip_ssl_verification = True


# Print Cluster name.
cluster_info = cohesity_client.cluster.get_basic_cluster_info()
print("Cluster Name : %s" % cluster_info.name)

