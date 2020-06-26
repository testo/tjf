from flask import Flask
from flask_cors import CORS
import requests
import json
import os

app = Flask(__name__)
CORS(app)

@app.route('/deviceInfo')
def get_deviceInfo():
    with open(os.path.dirname(__file__) + '/../examples/t300/deviceInfo.json') as json_file:
        data = json.load(json_file)
    
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/customer')
def get_customer():
    with open(os.path.dirname(__file__) + '/../examples/customer-v2.0.0.json') as json_file:
        data = json.load(json_file)

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

    return response

@app.route('/measuringPoints')
def get_measuringPoints():
    with open(os.path.dirname(__file__) + '/../examples/measuringPoints-v2.0.0.json') as json_file:
        data = json.load(json_file)

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

    return response