import telebot

# --- Main menu ---
main_menu = telebot.types.ReplyKeyboardMarkup(True)
main_menu.row('Хочу оставить заявку на обратную связь.')

# --- Delete markup ---
del_markup = telebot.types.ReplyKeyboardRemove()