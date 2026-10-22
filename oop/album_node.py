import os, pickle, sys
from pkl_inters import clear_mdb

class AlbumNode():
    def __init__(self, name = None, release_date = None, acquisition_date = None, discogs_id = None, artist = None):
        self.name = name
        self.release_date = release_date
        self.acquisition_date = acquisition_date
        self.discogs_id = discogs_id
        self.artist = artist

    def set_artist(self, artist: ArtistNode):
        self.artist = artist

    def set_release_date(self, date:Date):
        self.release_date = date

    def set_acquisition_date(self, date:Date):
        self.acquisition_date = date

    def set_discogs_id(self, id):
        self.discogs_id = id

    def __repr__(self):
        string = f'''{self.artist.name}
{self.name}
{self.release_date}
{self.discogs_id}'''
        return string

class ArtistNode():
    def __init__(self, name = None, albums = []):
        self.name = name
        if albums != []:
            for album in albums:
                album.set_artist(self)
        self.albums = albums

    def get_album_names(self):
        album_names = []
        for album in self.albums:
            album_names.append(album.name)
        return album_names

    def get_album_tuples(self):
        albums = []
        for album in self.albums:
            albums.append([album.name, album])
        return albums

    def get_album(self, album_name:str):
        albums = self.get_album_tuples()
        for album in albums:
            if album[0].lower() == album_name.lower():
                return True, album[1]
        return False, None

    def add_album(self, album:AlbumNode):
        album_found, orig_album_node = self.get_album(album.name)
        if not album_found:
            self.albums.append(album)
            album.set_artist(self)
        else:
            if album.release_date != None:
                orig_album_node.set_release_date(album.release_date)
            if album.discogs_id != None:
                orig_album_node.set_discogs_id(album.discogs_id)
            if album.acquisition_date != None:
                orig_album_node.set_acquisition_date(album.acquisition_date)
        self.albums = sorted(self.albums, key=lambda x:x.release_date.year)

    def __repr__(self):
        string = self.name
        if self.albums != []:
            for album in self.albums:
                string += f'\n-{album.name} ({album.release_date.year})'
        return string

class MusicDatabase():
    def __init__(self, artists = []):
        self.artists = artists

    def __repr__(self):
        string = ''
        if self.artists != []:
            for artist in self.artists:
                string += artist.__repr__() + "\n"
        return string

    def get_artist_names(self):
        artist_names = []
        for artist in self.artists:
            artist_names.append(artist.name)
        return artist_names

    def add_artist(self, artist: ArtistNode):
        if not artist.name in self.get_artist_names():
            self.artists.append(artist)
        else:
            print(f"Artist: {artist.name} already in database. Adding Albums")
            for album in artist.albums:
                artist.add_album(album)
        self.artists = sorted(self.artists, key=lambda x:x.name)

    def dump(self, filepath: str):
        abs_filepath = os.path.abspath(filepath)
        clear_mdb(abs_filepath)
        pickle.dump(self, open(abs_filepath, 'wb'))