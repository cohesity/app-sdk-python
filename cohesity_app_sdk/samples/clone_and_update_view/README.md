## Usage: 
```
python clone_and_update_view.py --view_name=<name_of_view> --clone_name=<cloned_view_name>
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

## Example Clone view
``` 
json_req = {"cloneViewName": clone_name, "sourceViewName": view_name}
resp = self.view_client.create_clone_view(body=json_req)
```

## Response Output (Pretty Printed for readability)
```
Cloned view:
{u'access_sids': None,
 u'aliases': None,
 u'all_smb_mount_paths': None,
 u'basic_mount_path': u'/DefaultStorageDomain/clone-view/fs',
 u'case_insensitive_names_enabled': True,
 u'create_time_msecs': 1548801042647,
 u'data_lock_expiry_usecs': None,A
 u'description': u'',
 u'enable_filer_audit_logging': False,
 u'enable_mixed_mode_permissions': False,
 u'enable_nfs_view_discovery': None,
 u'enable_smb_access_based_enumeration': False,
 u'enable_smb_encryption': None,
 u'enable_smb_view_discovery': True,
 u'enforce_smb_encryption': None,
 u'file_extension_filter': {u'file_extensions_list': None,
                            u'is_enabled': False,
                            u'mode': u'kBlacklist',
                            u'py/object': u'cohesity_management_sdk.models.file_extension_filter.FileExtensionFilter'},
 u'file_lock_config': None,
 u'logical_quota': None,
 u'logical_usage_bytes': 3693171957,
 u'name': u'clone-view',
 u'nfs_mount_path': u'server.eng.cohesity.com:/clone-view',
 u'protocol_access': u'kAll',
 u'py/object': u'cohesity_management_sdk.models.view.View',
 u'qos': {u'principal_name': u'Backup Target Low',
          u'py/object': u'cohesity_management_sdk.models.qo_s.QoS'},
 u's_3_access_path': u'https://server.eng.cohesity.com:3000/clone-view',
 u'security_mode': u'kNativeMode',
 u'smb_mount_path': u'\\\\server.eng.cohesity.com\\clone-view',
 u'smb_permissions_info': {u'owner_sid': u'S-1-5-32-544',
                           u'permissions': [{u'access': u'kFullControl',
                                             u'mode': u'kFolderSubFoldersAndFiles',
                                             u'mtype': u'kAllow',
                                             u'py/object': u'cohesity_management_sdk.models.smb_permission.SmbPermission',
                                             u'sid': u'S-1-1-0',
                                             u'special_access_mask': None,
                                             u'special_type': None}],
                           u'py/object': u'cohesity_management_sdk.models.smb_permissions_info.SmbPermissionsInfo'},
 u'storage_policy_override': None,
 u'subnet_whitelist': None,
 u'tenant_id': None,
 u'view_box_id': 5,
 u'view_box_name': u'DefaultStorageDomain',
 u'view_id': 64367,
 u'view_protection': None}

```

## Example Update cloned view
``` 
req_json = {"description": description,
            "protocolAccess": self.PROTOCOL[protocol_access]}
resp = self.view_client.update_view_by_name(body=req_json, name=view_name)
```

## Example Output
```
{u'access_sids': None,
 u'aliases': None,
 u'all_smb_mount_paths': None,
 u'basic_mount_path': u'/DefaultStorageDomain/clone-view/fs',
 u'case_insensitive_names_enabled': True,
 u'create_time_msecs': 1548801042647,
 u'data_lock_expiry_usecs': None,
 u'description': u'View to restrict access to s3 only.',
 u'enable_filer_audit_logging': False,
 u'enable_mixed_mode_permissions': False,
 u'enable_nfs_view_discovery': False,
 u'enable_smb_access_based_enumeration': False,
 u'enable_smb_encryption': None,
 u'enable_smb_view_discovery': False,
 u'enforce_smb_encryption': None,
 u'file_extension_filter': {u'file_extensions_list': None,
                            u'is_enabled': False,
                            u'mode': u'kBlacklist',
                            u'py/object': u'cohesity_management_sdk.models.file_extension_filter.FileExtensionFilter'},
 u'file_lock_config': None,
 u'logical_quota': None,
 u'logical_usage_bytes': 3693171957,
 u'name': u'2nwTG_cloned_view_ashish-view1',
 u'nfs_mount_path': u'server.eng.cohesity.com:/clone-view',
 u'protocol_access': u'kNFSOnly',
 u'py/object': u'cohesity_management_sdk.models.view.View',
 u'qos': {u'principal_name': u'Backup Target Low',
          u'py/object': u'cohesity_management_sdk.models.qo_s.QoS'},
 u's_3_access_path': None,
 u'security_mode': u'kNativeMode',
 u'smb_mount_path': None,
 u'smb_permissions_info': {u'owner_sid': u'S-1-5-32-544',
                           u'permissions': [{u'access': u'kFullControl',
                                             u'mode': u'kFolderSubFoldersAndFiles',
                                             u'mtype': u'kAllow',
                                             u'py/object': u'cohesity_management_sdk.models.smb_permission.SmbPermission',
                                             u'sid': u'S-1-1-0',
                                             u'special_access_mask': None,
                                             u'special_type': None}],
                           u'py/object': u'cohesity_management_sdk.models.smb_permissions_info.SmbPermissionsInfo'},
 u'storage_policy_override': None,
 u'subnet_whitelist': None,
 u'tenant_id': None,
 u'view_box_id': 5,
 u'view_box_name': u'DefaultStorageDomain',
 u'view_id': 64367,
 u'view_protection': None}

```
