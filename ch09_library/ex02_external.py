#-*- coding:cp949 -*-

# �����Լ�
# sys ����� ���̽� ���������Ͱ� �����ϴ� ������� �Լ�����
# ���� ������ �� �ְ� ���ִ� ����̴�.
# ��� �࿡�� �μ� �����ϱ� - sys.argv

import sys

# print(sys.argv)
# ['C:��Program Files��Intel��dev��workspace��foundation��ch09_library��ex02_external.py']
# ['C:��Program Files��Intel��dev��workspace��foundation��ch09_library��ex02_external.py', 'test1', 'test2']

if len(sys.argv) == 4:
    print(sys.argv)
    if sys.argv[1] == "name":
        print(sys.argv[2])
    # ['C:��Program Files��Intel��dev��workspace��foundation��ch09_library��ex02_external.py', 'arg1', 'arg2', 'arg3']
    # sys.exit()  # ������ ���α׷��� �����Ѵ�.
else: 
    print("����: python *.py arg1 arg2 arg3")
    
# �ڽ��� ���� ��� �ҷ��� ����ϱ� - sys.path
import sys
print(sys.path)
'''
['C:��Program Files��Intel��dev��workspace��foundation��ch09_library', 
'C:��Program Files��Intel��dev��workspace��foundation', 
'C:��ProgramData��Anaconda3��DLLs', 
'C:��ProgramData��Anaconda3��lib', 
'C:��ProgramData��Anaconda3', 
'C:��ProgramData��Anaconda3��lib��site-packages', 
'C:��ProgramData��Anaconda3��lib��site-packages��win32', 
'C:��ProgramData��Anaconda3��lib��site-packages��win32��lib', 
'C:��ProgramData��Anaconda3��lib��site-packages��Pythonwin', 
'C:��ProgramData��Anaconda3��python37.zip']
'''

sys.path.append("C:/doit/")
print(sys.path)
'''
['C:��Program Files��Intel��dev��workspace��foundation��ch09_library', 'C:��Program Files��Intel��dev��workspace��foundation', 
'C:��ProgramData��Anaconda3��DLLs', 
'C:��ProgramData��Anaconda3��lib', 
'C:��ProgramData��Anaconda3', 
'C:��ProgramData��Anaconda3��lib��site-packages', 
'C:��ProgramData��Anaconda3��lib��site-packages��win32', 
'C:��ProgramData��Anaconda3��lib��site-packages��win32��lib', 
'C:��ProgramData��Anaconda3��lib��site-packages��Pythonwin', 
'C:��ProgramData��Anaconda3��python37.zip', 
'C:/doit/']
'''

from mod1 import add, sub
print(add(3,4))
# 7


# pickle�� ��ü�� ���·� �״�� �����ϸ鼭 ���Ͽ� �����ϰ� �ҷ��� �� 
# �ְ� �ϴ� ����̴�.
import pickle
f = open("test.txt", "wb")
data = {1:'python', 2:'you need'}  # ��ųʸ� ��ü
pickle.dump(data, f)
f.close()

# ���� �ִ� ��ųʸ� ��ü ���� �״�� �Ҿ����
f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)
# {1: 'python', 2: 'you need'}



# OS ����� ȯ�溯���� ���丮, ���� ���� OS �ڿ��� ������ �� �ְ�
# ���ִ� ����̴�.
# 1. os.environ�� �ý����� ȯ�� ���� ���� �˷��ش�.
import os
print(os.environ)  
# environ({'ALLUSERSPROFILE': 'C:��ProgramData', 'APPDATA': 'C:��Users��user��AppData��Roaming', 'COMMONPROGRAMFILES': 'C:��Program Files��Common Files', 'COMMONPROGRAMFILES(X86)': 'C:��Program Files (x86)��Common Files', 'COMMONPROGRAMW6432': 'C:��Program Files��Common Files', 'COMPUTERNAME': 'LECTURER', 'COMSPEC': 'C:��WINDOWS��system32��cmd.exe', 'DRIVERDATA': 'C:��Windows��System32��Drivers��DriverData', 'HOMEDRIVE': 'C:', 'HOMEPATH': '��Users��user', 'IDE_PROJECT_ROOTS': 'C:��Program Files��Intel��dev��workspace��foundation', 'JAVA_HOME': 'C:��Program Files��Java��jdk1.8.0_212', 'LOCALAPPDATA': 'C:��Users��user��AppData��Local', 'LOGONSERVER': '����LECTURER', 'NUMBER_OF_PROCESSORS': '4', 'ONEDRIVE': 'C:��Users��user��OneDrive', 'OS': 'Windows_NT', 'PATH': 'C:/Program Files/Java/jdk1.8.0_212/bin/../jre/bin/server;C:/Program Files/Java/jdk1.8.0_212/bin/../jre/bin;C:/Program Files/Java/jdk1.8.0_212/bin/../jre/lib/amd64;C:��ProgramData��Anaconda3;C:��ProgramData��Anaconda3��Library��mingw-w64��bin;C:��ProgramData��Anaconda3��Library��usr��bin;C:��ProgramData��Anaconda3��Library��bin;C:��ProgramData��Anaconda3��Scripts;C:��oraclexe��app��oracle��product��11.2.0��server��bin;C:��WINDOWS��system32;C:��WINDOWS;C:��WINDOWS��System32��Wbem;C:��WINDOWS��System32��WindowsPowerShell��v1.0��;C:��Program Files��Java��jdk1.8.0_212��bin;C:��Program Files��Java��jdk1.8.0_212��bin;C:��WINDOWS��System32��OpenSSH��;C:��Program Files��Bandizip��;C:��Users��user��AppData��Local��Microsoft��WindowsApps;C:��Program Files��Intel��dev��eclipse;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 94 Stepping 3, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '5e03', 'PROGRAMDATA': 'C:��ProgramData', 'PROGRAMFILES': 'C:��Program Files', 'PROGRAMFILES(X86)': 'C:��Program Files (x86)', 'PROGRAMW6432': 'C:��Program Files', 'PROMPT': '$P$G', 'PSMODULEPATH': 'C:��WINDOWS��system32��WindowsPowerShell��v1.0��Modules��', 'PUBLIC': 'C:��Users��Public', 'PYDEV_COMPLETER_PYTHONPATH': 'C:��Program Files��Intel��dev��eclipse��plugins��org.python.pydev.core_7.2.1.201904261721��pysrc', 'PYDEV_CONSOLE_ENCODING': 'utf-8', 'PYTHONIOENCODING': 'utf-8', 'PYTHONPATH': 'C:��Program Files��Intel��dev��eclipse��plugins��org.python.pydev.core_7.2.1.201904261721��pysrc��pydev_sitecustomize;C:��Program Files��Intel��dev��workspace��foundation;C:��ProgramData��Anaconda3��DLLs;C:��ProgramData��Anaconda3��lib;C:��ProgramData��Anaconda3;C:��ProgramData��Anaconda3��lib��site-packages;C:��ProgramData��Anaconda3��lib��site-packages��win32;C:��ProgramData��Anaconda3��lib��site-packages��win32��lib;C:��ProgramData��Anaconda3��lib��site-packages��Pythonwin', 'PYTHONUNBUFFERED': '1', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:��WINDOWS', 'TEMP': 'C:��Users��user��AppData��Local��Temp', 'TMP': 'C:��Users��user��AppData��Local��Temp', 'USERDOMAIN': 'LECTURER', 'USERDOMAIN_ROAMINGPROFILE': 'LECTURER', 'USERNAME': 'user', 'USERPROFILE': 'C:��Users��user', 'WINDIR': 'C:��WINDOWS', '__COMPAT_LAYER': 'Installer'})
print(os.environ["JAVA_HOME"])
# C:�Program Files�Java�jdk1.8.0_212

