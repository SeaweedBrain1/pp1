def f(string): 
    for i in range(0, len(string)):
        left = string[i]
        right = string[len(string)-i-1]
        if right != left:
            return(False)
    return True

print(f("12-11-21"))
print(f(""))