# trieda Movie
class Movie:
    # konstruktor, definovanie parametrov triedy film
    def __init__(self, title, year, genre, duration, director):
        self._title = title
        self._year = year
        self._genre = genre
        self._duration = duration
        self._director = director

    # vypis
    def print(self):
        # {:20} = formatovanie, kolko miest treba
        print("| {:20} | {:4} | {:6} | {:3}m | {:10} |".format(
            self._title,
            self._year,
            self._genre,
            self._duration,
            self._director
        ))


# trieda Library
class Library:
    # konstruktor, definovanie parametrov triedy kniznica
    def __init__(self):
        self._movie_library = list()

    # pridanie defaultnych filmov do databazy
    def seed(self):
        # .append = vloz
        movie = Movie("Matrix", 1999, "sci-fi", 136, "Wachovski")
        self._movie_library.append(movie)
        movie = Movie("Jurassic Park", 1993, "action", 127, "Spielberg")
        self._movie_library.append(movie)
        movie = Movie("Stargate", 1994, "sci-fi", 128, "Oniel")
        self._movie_library.append(movie)

    # vypis
    def print(self):
        print("| {:20} | {:4} | {:6} | {:3} | {:10} |".format(
            "Title",
            "Year",
            "Genre"
            "Time",
            "Director"
        ))

        for i in self._movie_library:
            i.print()

    # Pridanie filmu do databazy
    def addMovie(self):
        title = input("Enter the title of a movie: ")

        # Input pre rok
        while True:
            try:
                year = int(input("Enter the release year: "))
            except ValueError:
                print("Please enter valid year in range 1900-2023.")
                continue
            if 1900 <= year <= 2023:
                print("The entered year of movie {0} has been accepted.".format(year))
                break
            else:
                print("The release year of film must be in range 1900-2023.")

        # Input pre zaner
        while True:
            try:
                genre = str(input("Enter the genre of a film: "))
            except ValueError:
                print("Please enter valid genre of the film containing 4-20 characters.")
                continue
            if genre.isnumeric() == False and 4 <= len(genre) <= 20:
                print("The entered genre of movie {0} has been accepted.".format(genre))
                break
            else:
                print("The genre of film must contain 4-20 characters.")

        # Input pre dlzku filmu
        while True:
            try:
                duration = int(input("Enter the duration of a film in minutes: "))
            except ValueError:
                print("Please enter valid duration of a movie in minutes in range 10-600.")
                continue
            if 10 <= duration <= 600:
                print("The entered duration of movie {0} has been accepted.".format(duration))
                break
            else:
                print("The duration of film must be in minutes in range of 10-600.")

        # Input pre meno rezisera
        while True:
            try:
                director = str(input("Enter the surname of film's a director: "))
            except ValueError:
                print("Please enter valid surname of film's a director containing 2-20 characters.")
                continue
            if director.isnumeric() == False and 2 <= len(director) <= 20:
                print("The entered surname of film's a director {0} has been accepted.".format(director))
                break
            else:
                print("The surname of a director must contain 2-20 characters.")

        # po dokonceni cyklu zapis
        self._movie_library.append(Movie(title, year, genre, duration, director))

    # Vyhladanie filmu v databaze podla nazvu
    def findMovie(self, title):
        for i in self._movie_library:
            if i._title == title:
                return i
        return None

    # Vymazanie filmu z databazy
    def deleteMovie(self):
        self.print()
        print()
        title = input("Enter the title of a film you want to remove: ")
        movie = self.findMovie(title)
        if movie is None:
            print("Movie with title {} was not found in the library.".format(title))
            return

        self._movie_library.remove(movie)
        print("Movie with title {} was removed successfully.".format(title))

    # Hlavne menu
    def menu(self):
        print("0 - Add movie")
        print("1 - Remove movie")
        print("2 - Print Library")
        print("3 - Save Library")
        print("q - Exit")
        print()

        choice = input("Select an option (0-3,g): ")
        if choice == "0":
            self.addMovie()
        if choice == "1":
            self.deleteMovie()
        if choice == "2":
            self.print()
        if choice == "3":
            self.saveMovieLibrary()
        else:
            exit()

    # Banner
    def banner(self):
        print("Movie Library, version 0.1a1")
        print()

    # Ulozenie kniznice
    def saveMovieLibrary(self):
        subor = open('movie_library.txt', 'w')
        subor.write("| {:20} | {:4} | {:6} | {:3} | {:10} |".format(
            "Title",
            "Year",
            "Genre"
            "Time",
            "Director"
        ))

        for i in self._movie_library:
            subor.write("\n| {:20} | {:4} | {:6} | {:3}m | {:10} |".format(
                i._title,
                str(i._year),
                i._genre,
                str(i._duration),
                i._director
            ))

        subor.close()


# Main metoda
if __name__ == "__main__":
    library = Library()
    library.seed()

    library.banner()
    while True:
        library.menu()
