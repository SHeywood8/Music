import os, pickle
from date_class import Date
import pickle_interactions as pkl

class AlbumNode():
    def __init__(self, name = None, release_date = None, acquisition_date = None, discogs_id = None, artist = None):
        self.name = name
        self.release_date = release_date
        self.acquisition_date = acquisition_date
        self.discogs_id = discogs_id
        self.artist = artist
        return

    def set_artist(self, artist: ArtistNode):
        self.artist = artist
        return

    def set_release_date(self, date:Date):
        self.release_date = date
        return

    def set_acquisition_date(self, date:Date):
        self.acquisition_date = date
        return

    def set_discogs_id(self, id):
        self.discogs_id = id
        return

    def __repr__(self):
        string = f'''{self.artist.name}
{self.name}
{self.release_date}
{self.discogs_id}'''
        return string



class ArtistNode():
    def __init__(self, name = None, albums:list = []):
        self.name = name
        if albums != []:
            for album in albums:
                album.set_artist(self)
        self.albums = albums
        return

    def get_album_names(self):
        album_names = []
        for album in self.albums:
            album_names.append(album.name)
        return album_names

    def get_album(self, album_name:str):
        for album in self.albums:
            if album.name.lower() == album_name.lower():
                return True, album
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
        self.albums = sorted(self.albums, key=lambda x:x.release_date)
        return

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

    def get_artist(self, artist_name:str):
        for artist in self.artists:
            if artist.name.lower() == artist_name.lower():
                return True, artist
        return False, None

    def get_artist_names(self):
        artist_names = []
        for artist in self.artists:
            artist_names.append(artist.name)
        return artist_names

    def add_artist(self, artist: ArtistNode):
        artist_found, orig_artist_node = self.get_artist(artist.name)
        if not artist_found:
            self.artists.append(artist)
            self.artists = sorted(self.artists, key=lambda x:x.name)
        else:
            for album in artist.albums:
                orig_artist_node.add_album(album)
        return

    def remove_artist(self, artist: ArtistNode):
        artist_index = self.artists.index(artist)
        self.artists.pop(artist_index)
        return

    def add_album(self, album: AlbumNode):
        artist_node = album.artist
        if album.artist != None:
            artist_found, orig_artist_node = self.get_artist(artist_node.name)
            if not artist_found:
                self.add_artist(artist_node)
            else:
                album.set_artist(orig_artist_node)
                orig_artist_node.add_album(album)
        else:
            print("Cannot add Album without Artist to Database.")
        return


    def dump(self, filepath: str):
        if filepath == '':
            filepath = "data/mdb.pkl"
        abs_filepath = os.path.abspath(filepath)
        #pkl.clear_mdb(abs_filepath)
        pickle.dump(self, open(abs_filepath, 'wb'))
        return