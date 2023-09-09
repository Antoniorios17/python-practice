import json
json_string ="""
{
  "check": "Healthy",
  "Checks": [
    {
      "Name": "Connections",
      "check": "Healthy"
    },
    {
      "Name": "ConnectionRead",
      "check": "unHealthy"
    },
    {
      "Name": "redis",
      "check": "Healthy"
    },
    {
      "Name": "ProcessCheck",
      "check": "Healthy"
    },
    {
      "Name": "UserProfile",
      "check": "unHealthy"
    },
    {
      "Name": "features",
      "check": "unHealthy",
      "Description": "sample sample sample"
    },
    {
      "Name": "shutdown",
      "check": "Healthy"
    },
    {
      "Name": "lifespan",
      "check": "unHealthy"
    }
  ]
}

"""

# make a function that wil output the number of healthy and unhealthy checks
# make a fucntion that will output the names of unhealthy checks
data = json.loads(json_string)
# print(type(data))

# print(data["Checks"])
unhealthy=0
healthy= 0
for check in data["Checks"]:
    if check["check"] == "Healthy":
        healthy += 1
    elif check["check"] == "unHealthy":
        unhealthy +=1
print("healthy =", healthy, "unhealthy=",unhealthy)

for check in data["Checks"]:
    if check["check"] == "unHealthy":
        print(check["Name"], "is unhealthy")

