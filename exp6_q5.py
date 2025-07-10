n = int(input())
movies = {}
for _ in range(n):
    name = input()
    year = int(input())
    director = input()
    production_cost = float(input())
    collection = float(input())
    movies[name] = {
        "year": year,
        "director": director,
        "production_cost": production_cost,
        "collection": collection
    }

for movie in movies:
    print(movie, movies[movie])

for movie in movies:
    if movies[movie]["year"] < 2015:
        print(movie)

for movie in movies:
    if movies[movie]["collection"] > movies[movie]["production_cost"]:
        print(movie)

director_name = input()
for movie in movies:
    if movies[movie]["director"] == director_name:
        print(movie)
