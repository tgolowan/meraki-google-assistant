# A very simple Flask Hello World app for you to get started with...
import requests
import json
from flask import Flask
# Application input
api_key = ''
ssids = ''
net_id = ''
url_guest_ssid = f'https://api.meraki.com/api/v0/networks/{net_id}/ssids/{ssids}'
app = Flask(__name__)
# Parse a webhook and send API call to enable SSID
@app.route('/enable_ssid',methods=["POST"])
def enable_ssid():
    meraki_headers = {
        'x-cisco-meraki-api-key': api_key,
        'content-type': 'application/json'
        }
    payload = {
        "name": "Guest Wifi",
        "enabled": True,
        "splashPage": "None",
        "perClientBandwidthLimitUp": 0,
        "perClientBandwidthLimitDown": 0,
        "ssidAdminAccessible": False,
        "ipAssignmentMode": "NAT mode",
        "authMode": "open"
        }
    requests.put(url_guest_ssid, headers=meraki_headers, data=json.dumps(payload))
    return "True"
# Parse a webhook and send API call to disable SSID
@app.route('/disable_ssid',methods=["POST"])
def disable_ssid():
    meraki_headers = {
        'x-cisco-meraki-api-key': api_key,
        'content-type': 'application/json'
        }
    payload = {
        "name": "Guest Wifi",
        "enabled": False,
        "splashPage": "None",
        "perClientBandwidthLimitUp": 0,
        "perClientBandwidthLimitDown": 0,
        "ssidAdminAccessible": False,
        "ipAssignmentMode": "NAT mode",
        "authMode": "open"
        }
    requests.put(url_guest_ssid, headers=meraki_headers, data=json.dumps(payload))
    return "True"
