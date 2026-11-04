from mdb_classes import AlbumNode, ArtistNode, MusicDatabase
import sys
import pickle_interactions as pkl
import info_inputs as inp

def add_entry(filepath):
    mdb:MusicDatabase = pkl.load_mdb(filepath)
    if mdb == None:
        return

    response = input("What would you like to add?\n1. Artist (Use to add an empty artist, or to add multiple albums to/with an artist.)\n2. Album (Use to add a single album to an existing or new artist.)\nEnter Number: ")
    if response.lower() in ["1", "artist"]:
        add_artist(mdb)
        while True:
            if input("Add another artist? Y/n: ").lower() != "y":
                break
            add_artist(mdb)
    elif response.lower() in ["2", "album"]:
        add_album(mdb)
        while True:
            if input("Add another album? Y/n: ").lower() != "y":
                break
            add_album(mdb)
    else:
        print("Invalid response.")
    mdb.dump(filepath)
    return

def add_artist(mdb:MusicDatabase):
    artist_name = inp.get_artist_name()
    if artist_name == '':
        return
    artist = ArtistNode(artist_name, [])
    
    while True:
        response = input("Add Album? Y/n: ")
        if response.lower() == "y":
            new_album = AlbumNode(
                    name = inp.get_album_name(),
                    release_date = inp.get_album_release_date(),
                    acquisition_date = inp.get_album_acquisition_date(),
                    discogs_id = inp.get_discogs_id(),
                    artist = artist
                )
            artist.add_album(new_album)
            continue
        else:
            break

    confirm = input(f"Add the following artist to the database?\n{artist.albums_to_str()}\nY/n: ")
    if confirm.lower() != "y":
        return
    
    mdb.add_artist(artist)
    return

def add_album(mdb:MusicDatabase):
    new_album = AlbumNode(
        artist = inp.get_artist_name(),
        name = inp.get_album_name(),
        release_date = inp.get_album_release_date(),
        acquisition_date=inp.get_album_acquisition_date(),
        discogs_id=inp.get_discogs_id()
    )
    
    confirm = input(f"Add the following album to the database?\n{new_album.to_str()}\nY/n: ")
    if confirm.lower() != "y":
        return

    mdb.add_album(new_album)
    return

if __name__ == "__main__":
    args = sys.argv
    try:
        filepath = args[1]
    except:
        filepath = ''
        print("File path not found or not included. Using default file path.")
    add_entry(filepath)