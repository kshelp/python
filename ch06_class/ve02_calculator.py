# Calculator 클래스
class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

# 여기에 코드를 기입한다.
class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)
# 3