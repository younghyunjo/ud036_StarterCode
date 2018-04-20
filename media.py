class Movie():
    """ This class represent movie information
    Movie classs needs three arguments.
    title is movie`s title.
    poster_image is poster_image url.
    youtube_url is movie trailer youtube url.
    """

    def __init__(self, title, poster_image, youtube_url):
        self.title = title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_url
