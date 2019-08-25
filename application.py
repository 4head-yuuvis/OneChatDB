# template taken from https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html

from flask import Flask, jsonify, request, render_template
from google.cloud import translate
from flask_cors import CORS
import requests
import json
import os
import time
import sys

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/andrew/Downloads/onechat-1566682458777-50c2ac0e1c1b.json"


# project_id = 'onechat-1566682458777'
# text = 'Text you wish to translate'
# location = 'global'



application = Flask(__name__)
CORS(application)

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

# def add_cors_headers(response):
#     response.headers["Access-Control-Allow-Origin"] = "*"
#     response.headers["Access-Control-Allow-Credentials"] = "true"
#     response.headers["Access-Control-Allow-Headers"] = "application/x-www-form-urlencoded"
#     response.headers["Access-Control-Allow-Methods"] = "GET"
#     return response


# application.after_request(add_cors_headers)

@application.route('/translate')
def run_quickstart():
    # [START translate_quickstart]
    # Imports the Google Cloud client library
    message = request.args.get('message')
    tgt = request.args.get('tgt')

    # Instantiates a client
    translate_client = translate.Client()

    # The text to translate
    text = u'{}'.format(message)
    # The target language
    target = tgt

    # Translates some text into Russian
    translation = translate_client.translate(
        text,
        target_language=target)

    # with open('../chatApp/src/components/output.txt', 'w') as file:
    #     file.write(u'{}'.format(translation['translatedText']))
    return (u'{}'.format(translation['translatedText']))
    # print(u'Text: {}'.format(text))
    # print(u'Translation: {}'.format(translation['translatedText']))
    # [END translate_quickstart]

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True

    port = int(os.environ.get("PORT", 5000))
    application.run(host="0.0.0.0", port=port)
