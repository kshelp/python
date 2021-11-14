#-*- coding:utf-8 -*-

class Family:
    lastname = "김"  # 클래스 변수
    
    
print(Family.lastname) # 김

a = Family()
b = Family()
print(a.lastname) # 김
print(b.lastname) # 김

Family.lastname = "박"
b.lastname = "이"
print(a.lastname) # 박
print(b.lastname) # 박

# id 함수는 객체의 주소값를 바탕으로 계산된 정수값이다.
print(id(Family.lastname))
print(id(a.lastname))
print(id(b.lastname))
'''
1248765563808
1248765563808
1248765563808
'''
