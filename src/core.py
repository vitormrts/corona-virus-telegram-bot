from telegram.ext import CommandHandler, Filters, MessageHandler, Updater, Dispatcher
from telegram import Bot, Update
import os
from conf.settings import TELEGRAM_TOKEN
import json


def read_json():
    with open('/home/vitormrts/Área de Trabalho/Projects/corona-virus-telegram-bot/src/ranking.json', 'r', encoding='utf8') as f:
        return json.load(f)


def total_cases(bot, update: Update, **optional_args):
    data = read_json()
    data_cases = data['totcases']
    i = 0
    msg = ''
    for case in data_cases:
        if i == 0:
            msg += f"{case['total']} total active cases in World 🤒🌎\n\n"
        else:
            msg += f"{i}) {case['country']}\nTotal cases: {case['total']}\n\n"
        i += 1
    bot.message.reply_text(msg, quote=False)


def new_cases(bot, update: Update):
    data = read_json()
    data_cases = data['newcases']
    i = 0
    msg = ''
    for case in data_cases:
        if i == 0:
            msg += f"{case['total']} total active cases in World 🤒🌎\n\n"
        else:
            msg += f"{i}) {case['country']}\nTotal cases: {case['total']}\n\n"
        i += 1

    bot.message.reply_text(msg, quote=False)


def total_deaths(bot, update: Update):
    data = read_json()
    data_cases = data['totdeaths']
    msg = ''
    i = 0
    for case in data_cases:
        if i == 0:
            msg += f"{case['total']} total active cases in World 🤒🌎\n\n"
        else:
            msg += f"{i}) {case['country']}\nTotal cases: {case['total']}\n\n"
        i += 1

    bot.message.reply_text(msg, quote=False)


def new_deaths(bot, update: Update):
    data = read_json()
    data_cases = data['newdeaths']
    i = 0
    msg = ''
    for case in data_cases:
        if i == 0:
            msg += f"{case['total']} total active cases in World 🤒🌎\n\n"
        else:
            msg += f"{i}) {case['country']}\nTotal cases: {case['total']}\n\n"
        i += 1
    bot.message.reply_text(msg, quote=False)


def total_recovered(bot, update: Update):
    data = read_json()
    data_cases = data['totrecovered']
    i = 0
    msg = ''
    for case in data_cases:
        if i == 0:
            msg += f"{case['total']} total active cases in World 🤒🌎\n\n"
        else:
            msg += f"{i}) {case['country']}\nTotal cases: {case['total']}\n\n"
        i += 1

    bot.message.reply_text(msg, quote=False)


def active_cases(bot, update: Update):
    data = read_json()
    data_cases = data['activecases']
    msg = ''
    i = 0
    for case in data_cases:
        if i == 0:
            msg += f"{case['total']} total active cases in World 🤒🌎\n\n"
        else:
            msg += f"{i}) {case['country']}\nTotal cases: {case['total']}\n\n"
        i += 1

    bot.message.reply_text(msg, quote=False)


def webhook():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('totalcases', total_cases))
    dispatcher.add_handler(CommandHandler('newcases', new_cases))
    dispatcher.add_handler(CommandHandler('totaldeaths', total_deaths))
    dispatcher.add_handler(CommandHandler('newdeaths', new_deaths))
    dispatcher.add_handler(CommandHandler('totalrecovered', total_recovered))
    dispatcher.add_handler(CommandHandler('activecases', active_cases))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    webhook()
