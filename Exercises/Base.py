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
    pass

# Loop counter
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
