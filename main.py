import telebot
import time
from config import token_api
from intro_text import intro_text
import markups as mark

my_id = -4174453747


def get_info_user(bot, message):  # функция для отправки информации о юзере в личку
    bot.send_message(my_id, message.text + ' '
                     + f'{message.chat.id}' + ' '
                     + f'{message.from_user.first_name}' + ' '
                     + f'{message.from_user.last_name}')

def run_bot():
    bot = telebot.TeleBot(token_api)

    @bot.message_handler(commands=['start'])  # приветственная функция
    def send_welcome(message):


        img = open('title.png', 'rb')
        bot.send_photo(message.chat.id, img)
        welcome_user = f'Здравствуйте {message.from_user.first_name} {message.from_user.last_name}' + intro_text

        bot.send_message(message.chat.id, welcome_user,
                         reply_markup=mark.main_menu)

    @bot.message_handler(content_types=['text'])
    def send_markup(message):
        if message.text == 'Хочу оставить заявку на обратную связь.':
            bot.send_message(message.chat.id, 'Хорошо! Напишите свой номер и имя, с вами ближайшее время свяжуться.', reply_markup=mark.del_markup)
        elif message.text:
            bot.send_message(message.chat.id, 'Спасибо, с Вами свяжутся в ближайшее время!',
                             reply_markup=mark.del_markup)
            get_info_user(bot, message)

        elif message.text == 'Назад':
            img = open('title.png', 'rb')
            bot.send_photo(message.chat.id, img)
            bot.send_message(message.chat.id, intro_text,
                             reply_markup=mark.main_menu)
        else:
            bot.send_message(message.chat.id, 'Я Вас не понял =(')

    while True:  # функция для пулинга
        print('=^.^=')

        try:
            bot.polling(none_stop=True, interval=3, timeout=20)
            print('Этого не должно быть')
        except telebot.apihelper.ApiException:
            print('Проверьте связь и API')
            time.sleep(10)
        except Exception as e:
            print(e)
            time.sleep(60)


if __name__ == '__main__':
    run_bot()
