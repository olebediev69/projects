import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from datetime import time
import pytz
from datetime import datetime
from time import sleep
from translate import Translator

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

commands = [['@chaplygvad @ugubugu'], ['@glebkaa @omal1k'], ['@KashchenkoMax @khomenko_pavlo'],
    ['@facelesss148 @caplit'], ['@nazarr_lev @tserbermax'], ['@Alex_sport96 @VioTuro']]
zones = [
    ['плита', 'стіл', 'поверхні', 'холодильники зовні та зверху'],
    ['відсутність сміття', 'відсутність брудного посуду', 'духовка', 'помити смітник'],
    ['фасади', 'підвіконня', 'підлогу підмести, помити'],
    ['столи', 'тумба', 'стіл (телевізор)', 'підлогу підмести, помити'],
    ['протерти пил', 'помити підлогу', 'викинути сміття', 'відсутність зайвих речей на столах та підлозі;', 'гардероб: підлогу, відсутність зайвих речей'],
    ['винести сміття', 'помити смітник', 'душові кабіни', 'килимки', 'підлогу підмести, помити'],
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text="Yo imma schedule bot")

async def print_duties(update:Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    current_date = datetime.now()
    formatted_date = current_date.strftime("%A %H:%M")
    day, time = formatted_date.split(" ")
    while day in ['Monday', 'Wednesday', 'Friday'] and time in ['17:19', '13:00']:
        current_date = datetime.now()
        formatted_date = current_date.strftime("%A %H:%M")
        day, time = formatted_date.split(" ")
        translator = Translator(to_lang='uk')
        translated_date = translator.translate(day)
        general_dictionary = {key: {'mention': commands[key - 1], 'zone': zones[key - 1]} for key in range(1, 7)}
        message = str()
        start_text =(f'❗*Розклад на {translated_date}*❗')
        message += start_text
        for i in general_dictionary.values():
            message += (f"• {' '.join(i['mention'])}: {', '.join(i['zone'])}\n")
        context.bot.send_message(chat_id=chat_id, text=message + '• @osygne @iEmirAld: унітази, біде, дзеркало, раковини', parse_mode='Markdown')

        commands.append(commands.pop(0))
        sleep(7200)
    else:
        sleep(1)
    # context.job_queue.run_daily(context.bot.send_message(chat_id=chat_id, text=message), time=time(hour=12,minute=56,tzinfo=pytz.timezone('Europe/Kyiv')),chat_id=update.effective_chat.id)

async def normal_duties(update: Update, context: ContextTypes.DEFAULT_TYPE):
    job_kwargs = {
        'time': time(hour=12, minute=21, tzinfo=pytz.timezone('Europe/Kyiv')),
        'days': (0, 2, 4),
        'chat_id': update.effective_chat.id
    }
    context.job_queue.run_daily(print_duties, **job_kwargs)

if __name__ == '__main__':
    application = ApplicationBuilder().token('6860832765:AAE-blKVnHYc1-QFt1r7aM4OTzdX3lpz0NM').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    print_duties_handler = CommandHandler('d', print_duties)
    application.add_handler(print_duties_handler)

    normal_duties_handler = CommandHandler('n', normal_duties)
    application.add_handler(normal_duties_handler)

    application.run_polling()