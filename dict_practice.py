import json

# sample dictionary

data = {"president": {
            "name": "Barack Obama",
            "number": 45

        }
}

json_string = json.dumps(data)
# print(json_string)

json_formatted_string = json.dumps(data, indent = 4)
# print(json_formatted_string)

####################################################
# print("*********BREAK*********")

# talking dictionary and creating a json file
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent = 4)


# deserializtion, Converting JSON to dictionary

with open("data_file.json", "r") as read_file:
    dataV2 = json.load(read_file)



#
# print("**************BREAK**********")

example = {
  "Teams":[
    {"Giants":[{"wins":4}, {"losses":1}]},
    {"Patriots":[{"wins":2}, {"losses":3}]},
    {"Chiefs":[{"wins":4}, {"losses":1}]}
  ]
}


# print(example["Teams"])
# print(type(example["Teams"]))
# print(example["Teams"][0])
# print(example["Teams"][1]["Patriots"])

print(example["Teams"][0]["Giants"][0]["wins"])