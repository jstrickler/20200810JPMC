
def my_coroutine():
    in_value = 'WOMBAT'
    while True:
        in_value = yield in_value.upper()
        # print("in coroutine function: in_value is", in_value)

m = my_coroutine()
print(m)
print(next(m))
result = m.send('whoopee')
print(result)

result = m.send('kangaroo')
print(result)
