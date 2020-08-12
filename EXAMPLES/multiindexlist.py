#!/usr/bin/env python


class MultiIndexList(list):  # <1>

    def __getitem__(self, selector):  # <2>
        if isinstance(selector, tuple):  # <3>
            if len(selector) == 0:
                raise ValueError("Tuple must be non-empty")
            else:
                tmp_list = []
                for index in selector:
                    tmp_list.append(
                        super().__getitem__(index)  # <4>
                    )
                return tmp_list
        else:  # integers and slices are handled by default
            return super().__getitem__(selector)  # <5>


if __name__ == '__main__':
    m = MultiIndexList(
        'banana peach nectarine fig kiwi lemon lime'.split()
    )  # <6>
    m.append('apple')  # <7>
    m.append('mango')
    print(m)

    print(m[0])  # MultiIndexList.__getitem__(m, 0)
    print(m[1])
    print(m[5, 2, 0])  # <8>  # MultiIndexList.__getitem(m, (5, 2, 0)
    print(m[:4])  # MultiIndexList.__getitem__(:4)   # slice(Null,4)
    print(len(m))
    print(m[5, ])
    print(m[:2, -2:])
    print()
    print(m)
    m.extend(['durian', 'kumquat'])
    print(m)
    print()
    for fruit in m:
        print(fruit)
    print(len(fruit))

    m[4] = "Leeloo"
    m.append("peach")
    print(m)
