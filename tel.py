import telebot
token="5256405774:AAEDiPEyT9rUXoOAgX6jAmwElaxYh1-0914"
# Создаем экземпляр бота
bot = telebot.TeleBot(token)
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет, этот бот создан для обхода ошибки вотсапп, для того что бы использовать бота просто укажи номер телефона с любом доступном формате )')
# Получение сообщений от юзера

@bot.message_handler(content_types=["text"])
def handle_text(message):
    s = message.text.replace("+","")
    s1 = s.replace("-","")
    s2 = s1.replace(" ","")
    s3 = s2.replace("(","")
    s4 = s3.replace(")","")
    s5= "whatsapp://send/?phone="+s4
    #replace("+"&"-"&"("&")"&" ","")
    bot.send_message(message.chat.id, 'Твоя ссылка для перехода в чат:')
    bot.send_message(message.chat.id,'whatsapp://send/?phone=' + s4)
    bot.send_message(message.chat.id,'Скопируй и вставь в адресную строку браузера 😇')
# Запускаем бота
bot.polling(none_stop=True, interval=0)
