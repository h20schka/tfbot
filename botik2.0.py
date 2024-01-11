import random
import telebot
from telebot import types
import sqlite3


bot = telebot.TeleBot('6136206390:AAEiK353AYv9sapXg_HcgIYwb1bdmaj3fhg')


answers = ['Я не зрозумію, що ти хочеш сказати.',
'Вибач, я тебе не розумію.',
'Я не знаю такої команди.',
'Мій розробник не казав,
що відповідатиме в такій ситуації... >_<']


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Українська')
    button2 = types.KeyboardButton('Deutsch')
    markup.row(button1)
    markup.row(button2)
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Мова/Sprache:', reply_markup=markup)

@bot.message_handler(commands=['buymenu'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🚬 Elf Bar 2000')
    button2 = types.KeyboardButton('🚬 Elf Bar BC 5000 ultra')
    markup.row(button1)
    markup.row(button2)
    if message.text == '/buymenu':
        bot.send_message(message.chat.id, f'Привіт, {message.from_user.first_name}!\nУ мене ти зможеш купити деякі товари!', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Головне меню:', reply_markup=markup)
@bot.message_handler(commands=['buymenu']) #D
def welcomе(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🚬 Elf Вar 2000')
    button2 = types.KeyboardButton('🚬 Elf Вar BC 5000 ultra')
    markup.row(button1)
    markup.row(button2)
    if message.text == '/buymenu':       
        bot.send_message(message.chat.id, f'Привіт, {message.from_user.first_name}!\nУ мене ти зможеш купити деякі товари!', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Hauptmenü:', reply_markup=markup)

@bot.message_handler(content_types='photo')
def get_photo(message):
    bot.send_message(message.chat.id, 'Умене не має можливості переглядати фото :(')

@bot.message_handler()
def info(message):
    if message.text == 'Українська':
        UKRChapter(message)
    elif message.text == 'Deutsch':
        DChapter(message)

    elif message.text == '🚬 Elf Bar 2000':
        goodsChapterUKR(message)
    elif message.text == '🚬 Elf Bar BC 5000 ultra':
        infoChapterUKR(message)

    elif message.text == '🚬 Elf Bar 2000':
        goodsChapterD(message)
    elif message.text == '🚬 Elf Bar BC 5000 ultra':
        infoChapterD(message)

    elif message.text == '🚬 Elf Вar 2000':
        goodsChapterD(message)
    elif message.text == '🚬 Elf Вar BC 5000 ultra':
        infoChapterD(message)

    elif message.text == '🔹 Redmojito':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Замовити')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '2000 затяжок;\n6,5 мл рідини;\nАккумулятор 1200 mAh;\n5%/50мг', reply_markup=markup)
        file = open('./Redmojito.jpg', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 KiwiBerry':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Замовити')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '2000 затяжок;\n6,5 мл рідини;\nАккумулятор 1200 mAh;\n5%/50мг', reply_markup=markup)
        file = open('./KiwiBerry.jpg', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)


    elif message.text == '🔹 PeachMangoGuava':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Замовити')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '2000 затяжок;\n6,5 мл рідини;\nАккумулятор 1200 mAh;\n5%/50мг', reply_markup=markup)
        file = open('./PeachMangoGuava.jpg', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)


    elif message.text == '🔹 PineappleIce':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Замовити')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '2000 затяжок;\n6,5 мл рідини;\nАккумулятор 1200 mAh;\n5%/50мг', reply_markup=markup)
        file = open('./PineappleIce.jpg', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)


    elif message.text == '🔹 StrawberryGrape':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Замовити')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '2000 затяжок;\n6,5 мл рідини;\nАккумулятор 1200 mAh;\n5%/50мг', reply_markup=markup)
        file = open('./StrawberryGrape.jpg', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)


    elif message.text == '🔹 GrapeEnergy':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Замовити')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '2000 затяжок;\n6,5 мл рідини;\nАккумулятор 1200 mAh;\n5%/50мг', reply_markup=markup)
        file = open('./GrapeEnergy.jpg', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)


    elif message.text == '🔹 BananaMilk':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Замовити')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '2000 затяжок;\n6,5 мл рідини;\nАккумулятор 1200 mAh;\n5%/50мг', reply_markup=markup)
        file = open('./BananaMilk.jpg', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 GrapeIce':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Замовити')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '2000 затяжок;\n6,5 мл рідини;\nАккумулятор 1200 mAh;\n5%/50мг', reply_markup=markup)
        file = open('./GrapeIce.jpg', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 KiwiPassionFruitGuava':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Замовити')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '2000 затяжок;\n6,5 мл рідини;\nАккумулятор 1200 mAh;\n5%/50мг', reply_markup=markup)
        file = open('./KiwiPassionFruitGuava.jpg', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 Watermelonlemon':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Замовити')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '2000 затяжок;\n6,5 мл рідини;\nАккумулятор 1200 mAh;\n5%/50мг', reply_markup=markup)
        file = open('./Watermelonlemon.jpg', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 CoffeTobacco':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Замовити')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        file = open('./CoffeTobacco.jpg', 'rb')
        bot.send_message(message.chat.id, '2000 затяжок;\n6,5 мл рідини;\nАккумулятор 1200 mAh;\n5%/50мг' , reply_markup=markup)
        bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 Strawberry Mango':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Замовити')
        button2 = types.KeyboardButton('↩️ Назад до товарів')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '5000 зятяжок;\n13 мл рідини;\nАккумулятор 650mAh;\n5%/50мг або 2%/20мг;\nType-C', reply_markup=markup)
        #file = open('./Strawberry Mango.jpg', 'rb')
        #bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 Strawberry Watermelon Peach':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Замовити')
        button2 = types.KeyboardButton('↩️ Назад до товарів')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '5000 зятяжок;\n13 мл рідини;\nАккумулятор 650mAh;\n5%/50мг або 2%/20мг;\nType-C', reply_markup=markup)
        #file = open('./Strawberry Watermelon Peach.jpg', 'rb')
        #bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 Tobacco':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Замовити')
        button2 = types.KeyboardButton('↩️ Назад до товарів')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '5000 зятяжок;\n13 мл рідини;\nАккумулятор 650mAh;\n5%/50мг або 2%/20мг;\nType-C', reply_markup=markup)
        #file = open('./Tobacco.jpg', 'rb')
        #bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 Kiwi Dragon Fruit Berry':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Замовити')
        button2 = types.KeyboardButton('↩️ Назад до товарів')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '5000 зятяжок;\n13 мл рідини;\nАккумулятор 650mAh;\n5%/50мг або 2%/20мг;\nType-C', reply_markup=markup)
        #file = open('./Kiwi Dragon Fruit Berry.jpg', 'rb')
        #bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 Blue Cotton Candy':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Замовити')
        button2 = types.KeyboardButton('↩️ Назад до товарів')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '5000 зятяжок;\n13 мл рідини;\nАккумулятор 650mAh;\n5%/50мг або 2%/20мг;\nType-C', reply_markup=markup)
        #file = open('./Blue Cotton Candy .jpg', 'rb')
        #bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 Kiwi Passion Fruit Guava':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Замовити')
        button2 = types.KeyboardButton('↩️ Назад до товарів')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '5000 зятяжок;\n13 мл рідини;\nАккумулятор 650mAh;\n5%/50мг або 2%/20мг;\nType-C', reply_markup=markup)
        #file = open('./Kiwi Passion Fruit Guava.jpg', 'rb')
        #bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 Grape Honeydew':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Замовити')
        button2 = types.KeyboardButton('↩️ Назад до товарів')
        markup.row(button1, button2)
        bot.send_message(message.chat.id,'5000 зятяжок;\n13 мл рідини;\nАккумулятор 650mAh;\n5%/50мг або 2%/20мг;\nType-C',reply_markup=markup)
        # file = open('./Grape Honeydew.jpg', 'rb')
        # bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 Raspberry Watermelon':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Замовити')
        button2 = types.KeyboardButton('↩️ Назад до товарів')
        markup.row(button1, button2)
        bot.send_message(message.chat.id,'5000 зятяжок;\n13 мл рідини;\nАккумулятор 650mAh;\n5%/50мг або 2%/20мг;\nType-C',reply_markup=markup)
        # file = open('./Raspberry Watermelon.jpg', 'rb')
        # bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 Orange Soda':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Замовити')
        button2 = types.KeyboardButton('↩️ Назад до товарів')
        markup.row(button1, button2)
        bot.send_message(message.chat.id,'5000 зятяжок;\n13 мл рідини;\nАккумулятор 650mAh;\n5%/50мг або 2%/20мг;\nType-C',reply_markup=markup)
        # file = open('./Orange Soda .jpg', 'rb')
        # bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🗒 Наявність': #2000
        with open('Elf Bar 2000.txt', 'r') as file:
            data = file.read()
        bot.send_message(chat_id=message.chat.id, text=data)
        #bot.send_message(message.chat.id, '2Elf Bar 2000' + '\n' +"#PeachMangoGuava (2)" + '\n' +'#JuicyPeach (0)'+ '\n' +'#BlueRazzIce(0)' + '\n' +'#Cola (0)'+ '\n' +'#PineappleMangoOrange (0)'+ '\n' +'#WatermelonLemon (0)'+ '\n' +'#RedMojito (0)'+ '\n' +'#MangoPeachWatermelon (0)'+ '\n' +'#PineappleIce (0)'+ '\n' +'#BananaMilk (1)'+ '\n' +'#SourApple (0)'+ '\n' +'#KiwiBerry (0)'+ '\n' +'#KiwiPassionFruitGuava (0)'+ '\n' +'#StrawberryGrape (1)'+ '\n' +'#CoffeeTobacco (1)'+ '\n' +'#GrapeEnergy (1)'+ '\n' +'#GrapeIce (0)'+ '\n', reply_markup=markup)

    elif message.text == '📒 Нaявність': #5000
        with open('Elf Bar BC 5000 ultra.txt', 'r') as file:
            data = file.read()
        bot.send_message(chat_id=message.chat.id, text=data)

    elif message.text == '💳 Замовити': 
        #bot.send_message(message.chat.id, 'https://t.me/infrontoftheM1')
        bot.send_message(message.chat.id, 'Замовити:\nhttps://t.me/IliasMah \nабо \nhttps://t.me/infrontoftheM1')
        #bot.send_message(message.chat.id, 'Щоб замовити напиши менеджеру')

    elif message.text == '↩️ Назад':
        goodsChapterUKR(message)
    elif message.text == '↩️ Назад до товарів':
        infoChapterUKR(message)
    elif message.text == '↩️ Назад до меню':
        welcome(message)

    elif message.text == '🔹 Redmojitо':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Befehl')
        button2 = types.KeyboardButton('↩️ Zurück')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '2000 Züge;\n6,5 ml Flüssigkeit;\nAkkumulator 1200 mAh;\n5%/50mg', reply_markup=markup)
        file = open('./Redmojito.jpg', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 KiwiВerry':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Befehl')
        button2 = types.KeyboardButton('↩️ Zurück')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '2000 Züge;\n6,5 ml Flüssigkeit;\nAkkumulator 1200 mAh;\n5%/50mg',
                         reply_markup=markup)
        file = open('./KiwiBerry.jpg', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)


    elif message.text == '🔹 PeachMangоGuava':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Befehl')
        button2 = types.KeyboardButton('↩️ Zurück')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '2000 Züge;\n6,5 ml Flüssigkeit;\nAkkumulator 1200 mAh;\n5%/50mg',
                         reply_markup=markup)
        file = open('./PeachMangoGuava.jpg', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)


    elif message.text == '🔹 PinеappleIce':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Befehl')
        button2 = types.KeyboardButton('↩️ Zurück')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '2000 Züge;\n6,5 ml Flüssigkeit;\nAkkumulator 1200 mAh;\n5%/50mg',
                         reply_markup=markup)
        file = open('./PineappleIce.jpg', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)


    elif message.text == '🔹 StrаwberryGrape':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Befehl')
        button2 = types.KeyboardButton('↩️ Zurück')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '2000 Züge;\n6,5 ml Flüssigkeit;\nAkkumulator 1200 mAh;\n5%/50mg',
                         reply_markup=markup)
        file = open('./StrawberryGrape.jpg', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)


    elif message.text == '🔹 GrаpeEnergy':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Befehl')
        button2 = types.KeyboardButton('↩️ Zurück')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '2000 Züge;\n6,5 ml Flüssigkeit;\nAkkumulator 1200 mAh;\n5%/50mg',
                         reply_markup=markup)
        file = open('./GrapeEnergy.jpg', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)


    elif message.text == '🔹 BаnanaMilk':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Befehl')
        button2 = types.KeyboardButton('↩️ Zurück')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '2000 Züge;\n6,5 ml Flüssigkeit;\nAkkumulator 1200 mAh;\n5%/50mg',
                         reply_markup=markup)
        file = open('./BananaMilk.jpg', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)


    elif message.text == '🔹 GrаpeIce':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Befehl')
        button2 = types.KeyboardButton('↩️ Zurück')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '2000 Züge;\n6,5 ml Flüssigkeit;\nAkkumulator 1200 mAh;\n5%/50mg',
                         reply_markup=markup)
        file = open('./GrapeIce.jpg', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 KiwiPаssionFruitGuava':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Befehl')
        button2 = types.KeyboardButton('↩️ Zurück')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '2000 Züge;\n6,5 ml Flüssigkeit;\nAkkumulator 1200 mAh;\n5%/50mg',
                         reply_markup=markup)
        file = open('./KiwiPassionFruitGuava.jpg', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 Watеrmelonlemon':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Befehl')
        button2 = types.KeyboardButton('↩️ Zurück')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '2000 Züge;\n6,5 ml Flüssigkeit;\nAkkumulator 1200 mAh;\n5%/50mg',
                         reply_markup=markup)
        file = open('./Watermelonlemon.jpg', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 CоffeTobacco':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Befehl')
        button2 = types.KeyboardButton('↩️ Zurück')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '2000 Züge;\n6,5 ml Flüssigkeit;\nAkkumulator 1200 mAh;\n5%/50mg',
                         reply_markup=markup)
        file = open('./CoffeTobacco.jpg', 'rb')
        bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 Strawberrу Mango':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Befehl')
        button2 = types.KeyboardButton('↩️ Zurück zu den Produkten')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '5000 Bräutigame;\n13 ml Flüssigkeit;\nAkkumulator 650mAh;\n5%/50mg oder 2%/20mg;\nType-C', reply_markup=markup)
        #file = open('./Strawberry Mango.jpg', 'rb')
        #bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 Strаwberry Watermelon Peach':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Befehl')
        button2 = types.KeyboardButton('↩️ Zurück zu den Produkten')
        markup.row(button1, button2)
        bot.send_message(message.chat.id,
                         '5000 Bräutigame;\n13 ml Flüssigkeit;\nAkkumulator 650mAh;\n5%/50mg oder 2%/20mg;\nType-C',
                         reply_markup=markup)
        #file = open('./Strawberry Watermelon Peach.jpg', 'rb')
        #bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 Tobaccо':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Befehl')
        button2 = types.KeyboardButton('↩️ Zurück zu den Produkten')
        markup.row(button1, button2)
        bot.send_message(message.chat.id,
                         '5000 Bräutigame;\n13 ml Flüssigkeit;\nAkkumulator 650mAh;\n5%/50mg oder 2%/20mg;\nType-C',
                         reply_markup=markup)
        #file = open('./Tobacco.jpg', 'rb')
        #bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 Kiwі Dragon Fruit Berry':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Befehl')
        button2 = types.KeyboardButton('↩️ Zurück zu den Produkten')
        markup.row(button1, button2)
        bot.send_message(message.chat.id,
                         '5000 Bräutigame;\n13 ml Flüssigkeit;\nAkkumulator 650mAh;\n5%/50mg oder 2%/20mg;\nType-C',
                         reply_markup=markup)
        #file = open('./Kiwi Dragon Fruit Berry.jpg', 'rb')
        #bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 Blue Cottоn Candy':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Befehl')
        button2 = types.KeyboardButton('↩️ Zurück zu den Produkten')
        markup.row(button1, button2)
        bot.send_message(message.chat.id,
                         '5000 Bräutigame;\n13 ml Flüssigkeit;\nAkkumulator 650mAh;\n5%/50mg oder 2%/20mg;\nType-C',
                         reply_markup=markup)
        #file = open('./Blue Cotton Candy .jpg', 'rb')
        #bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 Kiwi Passiоn Fruit Guava':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Befehl')
        button2 = types.KeyboardButton('↩️ Zurück zu den Produkten')
        markup.row(button1, button2)
        bot.send_message(message.chat.id,
                         '5000 Bräutigame;\n13 ml Flüssigkeit;\nAkkumulator 650mAh;\n5%/50mg oder 2%/20mg;\nType-C',
                         reply_markup=markup)
        #file = open('./Kiwi Passion Fruit Guava.jpg', 'rb')
        #bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 Grape Honeydеw':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Befehl')
        button2 = types.KeyboardButton('↩️ Zurück zu den Produkten')
        markup.row(button1, button2)
        bot.send_message(message.chat.id,
                         '5000 Bräutigame;\n13 ml Flüssigkeit;\nAkkumulator 650mAh;\n5%/50mg oder 2%/20mg;\nType-C',
                         reply_markup=markup)
        # file = open('./Grape Honeydew.jpg', 'rb')
        # bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 Raspberry Watеrmelon':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Befehl')
        button2 = types.KeyboardButton('↩️ Zurück zu den Produkten')
        markup.row(button1, button2)
        bot.send_message(message.chat.id,
                         '5000 Bräutigame;\n13 ml Flüssigkeit;\nAkkumulator 650mAh;\n5%/50mg oder 2%/20mg;\nType-C',
                         reply_markup=markup)
        # file = open('./Raspberry Watermelon.jpg', 'rb')
        # bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🔹 Orange Sodа':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Befehl')
        button2 = types.KeyboardButton('↩️ Zurück zu den Produkten')
        markup.row(button1, button2)
        bot.send_message(message.chat.id,
                         '5000 Bräutigame;\n13 ml Flüssigkeit;\nAkkumulator 650mAh;\n5%/50mg oder 2%/20mg;\nType-C',
                         reply_markup=markup)
        # file = open('./Orange Soda .jpg', 'rb')
        # bot.send_photo(message.chat.id, file, reply_markup=markup)

    elif message.text == '🗒 Vеrfügbarkeit': #2000
        with open('Elf Bar 2000.txt', 'r') as file:
            data = file.read()
        bot.send_message(chat_id=message.chat.id, text=data)
        #bot.send_message(message.chat.id, '2Elf Bar 2000' + '\n' +"#PeachMangoGuava (2)" + '\n' +'#JuicyPeach (0)'+ '\n' +'#BlueRazzIce(0)' + '\n' +'#Cola (0)'+ '\n' +'#PineappleMangoOrange (0)'+ '\n' +'#WatermelonLemon (0)'+ '\n' +'#RedMojito (0)'+ '\n' +'#MangoPeachWatermelon (0)'+ '\n' +'#PineappleIce (0)'+ '\n' +'#BananaMilk (1)'+ '\n' +'#SourApple (0)'+ '\n' +'#KiwiBerry (0)'+ '\n' +'#KiwiPassionFruitGuava (0)'+ '\n' +'#StrawberryGrape (1)'+ '\n' +'#CoffeeTobacco (1)'+ '\n' +'#GrapeEnergy (1)'+ '\n' +'#GrapeIce (0)'+ '\n', reply_markup=markup)

    elif message.text == '📒 Verfügbarkeit': #5000
        with open('Elf Bar BC 5000 ultra.txt', 'r') as file:
            data = file.read()
        bot.send_message(chat_id=message.chat.id, text=data)

    elif message.text == '💳 Befehl': 
        #bot.send_message(message.chat.id, 'https://t.me/infrontoftheM1')
        bot.send_message(message.chat.id, 'Befehl:\nhttps://t.me/IliasMah \noder \nhttps://t.me/infrontoftheM1')
        #bot.send_message(message.chat.id, 'Щоб замовити напиши менеджеру')

    elif message.text == '↩️ Zurück':
        goodsChapterD(message)
    elif message.text == '↩️ Zurück zu den Produkten':
        infoChapterD(message)
    elif message.text == '↩️ Zurück zum Menü':
        welcomе(message)

    
    else:
        bot.send_message(message.chat.id, answers[random.randint(0, 3)])

