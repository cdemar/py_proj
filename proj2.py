import random
import string


# Function to shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return "".join(tempList)


# Ask user to input pw length they want
while True:
    user_input = input("How long do you want your password? ")

    try:
        pw_length = int(user_input)

        if pw_length < 8:
            print("Your number should be more than 8 characters for good security.")
        else:
            break

    except ValueError:
        print("Please, Enter numbers only.")

# To know what kind of characters to put in the password
character_list = ""
uppercase_list = string.ascii_uppercase
lowercase_list = string.ascii_lowercase
digits_list = string.digits
punctuation_list = ["!", "#", "$", "%", "&", "*", "?", "@"]

print(
    """
Chose character set for password from these:
1. Uppercase Letter (A,B,C)
2. Lowercase Letter (a,b,c)
3. Number (1,2,3)
4. Spechal Characters (!,@,#,$,%,&,*)
5. Exit"""
)

selected_sets = []

while True:
    choice = int(input("Pick a Number: "))

    if choice == 1:
        # Adds uppercase letters to list
        character_list += uppercase_list
        selected_sets.append(uppercase_list)
    elif choice == 2:
        # Adds lowercase letters to list
        character_list += lowercase_list
        selected_sets.append(lowercase_list)

    elif choice == 3:
        # adds numbers to the list
        character_list += digits_list
        selected_sets.append(digits_list)

    elif choice == 4:
        # adds special characters to the list
        character_list += "".join(punctuation_list)
        selected_sets.append(punctuation_list)
    elif choice == 5:
        if character_list == "":
            print("You must choose at least one character set.")
        else:
            break
    else:
        print("Please pick a valid option.")

# Ensure password contains at least 2 of each selected type
password = []
for selected_set in selected_sets:
    for _ in range(2):
        password.append(random.choice(selected_set))

# Fill the rest of the password length with random choices from the combined list
while len(password) < pw_length:
    password.append(random.choice(character_list))

# Shuffle the final password
password = shuffle(password)

# Output the generated password
print("The random password is: " + password)
