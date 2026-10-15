import os, sys, json

def dict_to_json(dict):
    with open('albums.json', 'w') as f:
        json.dump(dict, f)
        f.close()
    return

def json_to_dict(filepath):
    if not os.path.exists(filepath):
        dict_to_json({})
    with open(filepath, 'r') as f:
        content = f.read()
        f.close()
    return json.loads(content)

def get_album_info(fields = "1234"):
    album_info = [None]*4

    valid_input = False
    for i in range(1,5):
        if str(i) in fields:
            valid_input = True
    if not valid_input:
        print("Invalid Input")
        return album_info

    if "1" in fields:
        artist_name = input("Artist Name: ")
        if artist_name.lower() in ["esc", "escape", "end"]:
            return None
        album_info[0] = artist_name

    if "2" in fields:
        album_name = input("Album Name: ")
        album_info[1] = album_name

    if "3" in fields:
        while True:
            release_year = input("Year of Release: ")
            try:
                release_year = int(release_year)
                break
            except:
                print("Error: Input must be an integer.")
        album_info[2] = release_year

    if "4" in fields:
        OpenScrobbler_link = input("OpenScrobbler Link: ")
        if OpenScrobbler_link[0] != "h":
            OpenScrobbler_link = "https://openscrobbler.com/scrobble/album/view/dsid/release-" + OpenScrobbler_link
            album_info[3] = OpenScrobbler_link
    
    return album_info

def add_album_to_dict(album_info):
    artist_name, album_name, release_year, OpenScrobbler_link = album_info

    album_dict = json_to_dict('albums.json')

    if artist_name not in album_dict:
        album_dict[artist_name] = {}
    
    album_dict[artist_name][album_name] = {"year" : release_year, "link" : OpenScrobbler_link}

    dict_to_json(album_dict)
    return

def remove_album_from_dict(album_info):
    artist_name, album_name, _, _ = album_info

    album_dict = json_to_dict('albums.json')

    del album_dict[artist_name][album_name]
    if album_dict[artist_name] == {}:
        del album_dict[artist_name]

    dict_to_json(album_dict)
    return

def update_readme():
    total_album_count = 0
    
    album_dict = json_to_dict('albums.json')
    html_albums = '''<h1>Music</h1>

<h3>Links</h3>

<a href="https://www.last.fm/user/Jam847">last.fm</a>

<a href="https://openscrobbler.com/">OpenScrobbler</a>

<a href="https://www.discogs.com/user/jam847/collection">Discogs</a>

<h3>CDs</h3>

'''
    all_artists = list(album_dict.keys())
    all_artists.sort()

    for artist in all_artists:
        if artist[:4] == "test":
            continue
        album_tuples = get_artist_albums(artist)
        album_count = len(album_tuples)
        total_album_count += album_count

        album_html = f'<details><summary>{artist}'
        if album_count > 1:
            album_html += f' ({album_count})'
        album_html += '</summary>\n<ul>\n'

        for tuple in album_tuples:
            album_html += f'<li><a href="{tuple[3]}">{tuple[1]}</a> ({tuple[2]})</li>\n'
        album_html += '</ul></details>\n'
        html_albums += album_html
    html_albums += f"\n\n<p>Total CDs: {total_album_count}</p>"
    with open('README.md', 'w') as f:
        f.write(html_albums)
        f.close()
    
    return

def update_table():
    markdown_table = '|Artist|Album|Release Year|OpenScrobbler Link\n|-----|-----|-----|-----|\n'
    all_albums = get_all_albums()
    for album in all_albums:
        album_row_md = f'|{album[0]}|{album[1]}|{album[2]}|[Link]({album[3]})|\n'
        markdown_table += album_row_md
    with open('album-table.md', 'w') as f:
        f.write(markdown_table)
        f.close()
    return

def edit_entry():
    album_dict = json_to_dict('albums.json')
    album_artists = list(album_dict.keys())
    album_artists.sort()
    print("To find entry to edit, enter:")
    while True:
        edit_artist = input("Artist Name: ")
        if edit_artist not in album_artists:
            print("Artist not found.")
            continue
        else:
            print("Artist found. Albums listed below.")
            break

    artist_albums = list(album_dict[edit_artist].keys())
    artist_albums.sort()
    for album in artist_albums:
        print(album)
        
    while True:
        edit_album = input("Album Name: ")
        if not edit_album in album_dict[edit_artist]:
            print("Album not found.")
            continue
        else:
            print("Album found. Full information listed below.")
            break

    album_dict_entry = album_dict[edit_artist][edit_album]
    album_tuple = [edit_artist, edit_album, album_dict_entry['year'],album_dict_entry['link']]
    edit_tuple = ['Artist Name', 'Album Name', 'Release Year', 'OpenScrobbler Link']
    for i in range(4):
        print(f'{i+1}. {edit_tuple[i]}: {album_tuple[i]}')
    while True:
        edit_index = input("Enter numbers of information to edit: ")
        new_album_tuple = get_album_info(edit_index)
        if new_album_tuple == [None] * 4:
            print("Invalid input. Some combination of 1-4 expected.")
            continue
        else:
            break
    for i in range(4):
        if new_album_tuple[i] == None:
            new_album_tuple[i] = album_tuple[i]
    remove_album_from_dict(album_tuple)
    add_album_to_dict(new_album_tuple)
    return

