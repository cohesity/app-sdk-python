## Usage: 
```
python on_demand_job_run.py --job_name <name_of_protection_job>
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
req_body = ProtectionRunParameters()
req_body.run_type = RunType2Enum.KREGULAR
self.jobs_controller.create_run_protection_job(id=job_id, body=req_body)

# Get the status of this Job run.
jresp = cohesity_client.protection_runs.get_protection_runs(job_id=job_id, num_runs=1)[0]
```

## Example Output
```
01-01-2019 15:06:44	    VM Backup
01-01-2019 16:31:52	    Oracle 
01-01-2019 18:54:08	    NAS Backup
```

