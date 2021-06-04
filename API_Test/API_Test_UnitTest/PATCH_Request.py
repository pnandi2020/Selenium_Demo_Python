import unittest
import requests
import json


class Test(unittest.TestCase):

    def test_student_post_request(self):
        api_url = "https://chercher.tech/sample/api/product/update"
        # Here we are providing new existing id to update the records
        data = json.dumps({'id':4623, 'name':'Data', 'description':'Welcome to Code', 'price': 5500})
        resp = requests.patch(api_url, data)
        print(resp)
        self.assertEqual(200, resp.status_code)

if __name__ == "__main__":
    unittest.main()

# Verify the result using below link
# https://chercher.tech/sample/api-ui