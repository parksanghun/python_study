a = input()
a = int(a)
print(a * 2)

input('문자열을 입력하세요.: ')

a = int(input('a 숫자를 입력하세요.: '))
b = int(input('b 숫자를 입력하세요.: '))

print(str(a) + str(b))

print(a * b)

strArray = input("문자열 두 개를 띄어쓰기를 사용하여 입력하세요.").split()
print(strArray)

a, b = input("문자열 두 개를 띄어쓰기를 사용하여 입력하세요.").split()
print(a)
print(b)

a = map(int, input().split())
a = list(a)

a, b, c = map(float, input().split())
print(a + b + c)

a = map(float, [1.0, 2.0])
a = list(a)
print(a)

a = map(float, [1.0])
a = list(a)
print(a)


print(1, 2, 3, sep='\n')

print(5/2)
print(5//2)
print(2 ** 10)

print(16,':',9)
print(16, 9, sep=":")
print(16, 9, end=":")

print('Hello', '\n', 'Python', sep='')