def remove_entry():
    album_dict = json_to_dict('albums.json')
    album_artists = list(album_dict.keys())
    album_artists.sort()
    while True:
        edit_artist = input("Artist Name: ")
        if edit_artist.lower() == "end":
            return
        elif edit_artist not in album_artists:
            print("Artist not found.")
            continue
        else:
            break

    print("Albums:")
    artist_albums = list(album_dict[edit_artist].keys())
    artist_albums.sort()
    for album in artist_albums:
        print(f'-{album}')
        
    while True:
        edit_album = input("Album Name: ")
        if not edit_album in album_dict[edit_artist]:
            print("Album not found.")
            continue
        else:
            break

    album_dict_entry = album_dict[edit_artist][edit_album]
    album_tuple = [edit_artist, edit_album, album_dict_entry['year'],album_dict_entry['link']]
    edit_tuple = ['Artist Name', 'Album Name', 'Release Year', 'OpenScrobbler Link']
    print("\n=== Entry ===")
    for i in range(4):
        print(f'{edit_tuple[i]}: {album_tuple[i]}')
    print("=== Entry ===\n")
    while True:
        response = input("""Remove album entry? If this is the only album entry for the artist, the artist will also be removed.
Y/n: """)
        if response.lower() == "y":
            remove_album_from_dict(album_tuple)
            break
        elif response.lower() == "n":
            return
    return

def find_entry():
    return

def clear_all_entries():
    confirmation = input("Are you sure you want to wipe all added albums? Y/n\n")
    if confirmation == "Y":
        dict_to_json({})
    return

def add_entry():
    album_info = get_album_info()
    if album_info == None:
        return 0
    add_album_to_dict(album_info)
    return None

def bulk_add_entry():
    print("Now bulk adding albums. Type 'esc' or 'Escape' to cancel.")
    while True:
        result = add_entry()
        if result == 0:
            break
    return

def get_all_albums(with_test = False):
    album_dict = json_to_dict('albums.json')
    album_artists = list(album_dict.keys())
    album_artists.sort()
    all_albums = []
    for album_artist in album_artists:
        if album_artist[0:4] == "test" and not with_test:
            continue
        artist_albums = list(album_dict[album_artist].keys())
        artist_albums.sort()
        artist_albums_tuples = []
        for artist_album in artist_albums:
            album_tuple = [album_artist, artist_album, album_dict[album_artist][artist_album]['year'], album_dict[album_artist][artist_album]['link']]
            artist_albums_tuples.append(album_tuple)
        artist_albums_tuples = sorted(artist_albums_tuples, key=lambda x:x[2])
        all_albums += artist_albums_tuples
    return all_albums

def get_artist_albums(artist_name):
    album_dict = json_to_dict('albums.json')
    artist_albums = []
    if artist_name not in album_dict:
        return artist_albums
    for album in album_dict[artist_name].keys():
        album_entry = album_dict[artist_name][album]
        album_tuple = [artist_name, album, album_entry["year"], album_entry["link"]]
        artist_albums.append(album_tuple)
    return sorted(artist_albums, key=lambda x:x[2])

def get_albums(album_name):
    return [x for x in get_all_albums(True) if x[1] == album_name]

def format_album_tuple(album_tuple, header = True, footer = True):
    content = ''
    if header:
        content += '=== Entry ===\n'
    content += f'''Artist Name: {album_tuple[0]}
Album Name: {album_tuple[1]}
Release Year: {album_tuple[2]}
OpenScrobbler Link: {album_tuple[3]}'''
    if footer:
        content += '\n=== Entry ==='
    return content

def lprint(lst):
    if type(lst) != list:
        print("Input not a list.")
    else:
        for x in lst:
            print(x)
    return


def main():
    while True:
        content = input("What would you like to do?\n")
        match content.lower():
            case "help" | "?":
                print("""add - Add an album.
ba, bulkadd - Add multiple albums back to back.
rm, remove - Remove an album.
ed, edit - Edit an existing album.
qr, query - Find an album entry.
up, update - Update 'README.md' and 'album-table.md' with all newly added albums.
cl, clear - Wipe added albums.
end - Exit this program.
Help, ? - show this list.""")
            case "add":
                add_entry()
            case "ba" | "bulkadd":
                bulk_add_entry()
            case "rm" | "remove":
                remove_entry()
            case "ed" | "edit":
                edit_entry()
            case "qr" | "query":
                find_entry()
            case "up" | "update":
                update_readme()
                update_table()
            case "cl" | "clear":
                clear_all_entries()
            case "end":
                return
            case _:
                print(f"Command {content} not found. Type 'Help' or '?' for command list.")


if __name__ == "__main__":
    main()