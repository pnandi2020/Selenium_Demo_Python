import json
import urllib.request

# download raw json object
url = "https://api.gdax.com/products/BTC-EUR/ticker"
data = urllib.request.urlopen(url).read().decode()

# parse json object
obj = json.loads(data)

# output some object attributes
print('$ ' + obj['price'])
print('$ ' + obj['volume'])