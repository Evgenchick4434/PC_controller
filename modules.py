# Copyright 2024 Evgenchick4434 (https://github.com/Evgenchick4434)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import time
import datetime
import plyer
import locale
import wikipedia
from bs4 import BeautifulSoup as BS
import requests
import os
import pyautogui as pg
import pyscreenshot
import html
import random
from config import Console_log


def get_date():
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

    current_date = datetime.datetime.now()

    formatted_date = current_date.strftime("%d %B")

    month_names = {'январь': 'Января', 'февраль': 'Февраля', 'март': 'Марта',
                   'апрель': 'Апреля', 'май': 'Мая', 'июнь': 'Июня',
                   'июль': 'Июля', 'август': 'Августа', 'сентябрь': 'Сентября',
                   'октябрь': 'Октября', 'ноябрь': 'Ноября', 'декабрь': 'Декабря'}
    words = formatted_date.split()
    last_word = words[-1].lower()
    if last_word in month_names:
        words[-1] = month_names[last_word]
        formatted_date = ' '.join(words)

    if Console_log == True:
        print(f'Получена дата: {formatted_date}')
    return formatted_date


unformatted_time = time.localtime()

current_time = time.strftime("%H:%M", unformatted_time)

wikipedia.set_lang('ru')

def get_weather():
    url = 'https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%9A%D0%B0%D0%BB%D0%B8%D0%BD%D0%B8%D0%BD%D0%B3%D1%80%D0%B0%D0%B4%D0%B5'
    class_ = 'ArchiveTemp'

    r = requests.get(url)
    html = BS(r.text, 'html.parser')
    t = html.find(class_=class_).find(class_='t_0').text

    url = 'https://meteo7.ru/forecast/35799'
    class_ = 'descripcion wopr'     # Класс в котором нужный класс (чтобы не путались)

    r = requests.get(url)
    html = BS(r.text, 'html.parser')
    w = html.find(class_=class_).find(class_='cl').text



    url = 'https://meteo7.ru/forecast/35799'
    class_ = 'descripcion wopr'     # Класс в котором нужный класс (чтобы не путались)

    r = requests.get(url)
    html = BS(r.text, 'html.parser')
    osadki = html.find(class_=class_).find(class_='pr').text


    weather_emoji = '🌦'
    if w == 'пасмурно':
        weather_emoji = '☁️'
    elif w == 'значительная облачность':
        weather_emoji = '🌧️'
    elif w == 'ясно':
        current_time = datetime.datetime.now().time()
        if datetime.time(20, 0) <= current_time or current_time <= datetime.time(6, 0):
            night_time = True
        else:
            night_time = False


        if night_time == False:
            weather_emoji = '☀️'
        elif night_time == True:
            weather_emoji = '🌙'
    elif w == 'малооблачно':
        weather_emoji = '🌤️'
    elif w == 'переменная облачность':
        weather_emoji = '🌤️'
    elif w == 'облачно с прояснениями':
        weather_emoji = '🌤️'


    weather = f'{weather_emoji}️ За окном {t}, {w}.'

    if Console_log == True:
        print(f'Получена погода: {weather}')
    return weather



def get_courses():
    url = 'https://www.binance.com/en-GB/price/bitcoin'
    class_ = 'css-1267ixm'

    r = requests.get(url)
    html = BS(r.text, 'html.parser')
    BTC = html.find(class_=class_).find(class_='css-1bwgsh3').text


    url = 'https://www.binance.com/en-GB/price/ethereum'
    class_ = 'css-1267ixm'

    r = requests.get(url)
    html = BS(r.text, 'html.parser')
    ETH = html.find(class_=class_).find(class_='css-1bwgsh3').text


    url = 'https://ru.investing.com/currencies/usd-rub'
    class_ = 'mb-3 flex flex-wrap items-center gap-x-4 gap-y-2 md:mb-0.5 md:gap-6'

    r = requests.get(url)
    html = BS(r.text, 'html.parser')
    USD = html.find(class_=class_).find(class_='text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]').text


    currency_courses = f'[₿] Bitcoin: {BTC}\n[💎] Ethereum: {ETH}\n[💲] Доллар: ₽ {USD}'

    if Console_log == True:
        print(f'Получены курсы валют: {currency_courses}')
    return currency_courses

