import telebot
import telebot.types

API_KEY = "5655827893:AAFWtirXSN7ayS9xq9UKgi2KnvbVzxYl0rc"
BOT_NAME = "Programmerhumor_bot"

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=["greet"])
def greet(message):
    bot.send_message(message, "Hey!")


# bot.polling()
