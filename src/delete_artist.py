from mdb_classes import MusicDatabase
import sys
import pickle_interactions as pkl
import info_inputs as inp

def delete_artist(filepath = ''):
    mdb:MusicDatabase = pkl.load_mdb(filepath)
    if mdb == None:
        return

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

    mdb.dump(filepath)
    return

if __name__ == "__main__":
    args = sys.argv
    try:
        filepath = args[1]
    except:
        filepath = ''
        print("File path not found or not included. Using default file path.")
    delete_artist(filepath)