import random as rd

name = '박상훈'
age = 35
print('%s는 %d세 입니다' %(name, age))

i = 0
while i != 3:
    i = rd.randint(1, 45)
    print(i)

# while not 0:
#     print('11')

i, j = 2, 5
while i < 33:
    print(i, j)
    i = i*2
    j = j-1

for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)


for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

