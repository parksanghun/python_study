sec = int(input("시간을 초 단위로 입력하세요: "))
minute = sec // 60
second = sec % 60
hour = minute // 60
minute = minute % 60
print(sec, "초는", hour, "시간", minute, "분", second, "초입니다.")