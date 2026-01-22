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

def get_album_info():
    artist_name = input("Artist Name: ")
    if artist_name.lower() in ["esc", "escape", "end"]:
        return None
    album_name = input("Album Name: ")
    while True:
        release_year = input("Year of Release: ")
        try:
            release_year = int(release_year)
            break
        except:
            print("Error: Input must be an integer.")
    OpenScrobbler_link = input("OpenScrobbler Link: ")
    return (artist_name, album_name, release_year, OpenScrobbler_link)

def add_album_to_dict(album_info):
    artist_name, album_name, release_year, OpenScrobbler_link = album_info

    album_dict = json_to_dict('albums.json')

    if artist_name not in album_dict:
        album_dict[artist_name] = {}
    
    album_dict[artist_name][album_name] = {"year" : release_year, "link" : OpenScrobbler_link}

    dict_to_json(album_dict)
    return

def update_readme():
    album_dict = json_to_dict('albums.json')
    html_albums = '<h1>Music</h1>\n\n'
    album_artists = list(album_dict.keys())
    album_artists.sort()
    for album_artist in album_artists:
        album_html = f'<details><summary>{album_artist}</summary>\n<ul>\n'
        artist_albums = list(album_dict[album_artist].keys())
        artist_albums.sort()
        artist_albums_tuples = []
        for artist_album in artist_albums:
            album_tuple = [artist_album, album_dict[album_artist][artist_album]['year'], album_dict[album_artist][artist_album]['link']]
            artist_albums_tuples.append(album_tuple)
        artist_albums_tuples = sorted(artist_albums_tuples, key=lambda x:x[1])
        for tuple in artist_albums_tuples:
            album_html += f'<li><a href="{tuple[2]}">{tuple[0]}</a> ({tuple[1]})</li>\n'
        album_html += '</ul></details>\n'
        html_albums += album_html
    with open('README.md', 'w') as f:
        f.write(html_albums)
        f.close()
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
up, update - Update 'README.md' with all newly added albums.
cl, clear - Wipe added albums.
end - Exit this program.
Help, ? - show this list.""")
            case "add":
                album_info = get_album_info()
                if album_info == None:
                    break
                add_album_to_dict(album_info)
            case "ba" | "bulkadd":
                print("Now bulk adding albums. Type 'esc' or 'Escape' to cancel.")
                while True:
                    album_info = get_album_info()
                    if album_info == None:
                        break
                    add_album_to_dict(album_info)
            case "rm" | "remove":
                print("'Remove' function not yet added.")
            case "ed" | "edit":
                print("'Edit' function not yet added.")
            case "end":
                return
            case "up" | "update":
                update_readme()
            case "cl" | "clear":
                confirmation = input("Are you sure you want to wipe all added albums? Y/n\n")
                if confirmation == "Y":
                    dict_to_json({})
            case _:
                print(f"Command {content} not found. Type 'Help' or '?' for command list.")


if __name__ == "__main__":
    main()