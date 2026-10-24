from date_class import str_to_date

def get_artist_name():
    return input("Artist Name: ")

def get_album_name():
    return input("Album Name: ")

def get_date(msg:str):
    date = None
    while date == None:
        response = input(msg)
        date = str_to_date(response)
    return date

def get_album_release_date():
    return get_date("Album Release Date (yyyy-mm-dd): ")

def get_album_acquisition_date():
    return get_date("Album Acquisition Date (yyyy-mm-dd): ")

def get_discogs_id():
    valid = False
    while not valid:
        response = input("Discogs ID: ")
        try:
            id = int(response)
            valid = True
        except:
            print("Invalid input. ID should be an integer.")
    return id

