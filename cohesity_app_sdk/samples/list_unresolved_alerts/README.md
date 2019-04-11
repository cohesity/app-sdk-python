## Usage: 
```
python list_unresolved_alerts.py --max_alerts 10
```

## Connect to the Cohesity Cluster
Following steps are required to setup connection with the Cohesity Cluster

### Authentication
In order to setup authentication and initialization of the API client, you need the following information.

```python
# Configuration parameters and credentials

import os
from cohesity_app_sdk.app_client import AppClient
app_auth_token = os.getenv('APP_AUTHENTICATION_TOKEN')
app_endpoint_ip = os.getenv('APPS_API_ENDPOINT_IP')
app_endpoint_port = os.getenv('APPS_API_ENDPOINT_PORT')
app_client = AppClient(app_auth_token, app_endpoint_ip, app_endpoint_port)

# Get the management access token.
token = app_cli.token_management
mgmt_auth_token = token.create_management_access_token()

# Initialize the Cohesity Client.
cluster_ip = os.getenv('HOST_IP')
cohesity_client = CohesityClient(cluster_vip=cluster_ip, auth_token=mgmt_auth_token)
```


## Example
``` 
alerts= cohesity_client.alerts
alerts_list = alerts.get_alerts(max_alerts=max_alerts, alert_state_list=[AlertStateListEnum.KOPEN])
```


## Example Output
```
01-01-2019 15:27:25              CLUSTER              INFO
01-01-2019 15:39:16             NODE_HEALTH        WARNING

```
