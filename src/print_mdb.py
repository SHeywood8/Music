from mdb_classes import MusicDatabase
import os, sys
import pickle_interactions as pkl

def print_mdb(filepath):
    mdb = pkl.load_mdb(filepath)
    print(mdb)

if __name__ == "__main__":
    args = sys.argv
    try:
        filepath = args[1]
    except:
        print("File path not found or not included. Using default file path.")
        filepath = ''
    print_mdb(filepath)