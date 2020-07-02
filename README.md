# XFExchangeMISPsync
This script has been created to sync events and data from XForce Exchange (https://exchange.xforce.ibmcloud.com/)
and MISP (https://www.misp-project.org/). There are maybe simpler and better ways to do it, but this is at least
(Yet Another...) way to do it.

![Basic Idea](https://raw.githubusercontent.com/johestephan/XFExchangeMISPsync/master/doc/overview.png)

### config.ini
The configuration is done via a config file which will be parsed. In order to make this solution work you need to
know your API keys (apikey and password on XForce Exchange / authkey on MISP) as well as the involved URLs

```
[XFORCE]
endpoint = https://api.xforce.ibmcloud.com/
type = public
apikey = CHANGEME
apipassword = CHANGEME

[MISP]
endpoint = CHANGEME
authkey = CHANGEME
```

NOTE: In order to fetch private or shared collection you can adjust the "type" endpoint to shared or private

### script

The script will fetch all collections and push them to MISP. THIS WILL LEAD TO DUPLICATES until solved later.

Please install the required modules and run the script
```
cd syncscript
pip3 install -r requirements.txt --user

python3 sync.py
```
