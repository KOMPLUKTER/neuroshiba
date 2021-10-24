import telebot
import requests
from telebot import types
from PIL import Image, ImageDraw, ImageFont


bot = telebot.TeleBot('1603779921:AAF2pSSIS0cyOHZk-RslHWGQKPUU4PrqW7g')

joinedfile = open(r"C:\Program Files (x86)\shibabot\users_id\users.txt", "r")
joinedusers = set()
for line in joinedfile:
    joinedusers.add(line.strip())
joinedfile.close()

joinedfilename = open(r"C:\Program Files (x86)\shibabot\users_id\names.txt", "r")
joinedusersname = set()
for line in joinedfilename:
    joinedusersname.add(line.strip())
joinedfilename.close()

def beginning(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Список команд")
    markup.add(item1)
    bot.send_message(message.from_user.id, "Выберите команду", reply_markup=markup)

def groups(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item32 = types.KeyboardButton("Котоген")
    item34 = types.KeyboardButton("TNSJ")
    item_back = types.KeyboardButton("Вернуться в начало")
    markup.add(item32, item34, item_back)
    if message.text == 'Вернуться в начало':
        bot.send_message(message.from_user.id, 'Возвращаю в начальное меню')
        beginning(message)
    else:
        bot.register_next_step_handler(message, groups_reg)
        bot.send_message(message.from_user.id,
                         f'Выберите режим работы. Выбирай мудро.',
                         reply_markup=markup)

def pic_gen(message):

    r = requests.post('http://212.193.50.2:777/one_field_tools', json=
    {
        "option": "Hero Story Intro",
        "field_value": "Красивые пушистые коты",
        "tone": "Friendly"
    })

    p = requests.get('https://thiscatdoesnotexist.com')
    out = open("C:\\Users\\Иван\\Desktop\\shiba_cats\\img.jpg", "wb")
    out.write(p.content)
    out.close()

    im = Image.open("C:\\Users\\Иван\\Desktop\\shiba_cats\\img.jpg")
    draw_text = ImageDraw.Draw(im)

    for i in range(20):
        if len(r.json()['texts'][i].split('.')[0]) < 56:
            text = str(r.json()['texts'][i].split('.')[0])
            break

    text = text.split(" ")
    text1 = ''
    text2 = ''
    flag = 1
    for i in text:
        if len(text1) + len(i) < 23 and flag:
            text1 += " " + i
        else:
            if flag == 1:
                text2 += i
                flag = 0
            else:
                text2 += " " + i
    text1 = text1[1:]
    text1 = str(text1)
    text2 = str(text2)

    if 23 < len(text1):
        x = 3
    if 18 < len(text1) < 24:
        x = 10 #30
    if 13 < len(text1) < 19:
        x = 25 #45
    else:
        x = 50 #80

    font = ImageFont.truetype('C:\\Windows\\Fonts\\Lobster-Regular.ttf', size=40)

    offset = 3
    shadowcolor = 'black'
    imgWidth, imgHeight = im.size

    y = 385  # координата начала по y

    for off in range(offset):
        draw_text.text((x - off, y), text1, font=font, fill=shadowcolor)
    draw_text.text((x + off, y), text1, font=font, fill=shadowcolor)
    draw_text.text((x, y + off), text1, font=font, fill=shadowcolor)
    draw_text.text((x, y - off), text1, font=font, fill=shadowcolor)
    draw_text.text((x - off, y + off), text1, font=font, fill=shadowcolor)
    draw_text.text((x + off, y + off), text1, font=font, fill=shadowcolor)
    draw_text.text((x - off, y - off), text1, font=font, fill=shadowcolor)
    draw_text.text((x + off, y - off), text1, font=font, fill=shadowcolor)
    draw_text.text((x, y), text1, font=font, fill="#fff")
    del draw_text

    draw_text = ImageDraw.Draw(im)
    if len(text2) > 28:
        razn = len(text2) - 28
        text2 = text2[:razn]

    if 23 < len(text2):
        x2 = 10
    if 18 < len(text2) < 24:
        x2 = 10 #16
    if 13 < len(text2) < 19:
        x2 = 50 #70
    else:
        x2 = 75 #125

    font = ImageFont.truetype('C:\\Windows\\Fonts\\Lobster-Regular.ttf', size=40)

    offset2 = 3
    shadowcolor = 'black'
    imgWidth, imgHeight = im.size

    y2 = 450  # координата начала по y

    for off in range(offset2):
        draw_text.text((x2 - off, y2), text2, font=font, fill=shadowcolor)
    draw_text.text((x2 + off, y2), text2, font=font, fill=shadowcolor)
    draw_text.text((x2, y2 + off), text2, font=font, fill=shadowcolor)
    draw_text.text((x2, y2 - off), text2, font=font, fill=shadowcolor)
    draw_text.text((x2 - off, y2 + off), text2, font=font, fill=shadowcolor)
    draw_text.text((x2 + off, y2 + off), text2, font=font, fill=shadowcolor)
    draw_text.text((x2 - off, y2 - off), text2, font=font, fill=shadowcolor)
    draw_text.text((x2 + off, y2 - off), text2, font=font, fill=shadowcolor)
    draw_text.text((x2, y2), text2, font=font, fill="#fff")
    del draw_text

    rr = requests.post('http://212.193.50.2:777/two_field_tools', json={
        "option": "Product Descriptions",
        "main_field_value": "интересные факты о котах",
        "secondary_field_value": "Коты",
        "tone": "Friendly"
    })
    fuckt = "¯\_(ツ)_/¯"
    for i in range(len(rr.json()['texts']) - 1):
        if (
                'сайт' and 'альбоме' and 'fact' and 'знать' and '/' and 'собран' and 'журнале' and 'справочнике' and 'книге' and 'выложены' and 'читайте' and 'Читайте' and 'блоге' and 'факт') not in \
                rr.json()['texts'][i]:
            fuckt = rr.json()['texts'][i]
            break
    bot.send_photo(message.from_user.id, im, caption=fuckt)
    print(text1)
    print(text2)

    beginning(message)


def groups_reg(message):
    if message.text == 'Вернуться в начало':
        beginning(message)
        bot.send_message(message.from_user.id, 'Возвращаю в начальное меню')
    else:
        if message.text == 'Котоген':
            bot.send_message(message.from_user.id, f'Процесс запуска генератора изображений')
            bot.send_message(message.from_user.id, "...")
            pic_gen(message)

        elif message.text == 'TNSJ':
            bot.send_message(message.from_user.id, f'Процесс сбора и анализа данных. Обработка занимает некоторое время')
            bot.send_message(message.from_user.id, "...")
            bot.send_message(message.from_user.id, "Заглушка для тестов")

        elif message.text == 'Мудро' or message.text == 'мудро':
            bot.reply_to(message, f'А ты шаришь)')


@bot.message_handler(commands=['start'])
def send_welcome(message):

    if not str(message.chat.id) in joinedusers:
        joinedfile = open(r"C:\Program Files (x86)\shibabot\users_id\users.txt", "a")
        joinedfile.write(str(message.chat.id) + "\n")
        joinedusers.add(message.chat.id)

        joinedfilename = open(r"C:\Program Files (x86)\shibabot\users_id\names.txt", "a")
        joinedfilename.write(str(message.chat.id) + ' ' + str(message.from_user.first_name)+ ' ' + str(message.from_user.last_name)+ ' ' + str(message.from_user.username)+ "\n")
        joinedusersname.add(message.chat.id)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Список команд")
    markup.add(item1)

    bot.send_message(message.from_user.id, f'Добро пожаловать! Я умею немного, но для просмотра доступных команд нажмите на "Список команд"', reply_markup=markup)
    sticker = open('C:\Program Files (x86)\shibabot\stickors\sticker1.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Список команд':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Выбор режима")
        item_back = types.KeyboardButton("Вернуться в начало")
        markup.add(item2, item_back)
        bot.register_next_step_handler(message, groups)
        bot.send_message(message.from_user.id, f'Вот весь мой функционал', reply_markup=markup)
        if message.text == 'Вернуться в начало':
            bot.send_message(message.from_user.id, 'Возвращаю в начальное меню')
            bot.register_next_step_handler(message, beginning)
    elif message.text == 'Вернуться в начало':
        beginning(message)
        bot.send_message(message.from_user.id, 'Возвращаю в начальное меню')
    else:
        bot.reply_to(message, 'Нельзя выполнить действие в данный момент. Дождитесь завершения работы генератора.')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.from_user.id, f'Вот весь мой функционал.')
    bot.register_next_step_handler(message, groups)



@bot.message_handler(commands=['broadcast'])
def send_broadcast(message):
    for user in joinedusers:
        bot.send_message(user, message.text[message.text.find(' '):])


bot.polling(none_stop=True, interval=0)