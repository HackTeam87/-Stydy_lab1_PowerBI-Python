# -*- coding: utf-8 -*-
# Скрипт для программы визуализации данных POWER BI.
# API позволяет получить информацию о наличных курсах валют ПриватБанка и НБУ на текущую  или выбранную дату. 
# Архив хранит данные за последние 4 года.
#API = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'


# импортируем необходимые библиотеки
import time
import requests
import pandas as pd

# получаем текущюю дату
day = time.strftime("%d.%m.%Y")

# подставляем дату и получаем данные из API приватбанка в формате JSON
API2 = 'https://api.privatbank.ua/p24api/exchange_rates?json&date=' + day

result = requests.get(API2)
res = result.json()

# формируем датафрейм
exchange = pd.DataFrame(res)
print(exchange)
    

