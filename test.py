"""
Testing how append works, whether or not I can use that to create a file
or if I have to use 'w' to create and then 'a' to append.
"""

filename = 'test.txt'

with open('test.txt', 'a') as file_object:
    file_object.write("If this works, you can use 'a' to\n")
    file_object.write("create a file as well as append.")

"""
And it worked!!  So, I, at this point, think it would just be habit to always
use 'a' so you're never worried about overwritting what you already have unless
there is a specific reason to overwrite it.
"""
