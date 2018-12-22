hello = 'Hello, World!!!'
print(hello[0])
print(hello[5])
print(hello[-1]) # 맨뒤
print(hello[len(hello) - 1])

print(hello[0:3])
print(hello[0:20])
print(hello[0:len(hello)])

print(hello.replace('World', 'Korea'))
print(hello.split())

a = ' '
print(a.join(['apple', 'pear', 'grape', 'orange']))
# 전화번호에서 응용 가능
a = '-'
print(a.join(['010', '6754', '1984']))

s = 'python'
print(s.upper())
print(s.lower())


s = '   python '
print('[' + s.lstrip() + ']')
print('[' + s.rstrip() + ']')
print('[' + s.strip() + ']')

s = ', python.'
print('[' + s.lstrip(',. ') + ']')
print('[' + s.rstrip(',. ') + ']')
print('[' + s.strip(',. ') + ']')


path = '/usr/bin/python'
x = path.split('/')
print(x)
x.reverse()
print(x)
filename = x[0]
print(filename)

print(path.rfind('/'))

print(path[path.rfind('/')+1:])

def add(a, b):
    return a + b

print(add(10, 20))
print(add.__doc__)
print(add.__name__)


word = input('단어를 입력하세요.')

is_palindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-1 - i]:
        is_palindrome = False
        break

print(is_palindrome)

def hello():
    print('Hello World')

hello()

def passTest():
    pass

passTest()