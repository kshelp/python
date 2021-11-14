#-*- coding:cp949 -*-

# 외장함수
# sys 모듈은 파이썬 인터프리터가 제공하는 변수들과 함수들을
# 직접 제어할 수 있게 해주는 모듈이다.
# 명령 행에서 인수 전달하기 - sys.argv

import sys

# print(sys.argv)
# ['C:굚Program Files굚Intel굚dev굚workspace굚foundation굚ch09_library굚ex02_external.py']
# ['C:굚Program Files굚Intel굚dev굚workspace굚foundation굚ch09_library굚ex02_external.py', 'test1', 'test2']

if len(sys.argv) == 4:
    print(sys.argv)
    if sys.argv[1] == "name":
        print(sys.argv[2])
    # ['C:굚Program Files굚Intel굚dev굚workspace굚foundation굚ch09_library굚ex02_external.py', 'arg1', 'arg2', 'arg3']
    # sys.exit()  # 강제로 프로그램을 종료한다.
else: 
    print("사용법: python *.py arg1 arg2 arg3")
    
# 자신이 만들 모듈 불러와 사용하기 - sys.path
import sys
print(sys.path)
'''
['C:굚Program Files굚Intel굚dev굚workspace굚foundation굚ch09_library', 
'C:굚Program Files굚Intel굚dev굚workspace굚foundation', 
'C:굚ProgramData굚Anaconda3굚DLLs', 
'C:굚ProgramData굚Anaconda3굚lib', 
'C:굚ProgramData굚Anaconda3', 
'C:굚ProgramData굚Anaconda3굚lib굚site-packages', 
'C:굚ProgramData굚Anaconda3굚lib굚site-packages굚win32', 
'C:굚ProgramData굚Anaconda3굚lib굚site-packages굚win32굚lib', 
'C:굚ProgramData굚Anaconda3굚lib굚site-packages굚Pythonwin', 
'C:굚ProgramData굚Anaconda3굚python37.zip']
'''

sys.path.append("C:/doit/")
print(sys.path)
'''
['C:굚Program Files굚Intel굚dev굚workspace굚foundation굚ch09_library', 'C:굚Program Files굚Intel굚dev굚workspace굚foundation', 
'C:굚ProgramData굚Anaconda3굚DLLs', 
'C:굚ProgramData굚Anaconda3굚lib', 
'C:굚ProgramData굚Anaconda3', 
'C:굚ProgramData굚Anaconda3굚lib굚site-packages', 
'C:굚ProgramData굚Anaconda3굚lib굚site-packages굚win32', 
'C:굚ProgramData굚Anaconda3굚lib굚site-packages굚win32굚lib', 
'C:굚ProgramData굚Anaconda3굚lib굚site-packages굚Pythonwin', 
'C:굚ProgramData굚Anaconda3굚python37.zip', 
'C:/doit/']
'''

from mod1 import add, sub
print(add(3,4))
# 7


# pickle은 객체의 형태로 그대로 유지하면서 파일에 저장하고 불러올 수 
# 있게 하는 모듈이다.
import pickle
f = open("test.txt", "wb")
data = {1:'python', 2:'you need'}  # 딕셔너리 객체
pickle.dump(data, f)
f.close()

# 원래 있던 딕셔너리 객체 상태 그대로 불어오기
f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)
# {1: 'python', 2: 'you need'}



