from album_node import AlbumNode, ArtistNode, MusicDatabase
from date import Date


def main():
    artist1 = ArtistNode("Beartooth")
    artist1.add_album(AlbumNode("Pure Ecstasy", Date(2026,8,28), 38293944))
    artist1.add_album(AlbumNode("Disgusting", Date(2014,6,10), 5784769))

    artist2 = ArtistNode("Honey Revenge",
                         [AlbumNode("Retrovision", Date(2023)),
                          AlbumNode("Loving and Losing", Date(2026))])

    mdb = MusicDatabase([artist1, artist2])

    print(mdb.artists[1].albums[0])
    return

if __name__ == "__main__":
    main()