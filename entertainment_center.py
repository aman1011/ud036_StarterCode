import movie
import fresh_tomatoes

# Creating  instance for movie 1.
sorcerer_stone = movie.Movie(
    "Harry Potter and the Sorcerer's Stone",
    "It's all in the J.K. Rowling's Harry Potter and the Sorcerer's Stone",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
    "https://www.youtube.com/watch?v=VyHV0BRtdxo")

# Creating  instance for movie 2.
chamber_of_secret = movie.Movie(
    "Harry Potter and the Chamber of secrets",
    "It's all in the J.K. Rowling's Harry Potter and the Chamber of Secrets",
    "https://upload.wikimedia.org/wikipedia/en/c/c0/Harry_Potter_and_the_Chamber_of_Secrets_movie.jpg",
    "https://www.youtube.com/watch?v=1bq0qff4iF8")

# Creating  instance for movie 3.
prisoner_of_azkaban = movie.Movie(
    "Harry Potter and the Prisoner of Azkaban",
    "It's all in the J.K. Rowling's Harry Potter and the Prisoner of Azkaban",
    "https://upload.wikimedia.org/wikipedia/en/b/bc/Prisoner_of_azkaban_UK_poster.jpg",
    "https://www.youtube.com/watch?v=lAxgztbYDbs")

# Creating  instance for movie 4.
goblet_of_fire = movie.Movie(
    "Harry Potter and the Goblet of Fire",
    "It's all in the J.K. Rowling's Harry Potter and the Goblet of Fire",
    "https://upload.wikimedia.org/wikipedia/en/c/c9/Harry_Potter_and_the_Goblet_of_Fire_Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=3EGojp4Hh6I")

# Creating  instance for movie 5.
order_of_phoenix = movie.Movie(
    "Harry Potter and the Order of Phoenix",
    "It's all in the J.K. Rowling's Harry Potter and the Order of Phoenix",
    "https://upload.wikimedia.org/wikipedia/en/e/e7/Harry_Potter_and_the_Order_of_the_Phoenix_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=y6ZW7KXaXYk")

# Creating  instance for movie 6.
half_blood_prince = movie.Movie(
    "Harry Potter and the Half-Blood Prince",
    "It's all in the J.K. Rowling's Harry Potter and the Half-Blood Prince",
    "https://upload.wikimedia.org/wikipedia/en/thumb/3/3f/Harry_Potter_and_the_Half-Blood_Prince_poster.jpg/220px-Harry_Potter_and_the_Half-Blood_Prince_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=sg81Lts5kYY")

# Creating  instance for movie 7.
deathly_hallow_first = movie.Movie(
    "Harry Potter and the Deathly Hallows - Part 1",
    ("It's all in the J.K. Rowling's Harry Potter and the",
        " Deathly Hallows - Part 1"),
    "https://upload.wikimedia.org/wikipedia/en/2/2d/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_1.jpg",  # noqa
    "https://www.youtube.com/watch?v=MxqsmsA8y5k")

# Creating  instance for movie 8.
deathly_hallow_second = movie.Movie(
    "Harry Potter and the Deathly Hallows - Part 2",
    ("It's all in the J.K. Rowling's Harry Potter and the",
        " Deathly Hallows - Part 2"),
    "https://upload.wikimedia.org/wikipedia/en/d/df/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_2.jpg",  # noqa
    "https://www.youtube.com/watch?v=mObK5XD8udk")

# Making a list of the movie to be fed to fresh_tomatoes.open_movies_page
movies = [
    sorcerer_stone,
    chamber_of_secret,
    prisoner_of_azkaban,
    goblet_of_fire,
    order_of_phoenix,
    half_blood_prince,
    deathly_hallow_first,
    deathly_hallow_second,
]

# call the already built function from fresh_tomatoes module
fresh_tomatoes.open_movies_page(movies)
