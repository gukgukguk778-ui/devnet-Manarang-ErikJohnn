"""
Midterm Practical Exam — Movie Collection Manager
Student: Erik John D. Manarang
"""

movies = []


def display_menu():
    print("Enter movie title:")
    movie_title = input()
    print(f"movie added successfully.")
    
    view_movies = ["inception - Pecson bryan - watch", "Interstellar - pecson bryan - Unwatched", "The Matrix - Cruz Andrei - Watched"  ]
    for x in view_movies:
      print(x)
    # return the user's choice
    
    pass


def add_movie(movie_list):
   print("Enter movie title:")
    movie_title = input()
   print(f"movie added successfully.")
    pass


def view_movies(movie_list):
    view_movies = ["inception - Pecson bryan - watch", "Interstellar - pecson bryan - Unwatched", "The Matrix - Cruz Andrei - Watched"  ]
    for x in view_movies:
      print(x)
    pass


def count_watched_unwatched(movie_list):
    # loop through the list
    # count Watched vs Unwatched
    # return both counts
    pass


def find_movie(movie_list):
    # ask for a movie title
    # search the list
    # search should be case-insensitive
    # print the result or "Movie not found."
    pass


def main():
    # create the main menu loop
    # call the appropriate function based on the user's choice
    pass


main()
