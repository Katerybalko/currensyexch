# currensyexch
homework
import telebot
from config import keys, TOKEN
from utils import ConvertionExeption, CryptoConverter
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Для начала работы введи команду в таком формате:\n<имя валюты> \
<в какую валюту перевести> \
<сумма>\nПосмотреть все доступные валюты жми /valeues\nпиши имена валюты с маленькой буквы\nмежду словами ставь пробел\nнапример: доллар гривна 100'
    bot.reply_to(message, text)


@bot.message_handler(commands=['valeues'])
def valeues(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        valeues = message.text.split(' ')

        if len(valeues) != 3:
            raise ConvertionExeption('Слишком много параметров')

        quote, base, amount = valeues
        total_base = CryptoConverter.converter(quote, base, amount)

    except ConvertionExeption as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')


    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
         text = f'Цена {amount} {quote} в {base} - {total_base}'
         bot.send_message(message.chat.id, text)


bot.polling()
