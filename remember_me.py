import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'uname1.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'uname1.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet user by name after verifying the username is correct."""
    username = get_stored_username()
    if username:
        user = input(f"Are you {username}? Yes or No? ")
        if user.lower() == "no":
            username = get_new_username()
            print(f"We'll remember you, {username}!")
            return
        if user.lower() == "yes":
            print(f"Welcome back, {username}!")
            return
        else:
            print("Need either 'Yes' or 'No' here.")
            greet_user()
    else:
        username = get_new_username()
        print(f"We'll remember you, {username}!")

greet_user()

"""
Had some fun with this one.  Took a sec to get the check right but was able to do it
finally.  Tested with removing the file, entering 'yes', 'no', and some random keyboard
smashes.  Was finally able make sure all the output was correct.  Fun stuff!
"""