def goodsChapterUKR(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🔹 Redmojito')
    button2 = types.KeyboardButton('🔹 KiwiBerry')
    button3 = types.KeyboardButton('🔹 PeachMangoGuava')
    button4 = types.KeyboardButton('🔹 PineappleIce')
    button5 = types.KeyboardButton('🔹 StrawberryGrape')
    button6 = types.KeyboardButton('🔹 GrapeEnergy')
    button7 = types.KeyboardButton('🔹 BananaMilk')
    button8 = types.KeyboardButton('🔹 GrapeIce')
    button9 = types.KeyboardButton('🔹 KiwiPassionFruitGuava')
    button10 = types.KeyboardButton('🔹 Watermelonlemon')
    button11 = types.KeyboardButton('🔹 CoffeTobacco')
    button12 = types.KeyboardButton('🗒 Наявність')
    button13 = types.KeyboardButton('↩️ Назад до меню')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5, button6)
    markup.row(button7, button8)
    markup.row(button9, button10)
    markup.row(button11)
    markup.row(button12, button13)

    bot.send_message(message.chat.id, 'Ось усі товари:', reply_markup=markup)

def infoChapterUKR(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🔹 Strawberry Mango')
    button2 = types.KeyboardButton('🔹 Strawberry Watermelon Peach')
    button3 = types.KeyboardButton('🔹 Tobacco')
    button4 = types.KeyboardButton('🔹 Kiwi Dragon Fruit Berry')
    button5 = types.KeyboardButton('🔹 Blue Cotton Candy')
    button6 = types.KeyboardButton('🔹 Kiwi Passion Fruit Guava')
    button7 = types.KeyboardButton('🔹 Grape Honeydew')
    button8 = types.KeyboardButton('🔹 Raspberry Watermelon')
    button9 = types.KeyboardButton('🔹 Orange Soda')
    button10 = types.KeyboardButton('📒 Нaявність')
    button11 = types.KeyboardButton('↩️ Назад до меню')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5, button6)
    markup.row(button7, button8)
    markup.row(button9)
    markup.row(button10, button11)
    bot.send_message(message.chat.id, 'Ось усі товари:', reply_markup=markup)

