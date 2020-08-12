from datetime import datetime
from functools import wraps

def show_timestamp(my_func):

    @wraps(my_func)
    def replacement(*args, **kwargs):
        print(datetime.now().ctime())
        return my_func(*args, **kwargs)

    return replacement

@show_timestamp
def ham():
    print("Hello from ham()")

@show_timestamp
def toast():
    print("Hello from toast()")

@show_timestamp  # decorator
def barf(a, b, **config):
    print(a, b, config)

# barf = show_timestamp(barf)
barf(5, 10, file="barf.txt", country="Lithuania")
print("Name of barf function:", barf.__name__)
# ham = show_timestamp(ham)
ham()

# toast = show_timestamp(toast)
toast()
