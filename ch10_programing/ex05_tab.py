#-*- coding:utf-8 -*-

# 탭을 4개의 공백으로 바꾸기
import sys 

try:
    src = sys.argv[1]
    dst = sys.argv[2]
except:
    print("사용법: python *.py 입력파일명 출력파일명")
    sys.exit()

f = open(src, 'r')
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)

f = open(dst, 'w')
f.write(space_content)
f.close()