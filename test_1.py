temperature = int(input("Введите температуру"))
isRain = input("Идет ли дождь: да или нет?")
heaver_rain = input("Дождь сильный: да или нет?")
if 20<temperature<30:
    if "да" in isRain:
        print("Футболку, шорты и дождивик")
    else:
        print("футболку и шорты")
else:
    if temperature<0:
        print("Пуховик")
    else:
        if "нет" in isRain:
            print("Пальто")
        else:
            if "нет" in heaver_rain:
                print("Пальто и дождивик")
            else:
                print("Пальто, резиновые сапоги и зонт")