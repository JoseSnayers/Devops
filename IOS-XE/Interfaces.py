import requests
import json
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

device = {
"Host" : "devnetsandboxiosxe.cisco.com",
"Port" : 443,
"Username" : "admin",
"Password" : " C1sco12345"
}
url = f"https://{device['Host']}/data/ietf-interfaces:interface"

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

response = requests.get(url, headers=headers, auth=HTTPBasicAuth(device['Username'],device['Password']), verify=False)

if response.status_code == 200:
    print("Request was successful!")
else:
    print(response)
