#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит заданное количество конфет. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint


def easy_bot(sweets, max_candy):
    move = randint(1, max_candy) if sweets >= max_candy else randint(1, sweets)
    print(f'Бот забрал {move} конфет')
    sweets -= move
    print(f'Осталось {sweets} конфет')
    return sweets


def hard_bot(sweets, max_candy):
    move = sweets % (max_candy + 1)
    if move == 0:
        move = randint(1, max_candy) if sweets >= max_candy else sweets
    print(f'Бот забрал {move} конфет')
    sweets -= move
    print(f'Осталось {sweets} конфет')
    return sweets


def check_win(sweets, determing_moves, first_name, second_name):
    if sweets == 0:
        return first_name if determing_moves % 2 == 0 else second_name
    else:
        return False


def player_vs_easy_bot():
    name_player = input('Введите свое имя: ')
    sweets = 201
    max_candy = 28
    count_for_check_win = sweets // max_candy
    determing_moves = randint(0, 1)
    win = False
    while not win:
        if determing_moves % 2 == 0:
            sweets = move_player(name_player, sweets, max_candy)
        else:
            sweets = easy_bot(sweets, max_candy)
        if determing_moves >= count_for_check_win - 1:
            temp = check_win(sweets, determing_moves, name_player, 'Бот')
            if temp:
                print(f'{temp} выиграл')
                win = True
        determing_moves += 1


def player_vs_hard_bot():
    name_player = input('Введите свое имя: ')
    sweets = 201
    max_candy = 28
    count_for_check_win = sweets // max_candy
    determing_moves = randint(0, 1)
    win = False
    while not win:
        if determing_moves % 2 == 0:
            sweets = move_player(name_player, sweets, max_candy)
        else:
            sweets = hard_bot(sweets, max_candy)
        if determing_moves >= count_for_check_win - 1:
            temp = check_win(sweets, determing_moves, name_player, 'Бот')
            if temp:
                print(f'{temp} выиграл')
                win = True
        determing_moves += 1


def player_vs_player():
    name_first_player = input('Введите имя первого игрока: ')
    name_second_player = input('Введите имя второго игрока: ')
    sweets = int(input('Введите количество конфет: '))
    max_candy = 28
    count_for_check_win = sweets // max_candy
    determing_moves = randint(0, 1)
    win = False
    while not win:
        if determing_moves % 2 == 0:
            sweets = move_player(name_first_player, sweets, max_candy)
        else:
            sweets = move_player(name_second_player, sweets, max_candy)
        if determing_moves >= count_for_check_win - 1:
            temp = check_win(sweets, determing_moves,
                             name_first_player, name_second_player)
            if temp:
                print(f'{temp} выиграл(а)')
                win = True
        determing_moves += 1


def move_player(name_player, sweets, max_candy):
    valid = False
    while not valid:
        move = input(f'{name_player}, Ваш ход... ')
        try:
            move = int(move)
            if move > 0 and move <= max_candy and move <= sweets:
                print(f'Вы забрали {move} конфет')
                sweets -= move
                print(f'Осталось {sweets} конфет')
                valid = True
            else:
                print(
                    f'Количество взятых конфет должно быть в интервале от 1 до {max_candy} или не больше оставшегося количества конфет')
        except:
            print('Необходимо ввести целое число.')
    return sweets


type_game = input(
    'Введите 1, если хотите играть с другим игроком, и любую другую цифру, если с ботом... ')
if (type_game == '1'):
    player_vs_player()
else:
    intel = input(
        'Введите 0, если хотите играть с глупым ботом, и любую другую цифру, если с умным... ')
    if intel == '0':
        player_vs_easy_bot()
    else:
        player_vs_hard_bot()