# 2. os.chdir�� ���丮 ��ġ�� �����Ѵ�.
print(os.getcwd())
# C:�Program Files�Intel�dev�workspace�foundation�ch09_library
os.chdir("c:/doit")

# 3. os.getcwd
print(os.getcwd())
# c:�windows

# 4. os.system�� �ý��� ��ɾ ȣ���Ѵ�.
f = os.system("dir")  
print(f)
'''
2019-08-17  ���� 03:28    <DIR>          .
2019-08-17  ���� 03:28    <DIR>          ..
2019-08-17  ���� 03:12               151 mod1.py
2019-08-17  ���� 03:19               233 mod2.py
2019-08-17  ���� 03:28    <DIR>          mymod
2019-08-17  ���� 03:20    <DIR>          __pycache__
               2�� ����                 384 ����Ʈ
               4�� ���͸�  443,620,405,248 ����Ʈ ����
'''

# 5. os.popen�� ������ �ý��� ��ɾ��� ������� 
# �б��� ������ ���ϰ�ü�� �����ش�.
f = os.popen("dir")
print(f)
# <os._wrap_close object at 0x00000172D7410048>
print(f.read())


# shutil�� ������ ������ �ִ� ���̽� ����̴�.
import shutil
shutil.copy("c:/doit/mod1.py", "c:/doit/mod1_copied.py")


# glob�� Ư�� ���丮�� �ִ� ���� �̸� ��θ� �˾ƾ� �Ҷ� ����Ѵ�.
import glob
print(glob.glob("c:/Windows/t*"))
'''
['c:/Windows\\TAPI', 'c:/Windows\\Tasks', 
'c:/Windows\\Temp', 'c:/Windows\\TextInput', 
'c:/Windows\\tracing', 'c:/Windows\\twain_32', 
'c:/Windows\\twain_32.dll']
'''


# tempfile�� ������ �ӽ÷� ���� ����� �� ������ ����̴�.
import tempfile
filename = tempfile.mktemp()
print(filename)
# C:\Users\user\AppData\Local\Temp\tmpgqlod5m0


# time ����� �ð��� ���õǾ� �ִ�.
# time.time()�� UTC(Universal Time Coordinated, ���� ���� ǥ�ؽ�)
import time 
print(time.time())
# 1566624819.2461913
print(time.localtime(time.time()))
# time.struct_time(tm_year=2019, tm_mon=8, tm_mday=24, tm_hour=14, tm_min=34, tm_sec=47, tm_wday=5, tm_yday=236, tm_isdst=0)
print(time.asctime(time.localtime(time.time())))
# Sat Aug 24 14:36:20 2019

import time 
print(time.strftime("%Y/%m/%d %p %H:%M:%S", time.localtime(time.time())))

# time.sleep �Լ��� ������ �ð� ������ �� �� �ִ�.
import time 
for i in range(10):
    print(i)
    #time.sleep(1) # 1�ʰ� �Ͻ� ������Ų��.
    
    
# random�� ������ �߻���Ű�� ����̴�.
import random
print(random.random())  # 0 <= random.random() < 1 �� ������ �Ǽ����� ����
print(random.randint(1,10))  # 1~10������ �����߿��� �������� ����


import random
def random_pop(data):
    number = random.randint(0, len(data)-1) # 0~3������ ������ ����
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
        
# webbrowser�� �⺻ �� �������� �ڵ����� �����ϴ� ����̴�.
import webbrowser
webbrowser.open("http://www.naver.com")










 