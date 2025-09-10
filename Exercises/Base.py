"""
    Hi, I'm Roger and this is my first python exercises file.
    I'm starting this at 09/09/2025, 22:08 UTC-3, to practice for "Programming language paradigms in Python" class.
    All codes here are my beginner codes, so I can keep tracking what I've learned and centralize all my notes.
    I'll keep adding new codes in this file until I feel comfortable to take a next step in my studies.
"""
#region Variables
number1 = 8
number2 = 9
number3 = 10
number4 = 11

user_name = "Roger"
user_age = 25
user_city = "Varginha"

counter = 0
#endregion

# Calculate average, then print
average = (number1 + number2 + number3 + number4) / 4
print("The average number is: ", average)

# Print user data
print("Name:", user_name)
print("Age:", user_age, "years old")
print("City:", user_city)

# Loop counter
while counter < 5:
    print("Counter:", counter)
    counter += 1