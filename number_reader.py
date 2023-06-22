"""
And here we load the json data back into the program.
"""

from fileinput import filename
import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)