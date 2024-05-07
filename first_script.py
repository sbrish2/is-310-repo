'''
def check_movie_release(movie):
    movie_data = movie['name'] + " was released in " + str(movie['release_year'])
    if movie['release_year'] < 2000:
        print(f"{movie['name']} was released before 2000")
    else:
        print(f"{movie['name']} was released after 2000")
        return movie['name']

recent_movies = []

favorite_movies =[
    {
        "name": "The Matrix I",
        "release_year": 1999,
        "sequels": ["The Matrix II", "The Matrix III", "The Matrix IV"]
    },
    {
        "name": "Star Wars IV",
        "release_year": 1977,
        "sequels": ["Star Wars V", "Star Wars VI", "Star Wars VII", "Star Wars VIII", "Star Wars IX"],
        "prequels": ["Star Wars I", "Star Wars II", "Star Wars III"]
    }
]

def print_movie_name_and_year(movie):
    movie_data = movie['name'] + " was released in " + str(movie['release_year'])
    return movie_data


for movie in favorite_movies:
    new_movie_data = print_movie_name_and_year(movie)
    if movie['release_year'] > 1990:
        print(new_movie_data)

'''

class Movie:
    """Contains methods for data about a movie

    Methods:
    --------
    add_directors
    add_release_year
    calculate_age
    """
    def __init__(self, name):
        self.movie_name = name
        self.directors = []
        self.release_year = None
        self.age = 0
        self.sequels = []
        self.prequels = []


    def add_directors(self, directors):
        """Adds a list of directors of the movie

        Method argument:
        -----------------
        directors(list) -- A list of people who director the movie
        """
        if isinstance(directors, list) is False:
            directors = [directors]

        self.directors.extend(directors)


    def add_release_year(self, year):
        """Adds the release year of the movie

        Method argument:
        -----------------
        year(integer or string) -- A year the movie was released
        """

        self.release_year = int(year)

    def add_sequels(self, sequels):
        """Adds a list of sequels to the movie

        Method argument:
        -----------------
        sequels(list) -- A list of sequels to the movie
        """
        if isinstance(sequels, list) is False:
            sequels = [sequels]

        self.sequels.extend(sequels)

    def add_prequels(self, prequels):
        """Adds a list of prequels to the movie

        Method argument:
        -----------------
        prequels(list) -- A list of prequels to the movie
        """
        if isinstance(prequels, list) is False:
            prequels = [prequels]

        self.prequels.extend(prequels)


    def calculate_movie_age(self):
        """Calculates the age of the movie
        """
        self.age = 2024 - self.release_year

#a_movie = Movie("The Matrix I")
#a_movie.add_directors(["Lana Wachowski", "Lilly Wachowski"])
#a_movie.add_release_year(1999)
#a_movie.add_sequels(["The Matrix II", "The Matrix III", "The Matrix IV"])
#a_movie.calculate_movie_age()
#print(a_movie.add_directors.__doc__) 

import pathlib

current_directory = pathlib.Path().cwd()
print(current_directory)