def get_extra_currencies():
    url = 'https://www.binance.com/en-GB/price/bitcoin'
    class_ = 'css-1267ixm'

    r = requests.get(url)
    html = BS(r.text, 'html.parser')
    BTC_element = html.find(class_=class_)
    BTC = BTC_element.find(class_='css-1bwgsh3').text if BTC_element else "Не удалось найти курс Bitcoin"

    url = 'https://www.binance.com/en-GB/price/ethereum'
    r = requests.get(url)
    html = BS(r.text, 'html.parser')
    ETH_element = html.find(class_=class_)
    ETH = ETH_element.find(class_='css-1bwgsh3').text if ETH_element else "Не удалось найти курс Ethereum"

    url = 'https://ru.investing.com/currencies/usd-rub'
    class_ = 'mb-3 flex flex-wrap items-center gap-x-4 gap-y-2 md:mb-0.5 md:gap-6'

    r = requests.get(url)
    html = BS(r.text, 'html.parser')
    USD_element = html.find(class_=class_)
    USD = USD_element.find(
        class_='text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]').text if USD_element else "Не удалось найти курс Доллара"

    url = 'https://ru.investing.com/currencies/try-rub'
    r = requests.get(url)
    html = BS(r.text, 'html.parser')
    TRY_element = html.find(class_=class_)
    TRY = TRY_element.find(
        class_='text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]').text if TRY_element else "Не удалось найти курс Турецкой лиры"

    url = 'https://ru.investing.com/currencies/eur-rub'
    r = requests.get(url)
    html = BS(r.text, 'html.parser')
    EUR_element = html.find(class_=class_)
    EUR = EUR_element.find(
        class_='text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]').text if EUR_element else "Не удалось найти курс Евро"

    # Парсинг курса TRX
    url_trx = 'https://www.binance.com/en/price/tron'
    class_trx = 'css-1267ixm'
    r_trx = requests.get(url_trx)
    html_trx = BS(r_trx.text, 'html.parser')
    trx_element = html_trx.find(class_=class_trx)
    TRX = trx_element.find(class_='css-1bwgsh3').text if trx_element else "Не удалось найти курс TRX"

    # Парсинг курса TON
    url_ton = 'https://www.binance.com/en-GB/price/toncoin'
    class_ton = 'css-1267ixm'
    r_ton = requests.get(url_ton)
    html_ton = BS(r_ton.text, 'html.parser')
    ton_element = html_ton.find(class_=class_ton)
    TON = ton_element.find(class_='css-1bwgsh3').text if ton_element else "Не удалось найти курс TON"

    url = 'https://ru.investing.com/currencies/pln-rub'
    r = requests.get(url)
    html = BS(r.text, 'html.parser')
    PLN_element = html.find(class_=class_)
    PLN = PLN_element.find(
        class_='text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]').text if PLN_element else "Не удалось найти курс Злотого"

    extra_currency_courses = f'<b>✅ Актуальные курсы валют прямо сейчас:</b>\n\n<b>[₿]</b> Bitcoin: {BTC}\n[💎] Ethereum: {ETH}\n[💲] Доллар: ₽ {USD}\n[💶] Евро: ₽ {EUR}\n<b>[₺]</b> Лира: ₽ {TRY}\n[🔻] TON: {TON}\n[👑] TRX: {TRX}\n<b>[zł]</b> Злотый: ₽ {PLN}'

    if Console_log == True:
        print(f'Получены расширенные курсы валют: {extra_currency_courses}')

    return extra_currency_courses



def alert(text, app_name, title):
    plyer.notification.notify(
        message=f'{text}',
        app_name=f'{app_name}',
        title=f'{title}', )
    if Console_log == True:
        print(f'Отправлено уведомление с параметрами: text: {text}, app_name: {app_name}, title: {title}')

