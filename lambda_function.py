import requests
#from lxml import html , etree
from bs4 import BeautifulSoup
from creds import telegram_bot_token, chat_id, url

def get_price():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Accept-Encoding': None
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    price_element = soup.select_one('span.product-price.current-price-value')
    if price_element:
        price = price_element.get_text(strip=True)
        clean_price = price.replace('₹', '').replace(',', '')
        print(clean_price)
        return float(clean_price)
    else:
        print('Price not found')
        return None

def send_message(chat_id, message):
    send_message_url = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.get(send_message_url, params=params)
        
def main(event, context):
    p = get_price()
    
    if p < 129000:
        message = "HURRY It's Lower Rs "+ str(p)+'\n\n'+ url
    else:
        message = "Price now is => Rs "+ str(p)
    
    send_message(chat_id, message)



