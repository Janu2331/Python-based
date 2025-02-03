# Function to print student names and roll numbers
def print_students(student_names, roll_numbers):
    for name, roll in zip(student_names, roll_numbers):
        print(f"Student Name: {name}, Roll Number: {roll}")

# Creating lists for student names and roll numbers
student_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
roll_numbers = [1, 2, 3, 4, 5]

# Calling the function to print the details
print_students(student_names, roll_numbers)