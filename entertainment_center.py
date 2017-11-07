import fresh_tomatoes
import media

"""This contains the movies and their information;
that is initaized in the Movie class
in the Media Module for each movie.
"""

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "https://resizing.flixster.com/OD2Yrbt-xldV7SH2i90XkjcNUoY=/206x305/v1.bTsxMTIwNzIwNztqOzE3NTg5OzEyMDA7MjE5MDsyOTIw",# NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",# NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


tron_legacy = media.Movie("Tron Legacy",
                          "A son searching for his dad twenty years later",
                          "https://upload.wikimedia.org/wikipedia/en/c/c2/Tron_Legacy_poster.jpg", # NOQA
                          "https://www.youtube.com/watch?v=L9szn1QQfas")
                          

The_Handmaiden = media.Movie("The Handmaiden",
                  "A poor woman trying to rich Japanese widow to"
                             "save her family",
                  "https://resizing.flixster.com/85DDl2pQIoQJArrmjREFTcG5tog=/300x300/v1.bjsxMTExOTk1O2o7MTc1MTc7MTIwMDs4MDA7NTMz", # NOQA
                  "https://www.youtube.com/watch?v=EdSxl4ICTmQ",)


cloud_atlas = media.Movie("Cloud Atlas",
                          "The story of six separate storys throughout time"
                          "and how they connected",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTczMTgxMjc4NF5BMl5BanBnXkFtZTcwNjM5MTA2OA@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",# NOQA
                          "https://www.youtube.com/watch?v=ByehYal_cCs")


baby_driver = media.Movie("Baby Driver",
                          "The story of a boy trying to get away"
                          "from a life of crime",
                          "https://upload.wikimedia.org/wikipedia/en/8/8e/Baby_Driver_poster.jpg", # NOQA
                          "https://www.youtube.com/watch?v=D9YZw_X5UzQ")


"""imports "fresh_tomatoes" allows this to be transformed into
a movie website by using the funcion
"open_movies_page". The function takes the list and then
outputs it into an html webpage
contatining those movies.
"""

movies = [toy_story, avatar, tron_legacy, The_Handmaiden,
          cloud_atlas, baby_driver]
fresh_tomatoes.open_movies_page(movies)

