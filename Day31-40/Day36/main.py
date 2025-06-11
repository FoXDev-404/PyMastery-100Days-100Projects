import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY="Z72NEXXTX2KXFX8P"
NEWS_API_KEY="82dad75514ec47719b0964c28c07e6c1"

load_dotenv()

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

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if abs(percentage_change) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
        "sortBy": "relevancy",
        "pageSize": 3
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    
    three_articles = articles[:3]
    formatted_articles = [
        f"{STOCK}: {'🔺' if percentage_change > 0 else '🔻'}{abs(percentage_change):.2f}%\n"
        f"Headline: {article['title']}\n"
        f"Brief: {article['description']}\n"
        for article in three_articles
    ]
    print("\n".join(formatted_articles))

    ## STEP 3: Use https://www.twilio.com
    # Send a separate message for each article.
    TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_FROM_NUMBER = os.getenv("TWILIO_MESSAGING_SERVICE_SID")  # Use Messaging Service SID
    TO_NUMBER = os.getenv("PHONE_NUMBER")

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for message_body in formatted_articles:
        message = client.messages.create(
            body=message_body,
            messaging_service_sid=TWILIO_FROM_NUMBER,
            to=TO_NUMBER
        )
        print(f"Sent message SID: {message.sid}")

#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

