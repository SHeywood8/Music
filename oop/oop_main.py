from album_node import AlbumNode, ArtistNode, MusicDatabase
from date import Date
from pkl_inters import load_mdb, clear_mdb

import pickle

def main():
    mdb:MusicDatabase = load_mdb(PKL_FILEPATH)
    mdb.add_artist(ArtistNode("Bad Omens",[
        AlbumNode("Bad Omens", Date(2016, 8, 19), None, 8920859),
        AlbumNode("Finding God Before God Finds Me", Date(2019, 8, 2), None, 13993484),
        AlbumNode("The Death Of Peace Of Mind", Date(2022, 2, 25), None, 22306783)
    ]))
    mdb.dump(PKL_FILEPATH)
    return

if __name__ == "__main__":
    PKL_FILEPATH = "oop/oop_data.pkl"
    main()
    