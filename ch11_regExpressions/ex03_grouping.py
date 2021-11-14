#-*- coding: utf-8 -*-

import re

# ABC라는 문자열이 계속에서 반복되는지 조사하는 정규식
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
# <re.Match object; span=(0, 9), match='ABCABCABC'>
print(m.group(0)) # group(0)는 매치된 전체 문자열
#ABCABCABC

p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(1)) # group(1)는 첫 번째 그룹에 해당되는 문자열
# park
print(m.group(2)) # group(2)는 두 번째 그룹에 해당되는 문자열
# 010-1234-1234
print(m.group(3)) # group(3)는 국번 부분을 그룹핑한 것이다.
# 010
