import time

# 변수를 선언합니다.
counter = 0

def fibonacci2(n):
    # 피보나치 수를 구합니다.
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 함수를 선언합니다.
def fibonacci(n):
    # 어떤 피보나치 수를 구하는지 출력합니다.
    #print("fibonacci({})를 구합니다.".format(n))
    global counter
    counter += 1
    # 피보나치 수를 구합니다.
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 함수를 호출합니다.
st = time.time()
fibonacci(30)
et = time.time()
print(et-st)
print()

st = time.time()
fibonacci2(30)
et = time.time()
print(et-st)
