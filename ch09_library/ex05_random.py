
# 임의의 실수 생성
import random
print(random.random())  # 함수를 호출할 때마다 다른 값이 반환된다.
print(random.random())
print(random.uniform(3,4))  # 입력받은 두 값 사이의 float 값을 임의로 생성한다.

# 임의의 정수 생성
# random.randrange(20)은 0~20 사이의 수 중 중복을 허용한 임의의 정수를 생성한다.
r = [random.randrange(20) for i in range(10)]
print(r)
#[3, 11, 18, 13, 3, 18, 5, 1, 0, 2]

# random.sample(은 중복을 허용하지 않는다.
r = random.sample(range(20), 10)
print(r)
# [10, 12, 1, 8, 7, 11, 14, 9, 5, 15]

# 0~20 사이의 수 중 3의 배수만 출력한다.
r = [random.randrange(0, 20, 3) for i in range(5)]
print(r)
# [12, 0, 12, 6, 18]

# 시퀀스 객체 관련 연산
l = list(range(10))
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c = [random.choice(l) for i in range(3)]  # 중복 선택 가능
print(c)
# [6, 6, 9]
c = random.sample(l,3)  # 중복을 허용하지 않는다.
print(c)

print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(l)  # 시퀀스 객체를 임의로 섞는다.
print(l)
# [9, 6, 5, 0, 2, 4, 3, 8, 1, 7]

# 원본 객체를 변경하지 않고 원본 객체가 임의로 섞인 또 다른 객체를 얻는다.
l = list(range(10))
s = random.sample(l, 10)
print(s)
print(l)
