# str(object)는 문자열 형태로 객체를 변환하여 리턴하는 함수이다.
print(str(3))  # 3 -> '3'
print(int('3'))  # '3' -> 3
print(str('hi').upper())  # 'hi' -> 'HI'

print(dir(str))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# capitalize(): 첫 문자를 대문자로, 나머지 문자를 소문자로 바꿔준다.
print("PYTHON".capitalize())  # Python
print("python is powerful".capitalize())  # Python is powerful

# count(keyword,[start,[end]]): keyword가 몇 번이나 포함돼 있는지 알려준다.
print("python is powerful".count('p'))  # 2
print("python is powerful".count('p', 5))  # [5:]으로 슬라이싱하고 count한 결과와 동일
print("python is powerful".count('p', 0, -1))  # [0:-1]으로 슬라이싱하고 count한 결과와 동일

# encode([encoding,[errors]]): encode()를 거치면 인코딩이 있는 바이너리로 변환된다.
print('가나다'.encode('cp949'))  # b'\xb0\xa1\xb3\xaa\xb4\xd9'
print('가나다'.encode('utf-8'))  # b'\xea\xb0\x80\xeb\x82\x98\xeb\x8b\xa4'

# endswith(postfix,[start,[end]): postfix로 문자열이 끝나면 True를 반환하고 그 밖의 경우에는 False로 반환한다.
print("python is powerful".endswith('ful'))  # True
print("python is powerful".endswith('ful', 5))  # True
print("python is powerful".endswith('ful', 5, -1))  # False
