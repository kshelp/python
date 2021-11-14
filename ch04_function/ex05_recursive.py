# 재귀적 함수 호출

def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)

print(factorial(3)) # 6
print(factorial(4)) # 24


def hanoi(ndisks, startPeg=1, endPeg=3):
    if ndisks:
        hanoi(ndisks-1, startPeg, 6-startPeg-endPeg)
        print(startPeg, "번 기둥의", ndisks, "번 원반을", endPeg, "번 기둥에 옮깁니다.")
        hanoi(ndisks-1, 6-startPeg-endPeg, endPeg)

hanoi(ndisks=6)