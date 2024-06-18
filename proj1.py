import random
import string


# A function do shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return "".join(tempList)


# Main program starts here

# Uppercase Letters
uppercaseLetter1 = chr(random.randint(65, 90))
uppercaseLetter2 = chr(random.randint(65, 90))
# Lowercase Letters
lowercaseLetter1 = chr(random.randint(97, 122))
lowercaseLetter2 = chr(random.randint(97, 122))
# Digits
digit1 = chr(random.randint(48, 57))
digit2 = chr(random.randint(48, 57))
# Punctuation
punctuationSigns = ["!", "#", "$", "%", "&", "*", "?", "@"]
punctuationSign1 = random.choice(punctuationSigns)
punctuationSign2 = random.choice(punctuationSigns)


# Generate password using all the characters, in random order
password = (
    uppercaseLetter1
    + uppercaseLetter2
    + lowercaseLetter1
    + lowercaseLetter2
    + digit1
    + digit2
    + punctuationSign1
    + punctuationSign2
)
password = shuffle(password)

# Ouput
print(password)
