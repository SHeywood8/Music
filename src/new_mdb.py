from mdb_classes import MusicDatabase
import os, sys

def new_mdb(filepath):
    new_mdb = MusicDatabase()
    new_mdb.dump(filepath)

def main(filepath):
    if filepath == '':
        filepath = os.path.join(os.getcwd(), "data/mdb.pkl")
        print(filepath)
    if os.path.exists(filepath):
        overwrite = input("Music Database already exists in location. Overwrite? Y/n: ")
        if overwrite.lower() == "y":
            double_check = input("Warning: This will wipe the existing Database. Continue? Y/n: ")
            if double_check.lower() == "y":
                new_mdb(filepath)
    else:
        new_mdb(filepath)
    return

if __name__ == "__main__":
    args = sys.argv
    try:
        filepath = args[1]
    except:
        print("File path not found or not included. Using default file path.")
        filepath = ''
    main(filepath)