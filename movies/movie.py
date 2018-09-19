import webbrowser

class Movie:
    """ 
        Documentation of the class Movie
    """

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_id):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_id = trailer_youtube_id