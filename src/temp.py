import pickle_interactions as pkl
from mdb_classes import *

if __name__ == "__main__":
    mdb:MusicDatabase = pkl.load_mdb('')
    for artist in mdb.artists:
        artist.set_database(mdb)
    mdb.dump()