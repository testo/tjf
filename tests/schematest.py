import unittest
import requests
from jsonschema import validate
import json
import os
import pytest

#Before execution, a Flask server needs to be started
url = 'http://localhost:5000'

def request_helper(path, schemafile):
    response = requests.get(url=url + path)
    assert response.status_code == 200
    assert 'Access-Control-Allow-Origin' in response.headers
    with open(schemafile) as json_file:
        schema = json.load(json_file)
        instance = response.json()
        try:
            validate(instance=instance, schema=schema)
        except:
            pytest.fail('Validation failed!')

def test_device_info_legacy_match_schema():
    request_helper('/deviceInfo', os.path.dirname(__file__) + '/../schema/v2.0.0/deviceInfo-schema-legacy.json')

def test_device_info_post_fail():
    response = requests.post(url=url + '/deviceInfo')
    assert response.status_code != 200

def test_customer_match_schema():
    request_helper('/customer', os.path.dirname(__file__) + '/../schema/v2.0.0/customer-schema-v2.0.0.json')

def test_customer_post_fail():
    response = requests.post(url=url + '/customer')
    assert response.status_code != 200

def test_measuringpoint_match_schema():
    request_helper('/measuringPoints', os.path.dirname(__file__) + '/../schema/v2.0.0/measuringpoint-schema-v2.0.0.json')

def test_measuringpoint_post_fail():
    response = requests.post(url=url + '/measuringPoints')
    assert response.status_code != 200