import json

with open('order.json', 'r') as json_file:
    json_object = json.load(json_file)
print(json_object)
#print(json_object)
#The output is 2 because the value of the main key "orders" is a list with two elements.
print(len(json_object["orders"]))
#For example, to access the toppings of the first order, we would write:
print(json_object["orders"][0]["toppings"])
#We can use the dumps() method to get the pretty formatted JSON string.
print(json.dumps(json_object))

print(json.dumps(json_object, indent=1))