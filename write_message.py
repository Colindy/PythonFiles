"""
Here we are going to write to a file
"""
filename = 'programming.txt'

"""
So here we have some options, 'w' is write mode.  You can also do 'a' for apend mode or
'r' for read mode.  'r+' allows you to read and write to a file.

Be careful with 'w' as it will erase anything already in a file if the file already exists.
"""

with open(filename, 'w') as file_object: # This one will overwrite a file if it's already there or create it if it's not
    file_object.write("Anthony Richardson goes #4 to the Colts!\n")
    file_object.write("I can't wait till September when the season starts!\n")

with open(filename, 'a') as file_object:
    file_object.write("I wonder who else they'll pick in the draft!\n")
    file_object.write("Lucky me, I only have to wait a few more hours!!\n")
