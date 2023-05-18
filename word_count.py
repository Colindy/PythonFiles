prompt = "Please list a filename.\nEnter 'q' to quit.\n> "

def count_words(filename):
    """Here running a simple word counter on a given file"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass #print(f"Sorry, {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file, {filename} contains {num_words} words in it.")

while True:
    filename = input(prompt)
    if filename == 'q':
        break
    else:
        count_words(filename)
