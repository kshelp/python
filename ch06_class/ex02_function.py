#-*- coding:utf-8 -*-

result = 0  # 3 + 4 + 3 =10
result2 = 0 # 3 + 7 + 4 = 14
result3 = 0

# add 함수를 정의한다.
def add(num):
    global result
    result += num  # result = result + num
    return result 
def sub(num):
    global result 
    result -= num
    return result 

print(add(3))  # add 함수를 실행한다.
print(add(4))
print(sub(2))  # 5

def add2(num):
    global result2
    result2 += num 
    return result2 
def sub2(num):
    global result2 
    result2 -= num
    return result2 

print(add2(3))
print(add2(7))
print(sub2(2))

def add3(num):
    global result3
    result3 += num 
    return result3 
print(add3(4))
print(add3(2))
