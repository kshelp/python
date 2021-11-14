#-*- coding:utf-8 -*-

# 오류 회피하기
try:
    f = open("없는파일.txt",'r')
    
# 파일이 없더라도 오류를 발생시키지 않고 통과한다. 
except FileNotFoundError: 
    pass
