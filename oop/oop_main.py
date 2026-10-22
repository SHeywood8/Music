from album_node import AlbumNode, ArtistNode, MusicDatabase
from date import Date, str_to_date
from pkl_inters import load_mdb, clear_mdb
import cli

import pickle, os

def main():
    cli.main()
    return

if __name__ == "__main__":
    PKL_FILEPATH = "oop/oop_data.pkl"
    main()
