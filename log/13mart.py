def first(sel):
    for i in sel:
        x = list(filter(lambda x: x % 2 != 0, sel))
    a = list(map(lambda l: l , x))
    return a
print(first([1,2,3,4,5,6,7]))









