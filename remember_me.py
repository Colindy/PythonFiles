import json

username = input("What is your name? ")

filename = 'uname.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you, {username}!")