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
    filteredMatches.append(filteredTeams[j] + ' ' + 'vs' + ' ' + filteredTeams[j + 1] + filteredResults[j] + ':' + filteredResults[j + 1])
OneMessage = ''
for i in range(l//2):
    OneMessage = OneMessage + filteredMatches[i] + '\n'
url1 = 'https://ru.dltv.org/stats/heroes?period=1&&order=period_maps&dir=desc'
page1 = requests.get(url1)
allHeroes = []
allNumbers = []
soup1 = BeautifulSoup(page1.text, "html.parser")
allHeroes = soup1.findAll('div', class_='cell__name')
allNumbers = soup1.findAll('div', class_='cell__text')
filteredHeroes = []
filteredNumbers = []
for hero in allHeroes:
    filteredHeroes.append(hero.text)
for number in allNumbers:
    filteredNumbers.append(number.text)
print(len(filteredHeroes[7]))
HeroesandNumbers = []
HeroesandNumbers.append('Герой                 Карты  Баны  %Побед  Ср.время  KDA')
for i in range(123):
    HeroesandNumbers.append(filteredHeroes[i] + ((((22 - len(filteredHeroes[i])) * 3) // 2) * ' ') + filteredNumbers[5 * i] + ((7 - len(filteredNumbers[5 * i])) * ' ') + filteredNumbers[5 * i + 1] + ((6 - len(filteredNumbers[5 * i + 1])) * ' ') + filteredNumbers[5 * i + 2] + ((11 - len(filteredNumbers[5 * i + 2])) * ' ') + filteredNumbers[5 * i + 3] + ((10 - len(filteredNumbers[5 * i + 3])) * ' ')  + filteredNumbers[5 * i + 4])
OneMessage1 = ''
for i in range(31):
    OneMessage1 = OneMessage1 + HeroesandNumbers[i] + '\n'
keyboard1 = types.ReplyKeyboardMarkup(True)
@bot.message_handler(commands = ['start'])
def welcum(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Результаты за 4 дня")
    item2 = types.KeyboardButton("Pro meta last 3 month")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Салам алейкум,{0.first_name}! Уаййяяя".format(message.from_user, bot.get_me()), parse_mode = 'html', reply_markup=markup)

    markup.add(item1, item2)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Результаты за 4 дня':
            bot.send_message(message.chat.id, OneMessage, parse_mode = 'html')
        elif message.text == 'Pro meta last 3 month':
            bot.send_message(message.chat.id, OneMessage1, parse_mode = 'html')
            #bot.send_message(message.chat.id, "Мужик какая тебе дота иди проспись")
        else:
            bot.send_message(message.chat.id, 'Невероятная щедрость от меня - розыгрыш бесплатной арканы, вот ссылочка https://r.mtdv.me/giveaways/dota2')
#RUN
bot.polling(none_stop=True)

