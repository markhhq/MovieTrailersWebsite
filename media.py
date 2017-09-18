# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Movie():
    # This class provides a way to store movie related information

    def __init__(self, movie_title, date_released, director_name, box_office, movie_storyline, poster_image, trailer_youtube):
        # initialize instance of class Movie
        self.title = movie_title
        self.movie_date = date_released
        self.director = director_name
        self.box_office_result = box_office
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
    	# play movie trailers using Youtube URL

    	webbrowser.open(self.trailer_youtube_url)

