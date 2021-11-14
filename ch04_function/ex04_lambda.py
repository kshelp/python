# 람다함수: 익명함수
g = lambda x,y : x*y
print(g(2,3))  # 6

print((lambda x,y:x*y)(2,3))  # 6

def mul(x,y): # mul 함수 정의
    return x*y

print(mul(2,3)) # 6


def sqrt(x):
    x = x*x
    return x
print(list(map(sqrt,[1,2,3,4])))  # map(함수,자료)
# [1, 4, 9, 16]
print(list(map(lambda x:x*x, [1,2,3,4])))
# [1, 4, 9, 16]

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27] # 리스트
print(list(filter(lambda x:x%3==0, foo)))
# [18, 9, 24, 12, 27]

