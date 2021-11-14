class MaxLimitCalculator:
    # 생성자
    def __init__(self):
        self.value = 10    # 객체변수 value
    # 메소드(함수)
    def add(self, val):
        self.value += val
        # 코드 입력
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(30)
print(cal.value)
# 100
