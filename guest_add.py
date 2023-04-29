filename = 'guest.txt'
filename2 = 'language.txt'

prompt = "Please provide your name (enter 'q' to quit): "
prompt2 = "What's your favorite programing language (or 'q')? "

while True:
    
    guest = input(prompt)

    if guest == 'q':
        break
    else:
        print(f"Ahh, hello there {guest}!  I'll add you to the list.")
        with open('guest.txt', 'a') as file_object:
            file_object.write(f"{guest}\n")

    language = input(prompt2)

    if language == 'q':
        break
    else:
        print(f"Great! We will add {language} to the list of languages.")
        with open('language.txt', 'a') as file_object:
            file_object.write(f"{language}\n")

