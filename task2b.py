# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#
# b) Подумайте как наделить бота ""интеллектом""



a = 221
while a > 0:
    if a > 58:
        if a % 28 == 0:
            move_comp = 28
        else:
            move_comp = a % 28 -1
        a -= move_comp
        print(f'Компьютер убрал {move_comp} конфет')
        if a == 0:
            print('Победа компьютера!')
        print(f'Осталось {a} конфет')
        a -= int(input())
        if a == 0:
            print('Победа игрока!')
        print(f'Осталось {a} конфет')
    elif a < 59:
        if a == 57:
            move_comp = 28
            a -= move_comp
            print(f'Компьютер убрал {move_comp} конфет')
            print(f'Осталось {a} конфет')
        elif 29 < a < 57:
            move_comp = a - 29
            a -= move_comp
            print(f'Компьютер убрал {move_comp} конфет')
            print(f'Осталось {a} конфет')
        a -= int(input())
        print(f'Осталось {a} конфет')
        if a < 29:
            move_comp = a
            a -= move_comp
            print(f'Компьютер убрал {move_comp} конфет')
            print('Победа компьютера!')
        else:
            print('Победа игрока')
