import unittest
import requests
import json

class Test(unittest.TestCase):

    def test_delete_using_id(self):
        api_url = "https://chercher.tech/sample/api/product/delete?id=4607"
        resp = requests.delete(api_url)
        print(resp)
        self.assertEqual(200, resp.status_code)
if __name__ == "__main__":
    unittest.main()

    # Verify the result using below link
    # https://chercher.tech/sample/api-ui