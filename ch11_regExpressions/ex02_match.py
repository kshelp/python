#-*- coding: utf-8 -*-

import re
p = re.compile('[a-z]+')

# match 객체의 메서드
m = p.match("python")
print(m.group())  # 매치된 문자열을 리턴한다.
# 'python'

print(m.start())  # 매치된 문자열의 시작 위치를 리턴한다.
# 0

print(m.end())  # 매치된 문자열의 끝 위치를 리턴한다.
# 6

print(m.span())  # 매치된 문자열의 (시작,끝)에 해당되는 튜플을 리턴한다.
# (0, 6)


# search 객체의 메서드
m = p.search("3 python")
print(m.group())  # 매치된 문자열을 리턴한다.
# 'python'

print(m.start())  # 매치된 문자열의 시작 위치를 리턴한다.
# 2

print(m.end())  # 매치된 문자열의 끝 위치를 리턴한다.
# 8

print(m.span()) # 매치된 문자열의 (시작,끝)에 해당되는 튜플을 리턴한다.
# (2, 8)