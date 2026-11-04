from mdb_classes import AlbumNode, ArtistNode, MusicDatabase
import pickle_interactions as pkl
import info_inputs as inp
from date_class import str_to_date

def query_mdb(filepath):
    mdb:MusicDatabase = pkl.load_mdb(filepath)
    if mdb == None:
        return

    artist_name = inp.get_artist_name("Artist Name: ")
    if artist_name != '':
        artist_found, artist_node = mdb.get_artist(artist_name)
        if artist_found:
            artist_albums = artist_node.albums
            if len(artist_albums) == 0:
                print("Error: Artist has no albums.")
                return
            string = f"{artist_node.name} has the following albums:\n"
            albums = artist_node.albums
            for i in range(len(albums)):
                string += f"{i + 1}. {albums[i].name} ({albums[i].release_date.year})\n"
            string += "Enter number of album to query: "
            response = input(string)
            try:
                album_index = int(response) - 1
                album = albums[album_index]
            except:
                print("Response must be one of the integers listed above.")
                return
            edit_album(album)

    mdb.dump(filepath)
    return

def edit_album(album:AlbumNode):
    if not isinstance(album, AlbumNode):
        print("Error: Input is not an Album.")
        return

    while True:
        edit_field = input(f"""===Album Info===
1. Artist Name: {album.artist.name}
2. Album Name: {album.name}
3. Release Date: {album.release_date.__repr__()}
4. Acquisiton Date: {album.acquisition_date.__repr__()}
5. Discogs ID: {album.discogs_id}
===Album Info===
Enter field to edit (1-5). Leave blank to exit.
""")
        match edit_field:
            case "1":
                new_artist_name = inp.get_artist_name(f"New Artist Name [{album.artist.name}]: ")
                mdb:MusicDatabase = album.artist.database
                artist_found, artist_node = mdb.get_artist(new_artist_name)
                if artist_found:
                    album.set_artist(artist_node)
                else:
                    mdb.add_artist(ArtistNode(new_artist_name, [album]))
                mdb.dump()
                print("Artist changed.")
            case "2":
                new_album_name = inp.get_album_name(f"New Album Name [{album.name}]: ")
                album.set_name(new_album_name)
            case "3":
                new_album_release_date = inp.get_album_release_date(f"New Album Release Date [{album.release_date.__repr__()}]: ")
                album.set_release_date(new_album_release_date)
            case "4":
                new_album_acquisition_date = inp.get_album_acquisition_date(f"New Acquisition Date [{album.release_date.__repr__()}]: ")
                album.set_acquisition_date(new_album_acquisition_date)
            case "5":
                new_discogs_id = inp.get_discogs_id(f"New Discogs ID [{album.discogs_id}]: ")
                album.set_discogs_id(new_discogs_id)
            case "":
                break
            case "_":
                continue