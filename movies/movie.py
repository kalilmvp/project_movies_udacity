import webbrowser

class Movie:
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_id):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_id = trailer_youtube_id