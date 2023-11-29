countries = [
    {"name":"Poland", "population":38000000},
    {"name":"Germany", "population":123},
    {"name":"USA", "population":5555},
    {"name":"China", "population":476456},
    {"name":"France", "population":8957},
]
print("COUNTRY   POPULATION")
for n in countries:
    print(n['name'],(7-len(n["name"])+1)*" " ,n["population"])
