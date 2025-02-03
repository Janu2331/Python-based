# Ask for the user's name
name = input("Enter your name: ")

# Ask for the user's age
age = int(input("Enter your age: "))

# Calculate the birth year
from datetime import datetime
current_year = datetime.now().year
birth_year = current_year - age

# Print a personalized greeting
print(f"\nHello, {name}! Welcome to Python.")
print(f"You were born in {birth_year}.")

# Provide a message based on age
if age < 18:
    print("You're young and have a bright future ahead!")
elif 18 <= age < 50:
    print("You're in the prime of your life. Keep learning and growing!")
else:
    print("Age is just a number. Keep exploring new things!")
