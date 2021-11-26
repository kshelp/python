import tweepy

# 본인이 신청해서 생성한 문자열을 각각 복사해 넣습니다.
consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'

access_token = 'YOUR-ACCESS-TOKEN'
access_secret = '1DeZyTsYxUYhkYUaR3BAI3RKp'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

print("name:", api.me().name)
