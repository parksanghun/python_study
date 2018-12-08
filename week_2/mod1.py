# -*- coding: utf-8 -*-
# 평균 계산 함수
def mean(x):
    return sum(x) / len(x)

# 중간값 계산 함수
def median(x):
    n = len(x)
    x.sort()
    mid = n // 2
    if n % 2 == 1:
        return x[mid]
    else:
        low = mid - 1
        high = mid
        return (x[low] + x[high]) / 2
