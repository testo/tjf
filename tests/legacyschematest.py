import unittest
import requests
from jsonschema import validate
import json
import os
import pytest

#Before execution, a Flask server needs to be started
url = 'http://localhost:5000'

def test_matchSchema():
    response = requests.get(url=url + '/deviceInfo')
    assert response.status_code == 200
    with open(os.path.dirname(__file__) + '/../schema/v2.0.0/deviceInfo-schema-legacy.json') as json_file:
        schema = json.load(json_file)
        instance = response.json()
        try:
            validate(instance=instance, schema=schema)
        except:
            pytest.fail('Validation failed!')

def test_postFail():
    response = requests.post(url=url + '/deviceInfo')
    assert response.status_code != 200