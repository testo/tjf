import unittest
import requests
from jsonschema import validate
import json
import os

class TestRequests(unittest.TestCase):
    #Before execution, a Flask server needs to be started
    url = 'http://localhost:5000'

    def test_matchSchema(self):
        response = requests.get(url=self.url + '/deviceInfo')
        self.assertEquals(200, response.status_code)
        with open(os.path.dirname(__file__) + '/../schema/v2.0.0/deviceInfo-schema-legacy.json') as json_file:
            schema = json.load(json_file)
            instance = response.json()
            try:
                validate(instance=instance, schema=schema)
            except:
                self.fail("Validation failed!")

if __name__ == '__main__':
    unittest.main()