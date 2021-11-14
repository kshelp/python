#-*- coding:utf-8 -*-

class FourCal:
    # 생성자 메서드: 1.객체를 생성한다.
    #                2.변수를 초기화한다.
    def __init__(self, first, second): # 생성자 메서드
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first   # 클래스 변수
        self.second = second # 클래스 변수
    def add(self):  # 클래스 메서드(method) = 함수(function)
        result = self.first + self.second
        return result 
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class Person:
    " 부모 클래스"
    pass

class Student(Person):
    "자식 클래스"
    pass

# issubclass() 내장함수는 상관관계 인지 파악한다.
print(issubclass(Student, Person)) # True
print(issubclass(Person, Student)) # False
print(issubclass(Person, object))  # True
print(issubclass(Student, object)) # True

class Dog:
    pass

print(issubclass(Student, Dog)) # False
print(issubclass(Dog, Person)) # False
print(issubclass(Dog, object)) # True'


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
print(a.add()) # 6
print(a.pow()) # 4^2 = 16


