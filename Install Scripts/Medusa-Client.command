#!/usr/bin/env bash
cd /Users/yangzhiyi/Desktop/Distributivecom/webUI_Networking/clientshare/
export FLASK_APP=/Users/yangzhiyi/Desktop/Distributivecom/webUI_Networking/clientshare/client_v2.py
/usr/bin/open -a "/Applications/Google Chrome.app" 'http://127.0.0.1:5000/'
flask run
