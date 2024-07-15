from datetime import datetime
from translate import Translator
from time import sleep

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

while True:
    current_date = datetime.now()
    formatted_date = current_date.strftime("%A %H:%M")
    day, time = formatted_date.split(" ")
    while day in ['Monday', 'Wednesday', 'Friday'] and time in ['18:24', '13:00']:
        current_date = datetime.now()
        formatted_date = current_date.strftime("%A %H:%M")
        day, time = formatted_date.split(" ")
        translator = Translator(to_lang='uk')
        translated_date = translator.translate(day)
        general_dictionary = {key:{'mention':commands[key-1],'zone':zones[key-1]} for key in range(1,7)}
        message = str()
        start_text =f'❗*Розклад на {translated_date}*❗'
        message += start_text
        for i in general_dictionary.values():
            message += (f"• {' '.join(i['mention'])}: {', '.join(i['zone'])}\n")
        print(message + '• @osygne @iEmirAld: унітази, біде, дзеркало, раковини')

        commands.append(commands.pop(0))
        sleep(7200)
    else:
        sleep(1)
