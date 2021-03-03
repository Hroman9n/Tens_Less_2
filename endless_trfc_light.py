import time

### функции для работы программы ###

def red_init():     # для бесконечного цикла, если задан красный цвет как стартовый
    while 1:
        print("\nRED SIGNAL: STOP", '\n')
        time.sleep(3)
        print("YELLOW SIGNAL: BE READY TO GREEN SIGNAL AND MOVE", '\n')
        time.sleep(1)
        print("GREEN SIGNAL: MOVE", '\n')
        time.sleep(3)
        print("YELLOW SIGNAL: BE READY TO RED SIGNAL AND STOP MOVING")
        time.sleep(1)

def green_init():   # для бесконечного цикла, если задан зеленый цвет как стартовый
    while 1:
        print("\nGREEN SIGNAL: MOVE", '\n')
        time.sleep(3)
        print("YELLOW SIGNAL: BE READY TO RED SIGNAL AND STOP MOVING", '\n')
        time.sleep(1)
        print("RED SIGNAL: STOP", '\n')
        time.sleep(3)
        print("YELLOW SIGNAL: BE READY TO GREEN SIGNAL AND MOVE")
        time.sleep(1)


# функция для проверки света
def light_chk(light):
    if light == "red":                              # красный свет
        print("SIGNAL: STOP")
    elif light == "yellow":                         # желтый цвет
        print("SIGNAL: COLORS ARE ABOUT TO CHANGE (from red to green; from green to red)")
    elif light == "green":                          # зеленый цвет
        print("SIGNAL: MOVE")
    else:
        print("seems like there is no {0} light -_-".format(light)) # в случае если введен другой цвет

### конец вспомогательных функций ###


### Основные функции ###

def no_sleep():     # функция, если пользователь решил вбивать цвета руками
    chk = input("please write active light or exit if you want to quit the script: ")
    print()

    while chk != "exit":
        light_chk(chk)
        print()
        chk = input("please write active light or exit if you want to quit the script: ")
        print()


def with_sleep():       # функция для автоматической прокрутки светофора
    print()

    start = input("please write initial light (you can exit script by pressing ctrl+C): ")
    print()

    if start == "red":
        red_init()
    elif start == "green":
        green_init()
    elif start == "yellow":     # мы не можем определить порядок цветов, если нам передается просто желтый
        print("\n Cannot determine next color, please try enter red or green next time\n")
    else:
        print("seems like there is no {0} light -_-".format(start))
    
### конец основных функций ###


### отсюда начинается вызов программы ###
slp = input("are you gonna write light manualy (write man) or you want write just one light and let system cycle lights (write auto)? ")
print()

if slp == "man":
    no_sleep()
elif slp == "auto":
    with_sleep()
else:
    print("please, write man or auto instead of {0} next time".format(slp))
    exit 


print("\n thats all ^_^, be careful on the roads \n")