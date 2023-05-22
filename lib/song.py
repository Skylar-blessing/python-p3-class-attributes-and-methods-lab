class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        if cls.genre not in cls.genres:
            cls.genres.append(cls.genre)

    @classmethod
    def add_to_artists(cls):
        if cls.artist not in cls.artists:
            cls.artists.append(cls.artist)

    @classmethod
    def add_to_genre_count(cls):
        if cls.genre not in cls.genre_count:
            cls.genre_count[cls.genre] = 1
        else:
            cls.genre_count[cls.genre] += 1

    @classmethod
    def add_to_artist_count(cls):
        if cls.artist not in cls.artist_count:
            cls.artist_count[cls.artist] = 1
        else:
            cls.artist_count[cls.artist] += 1

ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
print(ninety_nine_problems.name)
# Output: "99 Problems"

print(ninety_nine_problems.artist)
# Output: "Jay-Z"

print(ninety_nine_problems.genre)
# Output: "Rap"

print(Song.count)
# Output: 1

print(Song.genres)
# Output: ["Rap"]

print(Song.artists)
# Output: ["Jay-Z"]

ninety_nine_problems.add_to_genre_count()
print(Song.genre_count)
# Output: {"Rap": 1}

ninety_nine_problems.add_to_artist_count()
print(Song.artist_count)
# Output: {"Jay-Z": 1}
