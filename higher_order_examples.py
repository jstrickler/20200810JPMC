
def spam():
    return 1234

def callit(func):
    return func()

print(callit(spam))

print(callit(lambda : 42))

#   ......lambda x, y: x * y......

