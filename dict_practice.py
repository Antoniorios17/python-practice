import json

# sample dictionary

data = {"president": {
            "name": "Barack Obama",
            "number": 45

        }
}

json_string = json.dumps(data)
print(json_string)

json_formatted_string = json.dumps(data, indent = 4)
print(json_formatted_string)

####################################################
print("*********BREAK*********")

# talking dictionary and creating a json file
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent = 4)


# deserializtion, Converting JSON to dictionary

