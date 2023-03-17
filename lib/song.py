class Song:

    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, new_genre):
        cls.genres.add(new_genre)

    @classmethod
    def add_to_artists(cls, new_artist):
        cls.artists.add(new_artist)
    
    @classmethod
    def add_to_genre_count(cls, new_genre):
        if cls.genre_count.get(new_genre):
            cls.genre_count[new_genre] += 1
        else:
            cls.genre_count[new_genre] = 1

    @classmethod
    def add_to_artist_count(cls, new_artist):
        if cls.artist_count.get(new_artist):
            cls.artist_count[new_artist] += 1
        else:
            cls.artist_count[new_artist] = 1

