# IDE(Integrated Development Environment): PyCharm, Eclipse

# 파이썬 함수의 구조
def sum(a, b):
    return a + b

a = 3
b = 4
c = sum(a, b)
print(c)


# 함수의 인자
# 기본 인자 값
print('-'*20)
def Times(a=10, b=20):
    return a*b

print(Times())
# 200

print(Times(5)) #a에만 5가 할당된다.
# 100
print(Times(b=5)) #a에만 5가 할당된다.
# 50

def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." %name)
    print("나이는 %d살입니다." %old)
    if man:
        print("남자입니다.")
        #return "남자입니다."
    else:
        print("여자입니다.")

say_myself("박응용", 27)
'''
나의 이름은 박응용입니다.
나이는 27살입니다.
남자입니다.
'''

say_myself("박응용",27,False)
'''
나의 이름은 박응용입니다.
나이는 27살입니다.
여자입니다.
'''

# 인자 전달 방식
a = 10
b = 20
def sum1(x, y):
    return x + y

print(sum1(a, b))  # 변수를 인자로 사용한다.
# 30


# 함수 안에서 선언된 변수의 효력 범위
x = 10
def sum2(x, y):
    x = 1
    return x + y

print(sum2(x, b))  # x=10, b=20
# 21


# 함수 안에서 함수 밖의 변수를 변경하는 방법
a = 1
def vartest():
    global a
    a = 0
    a = a + 2

vartest()
print("a =",a)
# a = 2


# 키워드 인자
def connectURI(server, port):
    str = "http://" + server + ":" + port
    return str

print(connectURI("test.com", "8080"))  # http://test.com:8080
print(connectURI(port="8080", server="test.com"))  # http://test.com:8080


# 가변 인자 리스트
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

result = sum_many(1,2,3,4,5,6)
print("result =",result)  # result = 21'


# 정의되지 않은 인자 처리하기
def userURIBuilder(server, port, **user):
    str = "http://" + server + ":" + port + "/?"
    for key in user.keys(): # user = {id:'userid', password='1234'}
        str += key + "=" + user[key] + "&"
    return str

print(userURIBuilder("test.com","8080",id='userid',password='1234'))
# http://test.com:8080/?id=userid&password=1234&

