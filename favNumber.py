import json

def get_fav_number():
    """Get the favorite number."""
    filename = favnum.json
    try:
        with open(filename) as f:
            favnum = json.load()
    except FileNotFoundError:
        return None
    else:
        return favnum

