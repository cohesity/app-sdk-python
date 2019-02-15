import os
from cohesity_app_sdk.app_client import AppClient
from cohesity_management_sdk.cohesity_client import CohesityClient


# Initialize the App.
app_auth_token = os.getenv('APP_AUTHENTICATION_TOKEN')
app_cli = AppClient(app_auth_token)
app_cli.config.disable_logging()
app_cli.config.app_endpoint_ip = os.getenv('APPS_API_ENDPOINT_IP')
app_cli.config.app_endpoint_port = os.getenv('APPS_API_ENDPOINT_PORT')

# Get the settings information.
settings = app_cli.settings
print settings.get_app_settings()

# Get the management access token.
token = app_cli.token_management
mgmt_auth_token = token.create_management_access_token()

# Initialize the Cohesity Client.
cohesity_client = CohesityClient(auth_token=mgmt_auth_token)
cluster_ip = os.getenv('HOST_IP')
cohesity_client.config.cluster_vip = cluster_ip
cohesity_client.config.skip_ssl_verification = True

# Print Cluster info.
print(cohesity_client.cluster.get_basic_cluster_info())
