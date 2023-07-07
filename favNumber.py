import json

def get_fav_number():
    """Get the favorite number."""
    filename = 'favnum.json'
    try:
        with open(filename) as f:
            favnum = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favnum

def get_new_favnum():
    """Gets a new favorite number as input."""
    favnum = input("What's your favorite number? ")
    filename = 'favnum.json'
    with open(filename, 'w') as f:
        json.dump(favnum, f)
    return favnum

def print_favnum():
    """The main function that brings it all together."""
    favnum = get_fav_number()
    if favnum:
        print(f"Your favorite number is {favnum}!")
    else:
        get_new_favnum()

print_favnum()