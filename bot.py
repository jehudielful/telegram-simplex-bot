# -*- coding: utf-8 -*-
import config
import telebot
import random
import time
import csv
import ipdb
#ipdb.set_trace()
from transliterate import translit, get_available_language_codes
#import get_available_language_codes
from transliterate.discover import autodiscover
autodiscover()

from transliterate.base import TranslitLanguagePack, registry

class ExampleLanguagePack(TranslitLanguagePack):
    language_code = "example"
    language_name = "Example"
    mapping = (
         u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
         u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA",
    )

registry.register(ExampleLanguagePack)
#print(translit(text, 'example'))


#f = open('C:\_WWWork\python\simplex_team_bot\words.csv')
#csv_f = csv.reader(f)
i=0

#with open('C:\_WWWork\_git\telegram-simplex-bot', encoding='utf-8') as csvfile:
with open('C:/_WWWork/_git/telegram-simplex-bot/words.csv', encoding='utf-8') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    gwords = []
    ewords = []
    for row in readCSV:
        #print (row)
        gword=row[1]
        eword=row[2]
        gwords.append(gword)
        ewords.append(eword)
    #print(gwords)
    #print(ewords)
str1 = '123456789'
str2 = 'qwertyuiopasdfghjklzxcvbnm'
str3 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
str4 = ',.<>/?;:"[]{}\|`~!@#$%^&*()-_+='
str_short = str1+str2
str_long = str1+str2+str3+str4

# Преобразуем получившуюся строку в список
ls = list(str_short)
lps = list (str_long)
random.seed(time.time())
random.shuffle(ls)
random.shuffle(lps)

# Извлекаем из списка 8 произвольных значений
mapping = (u"abcde", u"абцде")

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["pass"])
def password_generator(message):
    psw = ''.join([random.choice(ls) for x in range(8)])
    bot.send_message(message.chat.id, psw)

@bot.message_handler(commands=["longpass"])
def password_generator(message):
    psw = ''.join([random.choice(lps) for x in range(10)])
    bot.send_message(message.chat.id, psw)

@bot.message_handler(commands=["translit"])
def translit_it(message):
   bot.send_message(message.chat.id, translit(message.text[10:],  'example'))

@bot.message_handler(commands=["word"])
def german_words(message):
    starttime=time.time()
    while True:
        temp=random.randint(1,1000)
        bot.send_message(message.chat.id, gwords[temp] + ' - ' + ewords[temp])
        time.sleep(60.0 - ((time.time() - starttime) % 60.0))

if __name__ == '__main__':
     bot.polling(none_stop=True)