def alert_function(text):
    plyer.notification.notify(
        message=f'{text}',
        app_name=f'PC controller',
        title=f'📩 Сообщение из Telegram', )

    if Console_log == True:
        print(f'Отправлено уведомление с текстом: {text}')

def SMS_message(SMS_text):
    pg.alert(f'📩 Сообщение: {SMS_text}', 'Сообщение', button="❌ Закрыть")

    if Console_log == True:
        print(f'Доставлено сообщение с текстом: {SMS_text}')

def shutdown():
    if Console_log == True:
        print("Выключаю компьютер...")
    os.system("shutdown /s /t 0")

def shutdown_timer(time):
    os.system(f'shutdown /s /t {time}')
    if Console_log == True:
        print(f'Задан таймер выключения пк на {time} секунд')

def shutdown_stop():
    os.system("shutdown -a")
    if Console_log == True:
        print("Таймер выключения ПК отменён")

def lock():
    os.system("rundll32.exe user32.dll,LockWorkStation")
    plyer.notification.notify(
        message=f'Доступ ограничен через Telegram',
        app_name=f'Pc Controller',
        title=f'🚫 Windows заблокирован', )
    if Console_log == True:
     print("Windows заблокирована")

def screenshot_save():
    scr = pyscreenshot.grab()
    scr.save('screenshots/screenshot.png')
    if Console_log == True:
        print("Скриншот сохранён")

def console_command(command):
    if Console_log == True:
        print(f'Выполняю команду {command} в консоли...')
    os.system(f'{command}')

def restart():
    if Console_log == True:
        print("Перезагружаю компьютер...")
    os.system("shutdown /r /t 0")

def sleep_mode():
    if Console_log == True:
        print("Включаю спящий режим...")
    os.system("rundll32 powrprof.dll,SetSuspendState 0,1,0")

def get_news():
    url = 'https://habr.com/ru/all/'
    response = requests.get(url).text

    data = BS(response, 'html.parser')

    news_msg = ""
    count = 0
    for article in data.find_all('h2', class_='tm-title tm-title_h2'):
        title = article.a.span.text
        link = 'https://habr.com' + article.a['href']
        news_msg += f'👉 <b><a href="{link}">{title}</a></b>\n'
        count += 1
        if count >= 5:
            break

    if Console_log == True:
        print(f'Получены новости с Хабра: {news_msg}')
    return news_msg

def get_wiki(message):
    try:

        request_page = message.text
        python_page = wikipedia.page(request_page)
        escaped_url = html.escape(python_page.url)
        result = f'<b>🔎 Скорее всего, ты искал статью:</b>\n👉 <i><a href="{escaped_url}">{python_page.original_title}</a></i>'
    except:
        result = '🤔 Задай вопрос точнее'

    if Console_log == True:
        try:
            print(f'Получена статья с Википедии: {python_page.original_title}')
        except:
            print("Произошла ошибка при получении статьи с википедии. Ошибка обработана успешно")

    return result


def get_date_sign():
    date_sign = '⌛'

    if get_date() == '30 Января' or get_date() == '31 Января' or get_date() == '1 Января' or get_date() == '2 Января' or get_date() == '3 Января':
        random_numba = random.randint(0, 4)
        if random_numba == 0:
            date_sign = '🎄'

        elif random_numba == 1:
            date_sign = '🍊'

        elif random_numba == 2:
            date_sign = '🎅'

        elif random_numba == 3:
            date_sign = '❄️'

        elif random_numba == 4:
            date_sign = '☃️'

    if get_date() == '1 Апреля':
        random_number = random.randint(0, 3)
        if random_number == 0:
            date_sign = '🤡'

        elif random_number == 1:
            date_sign = '🎉'

        elif random_number == 2:
            date_sign = '🥳'

        elif random_number == 3:
            date_sign = '🎊'

    if Console_log == True:
        print(f'Получен date_sign: {date_sign}')
    return date_sign