# OS 모듈은 환경변수나 디렉토리, 파일 등의 OS 자원을 제어할 수 있게
# 해주는 모듈이다.
# 1. os.environ는 시스템의 환경 변수 값을 알려준다.
import os
print(os.environ)  
# environ({'ALLUSERSPROFILE': 'C:굚ProgramData', 'APPDATA': 'C:굚Users굚user굚AppData굚Roaming', 'COMMONPROGRAMFILES': 'C:굚Program Files굚Common Files', 'COMMONPROGRAMFILES(X86)': 'C:굚Program Files (x86)굚Common Files', 'COMMONPROGRAMW6432': 'C:굚Program Files굚Common Files', 'COMPUTERNAME': 'LECTURER', 'COMSPEC': 'C:굚WINDOWS굚system32굚cmd.exe', 'DRIVERDATA': 'C:굚Windows굚System32굚Drivers굚DriverData', 'HOMEDRIVE': 'C:', 'HOMEPATH': '굚Users굚user', 'IDE_PROJECT_ROOTS': 'C:굚Program Files굚Intel굚dev굚workspace굚foundation', 'JAVA_HOME': 'C:굚Program Files굚Java굚jdk1.8.0_212', 'LOCALAPPDATA': 'C:굚Users굚user굚AppData굚Local', 'LOGONSERVER': '굚굚LECTURER', 'NUMBER_OF_PROCESSORS': '4', 'ONEDRIVE': 'C:굚Users굚user굚OneDrive', 'OS': 'Windows_NT', 'PATH': 'C:/Program Files/Java/jdk1.8.0_212/bin/../jre/bin/server;C:/Program Files/Java/jdk1.8.0_212/bin/../jre/bin;C:/Program Files/Java/jdk1.8.0_212/bin/../jre/lib/amd64;C:굚ProgramData굚Anaconda3;C:굚ProgramData굚Anaconda3굚Library굚mingw-w64굚bin;C:굚ProgramData굚Anaconda3굚Library굚usr굚bin;C:굚ProgramData굚Anaconda3굚Library굚bin;C:굚ProgramData굚Anaconda3굚Scripts;C:굚oraclexe굚app굚oracle굚product굚11.2.0굚server굚bin;C:굚WINDOWS굚system32;C:굚WINDOWS;C:굚WINDOWS굚System32굚Wbem;C:굚WINDOWS굚System32굚WindowsPowerShell굚v1.0굚;C:굚Program Files굚Java굚jdk1.8.0_212굚bin;C:굚Program Files굚Java굚jdk1.8.0_212굚bin;C:굚WINDOWS굚System32굚OpenSSH굚;C:굚Program Files굚Bandizip굚;C:굚Users굚user굚AppData굚Local굚Microsoft굚WindowsApps;C:굚Program Files굚Intel굚dev굚eclipse;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 94 Stepping 3, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '5e03', 'PROGRAMDATA': 'C:굚ProgramData', 'PROGRAMFILES': 'C:굚Program Files', 'PROGRAMFILES(X86)': 'C:굚Program Files (x86)', 'PROGRAMW6432': 'C:굚Program Files', 'PROMPT': '$P$G', 'PSMODULEPATH': 'C:굚WINDOWS굚system32굚WindowsPowerShell굚v1.0굚Modules굚', 'PUBLIC': 'C:굚Users굚Public', 'PYDEV_COMPLETER_PYTHONPATH': 'C:굚Program Files굚Intel굚dev굚eclipse굚plugins굚org.python.pydev.core_7.2.1.201904261721굚pysrc', 'PYDEV_CONSOLE_ENCODING': 'utf-8', 'PYTHONIOENCODING': 'utf-8', 'PYTHONPATH': 'C:굚Program Files굚Intel굚dev굚eclipse굚plugins굚org.python.pydev.core_7.2.1.201904261721굚pysrc굚pydev_sitecustomize;C:굚Program Files굚Intel굚dev굚workspace굚foundation;C:굚ProgramData굚Anaconda3굚DLLs;C:굚ProgramData굚Anaconda3굚lib;C:굚ProgramData굚Anaconda3;C:굚ProgramData굚Anaconda3굚lib굚site-packages;C:굚ProgramData굚Anaconda3굚lib굚site-packages굚win32;C:굚ProgramData굚Anaconda3굚lib굚site-packages굚win32굚lib;C:굚ProgramData굚Anaconda3굚lib굚site-packages굚Pythonwin', 'PYTHONUNBUFFERED': '1', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:굚WINDOWS', 'TEMP': 'C:굚Users굚user굚AppData굚Local굚Temp', 'TMP': 'C:굚Users굚user굚AppData굚Local굚Temp', 'USERDOMAIN': 'LECTURER', 'USERDOMAIN_ROAMINGPROFILE': 'LECTURER', 'USERNAME': 'user', 'USERPROFILE': 'C:굚Users굚user', 'WINDIR': 'C:굚WINDOWS', '__COMPAT_LAYER': 'Installer'})
print(os.environ["JAVA_HOME"])
# C:괦rogram Files괟ava굁dk1.8.0_212

