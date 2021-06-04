import unittest
import requests
import json

class Test(unittest.TestCase):

    def test_post_data(self):
        api_url = "https://chercher.tech/sample/api/product/create"
        # Here we are providing new records incluidng id, as id is unique
        data = json.dumps({'id':4618, 'name':'New Data', 'description':'Welcome to Python'})
        resp = requests.post(api_url, data)
        print(resp)
        print(resp.status_code)

if __name__ == "__main__":
    unittest.main()

# Verify the result using below link
# https://chercher.tech/sample/api-ui