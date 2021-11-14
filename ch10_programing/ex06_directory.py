#-*- coding:utf-8 -*-

# 하위 디렉터리 검색하여 확장자가 .py인 파일만을 출력하기
import os

def search(dirname):
    try:
        # os.listdir는 해당 디렉토리에 있는 파일들의 리스트를 구한다.
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)  # 재귀함수 수행
            else:
                ext = os.path.splitext(full_filename)[-1] # 확장자만 추출한다.
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass


search("C:/Program Files/Intel")