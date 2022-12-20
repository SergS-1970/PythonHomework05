# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

candies = 333
max_move = 28

def Player_vs_player(candies, max_move):
    player = 0
    name_first_player = input('Введите имя первого игрока: ')
    name_second_player = input('Введите имя второго игрока: ')

    first_move = randint(1, 2)
    while candies > 0:
        if first_move == 1:
            player = 1
            print(f'Ход игрока {name_first_player}.')
            move = int(
                input('Введите количество конфет, которые Вы заберете: '))
            if move < 1 or move > max_move:
                print('Некорректное количество, попробуйте ещё раз: ')
                move = int(input('Введите количество конфет, которые Вы заберете: '))
            candies -= move
            print(f'Осталось {candies} конфет.')
            if candies == 0:
                break
            
            player = 2
            print(f'Ход игрока {name_second_player}.')
            move = int(
                input('Введите количество конфет, которые Вы заберете: '))
            if move < 1 or move > max_move:
                print('Некорректное количество, попробуйте ещё раз: ')
                move = int(input('Введите количество конфет, которые Вы заберете: '))
            
            candies -= move
            print(f'Осталось {candies} конфет.')
        else:
            player = 2
            print(f'Ход игрока {name_second_player}.')
            move = int(
                input('Введите количество конфет, которые Вы заберете: '))
            if move < 1 or move > max_move:
                print('Некорректное количество, попробуйте ещё раз: ')
                move = int(input('Введите количество конфет, которые Вы заберете: '))
            candies -= move
            print(f'Осталось {candies} конфет.')
            if candies == 0:
                break

            player = 1
            print(f'Ход игрока {name_first_player}.')
            move = int(
                input('Введите количество конфет, которые Вы заберете: '))
            if move < 1 or move > max_move:
                print('Некорректное количество, попробуйте ещё раз: ')
                move = int(input('Введите количество конфет, которые Вы заберете: '))
            candies -= move
            print(f'Осталось {candies} конфет.')

    name_winner = name_first_player if player == 1 else name_second_player
    print(f'Победил игрок {name_winner}')


def Player_vs_bot(candies, max_move, intel):
    player = 0
    name_player = input('Введите свое имя: ')

    first_move = randint(1, 2)
    while candies > 0:
        if first_move == 1:
            player = 1
            print(f'Ход игрока {name_player}.')
            move = int(
                input('Введите количество конфет, которые Вы заберете: '))
            if move < 1 or move > max_move:
                print('Некорректное количество, попробуйте ещё раз: ')
                move = int(input('Введите количество конфет, которые Вы заберете: '))
            candies -= move
            print(f'Осталось {candies} конфет.')
            if candies == 0:
                break

            player = 2
            if candies <= max_move:
                move = candies
            else:
                if intel == 0:
                    move = randint(1, max_move)
                else:
                    move = candies - max_move * (candies // max_move) - 1
                    if move <= 0:
                        move += max_move
            print(f'Бот забрал {move} конфет.')
            candies -= move
            print(f'Осталось {candies} конфет.')
        else:
            player == 2
            if candies <= max_move:
                move = candies
            else:
                if intel == 0:
                    move = randint(1, max_move)
                else:
                    move = candies - max_move * (candies // max_move) - 1
                    if move <= 0:
                        move += max_move
            print(f'Бот забрал {move} конфет.')
            candies -= move
            print(f'Осталось {candies} конфет.')
            if candies == 0:
                break

            player = 1
            print(f'Ход игрока {name_player}.')
            move = int(
                input('Введите количество конфет, которые Вы заберете: '))
            if move < 1 or move > max_move:
                print('Некорректное количество, попробуйте ещё раз: ')
                move = int(input('Введите количество конфет, которые Вы заберете: '))
            candies -= move
            print(f'Осталось {candies} конфет.')
    if player == 1:
        name_winner = name_player
    else:
        name_winner = 'бот'
    print(f'Победил(а) {name_winner}')


candies = 333
max_move = 28
type_game = int(input(
    'Введите 1, если хотите играть с другим игроком, и любую другую цифру, если с ботом... '))
if (type_game == 1):
    Player_vs_player(candies, max_move)
else:
    intel = int(input(
        'Введите 0, если хотите играть с глупым ботом, и любую другую цифру, если с умным... '))
    Player_vs_bot(candies, max_move, intel)
