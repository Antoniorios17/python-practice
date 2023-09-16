
listed_dict = [{"webserver" : ["1.255.255.254", "2.255.255.254", "3.255.255.254", "4.255.255.254"]},
{"database_server" : ["6.255.255.254", "7.255.255.254", "8.255.255.254", "10.255.255.254"]},
{"file_server": ["13.255.255.254", "16.255.255.254", "17.255.255.253", "20.255.255.254"]}]

room1 = {"room1":[listed_dict[0]["webserver"][0],listed_dict[0]["webserver"][1]]}
room2 = {"room2":[listed_dict[0]["webserver"][2],listed_dict[0]["webserver"][3]]}
room3 = {"room3":[listed_dict[1]["database_server"][0],listed_dict[1]["database_server"][1]]}
room4 = {"room4":[listed_dict[1]["database_server"][2],listed_dict[1]["database_server"][3]]}
room5 = {"room5":[listed_dict[2]["file_server"][0],listed_dict[2]["file_server"][1]]}
room6 = {"room6":[listed_dict[2]["file_server"][2],listed_dict[2]["file_server"][3]]}

rooms = [room1, room2, room3, room4, room5, room6]
print(rooms)
