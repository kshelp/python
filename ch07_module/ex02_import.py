# import 모듈
import mod1
print("="*10)
print(mod1.add(3,4))  # 7
print(mod1.sub(4,2))  # 2

# from 모듈 이름 import 모듈 함수
from mod1 import add
print(add(4,1)) # 5
# print(sub(4,2))
# NameError: name 'sub' is not defined

from mod1 import *
print(sub(7,1)) # 6