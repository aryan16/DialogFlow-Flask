import json
with open("self_contact.json", "r") as jsonFile:
    data = json.load(jsonFile)

for info in data:
        if info['firstName'] == 'self':
            info['lock'] = 1

with open("self_contact.json", "w") as jsonFile:
    json.dump(data, jsonFile)