filename = 'test.txt'
filename2 = 'random.txt'

try:
    with open(filename, encoding='utf-8') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print(f"Sorry, {filename} does not appear to exist.")
else:
    print(contents.rstrip())

try:
    with open(filename2, encoding='utf-8') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print(f"Sorry, {filename2} does not exist.")
else:
    for line in file_object:
        print(line.rstrip())
