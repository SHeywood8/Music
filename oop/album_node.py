class AlbumNode():
    def __init__(self, name = None, release_date = None, discogs_id = None, artist = None):
        self.name = name
        self.release_date = release_date
        self.discogs_id = discogs_id
        self.artist = artist

    def set_artist(self, artist: ArtistNode):
        self.artist = artist

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

    def add_album(self, album : AlbumNode):
        self.albums.append(album)
        album.set_artist(self)
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