import webbrowser
class Movie():

    # declaring the documentation.
    """ This is a class made for Udacity's Full Stack NanoDegree programme's first project """
    # declaring a claas variable.
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # Every class has a init function
    # otherwise known as constructor
    # which gets called upon while creating
    # an instance or object.
    def __init__(self, movie_title, movie_storyline, movie_poster_image, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
