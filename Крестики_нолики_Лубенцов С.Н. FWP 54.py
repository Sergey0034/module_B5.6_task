print("Привет!")
print("Давай сыграем в игру!")
print("Я думаю, что тебе прекрасно знакома игра \'крестики - нолики\'")
print("Начнем игру!")
field = [["-"]*3 for i in range(3)]
def playing_field():
    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {field[i][0]} {field[i][1]} {field[i][2]}")
def motion():
    x,y = map(int, input("Ваш ход: ").split())
    if 0 <= x <= 2 and 0 <= y <= 2:
        if field[x][y] == "-":
            return x,y
        else:
            print("Координата занята! Введите другую")
            return motion()
    else:
        print("Введите координаты: два числа через пробел в диапозоне от 0 до 2")
        return motion()

def win():
    for i in range(3):
        positions = []
        for j in range(3):
            positions.append(field[i][j])
        if positions == ["X","X","X"]:
            print("Поздравляем! Выиграл Крестик!")
            return True
        elif positions == ["0","0","0"]:
            print("Поздравляем! Выиграл Нолик!")
            return True

    for i in range(3):
        positions = []
        for j in range(3):
            positions.append(field[j][i])
        if positions == ["X", "X", "X"]:
            print("Поздравляем! Выиграл Крестик!")
            return True
        elif positions == ["0", "0", "0"]:
            print("Поздравляем! Выиграл Нолик!")
            return True

        positions = []
        for i in range(3):
            positions.append(field[i][i])
        if positions == ["X", "X", "X"]:
            print("Поздравляем! Выиграл Крестик!")
            return True
        elif positions == ["0", "0", "0"]:
            print("Поздравляем! Выиграл Нолик!")
            return True

        positions = []
        for i in range(3):
            positions.append(field[i][2-i])
        if positions == ["X", "X", "X"]:
            print("Поздравляем! Выиграл Крестик!")
            return True
        elif positions == ["0", "0", "0"]:
            print("Поздравляем! Выиграл Нолик!")
            return True


num = 0
while True:
    num+=1
    playing_field()
    if num % 2 == 1:
        print("Ходит Крестик")
    else:
        print("Ходит Нолик")
    x, y = motion()
    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    if win():
        break
    if num == 9:
        print("Игра закончилась! Ничья")
        break
