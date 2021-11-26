import json
import requests
import datetime

# 자신의 인증키를 복사해서 입력합니다.
#API_KEY = 'DSMHBRE2ko972AtKewahx0%2BgQB50XpSp8OKJmz1Ooflw%2BMOaxVHExy5tPigYTAqGE%2BlSFRDfP31KSR%2FdTSiWHw%3D%3D'
API_KEY = 'Nthm35khfZR6DRDqGytWeSGTeOWEmKBf293ItGFcZHOP%2BDHWzPGpb4bAnsLTfCSSfhwbCyhaaMFm%2FR7uuhIyRw%3D%3D'
API_KEY_decode = requests.utils.unquote(API_KEY)
#print(API_KEY_decode)

now = datetime.datetime.now()
date = "{:%Y%m%d}".format(now)
time = "{:%H00}".format(now)
print(date)
if(now.minute >= 30):
    time = "{0}00".format(now.hour)
else:
    time = "{0}00".format(now.hour-1)

req_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst"

baseDate = date
baseTime = time

nx_val = 60
ny_val = 127

num_of_rows = 30
page_no = 1

output_type = "json"
req_parameter = {"ServiceKey": API_KEY_decode,
                 "nx": nx_val, "ny": ny_val,
                 "base_date": baseDate, "base_time": baseTime,
                 "pageNo": page_no, "numOfRows": num_of_rows,
                 "dataType": output_type}

r = requests.get(req_url, params=req_parameter)

dict_data = r.json()
print(dict_data)
