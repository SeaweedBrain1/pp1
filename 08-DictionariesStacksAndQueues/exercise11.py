import json
movie = {
    "title":"film",
    "year":"1991",
    "actor":{"leading":"Jo Jo","supporting":"No No"},
    "oscar":False,
    "length":"2min",
    "good":"yes",
    "interesting":"yes"
}

file = open("favourite.json", "w") 
  
json.dump(movie, file, indent = 6) 
  
file.close()
