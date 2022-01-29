def createCounter():
    x = 0

    def counter():
        nonlocal x
        x = x+1
        return x
    return counter


f = createCounter()
print(f())
print(f())
print(f())
