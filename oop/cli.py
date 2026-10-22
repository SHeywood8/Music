from album_node import AlbumNode, ArtistNode, MusicDatabase
from date import Date, str_to_date
from pkl_inters import load_mdb, clear_mdb

PKL_FILEPATH = "oop/oop_data.pkl"

def get_album_info():
    artist_name = input("Artist Name: ")
    if artist_name == '':
        return None
    album_name = input("Album Name: ")

    release_date = None
    acquisition_date = None

    while release_date == None:
        release_date = str_to_date(input("Release Date (yyyy-mm-dd): "))

    while acquisition_date == None:
        acquisition_date = str_to_date(input("Acquisition Date (yyyy-mm-dd): "))


    discogs_id = input("Discogs ID: ")
    return [artist_name, album_name, release_date, acquisition_date, discogs_id]

def add_entry():
    mdb:MusicDatabase = load_mdb(PKL_FILEPATH)
    if mdb == None:
        mdb = MusicDatabase([])
    album_info = get_album_info()
    if album_info != None:
        mdb.add_artist(ArtistNode(album_info[0],[AlbumNode(album_info[1], album_info[2], album_info[3], album_info[4])]))
        print(mdb)
        mdb.dump(PKL_FILEPATH)
        return 1
    return 0

def bulk_add_entry():
    print("Now bulk adding albums. Leave artist field blank to cancel.")
    while True:
        result = add_entry()
        if result == 0:
            break
    return

def print_mdb():
    print(load_mdb(PKL_FILEPATH))

def remove_entry():
    print("Remove feature not yet implemented.")

def edit_entry():
    print("Edit feature not yet implemented.")

def find_entry():
    print("Query feature not yet implemented.")

def update():
    print("Update feature not yet implemented.")

def clear_all_entries():
    confirmation = input("Confirm wipe of Music Database? Y/n: ")
    if confirmation.lower() != "y":
        return 0
    clear_mdb(PKL_FILEPATH)
    return 1
    

def main():
    while True:
        content = input("What would you like to do?\n")
        match content.lower():
            case "help" | "?":
                print("""ad, add - Add an album.
ba, bulkadd - Add multiple albums back to back.
rm, remove - Remove an album.
ed, edit - Edit an existing album.
pr, print - Print database.
qr, query - Find an album entry.
up, update - Update 'README.md' and 'album-table.md' with all newly added albums.
cl, clear - Wipe added albums.
end, '' - Exit this program.
Help, ? - show this list.""")
            case "ad" | "add":
                add_entry()
            case "ba" | "bulkadd":
                bulk_add_entry()
            case "rm" | "remove":
                remove_entry()
            case "ed" | "edit":
                edit_entry()
            case "pr" | "print":
                print_mdb()
            case "qr" | "query":
                find_entry()
            case "up" | "update":
                update()
            case "cl" | "clear":
                clear_all_entries()
            case "end" | "":
                return
            case _:
                print(f"Command {content} not found. Type 'Help' or '?' for command list.")