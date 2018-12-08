# -*- coding: utf-8 -*-

class Account():
    # 객체 초기화
    def __init__(self, name, ini_bal):
        self.owner = name
        self.balance = ini_bal

    # 입금 메소드
    def deposit(self, amount):
        self.balance = self.balance + amount

    # 잔액 출력
    def printbal(self):
        print(self.balance)

    # 계좌 정보 출력
    def print_acc(self):
        print('''Account owner: %s Account balance: %s''' % (self.owner, self.balance))