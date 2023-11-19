def f(n):
    string = ""
    if n == 1:
        return "*"
    else:
        for i in range(1, n):
            string += "*/"
        string += "*"
        return string
if __name__ == "__main__":
    print(f(4))
