# Movie Trailer Webpage
Source code for a Movie Trailer website.

This is a simple project which will render an HTML page with some movie titles pinned as tiles.
Clicking this tiles will open it's trailer.
Enjoy these magnificent movies.

# How to run this code.
- Navigate to the folder containing the files **fresh_tomatoes.py** , **media.py** and **entertainment_centre.py**.
- Run the command `python entertainment_centre.py`.
This will open the web page

# How does it work.
- **media.py** works as the base module which has the base class **Movie()**.
- **media.Movie()** class is instantiated to create different objects for individual movies with their corresponding parameters.
- The movie objects are then compiled in a list and this list in turn is fed to the function **open_movies_page**from the module **fresh_tomatoes**.
