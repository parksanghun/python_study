# for 루프를 활용한 36개월 적금 프로그램
balance = 0
for month in range(1, 37):
    balance = balance + 30000
    print(month, "개월 입금, 현재 금액: ", balance, "원")
print("총 적금액:", balance)