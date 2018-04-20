import media
import fresh_tomatoes

# Declare lion_king instance
lion_king = media.Movie("Lion King",
                        "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
                        "https://www.youtube.com/watch?v=4sj1MT05lAA")

# Declare toy story instance
toy_story = media.Movie("Toy Story",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# Declare avatar instance
avatar = media.Movie("Avatar",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

# Declare school of rock instance
school_of_rock = media.Movie("School of Rock",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

# Declare wall e instance
wall_e = media.Movie("Wall E",
                     "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
                     "https://www.youtube.com/watch?v=8-_9n5DtKOc")

# Declare ai instance
ai = media.Movie("AI",
                 "https://upload.wikimedia.org/wikipedia/en/e/e6/AI_Poster.jpg",
                 "https://www.youtube.com/watch?v=_19pRsZRiz4")

# Make movie list to be displayed
movies = [lion_king, toy_story, avatar, school_of_rock, wall_e, ai]

# make a movies web page
fresh_tomatoes.open_movies_page(movies)
