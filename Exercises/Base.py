"""
    Hi, I'm Roger and this is my first python exercises file.
    I'm starting this at 09/09/2025, 22:08 UTC-3, to practice for "Programming language paradigms in Python" class.
    All codes here are my beginner codes, so I can keep tracking what I've learned and centralize all my notes.
    I'll keep adding new codes in this file until I feel comfortable to take a next step in my studies.
"""

#region GLOBAL VARIABLES
user_name = "Roger"
user_age = 25
user_city = "Varginha-MG, Brazil"

number1 = 8
number2 = 9
number3 = 10
number4 = 11

counter = 0

input_1 = str
input_2 = str
input_3 = str

sequence = []

CONVENTIONAL_CONSTANT = "Please, don't change my value, I'm trying to be a CONSTANT_VARIABLE."
#endregion

# Print user data
print("------------------ USER ------------------")
print(f"Name: {user_name}.")
print(f"Age: {user_age} years old.")
print(f"City: {user_city}.")

# Calculate average, then print
print("\n------------ CALCULATE AVERAGE ------------")
average = (number1 + number2 + number3 + number4) / 4
print(f"The four numbers are: {number1}, {number2}, {number3}, {number4}.\nAverage number is: {average}.")

# Function to print the counter text
def print_counter():
    print(f"Counter: {counter}.")
    return

# Loop counter from 0 to 4
print("\n-------------- COUNTER O-4 --------------")
while counter < 5:
    print_counter()
    counter += 1

# Check if counter is on 5
print("\n--------- AM I A LOCAL VARIABLE? ---------")
if counter == 5:
    local_variable = "I'm a local variable"
    print(f"{local_variable}!\nIf I'm really a local variable, then {local_variable} and the counter is now on five.")
    print_counter()

# Constant convention reminder
print("\n---- SHOULD I CHANGE CONSTANT VALUES? ----")
print(CONVENTIONAL_CONSTANT)

# Type validator
print("\n------------- TYPE VALIDATOR -------------")
# Check if an object matches a specific type
def type_compare_validator(object_target, type_reference):
     if isinstance(object_target, type_reference):
        return True
     else:
        return False

# Check if an object type is iterable
def type_iterator_validator(object_target):
    try:
        iter(object_target)
        return True
    except TypeError:
        return False

# Check if an input type can be boolean
def bool_input_validator(object_target):
    if object_target == "True" or "true" or "False" or "false":
        try:
            bool(object_target)
            return True
        except ValueError:
            return False
    else:
        return False

# Check if an input type can be int by comparing its int division by 1 with itself
def int_input_validator(object_target):
    try:
        object_target = float(object_target)
        return True if ((object_target // 1) == object_target) else False
    except ValueError:
        return False

# Check if an input type can be floated
def float_input_validator(object_target):
    try:
        object_target = float(object_target)
        return True
    except ValueError:
        return False

# Get what type of input it can be using
def get_input_type(object_target):
    can_be_int = int_input_validator(object_target)
    can_be_float = float_input_validator(object_target)
    can_be_bool = bool_input_validator(object_target)
    if can_be_int and can_be_bool:
        return int(object_target)
    elif can_be_float and not can_be_int:
        return float(object_target)
    elif can_be_int and can_be_float and can_be_bool:
        return bool(object_target)
    else:
        return str(object_target)

input_1 = get_input_type(input("Enter any data to validate its type: "))
print(f"Input type: {type(input_1)}.")
input_2 = input("\nEnter another data to validate its type: ")
input_2 = get_input_type(input_2)
print(f"Input type: {type(input_2)}.")
input_3 = get_input_type(input("\nEnter another data to validate its type: "))
print(f"Input type: {type(input_3)}.")

# Input and iterable types interation
print("\n-------- INPUT & LIST & ENUMERATE --------")
input_1 = str(input("Enter the 1º text: "))
input_2 = str(input("Enter the 2º text: "))
input_3 = str(input("Enter the 3ª text: "))
sequence = [input_1, input_2, input_3]

# Function that automatically print every item in a list ordered, starting at 1
def print_enumerated(object_target):
    is_object_type_iterable = type_iterator_validator(object_target)
    if is_object_type_iterable:
        for index, item  in enumerate(object_target, start=1):
            print(f"{index}º: {item}")
        return
    else:
        print(f"1º: {object_target}")
        return

print(f"\nTexts entered:")
print_enumerated(sequence)

print("\n--- GET CHARACTERS POLYMORPHIC FUNCTION ---")
#region FUNCTION DESCRIPTION
#   Function that get a sequence of characters from an object and return it.
#   It receives four parameters, that are:
#      1. object_target -> A variable, can be a number, a string, a list, or any kind.
#      2. object_type -> The type of the object to be authenticated before goes to designated course.
#      3. starts_from_left -> Boolean variable that says if the counting starts from left or right.
#      4. number_of_character -> A int value of how many characters will get.
#endregion
def get_characters(object_target, object_type, starts_from_left, number_of_characters):

    # Validate object type and certify that number_of_characters is an int type
    is_object_type_validated = type_compare_validator(object_target, object_type)
    is_object_type_iterable = type_iterator_validator(object_target)
    try:
        number_of_characters = number_of_characters // 1
    except Exception as e:
        return print(f"UNKNOWN ERROR: {e}")

    # Get characters from iterable
    if is_object_type_validated and is_object_type_iterable:
        local_list = []
        for i, item in enumerate(object_target):
            local_list.append(item[:number_of_characters]) if starts_from_left else local_list.append(item[-number_of_characters:])
        return local_list

    # Get characters from other types
    if is_object_type_validated:
        return object_target[:number_of_characters] if starts_from_left else object_target[-number_of_characters:]

    # Print a warning message if object type isn't validated
    else:
        print(f"TYPE NOT VALIDATED: {object_target} isn't a {object_type}.")
        return None

print(f"\nFirst 3 characters")
print_enumerated(get_characters(sequence, list, True, 3))

print(f"\nLast 3 characters")
print_enumerated(get_characters(sequence, list, False, 3))