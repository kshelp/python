#-*- coding: utf-8 -*-

# 파이썬에서 정규 표현식을 지원하는 re 모듈
import re

# 정규식을 이용한 문자열 검색
p = re.compile('[a-z]+') # 컴파일된 패턴 객체, a~z 문자가 최소 1번 이상 반복되어야 한다.

# match: 문자열의 처음부터 정규식과 매치되는지 조사한다.
m = p.match("python")
print(m)
print(m.group())
# <re.Match object; span=(0, 6), match='python'>
# python
m = p.match("3 python")
print(m)
# None

# search: 문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
m = p.search("python")
print(m)
print(m.group())
# <re.Match object; span=(0, 6), match='python'>
# python
m = p.search("3 python")
print(m)
print(m.group())
# <re.Match object; span=(2, 8), match='python'>
# python

# findall: 정규식과 매치되는 모든 문자열을 리스트로 리턴한다.
result = p.findall("life is too short short3")
print(result)
# ['life', 'is', 'too', 'short', 'short']

# finditer: 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 리턴한다.
result = p.finditer("life is too short")
print(result)
# <callable_iterator object at 0x00000000025AABE0>