# 2. os.chdir는 디렉토리 위치를 변경한다.
print(os.getcwd())
# C:괦rogram Files괞ntel괺ev굓orkspace괽oundation괹h09_library
os.chdir("c:/doit")

# 3. os.getcwd
print(os.getcwd())
# c:굓indows

# 4. os.system는 시스템 명령어를 호출한다.
f = os.system("dir")  
print(f)
'''
2019-08-17  오후 03:28    <DIR>          .
2019-08-17  오후 03:28    <DIR>          ..
2019-08-17  오후 03:12               151 mod1.py
2019-08-17  오후 03:19               233 mod2.py
2019-08-17  오후 03:28    <DIR>          mymod
2019-08-17  오후 03:20    <DIR>          __pycache__
               2개 파일                 384 바이트
               4개 디렉터리  443,620,405,248 바이트 남음
'''

# 5. os.popen은 실행한 시스템 명령어의 결과값을 
# 읽기모드 형태의 파일객체로 돌려준다.
f = os.popen("dir")
print(f)
# <os._wrap_close object at 0x00000172D7410048>
print(f.read())


# shutil은 파일을 복사해 주는 파이썬 모듈이다.
import shutil
shutil.copy("c:/doit/mod1.py", "c:/doit/mod1_copied.py")


# glob은 특정 디렉토리에 있는 파일 이름 모두를 알아야 할때 사용한다.
import glob
print(glob.glob("c:/Windows/t*"))
'''
['c:/Windows\\TAPI', 'c:/Windows\\Tasks', 
'c:/Windows\\Temp', 'c:/Windows\\TextInput', 
'c:/Windows\\tracing', 'c:/Windows\\twain_32', 
'c:/Windows\\twain_32.dll']
'''


# tempfile은 파일을 임시로 만들어서 사용할 때 유용한 모듈이다.
import tempfile
filename = tempfile.mktemp()
print(filename)
# C:\Users\user\AppData\Local\Temp\tmpgqlod5m0


# time 모듈은 시간과 관련되어 있다.
# time.time()는 UTC(Universal Time Coordinated, 협정 세계 표준시)
import time 
print(time.time())
# 1566624819.2461913
print(time.localtime(time.time()))
# time.struct_time(tm_year=2019, tm_mon=8, tm_mday=24, tm_hour=14, tm_min=34, tm_sec=47, tm_wday=5, tm_yday=236, tm_isdst=0)
print(time.asctime(time.localtime(time.time())))
# Sat Aug 24 14:36:20 2019

import time 
print(time.strftime("%Y/%m/%d %p %H:%M:%S", time.localtime(time.time())))

# time.sleep 함수는 일정한 시간 간격을 줄 수 있다.
import time 
for i in range(10):
    print(i)
    #time.sleep(1) # 1초간 일시 정지시킨다.
    
    
# random은 난수를 발생시키는 모듈이다.
import random
print(random.random())  # 0 <= random.random() < 1 의 임의의 실수값을 생성
print(random.randint(1,10))  # 1~10사이의 정수중에서 난수값을 리턴


import random
def random_pop(data):
    number = random.randint(0, len(data)-1) # 0~3사이의 임의의 정수
    return data.pop(number) # number=1, 

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data:
        print(random_pop(data)) # [1,2,3,5], [1,3,5]
'''
4
2
5
3
1
'''
        
# webbrowser는 기본 웹 브라우저를 자동으로 실행하는 모듈이다.
import webbrowser
webbrowser.open("http://www.naver.com")










 