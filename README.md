# 🐍 PC Controller - Управляй своим ПК дистанционно!

**╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╭╮╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮╱╱╱╱┃┃┃┃
┃╰━╯┣━━╮╭━━┳━━┳━╋╮╭╋━┳━━┫┃┃┃╭━━┳━╮
┃╭━━┫╭━╯┃╭━┫╭╮┃╭╮┫┃┃╭┫╭╮┃┃┃┃┃┃━┫╭╯
┃┃╱╱┃╰━╮┃╰━┫╰╯┃┃┃┃╰┫┃┃╰╯┃╰┫╰┫┃━┫┃
╰╯╱╱╰━━╯╰━━┻━━┻╯╰┻━┻╯╰━━┻━┻━┻━━┻╯**
ㅤㅤ  ****by Evgenchick4434 & Georgyrs****

_Привет! **PC Controller** поможет тебе управлять своим компьютером через Telegram бота - он имеет
обширный функционал, который мы планируем только расширять))_

_Второй разработчик_ - **[Georgyrs](https://github.com/Georgyrs)**

P.S. Если вы видели где-то похожий платный бот, имейте ввиду что наш сделан с нуля и не имеет ни к 
чему ткому отношения.

**Стартовое сообщение:**

    🖐 Привет, Evgenchick!  # Тут будет ваш никнейм Telegram

    ✅ Бот готов к работе!

    📅 Я календарь переверну и снова 12 Апреля  # Да, отсылка

    🕘 На часах 19:18  # Особенно круто когда 00:00

    ☁️️ За окном 13 °C, пасмурно.   # Погода в вашем городе. Да, смайлик меняется

    [₿] Bitcoin: $ 68,123.19
    [💎] Ethereum: $ 3,436.21     # Актуальные курсы валют
    [💲] Доллар: ₽ 93,4300


## 🚀 Функционал бота

_Здесь указаны все функции, которые умеет выполнять этот бот._

**⚙️ Управление ПК:**

    👉 Выключение / Перезагрузка ПК

    👉 Таймер на выключение пк / его отмена

    👉 Блокировка ПК

    👉 Уведомление через центр уведомлений Windows

    👉 Выполнение консольной команды

    👉 Скриншот экрана

**🖼️ Медиа:**

    👉 Пауза / продолжение воспроизведения

    👉 Следующий трек / видео

    👉 Предыдущий трек / видео

    👉 Увеличить громкость

    👉 Уменьшить громкость

    👉 Отключить звук

**📁 Файлы:**

    👉 Трансфер файла с телефона на ПК в задаваемую папку

    👉 Просмотр файлов в указанной директории

**📚 Другое:**

    👉 Поиск статьи в Википедии

    👉 Просмотр последних новостей с Хабра

    👉 Просмотр расширенных курсов валют*

`*` - планируется добавление аналитики по рынку



##### Так же важный функционал:

    😁 Шуфутинский вместо песочных часов под 1, 2 и 3 Сентября
    
    🎄 Новогодние эмодзи вместо песочных часов под новый год и после него


## ⚙️ Установка и настройка

1. **Устанавливаем все необходимые библиотеки из requirements.txt
командой** `pip install -r requirements.txt`

2. **Редактируем `config.py` под себя:**
```Python
    TOKEN = 'token'  # Токен вашего telegram бота

    whitelist = [0123456789]       # Белый список пользователей telegram бота

    transfer_folder = r"C:\Users\User\Documents"  # Путь для сохранения файлов (трансфер)

    Console_log = False  # Включить лог в консоли
```
3. **Запускаем `main.py`**

## ♻️ Дальнейшие обновления

_Это первый проект, который мы планируем обновлять, поскольку он действительно получился интересным
и решающим некоторые задачи._

**В планах на ближайшие обновления:**

    👉 Аналитика рынка валют и рекомендации

    👉 Список процессов и возможность завершать их по PID

    👉 Автозапуск и релизы на GitHub

    🚀 И многое другое!

## 🏆 Как поддержать автора?

**⭐ Во-первых, конечно, лучшей поддержкой будет поставить звезду (star) этому репозиторию
и подписаться на меня и** [Georgyrs](https://github.com/Georgyrs) **в GitHub!**

_☕ Но если вы альфонс и хотите сделать кодеру день - подарите ему тг премиум на аккаунт_
**`@Evgenchick4434`**

### © Рекоды / форки и отношение кодеров к ним
`_______________________________________________________`

❤️ Рекоды и форки - это хорошо, и мы только поддерживаем
таких прекрасных людей. Но, пожалуйста, оставляйте упоминание этого
репозитория хотя бы в `README.md`. Это будет большая поддержка))❤
