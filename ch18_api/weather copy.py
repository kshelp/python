import json
import requests
import datetime

# 자신의 인증키를 복사해서 입력합니다.
API_KEY = 'DSMHBRE2ko972AtKewahx0%2BgQB50XpSp8OKJmz1Ooflw%2BMOaxVHExy5tPigYTAqGE%2BlSFRDfP31KSR%2FdTSiWHw%3D%3D'
#API_KEY = 'DSMHBRE2ko972AtKewahx0+gQB50XpSp8OKJmz1Ooflw+MOaxVHExy5tPigYTAqGE+lSFRDfP31KSR/dTSiWHw=='
API_KEY_decode = requests.utils.unquote(API_KEY)
#print(API_KEY_decode)

now=datetime.datetime.now()
date="{:%Y%m%d}".format(now)
time="{:%H00}".format(now)
print(date)
if(now.minute >= 30):
    time="{0}00".format(now.hour)
else:
    time="{0}00".format(now.hour-1)

req_url="http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst"

baseDate=date
baseTime=time

nx_val=60
ny_val=127

num_of_rows=30
page_no=1

output_type="json"
req_parameter={"ServiceKey":API_KEY_decode,
                "nx":nx_val, "ny":ny_val,
                "base_date":baseDate, "base_time":baseTime,
                "pageNo":page_no, "numOfRows":num_of_rows,
                "dataType":output_type}

r=requests.get(req_url, params=req_parameter)

dict_data=r.json()
print(dict_data)

weather_items=dict_data['response']['body']['items']['item']
sky_cond=["맑음", "구름 조금", "구름 많음", "흐림"]
rain_type=["없음", "비", "비/눈", "눈", "소나기", "빗방울", "빗방울/눈날림", "눈날림"]

print("[발표 날짜:{} ".format(weather_items[0]['baseDate']))
print("[발표 시각:{} ".format(weather_items[0]['baseTime']))

print("[초단기 일기 예보]")
print("----------------기온----------------")
for k in range(len(weather_items)):
    weather_item=weather_items[k]

    fcstTime=weather_item['fcstTime']
    fcstValue=weather_item['fcstValue']

    if(weather_item['category']=='T1H'):
        print("*시각: {0}, 기온: {1}".format(fcstTime, fcstValue))
print("----------------습도----------------")

for k in range(len(weather_items)):
    weather_item=weather_items[k]

    fcstTime=weather_item['fcstTime']
    fcstValue=weather_item['fcstValue']

    if(weather_item['category']=='REH'):
        print("*시각: {0}, 습도: {1}[%]".format(fcstTime, fcstValue))
print("----------------하늘----------------")
for k in range(len(weather_items)):
    weather_item=weather_items[k]

    fcstTime=weather_item['fcstTime']
    fcstValue=weather_item['fcstValue']

    if(weather_item['category']=='SKY'):
        print("*시각: {0}, 하늘 상태: {1}".format(fcstTime, sky_cond[int(fcstValue)-1]))     
print("----------------강수형태----------------")
for k in range(len(weather_items)):
    weather_item=weather_items[k]

    fcstTime=weather_item['fcstTime']
    fcstValue=weather_item['fcstValue']

    if(weather_item['category']=='PTY'):
        print("*시각: {0}, 강수 형태: {1}".format(fcstTime, rain_type[int(fcstValue)]))
print("----------------강수량----------------")
for k in range(len(weather_items)):
    weather_item=weather_items[k]

    fcstTime=weather_item['fcstTime']
    fcstValue=weather_item['fcstValue']

    if(weather_item['category']=='RN1'):
        print("*시각: {0}, 1시간 강수량: {1}[mm]".format(fcstTime, fcstValue)) 

