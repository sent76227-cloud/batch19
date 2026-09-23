from models.movie import Movie

movies = []
for _ in range(5):
    movie_id = int(input("Enter Movie ID: "))
    movie_name = input("Enter Movie Name: ")
    genre = input("Enter Genre: ")
    rating = float(input("Enter Rating: "))
    ticket_price = int(input("Enter Ticket Price: "))
    movies.append(Movie(movie_id, movie_name, genre, rating, ticket_price))

print("\nAll Movies:")
for movie in movies:
    movie.display()

print("\nMovies with rating greater than 8:")
for movie in movies:
    if movie.rating > 8:
        print(f"{movie.movie_name} {movie.rating}")

genre_name = input("\nEnter genre to filter movies: ")
print(f"{genre_name} Movies:")
for movie in movies:
    if movie.genre == genre_name:
        print(movie.movie_name)

highest_movie = max(movies, key=lambda m: m.rating)
print(f"\nHighest Rated Movie: {highest_movie.movie_name} {highest_movie.rating}")

search_id = int(input("\nSearch Movie ID: "))
found = None
for movie in movies:
    if movie.movie_id == search_id:
        found = movie
        break
if found:
    print("Movie Found:")
    found.display()
else:
    print("Movie not found")

average_rating = sum(movie.rating for movie in movies) / len(movies)
print(f"\nAverage Movie Rating: {average_rating}")

print("\nMovies with ticket price greater than 300:")
for movie in movies:
    if movie.ticket_price > 300:
        print(f"{movie.movie_name} {movie.ticket_price}")
