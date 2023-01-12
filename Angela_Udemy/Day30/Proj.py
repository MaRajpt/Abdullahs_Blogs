import json

new_dict = {"kuku": {
        "email": "Abdullah@email.com",
        "password": "123ad"}
}


with open("data.json", 'r') as data_file:
    data = json.load(data_file)
    data.update(new_dict)

with open("data.json", 'w') as data_file:
    json.dump(data, data_file, indent=4)

