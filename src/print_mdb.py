from mdb_classes import MusicDatabase, ArtistNode
import os, sys
import pickle_interactions as pkl

def print_mdb_artists(filepath):
    mdb = pkl.load_mdb(filepath)
    print(mdb)
    return

def print_mdb(filepath):
    mdb:MusicDatabase = pkl.load_mdb(filepath)
    string = ''
    for artist in mdb.artists:
        artist:ArtistNode
        string += artist.albums_to_str() + "\n"
    print(string)

def print_mdb_albums(filepath):
    mdb:MusicDatabase = pkl.load_mdb(filepath)
    albums = mdb.get_all_ablums()
    string = ''
    for album in albums:
        string += f"{album.name} ({album.release_date.year}) [{album.artist.name}]\n"
    print(string)

if __name__ == "__main__":
    args = sys.argv
    try:
        filepath = args[1]
    except:
        print("File path not found or not included. Using default file path.")
        filepath = ''
    print_mdb_artists(filepath)