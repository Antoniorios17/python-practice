
# def remove_vowels(word):

#     new_list = list(word)

#     while("a" in new_list):
#         current_index = new_list.index("a")
#         new_list.pop(current_index)

#     while("e" in new_list):
#         current_index = new_list.index("e")
#         new_list.pop(current_index)

#     while("i" in new_list):
#         current_index = new_list.index("i")
#         new_list.pop(current_index)

#     while("o" in new_list):
#         current_index = new_list.index("o")
#         new_list.pop(current_index)

#     while("u" in new_list):
#         current_index = new_list.index("u")
#         new_list.pop(current_index)


#     new_string = ""

#     for i in range(len(new_list)):

#         new_string = new_string + new_list[i]
#     return new_string


def remove_char(some_char, some_list):
    new_list = some_list
    while(some_char in some_list):
        current_I = some_list.index(some_char)
        new_list.pop(current_I)
    return some_list

def remove_vowelsV2(word):

    new_list = list(word)

    new_list = remove_char("a", new_list)
    new_list = remove_char("e", new_list)
    new_list = remove_char("i", new_list)
    new_list = remove_char("o", new_list)
    new_list = remove_char("u", new_list)

    new_string = ""

    for i in range(len(new_list)):

        new_string = new_string + new_list[i]
    return new_string

print(remove_vowelsV2("aaarrrafvr"))