def goodsChapterD(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🔹 Redmojitо')
    button2 = types.KeyboardButton('🔹 KiwiВerry')
    button3 = types.KeyboardButton('🔹 PeachMangоGuava')
    button4 = types.KeyboardButton('🔹 PinеappleIce')
    button5 = types.KeyboardButton('🔹 StrаwberryGrape')
    button6 = types.KeyboardButton('🔹 GrаpeEnergy')
    button7 = types.KeyboardButton('🔹 BаnanaMilk')
    button8 = types.KeyboardButton('🔹 GrаpeIce')
    button9 = types.KeyboardButton('🔹 KiwiPаssionFruitGuava')
    button10 = types.KeyboardButton('🔹 Watеrmelonlemon')
    button11 = types.KeyboardButton('🔹 CоffeTobacco')
    button12 = types.KeyboardButton('🗒 Vеrfügbarkeit')
    button13 = types.KeyboardButton('↩️ Zurück zum Menü')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5, button6)
    markup.row(button7, button8)
    markup.row(button9, button10)
    markup.row(button11)
    markup.row(button12, button13)

    bot.send_message(message.chat.id, 'Hier sind alle Produkte:', reply_markup=markup)

def infoChapterD(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🔹 Strawberrу Mango')
    button2 = types.KeyboardButton('🔹 Strаwberry Watermelon Peach')
    button3 = types.KeyboardButton('🔹 Tobaccо')
    button4 = types.KeyboardButton('🔹 Kiwі Dragon Fruit Berry')
    button5 = types.KeyboardButton('🔹 Blue Cottоn Candy')
    button6 = types.KeyboardButton('🔹 Kiwi Passiоn Fruit Guava')
    button7 = types.KeyboardButton('🔹 Grape Honeydеw')
    button8 = types.KeyboardButton('🔹 Raspberry Watеrmelon')
    button9 = types.KeyboardButton('🔹 Orange Sodа')
    button10 = types.KeyboardButton('📒 Verfügbarkeit')
    button11 = types.KeyboardButton('↩️ Zurück zum Menü')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5, button6)
    markup.row(button7, button8)
    markup.row(button9)
    markup.row(button10, button11)
    bot.send_message(message.chat.id, 'Hier sind alle Produkte:', reply_markup=markup)

def UKRChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🚬 Elf Bar 2000')
    button2 = types.KeyboardButton('🚬 Elf Bar BC 5000 ultra')
    markup.row(button1, button2)
    bot.send_message(message.chat.id, 'Головне меню:', reply_markup=markup)
def DChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🚬 Elf Вar 2000')
    button2 = types.KeyboardButton('🚬 Elf Вar BC 5000 ultra')
    markup.row(button1, button2)
    bot.send_message(message.chat.id, 'Hauptmenü:', reply_markup=markup)

bot.polling(none_stop=True)