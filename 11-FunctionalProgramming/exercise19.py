grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
filtered = list(filter(lambda g: g>2, grades))
mean = round(sum(filtered)/len(filtered), 2)
print(mean)