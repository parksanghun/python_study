def not_ten(a):
    """ 이 함수는 10을 제외한 값만 허용하는 함수입니다. """
    if a == 10:
        return
    print(a, '입니다.', sep='')


not_ten(5)
not_ten(10)
help(not_ten)

def add_sub(a, b):
    return a + b, a- b

print(add_sub(10, 20))

x, y = add_sub(10, 20)
print(x)
print(y)

def divide_mod(a, b):
    return a/b , a%b

a,b = divide_mod(10, 3)
print(a)
print(b)
