#!/usr/bin/env python
#

from functools import wraps  # <1>


def multiply(multiplier): # <2>

    def deco(old_func): # <3>

        @wraps(old_func)  # <4>
        def new_func(*args, **kwargs): # <5>
            result = old_func(*args, **kwargs) # <6>
            return result * multiplier # <7>

        return new_func # <8>

    return deco # <9>



@multiply(4)
def spam():
    return 5


@multiply(10)
def ham():
    return 8

# ham = multiply(10)(ham)

a = spam()
b = ham()
print(a, b)


# @foo
# def bar():
#    pass
# SAME AS
# bar = foo(bar)

# @spam(a, b, c)
# def ham():
#    pass
# SAME AS
# ham = spam(a, b, c)(ham)
