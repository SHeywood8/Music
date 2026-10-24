from mdb_classes import AlbumNode, ArtistNode, MusicDatabase
import sys
import pickle_interactions as pkl
import info_inputs as inp

def add_entry(filepath):
    response = input("What would you like to add?\n1. Artist (Use to add an empty artist, or to add multiple albums to/with an artist.)\n2. Album (Use to add a single album to an existing or new artist.)\n")
    if response.lower() in ["1", "artist"]:
        add_artist(filepath)
    elif response.lower() in ["2", "album"]:
        print("Album adding not yet supported.")
    else:
        print("Invalid response.")
    return

def add_artist(filepath):
    mdb:MusicDatabase = pkl.load_mdb(filepath)
    if mdb == None:
        return

    artist_name = inp.get_artist_name()
    if artist_name == '':
        return
    artist = ArtistNode(artist_name)
    
    while True:
        response = input("Add Album? Y/n: ")
        if response.lower() == "y":
            artist.add_album(
                AlbumNode(
                    name = inp.get_album_name(),
                    release_date = inp.get_album_release_date(),
                    acquisition_date = inp.get_album_acquisition_date(),
                    discogs_id = inp.get_discogs_id(),
                    artist = artist
                )
            )
        else:
            break

    
    mdb.add_artist(artist)
    mdb.dump(filepath)
    return

if __name__ == "__main__":
    args = sys.argv
    try:
        filepath = args[1]
    except:
        filepath = ''
        print("File path not found or not included. Using default file path.")
    add_artist(filepath)