
class Spam:
    factor = 12

    def __call__(self):
        print("Important action...")

s = Spam()
s()

class TagWrapper:
    def __init__(self, tag):
        self._tag = tag

    def __call__(self, text):
        return "<{0}>{1}</{0}>".format(self._tag, text)

p = TagWrapper('p')
div = TagWrapper('div')
print(p('foo'))
print(div('bar'))


