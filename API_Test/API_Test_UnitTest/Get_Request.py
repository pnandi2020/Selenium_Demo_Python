import unittest
import requests


class Test(unittest.TestCase):

    def test_get_usa_details(self):
        r = requests.get("https://restcountries.eu/rest/v2/name/USA")
        print(r.json())
        print(r.status_code)
        self.assertEqual(200, r.status_code)


if __name__ == "__main__":
    unittest.main()

# Verify the result using below link
# https://chercher.tech/sample/api-ui