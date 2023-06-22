"""
Here I'm doing a simple json file creation.  I've changed the numbers in my program
in order to see if it overwrites or not.
"""
import json

numbers = [2, 5, 119, 146, 273, 316, 693]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

# 'a' would append but then the format is messed up as you end up with
# two [][] back to back.  Will stick with 'w' for this one