from date_class import str_to_date

def get_artist_name(msg = "Artist Name: "):
    return input(msg)

def get_album_name(msg = "Album Name: "):
    return input(msg)

def get_date(msg:str):
    date = None
    while date == None:
        response = input(msg)
        date = str_to_date(response)
    return date

def get_album_release_date(msg = "Album Release Date (yyyy-mm-dd): "):
    return get_date(msg)

def get_album_acquisition_date(msg = "Album Acquisition Date (yyyy-mm-dd): "):
    return get_date(msg)

def get_discogs_id(msg = "Discogs ID: "):
    valid = False
    while not valid:
        response = input(msg)
        try:
            id = int(response)
            valid = True
        except:
            print("Invalid input. ID should be an integer.")
    return id

