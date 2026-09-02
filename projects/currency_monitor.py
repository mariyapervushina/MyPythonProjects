import requests

from config import TOKEN, CHAT_ID

response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
data = response.json()
thresholds = {'USD': 85, 'TRY': 2.0}
message = ''
url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
for code in thresholds:
    value = data['Valute'][code]['Value']
    nominal = data['Valute'][code]['Nominal']
    name = data['Valute'][code]['Name']
    total = value / nominal
    if total < thresholds[code]:
        message += f'{name}: {total:.2f} ₽, меньше порога \n'
    else:
        message += f'{name}: {total:.2f} ₽, больше порога \n'
requests.post(url, data={'chat_id': CHAT_ID, 'text': message})
    