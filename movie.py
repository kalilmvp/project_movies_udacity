# coding: utf8


class Movie:
    """ This class represents a movie and it´s properties to be retrieved by the
        api and presented at the website.

    Attributes:
        title (str): The title of the movie.
        storyline (str): The overview of the movie.
        poster_image_url (str): The poster web url of the movie.
        trailer_youtube_id (str): The trailer youtube id to be concatened with
            the embed url of youtube.

    """

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_id):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_id = trailer_youtube_id
