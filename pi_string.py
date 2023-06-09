"""
Working with files here.
"""
filename = 'pi_digits.txt'
filename2 = 'pi_million_digits.txt'

with open(filename2) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

birthday = input("Enter your birthday, in form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi.")
else:
    print("Your birthday does not appear in the first million digits of pi. :(")
