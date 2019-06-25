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

  1. Invoke ```git clone https://github.com/cohesity/app-sdk-python.git```
  2. ```cd app-sdk-python```
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
app_endpoint_ip = os.getenv('APPS_API_ENDPOINT_IP')
app_endpoint_port = os.getenv('APPS_API_ENDPOINT_PORT')
app_client = AppClient(app_auth_token, app_endpoint_ip, app_endpoint_port)

```

# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [Volume](#volume)
* [TokenManagement](#token_management)
* [Settings](#settings)
* [MountController](#mount_controller)

## <a name="volume"></a>![Class: ](https://apidocs.io/img/class.png ".Volume") Volume

### Get controller instance

An instance of the ``` Volume ``` class can be accessed from the API Client.

```python
 volume_controller = client.volume
```

### <a name="create_volume"></a>![Method: ](https://apidocs.io/img/method.png ".Volume.create_volume") create_volume

> Use this API to create a new kubernetes persistent volume backed up by cohesity view.

```python
def create_volume(self,
                      volume_name,
                      volume_spec)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| volumeName |  ``` Required ```  | Name of the volume unique within the app instance. |
| volumeSpec |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
volume_name = 'volumeName'
volume_spec = VolumeSpec()

result = volume_controller.create_volume(volume_name, volume_spec)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Unauthorized. |
| 409 | Volume already exists with different parameters. |
| 500 | Unexpected error. |
| 502 | Bad Gateway. |
| 504 | Gateway Timeout. |




### <a name="get_volume"></a>![Method: ](https://apidocs.io/img/method.png ".Volume.get_volume") get_volume

> Gets the status of persistent volume owned by this app.

```python
def get_volume(self,
                   volume_name)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| volumeName |  ``` Required ```  | Name of the volume unique within the app instance. |



#### Example Usage

```python
volume_name = 'volumeName'

result = volume_controller.get_volume(volume_name)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Unauthorized |
| 404 | Volume doesn't exist. |
| 500 | Unexpected error |
| 502 | Bad Gateway. |
| 504 | Gateway Timeout. |




### <a name="delete_volume"></a>![Method: ](https://apidocs.io/img/method.png ".Volume.delete_volume") delete_volume

> Delete a previously created persistent volume owned by this app.

```python
def delete_volume(self,
                      volume_name)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| volumeName |  ``` Required ```  | Name of the volume unique within the app instance. |



#### Example Usage

```python
volume_name = 'volumeName'

volume_controller.delete_volume(volume_name)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Invalid parameters. |
| 401 | Unauthorized. |
| 404 | Volume doesn't exist. |
| 500 | Unexpected error. |
| 502 | Bad Gateway. |
| 504 | Gateway Timeout. |




[Back to List of Controllers](#list_of_controllers)

## <a name="token_management"></a>![Class: ](https://apidocs.io/img/class.png ".TokenManagement") TokenManagement

### Get controller instance

An instance of the ``` TokenManagement ``` class can be accessed from the API Client.

```python
 token_management_controller = client.token_management
```

### <a name="create_management_access_token"></a>![Method: ](https://apidocs.io/img/method.png ".TokenManagement.create_management_access_token") create_management_access_token

> Use this api to get a new management api token.

```python
def create_management_access_token(self)
```

#### Example Usage

```python

result = token_management_controller.create_management_access_token()

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Invalid token. |
| 500 | Unexpected error. |
| 502 | Bad Gateway. |
| 504 | Gateway Timeout. |




[Back to List of Controllers](#list_of_controllers)

## <a name="settings"></a>![Class: ](https://apidocs.io/img/class.png ".Settings") Settings

### Get controller instance

An instance of the ``` Settings ``` class can be accessed from the API Client.

```python
 settings_controller = client.settings
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
| 502 | Bad Gateway. |
| 504 | Gateway Timeout. |




[Back to List of Controllers](#list_of_controllers)

## <a name="mount_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MountController") MountController

### Get controller instance

An instance of the ``` MountController ``` class can be accessed from the API Client.

```python
 mount_controller = client.mount
```

### <a name="delete_unmount"></a>![Method: ](https://apidocs.io/img/method.png ".MountController.delete_unmount") delete_unmount

> Unmount previously mounted view/namespace.

```python
def delete_unmount(self,
                       dir_name)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| dirName |  ``` Required ```  | Name of the mount directory. |



#### Example Usage

```python
dir_name = 'dirName'

mount_controller.delete_unmount(dir_name)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Invalid parameters. |
| 401 | Invalid token. |
| 404 | Directory doesn't exist. |
| 500 | Unexpected error. |
| 502 | Bad Gateway. |
| 504 | Gateway Timeout. |




### <a name="create_mount"></a>![Method: ](https://apidocs.io/img/method.png ".MountController.create_mount") create_mount

> Allows you to mount a view/namespace.

```python
def create_mount(self,
                     mount_options)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| mountOptions |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
mount_options = MountOptions()

mount_controller.create_mount(mount_options)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Validation errors. |
| 401 | Invalid token. |
| 500 | Unexpected error. |
| 502 | Bad Gateway. |
| 504 | Gateway Timeout. |




[Back to List of Controllers](#list_of_controllers)

 
## Questions or Feedback :

We would love to hear from you. Please send your questions and feedback to: *developer@cohesity.com*
