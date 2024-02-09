import json

data_json = """
{
    "name": "Amir Hossein",
    "age": 26,
    "married": false,
    "children": null
}
"""

# data_to_json = json.dumps(data)
#
# print(data_to_json)

# with open("file.json", "w") as file:
#     json.dump(data, file, indent=4)

data = json.loads(data_json)
print(data)
