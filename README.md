Cohesity App SDK
=================

# Overview

The *Cohesity App SDK*  provides an easy-to-use language binding to 
harness the power of *Cohesity App APIs* in your python applications.These
 APIs are available for apps running on Cohesity Apps Infrastructure.


# Getting Started

The generated code uses Python packages named requests, jsonpickle and dateutil.
You can resolve these dependencies using pip ( https://pip.pypa.io/en/stable/ ).
This SDK uses the Requests library and will work for Python ```2 >=2.7.9``` and Python ```3 >=3.4```.

  1. Invoke ```git clone https://github.com/cohesity/python-client.git```
  2. ```cd cohesityAppSDK```
  2. Invoke ```pip install -r requirements.txt```
  3. Install cohesity_management_package: ```python setup.py install```. 
  This will install the package in PYTHONPATH.



## How to Use

The following section explains how to use the `cohesity_app_sdk`  package 
in a new project.

## Container Environment Parameters

The App Environment Container has the following parameters initialized by 
Athena.
```
HOST_IP
APPS_API_ENDPOINT_IP
POD_UID
APPS_API_ENDPOINT_PORT
APP_AUTHENTICATION_TOKEN
```
We use the above variables in various usecases to initialize and make call 
to Athena App server.

### Authentication
In order to setup authentication and initialization of the API client, you need the following information.

```python
# Configuration parameters and credentials

import os
from cohesity_app_sdk.app_client import AppClient
app_auth_token = os.getenv('APP_AUTHENTICATION_TOKEN')
o_auth_access_token = 'app_auth_token' # OAuth 2.0 Access Token
app_client = AppClient(o_auth_access_token)
app_client.config.app_endpoint_ip = os.getenv('APP_API_ENDPOINT_IP')
app_client.config.app_endpoint_ip = os.getenv('APPS_API_ENDPOINT_PORT')
```


# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [MountController](#mount_controller)
* [Settings](#settings)
* [TokenManagement](#token_management)

## <a name="mount_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MountController") MountController

### Get controller instance

An instance of the ``` MountController ``` class can be accessed from the API Client.

```python
 mount = app_client.mount
```

### <a name="create_mount"></a>![Method: ](https://apidocs.io/img/method.png ".MountController.create_mount") create_mount

> Allows you to mount a view/namespace.

```
def create_mount(self, mount_options)
```

#### Parameters

| Parameter |
|-----------|
| mountOptions | 



#### Example Usage

```python
mount_options = MountOptions()
mount.create_mount(mount_options)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Validation errors. |
| 401 | Invalid token. |
| 500 | Unexpected error. |




### <a name="delete_unmount"></a>![Method: ](https://apidocs.io/img/method.png ".MountController.delete_unmount") delete_unmount

> Unmount previously mounted view/namespace.

```python
def delete_unmount(self, dir_name)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| dirName |  ``` Required ```  | Name of the mount directory. |



#### Example Usage

```python
dir_name = 'dirName'
mount.delete_unmount(dir_name)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Invalid parameters. |
| 401 | Invalid token. |
| 404 | Directory doesn't exist. |
| 500 | Unexpected error. |




[Back to List of Controllers](#list_of_controllers)

## <a name="settings"></a>![Class: ](https://apidocs.io/img/class.png ".Settings") Settings

### Get controller instance

An instance of the ``` Settings ``` class can be accessed from the API Client.

```python
 settings_controller = app_client.settings
```

### <a name="get_app_settings"></a>![Method: ](https://apidocs.io/img/method.png ".Settings.get_app_settings") get_app_settings

> Returns app settings object.

```python
def get_app_settings(self)
```

#### Example Usage

```python

result = settings_controller.get_app_settings()

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Invalid token |
| 500 | Unexpected error |




[Back to List of Controllers](#list_of_controllers)

## <a name="token_management"></a>![Class: ](https://apidocs.io/img/class.png ".TokenManagement") TokenManagement

### Get controller instance

An instance of the ``` TokenManagement ``` class can be accessed from the API Client.

```python
 token_management = app_client.token_management
```

### <a name="create_management_access_token"></a>![Method: ](https://apidocs.io/img/method.png ".TokenManagement.create_management_access_token") create_management_access_token

> Use this api to get a new management api token.

```python
def create_management_access_token(self)
```

#### Example Usage

```python
# This example shows interaction of management token got from App SDK to 
# Cohesity Management SDK. 
from cohesity_management_sdk.cohesity_client import CohesityClient
token = token_management.create_management_access_token()
cohesity_client = CohesityClient(auth_token=token)
cluster_ip = os.getenv('HOST_IP')
cohesity_client.config.cluster_vip = cluster_ip
cohesity_client.cluster.get_basic_cluster_info() 
```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Invalid token. |
| 500 | Unexpected error. |


## Configure:

The generated code will pick up the default configurations from 
cohesity_app_sdk/configuration.py, hence, you 
can use configuration.py to set the attributes such as App Endpoint IP, App 
Endpoint Port etc before compilation.
 
 Note : These parameters can be easily overwritten in scripts. Please refer 
 to sample_app.py
 
## Questions or Feedback :

We would love to hear from you. Please send your questions and feedback to: *apps@cohesity.com*



