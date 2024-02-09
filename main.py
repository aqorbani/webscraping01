import json

data = {
    "name": "Amir Hossein",
    "age": "26",
    "married": False,
    "children": None
}

# data_to_json = json.dumps(data)
#
# print(data_to_json)

with open("file.json", "w") as file:
    json.dump(data, file, indent=4)
