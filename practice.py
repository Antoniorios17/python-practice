# print("Hello World")


# someName = input("what is your name: ")

# def this_means_ten():
    # print(10)

# this_means_ten()

def this_means_ten_v2():
    return 10

def average_test_scores(some_list):
    average = 0.0
    for i in range(0, len(some_list)):
        average = average + some_list[i]

    average = average / len(some_list)

    print(f'{average:.2f}')


scores = [100.0, 98.5, 95.7, 85.8, 95.6, 86.3]
# average_test_scores(scores)

def same_first_last(some_list):
    if some_list[0].lower() == some_list[-1].lower():
        print("yes, first and last are the same")
    else:
        print("first and last are not the same")

# Practice

# make a function called remove_vowels, its input will always be a string
# your function should return the string give but without any vowels inside of it

# string = input("insert string: ")
def remove_vowels():
    input_string = input("insert string: ")
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    result = ""
    for letter in input_string:
        if letter not in vowels:
            result = result + letter
    return result

print(remove_vowels())



