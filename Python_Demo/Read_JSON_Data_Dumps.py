import json
# Python Dictionary
client = {
    "name": "Nora",
    "age": 56,
    "id": "45355",
    "eye_color": "green",
    "wears_glasses": False
}

# Get a JSON formatted string
# without Indentation
#client_JSON = json.dumps(client)
# with Indentation
client_JSON = json.dumps(client, indent=4,sort_keys=True)
print(client_JSON)