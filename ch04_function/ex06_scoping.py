# 함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)  # 1


# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용하기
a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a) # 2

# 2. global 명령어 사용하기
a = 1
def vartest():
    global a
    a = a + 1

vartest()
print(a)  # 2