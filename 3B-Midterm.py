"""
Midterm Practical Exam — Movie Collection Manager
Student: Erik John D. Manarang
"""

movies = []


def display_menu():
    print (f"Add a movie")
    print (f"View all Movies")
    print (f"count watched vs unwatched")
    print (f"find a movie")
    print (f"Exit")
     menu = print(input"choose an option:")
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
    watch = 1
    unwatched = 0

    if watch > unwatched:
        print("Nothing Watch")
    elif watch == unwatched:
        print ("watched")    
    pass


def find_movie(movie_list):
    # ask for a movie title
    # search the list
    # search should be case-insensitive
    # print the result or "Movie not found."
    pass


def main():
    print (f"Add a movie")
    print (f"View all Movies")
    print (f"count watched vs unwatched")
    print (f"find a movie")
    print (f"Exit")
    menu = print(input"choose an option:")
    pass


main()
