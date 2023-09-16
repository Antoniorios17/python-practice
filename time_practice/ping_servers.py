import os

print("*** Welcome to the server checker ***\n")
servers = {"1": "3.81.114.140",
           "2": "3.81.215.202",
           "3": "3.81.215.202"}

for key , value in servers.items():
    print(key, value)
user_input = input("\nPlease select the server you want to check: \n")
ip = servers[user_input]

response = os.system("ping -c1 " + ip)

if response == 0:
  print(f"{servers[user_input]} is up and running!")
else:
  print(f"{servers[user_input]} is not running")


