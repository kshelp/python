# time 모듈은 시간과 관려되어 있다.
# time.time()은 UTC를 이용하여 현재 시간을 실수 형태로 리턴한다.
# UTC(Universal Time Code)는 1970년 1월1일 0시0분0초를 기준으로 지난시간을 초 단위로 리턴한다
import time

print(time.time())
print(time.gmtime())    #UTC 기준의 현재 시간
print(time.localtime()) #시스템 기준의 현재 시간
t = time.gmtime(1234567890)  #타임스탬프를 struct_time 시퀀스 객체로 변환
print(t)
print(t.tm_mon)
print(t.tm_hour)
print(time.asctime(t))
'''
time.struct_time(tm_year=2019, tm_mon=11, tm_mday=29, tm_hour=3, tm_min=44, tm_sec=7, tm_wday=4, tm_yday=333, tm_isdst=0)
time.struct_time(tm_year=2019, tm_mon=11, tm_mday=29, tm_hour=12, tm_min=44, tm_sec=7, tm_wday=4, tm_yday=333, tm_isdst=0)
time.struct_time(tm_year=2009, tm_mon=2, tm_mday=13, tm_hour=23, tm_min=31, tm_sec=30, tm_wday=4, tm_yday=44, tm_isdst=0)
2
23
Fri Feb 13 23:31:30 2009
'''

# time.sleep 함수는 일정한 시간 간격을 줄 수 있다.
import time
for i in range(10):
    print(i)
    time.sleep(1)
