import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from datetime import time
import pytz
from datetime import datetime

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

commands = {
    1: 'Чаплигін,Сушко', 2: 'Дядичкін,Омельченко', 3: 'Кащенко,Хоменко',
    4: 'Горфінкель,Танцюра', 5: 'Левицький,Поборцев', 6: 'Димитренко,Ткачов'
}

zones = {
    commands[1]: ['плита', 'стіл', 'поверхні', 'холодильники зовні та зверху'],
    commands[2]: ['відсутність сміття', 'відсутність брудного посуду', 'духовка', 'помити смітник'],
    commands[3]: ['фасади', 'підвіконня', 'підлогу підмести, помити'],
    commands[4]: ['столи', 'тумба', 'стіл (телевізор)', 'підлогу підмести, помити'],
    commands[5]: ['протерти пил', 'помити підлогу', 'викинути сміття', 'відсутність зайвих речей на столах та підлозі', 'гардероб: підлогу, відсутність зайвих речей'],
    commands[6]: ['винести сміття', 'помити смітник', 'душові кабіни', 'килимки', 'підлогу підмести, помити'],
    'Лебедєв,Емінов': ['унітази', 'біде', 'дзеркало', 'раковини']
}

command_list = list(commands.values()) + ['Лебедєв,Емінов']

current_date = datetime.now()
formatted_date = current_date.strftime('%d.%m')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text="Yo imma schedule bot")

async def print_duties(update:Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    message = f"*Розклад ({formatted_date}):*\n"
    for surnames in command_list:
        message += f"• {surnames}: {', '.join(zones[surnames])}\n"
    command_list.append(command_list.pop(0))
    # await context.bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')
    context.job_queue.run_daily(context.bot.send_message(chat_id=chat_id, text=message), time=time(hour=12,minute=56,tzinfo=pytz.timezone('Europe/Kyiv')),chat_id=update.effective_chat.id)

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