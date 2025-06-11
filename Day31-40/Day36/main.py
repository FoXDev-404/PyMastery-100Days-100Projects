import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY="your_stock_api_key_here"

## STEP 1: Use https://www.alphavantage.co
# Use intraday data as daily is now premium-only.
stock_params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
json_response = response.json()
if "Time Series (60min)" not in json_response:
    print("Error: 'Time Series (60min)' not found in response.")
    print("Response:", json_response)
    exit(1)
data = json_response["Time Series (60min)"]
data_list = [value for (key, value) in data.items()]
if len(data_list) < 2:
    print("Not enough data points returned.")
    exit(1)
# Use the last two closes as a proxy for "yesterday" and "day before yesterday"
latest_close = float(data_list[0]["4. close"])
previous_close = float(data_list[1]["4. close"])
percentage_change = ((latest_close - previous_close) / previous_close) * 100
print(f"{STOCK}: {percentage_change:.2f}%")

if abs(percentage_change) < 5:
    print("No significant change in stock price.")
    exit(0)

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

