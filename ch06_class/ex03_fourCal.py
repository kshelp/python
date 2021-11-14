#-*- coding:utf-8 -*-

# Ctrl + D: 한줄을 삭제하는 hot-key
# Ctrl + F11: 코드를 실행시키는 hot-key
# 클래스 구조 만들기
class FourCal:
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

a = FourCal()  # 클래스에서 객체를 생성한다.
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 8)
print(a.first)
# 4
print(a.second)
# 2
print(a.add())
# 6
print(a.mul()) # 4*2=8
print(a.sub()) # 4-2=2
print(a.div()) # 4/2=2.0

print(b.add()) # 3+8=11






