import pickle, os

def load_mdb(filepath:str):
    if filepath == '':
        filepath = os.path.join(os.getcwd(),"data/mdb.pkl")

    abs_filepath = os.path.abspath(filepath)

    if not os.path.exists(abs_filepath):
        print("Music Database not found. Check filepath.")
        return None
    print("Music Database successfully loaded from: " + abs_filepath + "\n")
    return pickle.load(open(abs_filepath, "rb"))

def clear_mdb(filepath: str):
    abs_filepath = os.path.abspath(filepath)
    if not os.path.exists(abs_filepath):
        return 0
    # confirmation = input("Confirm wipe of Music Database? Y/n: ")
    # if confirmation.lower() != 'y':
    #     return 0
    os.remove(abs_filepath)
    return 1

if __name__ == "__main__":
    print(os.getcwd())