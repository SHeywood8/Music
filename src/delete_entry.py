from mdb_classes import MusicDatabase, ArtistNode
import sys
import pickle_interactions as pkl
import info_inputs as inp

def delete_entry(filepath):
    mdb:MusicDatabase = pkl.load_mdb(filepath)
    if mdb == None:
        return

    response = input("What would you like to remove?\n1. Artist (Remove the whole artist, including albums.)\n2. Album (Remove a single album from an artist)\nEnter Number: ")
    match response:
        case "1":
            delete_artist(mdb)
        case "2":
            delete_album(mdb)


    mdb.dump(filepath)

def delete_artist(mdb:MusicDatabase):
    if len(mdb.artists) == 0:
        print("There are no artists in loaded database.")
        return

    artist_name = inp.get_artist_name()
    artist_found, artist_node = mdb.get_artist(artist_name)
    if not artist_found:
        print(f"Error: Artist {artist_name} not found.")
        return

    input_string = f"Confirm removal of {artist_name} from database? "
    if artist_node.albums != []:
        input_string += "\nThis will also remove the following albums:\n"
        for album in artist_node.albums:
            input_string += f"-{album.name} ({album.release_date.year})\n"
    input_string += "Y/n: "

    if input(input_string).lower() == "y":
        mdb.remove_artist(artist_node)
    return

def delete_album(mdb:MusicDatabase):
    if len(mdb.artists) == 0:
        print("There are no albums in loaded database.")
        return

    artist_name = inp.get_artist_name()
    artist_found, artist_node = mdb.get_artist(artist_name)
    if not artist_found:
        print(f"Error: Artist {artist_name} not found.")
        return

    artist_node:ArtistNode
    if len(artist_node.albums) == 0:
        print(f"Error: Artist has no albums.")

    string = f"{artist_node.name} has the following albums:\n"
    albums = artist_node.albums
    for i in range(len(albums)):
        string += f"{i + 1}. {albums[i].name}\n"
    string += "Enter number of album to delete: "
    response = input(string)
    try:
        album_index = int(response) - 1
        album = albums[album_index]
        confirmation = input(f"Confirm removal of album:\n{album.to_str()}\nY/n: ")
        if confirmation.lower() != "y":
            return
        _ = albums.pop(album_index)
        artist_node.albums = albums
        print("Album successfully removed.")
    except:
        print("Response must be one of the integers listed above.")
    return
            

if __name__ == "__main__":
    args = sys.argv
    try:
        filepath = args[1]
    except:
        filepath = ''
        print("File path not found or not included. Using default file path.")
    delete_artist(filepath)