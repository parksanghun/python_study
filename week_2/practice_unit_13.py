tel_input = '010-333-4444'
spam_tel_list = ['010-123-4567', '010-222-3333']

for spam_tel in spam_tel_list:
    if tel_input == spam_tel or tel_input == spam_tel:
        print('스팸입니다')
    else:
        print('지인입니다')


writtenTest = 75
toeic = 890

if writtenTest >= 80 and toeic >= 840:
    print('success')
else:
    print('fail')

fooList = list(range(1, 11))
print(fooList)

fooList = list(range(0, 11, 2))
print(fooList)

