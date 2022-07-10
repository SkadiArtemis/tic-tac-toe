import telebot

TOKEN = "5404492428:AAEmkmsj47X1OUPBMzjD6FfjqmN61l_jl_w"

bot = telebot.TeleBot(TOKEN)

@bot.message_handlers(comands=['start', 'help'])
def start(message):
    pass
@bot.message_handlers(content_type=['documents', 'audio'])
def handler_docs_audio(message):
    pass


