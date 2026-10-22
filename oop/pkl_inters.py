import pickle, os

def load_mdb(filepath: str):
    abs_filepath = os.path.abspath(filepath)
    if not os.path.exists(abs_filepath):
        print("Music Database not found.")
        return None
    return pickle.load(open(abs_filepath, "rb"))

def clear_mdb(filepath: str):
    abs_filepath = os.path.abspath(filepath)
    if not os.path.exists(abs_filepath):
        print("Music Database not found. Check filepath.")
        return 0
    # confirmation = input("Confirm wipe of Music Database? Y/n: ")
    # if confirmation.lower() != 'y':
    #     return 0
    os.remove(abs_filepath)
    return 1
    