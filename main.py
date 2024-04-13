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


import pyautogui as pg
from telebot import types
import telebot
import config
import os
import time
import random
import tabulate
from info import logo
from modules import (get_date, get_weather, get_courses, get_extra_currencies, shutdown, shutdown_stop, shutdown_timer,
                     sleep_mode, screenshot_save, restart, current_time, console_command, alert_function, lock,
                     SMS_message, get_news, get_wiki, get_date_sign)


bot = telebot.TeleBot(config.TOKEN)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("⚙️ Управление ПК")
item2 = types.KeyboardButton("📚 Другое")
item3 = types.KeyboardButton("🖼️ Медиа")
item4 = types.KeyboardButton("📂 Файлы")
markup.add(item4, item2, item3, item1)

print(logo)

@bot.message_handler(commands=['start'])
def privet(message):
    user_id_telegram = message.from_user.id
    if user_id_telegram in config.whitelist:
#        sti = open('static/yuhu.webm', 'rb')
#        bot.send_sticker(message.chat.id, sti)
        if get_date() != '1 Сентября' and get_date() != '2 Сентября' and get_date() != '3 Сентября':
            hourglass_message = bot.send_message(message.chat.id, get_date_sign())

        if get_date() == '1 Сентября' or get_date() == '2 Сентября':
            shufutinsky_calc = random.randint(0, 5)
            if shufutinsky_calc == 0:
                shufut = open('static/what_date_is_soon.jpg', 'rb')

            elif shufutinsky_calc == 2:
                shufut = open('static/kradetsya.jpg', 'rb')

            elif shufutinsky_calc == 3:
                shufut = open('static/uzhe mozhno.jpg', 'rb')

            elif shufutinsky_calc == 4:
                shufut = open('static/syet_v_dver.jpg', 'rb')

            elif shufutinsky_calc == 1:
                shufut = open('static/on yzhe blizko.jpg', 'rb')

            shufut_message = bot.send_photo(message.chat.id, shufut)

        elif get_date() == '3 Сентября':
            shufutinsky_calc = random.randint(0, 4)

            if shufutinsky_calc == 0:
                shufut = open('static/kakoe tam chiclo.jpg', 'rb')

            elif shufutinsky_calc == 1:
                shufut = open('static/shufutinov_den.jpg', 'rb')

            elif shufutinsky_calc == 2:
                shufut = open('static/kogda prevernyl.jpg', 'rb')

            elif shufutinsky_calc == 3:
                shufut = open('static/kak zhe ya vas segodnya.jpg', 'rb')

            elif shufutinsky_calc == 4:
                shufut = open('static/pereverni.jpg', 'rb')

            elif shufutinsky_calc == 5:
                shufut = open('static/perevernul.jpg', 'rb')

            shufut_message = bot.send_photo(message.chat.id, shufut)




        bot.send_message(message.chat.id, f'🖐 Привет, Evgenchick!\n\n<b>✅ Бот готов к работе!</b>\n\n📅 Я календарь переверну и снова <b>{get_date()}</b>\n\n🕘 На часах <b>{current_time}</b>\n\n<i>{get_weather()}</i>\n\n<b>{get_courses()}</b>'.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
        if get_date() != '1 Сентября' and get_date() != '2 Сентября' and get_date() != '3 Сентября':
            bot.delete_message(message.chat.id, hourglass_message.message_id)


        elif get_date() == '1 Сентября' or get_date() == '2 Сентября' or get_date() == '3 Сентября':
            bot.delete_message(message.chat.id, shufut_message.message_id)

    else:
        bot.send_message(message.chat.id, "❌ Вас нету в белом списке этого бота, он не для вас...")

@bot.message_handler(content_types=['text'])
def otvet(message):
    if message.chat.id in config.whitelist:
        if message.chat.type == 'private':
            if message.text == '⚙️ Управление ПК':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("🚫 Выключение", callback_data='shutdown')
                item2 = types.InlineKeyboardButton("🔄 Перезагрузка", callback_data='restart')
                item3 = types.InlineKeyboardButton("⌛ Таймер на выключение", callback_data='shutdown_timer')
                item4 = types.InlineKeyboardButton("🔒 Блокировка", callback_data='lock')
#                item5 = types.InlineKeyboardButton("😴 Спящий режим", callback_data='sleep_mode')
#                item6 = types.InlineKeyboardButton("✉️ Сообщение", callback_data='sms_message')
                item7 = types.InlineKeyboardButton("🚨 Уведомление", callback_data='alert')
                item8 = types.InlineKeyboardButton("🖥️ Команда", callback_data='console_command')
                item9 = types.InlineKeyboardButton("❌ Отмена таймера", callback_data='shutdown_stop')
                item10 = types.InlineKeyboardButton("🖼️ Скриншот", callback_data='screenshot')

                markup.add(item1, item2, item3, item4, item7, item8, item10, item9)

                bot.send_message(message.chat.id, "👇 Выбери действие:", reply_markup=markup)

            elif message.text == '📚 Другое':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("🧠 Википедия", callback_data='wikipedia')
                item2 = types.InlineKeyboardButton("📈 Курсы валют", callback_data='extra_currency_courses')
                item3 = types.InlineKeyboardButton("📰 Новости", callback_data='news')
                markup.add(item1, item3, item2)

                bot.send_message(message.chat.id, "👇 Выбери нужное:", reply_markup=markup)

            elif message.text == '🖼️ Медиа':
                markup = types.InlineKeyboardMarkup(row_width=3)
                item1 = types.InlineKeyboardButton("⏯", callback_data='pause')
                item2 = types.InlineKeyboardButton("➖ 🔊", callback_data='volume_minus')
                item3 = types.InlineKeyboardButton("🔇", callback_data='disable_audio')
                item4 = types.InlineKeyboardButton("⏪", callback_data='prevtrack')
                item5 = types.InlineKeyboardButton("⏩", callback_data='nexttrack')
                item6 = types.InlineKeyboardButton("🔊 ➕", callback_data='volume_plus')
                markup.add(item4, item1, item5, item3, item2, item6)

                bot.send_message(message.chat.id, "👇 Выбери действие:", reply_markup=markup)

            elif message.text == '📂 Файлы':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("📤 Отправить", callback_data='file_transfer')
                item2 = types.InlineKeyboardButton("📁 Проводник", callback_data='explorer')
#                item3 = types.InlineKeyboardButton("⚙️ Процессы", callback_data='process_list')
                markup.add(item1, item2)

                bot.send_message(message.chat.id, '👇 Выбирай нужное:', reply_markup=markup)

            elif message.text == '/about':
                bot.send_message(message.chat.id, "🐍 <u><i>Разработчики</i></u>:\n\n<b><a href='https://github.com/Evgenchick4434'>Evgenchick4434</a></b><i> - Разработчик, дизайнер.</i>\n<b><a href='https://github.com/Georgyrs'>Georgy</a></b><i> - Разработчик, браток короче)</i>\n\n<b>🪲 Нашли баг? <a href='https://forms.gle/AofqpZNgES5f5RBp7'>Сообщите мне</a></b>\n<b>❤️ Лучшим подарком для меня будет тг прем: @Evgenchick4434</b>".format(message.from_user, bot.get_me()), parse_mode='html')

            elif message.text == '/help':
                bot.send_message(message.chat.id, "<b>🛟 Помощь</b>\n\n👉 /start <i>- Если пропали кнопки</i>\n👉 /about <i>- Узнать больше о боте и его создателях</i>\n\n🪲<a href='https://forms.gle/AofqpZNgES5f5RBp7'><b>Сообщить о баге</b></a>".format(message.from_user, bot.get_me()), parse_mode='html')

            else:
                pass
    else:
        bot.send_message(message.chat.id, "❌ Вас нету в белом списке этого бота, он не для вас...")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'shutdown':
                shutdown()
                bot.send_message(call.message.chat.id, "✅")
                bot.send_message(call.message.chat.id, "✅ Выключаю ПК...")

            elif call.data == 'restart':
                restart()
                bot.send_message(call.message.chat.id, "⌛")
                bot.send_message(call.message.chat.id, "⌛ Перезагружаю ПК...")

            elif call.data == 'lock':
                lock()
                bot.send_message(call.message.chat.id, "🔒 Заблокировал ПК")

            elif call.data == 'sleep_mode':
                sleep_mode()
                bot.send_message(call.message.chat.id, "💤")
                bot.send_message(call.message.chat.id, "💤 Спящий режим включен")

            elif call.data == 'shutdown_stop':
                shutdown_stop()
                bot.send_message(call.message.chat.id, "❌ Успешно отменил выключение ПК")

            elif call.data == 'screenshot':
                screenshot_save()
                time.sleep(0.1)
                screenshot = open('screenshots/screenshot.png', 'rb')
                bot.send_photo(call.message.chat.id, screenshot)

            elif call.data == 'shutdown_timer':
                bot.send_message(call.message.chat.id, '⌛ Введи время до выключения в секундах:')
                bot.register_next_step_handler(call.message, process_timer_step)

            elif call.data == 'alert':
                bot.send_message(call.message.chat.id, '💬 Введи текст для уведомления:')
                bot.register_next_step_handler(call.message, process_alert_step)

            elif call.data == 'sms_message':
                bot.send_message(call.message.chat.id, '💬 Введи текст для сообщения:')
                bot.register_next_step_handler(call.message, process_msg_step)

            elif call.data == 'console_command':
                bot.send_message(call.message.chat.id, '🖥️ Введи команду:')
                bot.register_next_step_handler(call.message, process_cmd_step)

            elif call.data == 'extra_currency_courses':
                hourglass_message = bot.send_message(call.message.chat.id, get_date_sign())

                extra_currencies_result = get_extra_currencies().format(bot.get_me())

                bot.send_message(call.message.chat.id, extra_currencies_result, parse_mode='html')

                bot.delete_message(call.message.chat.id, hourglass_message.message_id)

            elif call.data == 'wikipedia':
                bot.send_message(call.message.chat.id, "🌏 Что тебя интересует?")
                bot.register_next_step_handler(call.message, process_wikipedia_step)

            elif call.data == 'news':
                time_message = bot.send_message(call.message.chat.id, get_date_sign())

                bot.send_message(call.message.chat.id, f'<b><i>📜 Новости с Хабра:</i></b>\n\n{get_news()}', parse_mode='html')
                bot.delete_message(call.message.chat.id, time_message.message_id)

            elif call.data == 'pause':
                pg.press('playpause')

            elif call.data == 'nexttrack':
                pg.press('nexttrack')

            elif call.data == 'prevtrack':
                pg.press('prevtrack')

            elif call.data == 'disable_audio':
                pg.press('volumemute')

            elif call.data == 'volume_minus':
                pg.press('volumedown')

            elif call.data == 'volume_plus':
                pg.press('volumeup')

            elif call.data == 'file_transfer':
                bot.send_message(call.message.chat.id, "📤 Отправь файл для передачи")
                bot.register_next_step_handler(call.message, process_document_step)

            elif call.data == 'explorer':
                bot.send_message(call.message.chat.id, "👉 Введите путь к директории:")
                bot.register_next_step_handler(call.message, process_explorer_input)




    except Exception as e:
        print(repr(e))


def process_timer_step(message):
    try:
        timer_time = int(message.text)
        shutdown_timer(timer_time)
        bot.send_message(message.chat.id, f'⏰ Таймер выключения установлен на {timer_time} секунд.')
    except ValueError:
        bot.send_message(message.chat.id, '⚠️ Введи корректное число секунд!')

def process_alert_step(message):
    alert_text = message.text
    alert_function(alert_text)
    bot.send_message(message.chat.id, f'💬 Отправлено уведомление с текстом: {alert_text}')

def process_msg_step(message):
    msg_text = message.text
    SMS_message(msg_text)
    bot.send_message(message.chat.id, f'💬 Отправлено сообщение с текстом: {msg_text}')

def process_cmd_step(message):
    try:
        cmd_command = message.text
        console_command(cmd_command)
        bot.send_message(message.chat.id, f'✅ Успешно выполнена команда: {cmd_command}')
    except:
        bot.send_message(message.chat.id, f'⚠️ При выполнении команды произошла ошибка. Вероятно, команда неверная')

def process_wikipedia_step(message):

        result = get_wiki(message)

        bot.send_message(message.chat.id, result, parse_mode='html')

def process_document_step(message):
    try:
        if message.document:

            file_info = bot.get_file(message.document.file_id)

            downloaded_file = bot.download_file(file_info.file_path)

            save_path = os.path.join(f'{config.transfer_folder}', message.document.file_name)

            with open(save_path, 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.send_message(message.chat.id, "📨 Файл успешно доставлен")
        else:
            bot.send_message(message.chat.id, "❌ Отправь файлом. Если это видео/фото, отправь его как файл")
    except:
        bot.send_message(message.chat.id, "❌ При сохранении файла произошла ошибка")


def process_explorer_input(message):
    try:
        user_input_path = message.text.strip()

        if os.path.exists(user_input_path):
            os.chdir(user_input_path)
            files_and_folders = os.listdir()
            table = tabulate.tabulate([(item,) for item in files_and_folders], headers=["Содержимое директории"])
            bot.send_message(message.chat.id, f"```\n{table}\n```", parse_mode="markdown")
        else:
            bot.send_message(message.chat.id, "❌ Указанная директория не существует.")

    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Произошла ошибка: {e}")




bot.polling(none_stop=True)
