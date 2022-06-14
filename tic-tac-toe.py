def greet():
    print("Добро пожаловать в игру")
    print("    Крестики нолики    ")
    print("x - номер строки")
    print("y - номер столбца")
    print("формат ввода: х y")

def show():
    print("    | 0 | 1 | 2 | ")
    print("------------------")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("------------------")
    print()
def ask():
    while True:
        cords = input("Ваш ход:").split()
        if len(cords) != 2:
            print("Введите вторую координату")
            continue
        x, y = cords
        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа!")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2 :
            print("Выход за пределы поля!")
            continue
        if field[x][y] != " ":
            print("Клетка уже занята!")
            continue
        return x, y
def combi_win():
    cords_win = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in cords_win:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выйграл крестик!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выйграл нолик!")
            return True
    return False
greet()
field = [[" "] * 3 for i in range(3) ]
count = 0
while True:
    count += 1
    show()
    if count % 2 ==1:
        print("Ходит крестик!")
    else:
        print("Ходит нолик!")
    x, y = ask()
    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if combi_win():
        break

    if count == 9:
        print("Ничья!")
        break
