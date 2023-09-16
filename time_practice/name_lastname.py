
def name_lastname():
    print("This is the Administrator Office")
    name = input("Please insert your name: ")
    lastname = ""
    lastname= input("Please type your lastname: ")
    if len(lastname) == 0:
        response = input("Would you like to submit without entering your last name?").strip().lower()
        if response[0] == 'y':
            print("The form was submitted")
        else:
            print("Goodbye")

print(name_lastname())