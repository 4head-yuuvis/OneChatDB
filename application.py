# template taken from https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html

from flask import Flask, jsonify, request, render_template
import requests
import json
import os
import time
import sys

application = Flask(__name__)

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

headerDict['Ocp-Apim-Subscription-Key'] = '0ddbbcd86e634d45be0bc1cc4c20c850'
session = requests.Session()
response = session.get(str(baseUrl+'/dms/objects/453129a7-1497-47fd-8dc5-5c2d9ef49bcb/history'), headers=headerDict)

@application.route('/')
def hello_world():
    return 'Hello, World!'

@application.route('/yuuvis-api')
def yuuvis_api():
    return (response.text)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True

    port = int(os.environ.get("PORT", 5000))
    application.run(host="0.0.0.0", port=port)
