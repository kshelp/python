#-*- coding:utf-8 -*-

# 내장함수
# abs(x)는 절대값을 돌려주는 함수
print(abs(3))
print(abs(-3))
print(abs(-1.2))

# all은 반복 가능한 자료형을 입력받아 그 값이 모두 참이면 True
print(all([1,2,-3])) # True
print(all([1,2,0]))  # False

# any는 하나라도 참이 있을 경우 True, 모두 거짓일 경우 False
print(any([1,2,0])) # True
print(any([0,'']))  # False

# chr(i)는 i에 영문자 코드(아스키 코드)값을 입력으로 받아 그
# 코드에 해당하는 문자를 출력하는 함수이다.
print(chr(97)) # 'a'
print(chr(65)) # 'A'
print(chr(44032)) # '가',  유니코드 값(44032) = '가'

# dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.
print(dir([1,2,3])) # 리스트 객체
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
print(dir({'1':'a'})) # 딕셔러리 객체
# ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

# divmod은 몫과 나머지를 튜플 형태로 리턴하는 함수이다.
print(divmod(7,3))
# (2, 1)
print(7/3)
print(int(7/3)) # 몫
print(7%3)      # 나머지

# enumerate 함수는 순서가 있는 자료형(리스트,튜플,문자열)을 입력을 받아
# 인덱스 값을 포함하는 enumerate 객체로 리턴한다.
i = 0
for name in ['body', 'foo', 'bar']:
    i += 1  # i = i + 1
    print(i-1, name)
'''
0 body
1 foo
2 bar
'''

for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
'''
0 body
1 foo
2 bar
'''

# eval(expression)은 실행 가능한 문자열을 입력으로 받아 
# 문자열을 실행한 결과값으로 리턴하는 함수이다.
print("1+2")       # '1+2'
print(eval("1+2")) # '3'

print("'hi'+'a'")       # 'hi'+'a'
print(eval("'hi'+'a'")) # 'hia'

print('divmod(4,3)')       # divmod(4,3)
print(eval('divmod(4,3)')) # (1, 1)

# filter 함수는 첫번째 인수로 함수이름을, 두번째 인수로 그 함수에 차례로
# 들어갈 반복 가능한 자료형을 받느다.
def positive(l):  # l = [1,-2,-3,4,-5]
    result = []  # 리스트 result = [1,4]
    for i in l:
        if i>0:
            result.append(i)
    return result

print(positive([1,-2,-3,4,-5]))
# [1, 4]


def positive1(x):
    return x > 0  # True or False

print(list(filter(positive1, [1,-2,-3,4,-5])))
# [1, 4]

print(list(filter(lambda x: x>0, [1,-2,-3,4,-5]))) # lambda는 익명함수를 만드는 식.
# [1, 4]


# hex(x)는 정수값을 입력받아 16진수(hexadecimal)로 변환하여 리턴하는 함수
print(hex(234))
# 0xea
print(hex(16))
# 0x10
print(hex(3))
# 0x3


# id(object)는 객체를 입력받아 객체의 고유 주소값을 리턴하는 함수이다.
a = 3
print(id(3))
# 140709019300752
print(id(a))
# 140709019300752


# input() 사용자 입력을 받은 함수이다.
#a = input("값을 입력하세요. ")
#print(a)


# int()는 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 
# 리턴하는 함수이다.
int('3')  # 문자열('3') -> 숫자(3)
print(int(3.4))  # 실수형(3.4) -> 정수형(3)


# Q4
# [1,-2,3,-5,8,-3] -> [1,3,8]
print(list(filter(lambda x: x>0, [1,-2,3,-5,8,-3])))
# [1, 3, 8]

# isinstance()
class Person:
    pass
a = Person()  # 객체를 생성하여 변수 a에 저장
print(isinstance(a, Person))
# True
b = 3
print(isinstance(b, Person))
# False


# len(s)은 입력값 s의 길이를 리턴하는 함수이다.
print(len("Python"))
# 6
print(len([1,2,3]))
# 3
print(len([1,'a']))
# 2


# list(s)는 반복 가능한 자료형 s를 입력받아 리스트로 만들어 리턴하는 함수
print(list("Python"))  # 문자형 -> 리스터형
# ['P', 'y', 't', 'h', 'o', 'n']


# map(f,iterable)은 함수(f)와 반복가능한(iterable) 자료형을 입력으로 받는다.
def two_times(numberList):  # [1,2,3,4]
    result = []  # [2,4,9,16]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)
# [2, 4, 6, 8]


def two_times1(x):
    return x*2

print(list(map(two_times1, [1,2,3,4])))
# [2, 4, 6, 8]

print(list(map(lambda x:x*2, [1,2,3,4])))
# [2, 4, 6, 8]

print(max([1,2,3]))
# 3
print(min([1,2,3]))
# 1

# oct는 8진수로 리턴하는 함수이다.
print(oct(34))
# 0o42
print(oct(8))
# 0o10

# open
f = open("binary_file", 'wb')


# ord(c)는 문자의 아스키 코드값을 리턴하는 함수이다.
print(ord('a'))  # 97
print(chr(97))   # 'a'


# pow(x,y)는 x의 y제곱한 결과값을 리턴하는 함수이다.
print(pow(2,4))
# 16  


# range([start], stop [, step])는 for문과 함께 자주 사용되는 함수이다.
print(list(range(5))) # 0~4
# [0, 1, 2, 3, 4]

print(list(range(5,10)))  # 5~9
# [5, 6, 7, 8, 9]

print(list(range(1,10,2)))  # 1~9, step=2
# [1, 3, 5, 7, 9]


# round는 숫자를 입력받아 반올림해 주는 함수이다.
print(round(4.6))
# 5
print(round(4.2))
# 4
print(round(5.678, 2))
# 5.68


# sorted(iterable) 함수는 입력값을 정렬한 후 그 결과를 리턴한다.
# sorted() vs. list.sort()
# sorted(): 정렬후에 값을 리스트로 리턴한다.
# list.sort(): 리스트를 정렬만 한다.
a = [3,1,2]
print(sorted(a))
# [1, 2, 3]
print(a.sort())
# None
print(a)
# [1, 2, 3]

print(sorted("zero"))  # 문자열('zero') -> 리스트
# ['e', 'o', 'r', 'z']


# str(object)는 문자열 형태로 객체를 변환하여 리턴하는 함수이다.
print(str(3))   # 3 -> '3'
print(int('3')) # '3' -> 3
print(str('hi').upper())  # 'hi' -> 'HI'

# sum
print(sum([1,2,3,4]))


# tuple(iterable)은 반복가능한 자료형을 입력받아 튜플형으로 변환한다.
print(tuple("abc"))
# ('a', 'b', 'c')
print(tuple([1,2,3]))
# (1, 2, 3)


# type(object)은 입력값의 자료형이 무엇인지 알려주는 함수이다.
print(type("abc"))
# <class 'str'>
print(type([]))
# <class 'list'>
print(type(3))
# <class 'int'>
f = open("binary_file", "wb")
print(type(f))
# <class '_io.BufferedWriter'>


# zip(iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 한다.
print(list(zip([1,2,3], [4,5,6,7])))
# [(1, 4), (2, 5), (3, 6)]
print(list(zip([1,2,3],[4,5,6],[7,8,9])))
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
