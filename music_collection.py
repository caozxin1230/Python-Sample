
# four classes:songs, artists, albums and playlists.
#For simplicity, assume that any song or album has a single “artist” value (which could represent more than one person), but you should include compilation albums (which contain songs by a selection of different artists). The “artist” of a compilation album can be a special value like “Various Artists”. You can also assume that each song is associated with a single album, but that multiple copies of the same song (which are included in different albums) can exist.

class song:
    def __init__(self, song_name):
        self.song_name = song_name
        self.albums = []
        self.artists = []

    def total_artist(self, number_artist):
        self.artists.append(number_artist)
        number_artist.add_song(self)

    def involved_album(self,number_album):
        self.albums.append(number_album)
        number_album.add_song(self)

class artist:
    def __init__(self,artist_name,style):
        self.artist_name = artist_name
        self.style = style
        self.songs = []
        self.albums = []

    def add_song(self,songs):
        self.songs = song(self,song_name)
        songs.append(song(self,song_name))

    def add_album(self,albums):
        self.albums = album(self,album_name)
        albums.append(album(self,album_name))


class album:
    def __init__(self,album_name):
        self.album_name= album_name
        self.artists = []

    def add_artist(self,artist_name,style):
        self.artist[artist_name] = artist(self,artist_name, style)
        artists.append(artist)

class playlist:
    def __init__(self,playlist_name,user):
        self.playlist_name = playlist_name
        self.user = user
        users = []

    def song_running(self,song_name):
        self.song = song(self, song_name)
        return self.song

class user:
    def __init__(self,user_name):
        self.user_name = user_name

#examples: "We are young" from Fun. & "somewhere out there" from Linda Ronstadt and James Ingram

song1 = song('We are young')

print(song1.song_name)