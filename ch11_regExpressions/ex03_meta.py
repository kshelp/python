#-*- coding: utf-8 -*-
import re

# | 메타 문자는 or과 동일한 의미로 사용된다.
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)
print(m.group())
# <re.Match object; span=(0, 4), match='Crow'>
# Crow

# ^ 메타 문자는 문자열의 맨 처음과 일치함을 의미한다.
print(re.search('^Life', 'Life is too short'))
print(re.search('^Life', 'My Life'))
# <re.Match object; span=(0, 4), match='Life'>
# None

# $ 메타 문자는 ^ 메타 문자와 반대의 경우이다. 즉, $는 문자열의 끝과 매치함을 의미한다.
print(re.search('short$', 'Life is too short'))
print(re.search('short$', 'Life is too short, you need python'))
# <re.Match object; span=(12, 17), match='short'>
# None

# \b는 단어 구분자(word boundary)이다. 보통 단어는 whitespace에 의해 구분이 된다.
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
# <re.Match object; span=(3, 8), match='class'>
# None

# \B 메타 문자는 \b 메타 문자와 반대의 경우이다. 즉, whitespace로 구분된 단어가 아닌 경우에만 매치된다.
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))
# None
print(p.search('the declassified algorithm'))
# <re.Match object; span=(6, 11), match='class'>
print(p.search('one subclass is'))
# None