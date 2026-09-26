"""
Midterm Practical Exam — Movie Collection Manager
Student: Erik John D. Manarang
"""
 
movies = []
 
 
def display_menu():
    print(" Movie Collection Manager ")
    print("1. Add a Movie")
    print("2. View all movies")
    print("3. Count watched vs unwatched")
    print("4. Find a movie")
    print("5. Exit")
    return input("Choose an option: ")
 
 
def add_movie(movie_list):
    added_movie = input("Enter Movie Title:")
    added_director = input("Enter Director:")
    movie_status = input("Status (Watched/Unwatched): ").strip().capitalize()
 
    movie = f"{added_movie} | Director: {added_director} | Status: {movie_status}"
    movie_list.append(movie)
    print("Movie added successfully.")
 
 
def view_movies(movie_list):
    if not movie_list:
        print("No movies in the collection")
        return
 
    for number, movie in enumerate(movie_list, start=1):
        print(f"{number}. {movie}")
 
 
def count_watched_unwatched(movie_list):
    watched = sum("status:watched" in movie.lower() for movie in movie_list)
    unwatched = sum("status:unwatched" in movie.lower() for movie in movie_list)
    print(f"Watched: {watched}")
    print(f"Unwatched: {unwatched}")
    return watched, unwatched
 
 
def find_movie(movie_list):
    movie_title = input("Enter movie title:").strip().lower()
 
    for movie in movie_list:
        title = movie.split(" | ", 1)[0].lower()
        if title == movie_title:
            print(movie)
            return movie
 
    print("Movie not found!.")
    return
 
def main():
    
 
 
main()
 