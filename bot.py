import telebot
import config
import random
import requests

from telebot import types
from bs4 import BeautifulSoup

url = 'https://ru.dltv.org/results'
page = requests.get(url)
allResults = []
allTeams = []
filteredResults = []
filteredTeams = []
soup = BeautifulSoup(page.text, "html.parser")
allTeams = soup.findAll('div', class_='match__item-team__name')
allResults = soup.findAll('div', class_='match__item-team__score')
for result in allResults:
    filteredResults.append(result.text)
for team in allTeams:
    filteredTeams.append(team.text)
bot = telebot.TeleBot(config.TOKEN)
l = len(filteredTeams)
filteredMatches=[]
k = 0
for j in range(0, l - 1, 2):
    filteredMatches.append(filteredTeams[j] + filteredResults[j] + '\n' + 'vs' + '\n' + filteredResults[j + 1] + filteredTeams[j + 1])
@bot.message_handler(commands = ['start'])
def welcum(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Результаты за 4 дня")
    item2 = types.KeyboardButton("Мои результаты")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Салам алейкум,{0.first_name}! Уаййяяя".format(message.from_user, bot.get_me()), parse_mode = 'html', reply_markup=markup)

    markup.add(item1, item2)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Результаты за 4 дня':
            for i in range(l // 2):
                bot.send_message(message.chat.id, filteredMatches[i], parse_mode = 'html')
        elif message.text == 'Мои результаты':
            bot.send_message(message.chat.id, "Мужик какая тебе дота иди проспись")
        else:
            bot.send_message(message.chat.id, "Ты шо бубон?")

#RUN
bot.polling(none_stop=True)

