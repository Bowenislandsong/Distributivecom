#!/usr/bin/env bash
text="MEDUSA.PYS CLIENT STARTING UP"
echo $text
export FLASK_APP=client_v2.py
chromium 'http://127.0.0.1:5000'
flask run
