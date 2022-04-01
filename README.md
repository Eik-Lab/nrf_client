# NRF Client for Python

## Getting started

To get started, install the library by running:
```bash
pip install git+https://github.com/Eik-Lab/nrf_client
```

## Usage

Currently, the library only supports fetching devices.
To do this, run the following code:
```python
from nrf_client import NrfAPI
TOKEN = "INSERT_TOKEN_HERE"
client = NrfAPI(TOKEN)
devices = client.get_devices()
```
This will give you the JSON object from the NRF API. 
Too for example get JSON from the request into a dict, run the following:
```python
json_body = devices.json()
data = json.loads(json_body)
```
To get the info of the devices, run the following code:
```python
data["items"]
```

## Contribution
Contributions to add support for more endpoints are welcome.
