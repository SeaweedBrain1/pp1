def f(t,c,n):
    for char in t:
        if t.count(c) == n:
            result = True
        else:
            result = False
    return result
print(f("abc","b",1))
print(f("xxaxxbxx","x",6))
print(f("qwerty","b",0))
print(f("abcdef","b",2))
print(f("book","o",1))

