import requests
import os
from twilio.rest import Client






## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
###############################################################################################################




#--------------------------------------------- STOCKS API --------------------------------------------------#


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


stock_difference = float
stock_api_key = "HNXPEL6RKCJ2IEX9"
parameters = {
    "function":  "TIME_SERIES_INTRADAY",
    "symbol":  "TSLA",
    "interval":  "5min",
    "apikey": "HNXPEL6RKCJ2IEX9"
}

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
stock_response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
stock_response.raise_for_status()
data = stock_response.json()
select_data = data['Time Series (5min)']
data_key = list(select_data.keys())[0]  ###########################    AMAZING TECHNIQUE , TO SELECT KEYS IN DICT USING INDEX

stock_begin = float(data['Time Series (5min)'][data_key]['1. open'])
stock_end = float(data['Time Series (5min)'][data_key]['4. close'])
stock_info = data['Meta Data']['3. Last Refreshed']
stock_date = stock_info[0:10]
stock_behaviour = (stock_begin/stock_end)
if stock_begin > stock_end:
    stock_difference = f"TESLA🔻{abs(round((stock_end/stock_begin)*100-100, 3))}%"       # ab() converts positive to negative number
else:
    stock_difference = f"TESLA🔺{abs(round((stock_begin / stock_end) * 100 - 100, 3))}%"
print(stock_difference)


#----------------------------------------------------- NEWS API ---------------------------------------------#

news_api = "ddace29d5fc64f9b99642f7778ed3cd6"

news_parameters= {
    "apikey": news_api,
    "q": "Tesla",
}

news_response = requests.get(url=f"https://newsapi.org/v2/everything", params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()

first_headline = news_data['articles'][0]['title']
first_news = news_data['articles'][0]['description']

second_headline = news_data['articles'][1]['title']
second_news = news_data['articles'][1]['description']

print(first_headline)
print(first_news)

print(second_headline)
print(second_news)

#------------------------------------------------------- TEXT ----------------------------------------#

recovery = "BvsNlAKHFA4d5qWcYLnqim1iRFWcyVCKqwmbZE-e"
phone_number = +18176461590
secret = "Eg8OwZAqw2GXUlTaRODOqgFFbEkgFphX"

sid = 'ACff137fd28518dd483bea732dfc91384e'
tok = 'c188e3db082bc3ccda0f529e2a44a6db'


account_sid=os.environ['TWILIO_ACCOUNT_SID'] = sid
auth_token=os.environ['TWILIO_AUTH_TOKEN'] = tok
client = Client(account_sid, auth_token)

message1 = client.messages.create(
    body=f"Send from your Twilio account\n{stock_difference}\nHeadline: {first_headline}\nBrief: {first_news}",
    from_ ='+18176461590',
    to='+923044111814'
)
message2 = client.messages.create(
    body=f"Send from your Twilio account\n{stock_difference}\nHeadline: {second_headline}\nBrief: {second_news}",
    from_ ='+18176461590',
    to='+923044111814'
)


