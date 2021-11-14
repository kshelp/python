#-*- coding:utf-8 -*-

# 오류 일부러 발생하기
class Bird:
    def fly(self):
        raise NotImplementedError


class Eagle(Bird):
    pass


eagle = Eagle()
eagle.fly()
'''
Traceback (most recent call last):
  File "C:\Program Files\Intel\dev\workspace\foundation\ch08_errorHandler\ex04_raise.py", line 14, in <module>
    eagle.fly()
  File "C:\Program Files\Intel\dev\workspace\foundation\ch08_errorHandler\ex04_raise.py", line 6, in fly
    raise NotImplementedError
NotImplementedError
'''