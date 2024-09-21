#Task 1: Imput Length Validator. Write a script that asks for and checks the length of the user's first name and last name.
#Both should be at least 2 characters long. If not, print an error message.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

if len(first_name) < 2:
    print("Error: First name must be at least 2 characters long.")
elif len(last_name) < 2:
    print("Error: Last name must be at least 2 characters long.")
else:
    print(f"Welcome, {first_name} {last_name}!")