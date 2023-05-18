prompt1 = "We're going to add some numbers.\nEnter 'q' to quit."
prompt2 = "Give me the first number: "
prompt3 = "Give me the second number: "

print(prompt1)

while True:

    x = input(prompt2)
    if x == 'q':
        break
    y = input(prompt3)
    if y == 'q':
        break

    try:
        x = int(x)
        y = int(y)
        print(x + y)
    except ValueError:
        print("I'm sorry, we need numbers to do addition.")
