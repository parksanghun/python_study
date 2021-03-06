# Hello, World! 출력
print('Hello, world!')
print("Hello, world!")
print('12345X7890')


"""
여러줄 주석
"""
print("hello")

'''
여러줄 주석
'''
print("hello")

# 수학 = 기호는 같다, 프로그램에서는 = 대입연산자
# 좌변 = 우변 : 우선순위 때문에 우변의 값, 변수, 수식이 먼저 연산 후 좌변(변수만) 대입됨 ex) a = 1 + 2
# 프로그램에서 같다는 어떻게 표현할까요? == 동등 연산자
a = 1 + 2

if a == 10:
    # 파이썬에서는 같은 레벨일 때 들여쓰기가 같아야 한다.
    print('10입니다.')
    print('입니다.')

print('밖의 print 구문')

# 2진수 Binary
print(0b110)
# 8진수 Octa
print(0o10)
# 16진수 Hexa
print(0xF)

# 10진수 -> 2진수 변환 : 10진수 숫자를 2로 나눈 나머지를 역순으로 읽어 2진수를 만듬 ex) 10(10진수) -> 1010(2진수)
# 2진수 -> 10진수 변환 : 2진수 자리수를 승수로 더한 결과 ex) 1010(2진수) -> 1x2의 3승 + 0x2의 2승 + 1x2의 1승 + 0x2의 0승(10진수)
# 2진수 -> 16진수 변환 : 2진수 4자리를 통합 16진수가 됨 ex) 10101010 -> AA(16진수)
# 16진수 -> 2진수 변환 : 16진수 4자리를 통합 2진수가 됨 ex) AA(16진수) -> 자리 수별로 10진수로 변환후 2로 나눈 나머지를 역순으로 읽어 2진수를 만듬

# 실수끼리 - 연산시에는 정확한 값이 출력되지 않기 때문에 == 연산자는 사용하지 않음
if(4.3-2.7) == 1.6:
    print("정상입니다")
else:
    print("비정상입니다.")

print(225 + 0.6 * 102)

x, y, z = 10, 20, 30
print(x, y, z)

x, y, z = 10.0, 20, 30.0
print(x, y, z)

x = 10
del x
print(x)

# c, java 에서는 선언구문으로만 사용 가능하지만 python에서는 변수의 선언만 하는 구문은 error 발생
x

박상훈 = 최광훈 = 500
print(박상훈)
print(최광훈)

x = 10
y = x
print(y)

x, y = 10, 20
x, y = y, x
print(x, y)

# 주석의 내용이 길어지면 다음줄에 연결 -> 역슬래쉬를 사용
hello = \
    ''' 
안녕하세요.
반갑습니다.
저는 박상훈입니다. 
    '''

print(hello)

