a = (10, 20, 30, 40, 50)
b = a.index(30)
print(b)

c = a.count(10)
print(c)

print(min(a))
print(max(a))

a = a * 3
print(a)

# tutle은 수정 안됨 -> TypeError: 'tuple' object does not support item assignment
try:
    a[0] = 20
except:
    print('ERROR', a)

a = tuple(i for i in range(10) if i % 2 == 0)
print(a)

a = (1.2, 2.5, 3.7, 4.6)
a = tuple(map(int, a))
print(a)