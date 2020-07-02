# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import pymisp
from configparser import ConfigParser
import requests
from requests.auth import HTTPBasicAuth

config_object = ConfigParser()
config_object.read("config.ini")

XFE = config_object['XFORCE']
MISP = config_object['MISP']

# Getting Public collections
response = requests.get(XFE['endpoint']+"/casefiles/public", auth=HTTPBasicAuth(XFE['APIkey'], XFE['APIpassword']))
data = response.json()

# getting individual case file IDs
for report in data['casefiles']:
    response = requests.get(XFE['endpoint']+"/casefiles/%s" % report['caseFileID'], auth=HTTPBasicAuth(XFE['APIkey'], XFE['APIpassword']))
    collection = response.json()
    print(report)
