movie_titles = ['Iron Man', 'Iron Man 2', 'Iron Man 3', 'Cars', 'How to Train Your Dragon']
file = open("movies.txt", 'w')
for n in movie_titles:
    file.write(n + "\n")
file.close()