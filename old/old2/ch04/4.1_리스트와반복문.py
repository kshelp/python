# 리스트는 어떻게 만들고 사용할까?

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

# 리스트의 인덱싱과 슬라이싱
# 리스트의 인덱싱
a = [1, 2, 3]
print(a)
# [1, 2, 3]
print(a[0])
#1
print(a[0] + a[2])
#4
print(a[-1])
#3
a = [1,2,3,['a','b','c']]
print(a[0])
#1
print(a[-1])
#['a','b','c']
print(a[3])
#['a','b','c']
print(a[-1][0])
#'a'

# 리스트의 슬라이싱
a = [1,2,3,4,5]
print(a[0:2])
#[1,2]
b = a[:2]
c = a[2:]
print(b)
#[1,2]
print(c) 
#[3,4,5]
a = "12345"
print(a[0:2])
#'12'

# 리스트 연산자
a = [1,2,3]
b = [4,5,6]
print(a+b)
print(a*3)
a[2]=4
print(a)
a[1:2] = ['a','b','c']
print(a)
a[1:3] = []
print(a)
#[1,'c',4]
del a[1]
print(a)
#[1,4]

a = [1, 2, 3]
a[2] + "h1"  # 형 오류(TypeError)가 발생한다. 
str(a[2]) + "hi"  # str()은 정수나 실수를 문자열의 형태로 바꾸어 주는 파이썬의 내장 함수이다.

# 리스트 관련 함수들
a = [1,2,3]
a.append(4)
print(a)
#[1,2,3,4]
a.append([5,6])
print(a)

a = [1,2,3]
a.extend([4,5])
print(a)
b = [6,7]
a.extend(b)
print(a)

a = [1,4,3,2]
a.sort()
print(a)
a = ['a','c','b']
a.sort()
print(a)
a = [1,2,3,1]
print(a.count(1))
#2
