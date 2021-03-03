light = input("what light is active now?: ")    # получение цвета светофора

if light == "red":                              # красный свет
    print("SIGNAL: STOP")
elif light == "yellow":                         # желтый цвет
    print("SIGNAL: COLORS ARE ABOUT TO CHANGE (from red to green; from green to red")
elif light == "green":                          # зеленый цвет
    print("SIGNAL: MOVE")
else:
    print("seems like there is no {0} light -_-".format(light)) # в случае если введен другой цвет