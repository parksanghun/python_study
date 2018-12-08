password = '20sk'
print(password)

if len(password) < 5:
    print('5자 이상 입력하세요.')
else:
    print('정상 처리되었습니다')

hello = '안녕하세요'

length = len(hello)
print(len(hello.encode('utf-8')))


hello = 'Hello, '
world = 'world!'
print(hello + world)

print(hello * 2)

hello = 'hello '
print(hello * 0)
print(hello * 3.5)

print('Hello ' + str(3))

print('hello,' + 10)

testList = list(i for i in range(10))
print(testList[0])
print(testList[1])
print(testList[2])
print(testList[9])
print(testList[10])

