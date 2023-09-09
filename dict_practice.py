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



