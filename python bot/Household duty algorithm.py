import schedule
import time
from datetime import datetime

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

command_list = list(commands.values())
command_list.append('Лебедєв,Емінов')

def print_duties():
    print(f"Розклад на {datetime.now().strftime('%A %H:%M')}")
    for surnames in command_list:
        print(f"• {surnames}: {', '.join(zones[surnames])}")
    command_list.append(command_list.pop(0))

for day in ['monday', 'wednesday', 'friday']:
    schedule.every().__getattribute__(day).at("08:46").do(print_duties)
    schedule.every().__getattribute__(day).at("08:47").do(print_duties)

while True:
    schedule.run_pending()
    time.sleep(1)