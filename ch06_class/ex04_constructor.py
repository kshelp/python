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
    
#a = FourCal()
#a.add()
# AttributeError: 'FourCal' object has no attribute 'first'

a = FourCal(4, 2)
print(a.first)
print(a.add())

b = FourCal()




