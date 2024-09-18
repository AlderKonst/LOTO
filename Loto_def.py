# Декораторы опять лишь мешают, из-за него рандомность работает не так как надо, да и зачем лишь для одной функции ...
# def decorate_print(f): # Декоратор для выделения карточек с именем игрока
#    def wrapper(name):
#        print('-' * (16 - int(0.5 * len(name))), name, '-' * (16 - int(0.5 * len(name))))
#        result = f(name)
#        print('-' * 34)
#        return result
#    return wrapper

import random

# Код для любого количества игроков
def players_add ():
    my_card = 'Моя карточка'
    pc_card = 'Карточка компа'
    players = []
    menu = input('1. Игра между двумя людьми\n2. Игра между двумя компами\n'
                 '3. Игра между человеком и компом\n4. Свой вариант\nВведите пункт меню: \n')
    if menu == '1':
        players = [f'{my_card}_1', f'{my_card}_2'] # Разные, чтобы не возникало ошибок
    elif menu == '2':
        players = [f'{pc_card}_1', f'{pc_card}_2'] # Разные, чтобы не возникало ошибок
    elif menu == '3':
        players = [my_card, pc_card]
    elif menu == '4':
        try:
            players_count = int(input('Введите количество игроков\n'))
            players = [input(f'Введите {i}-го игрока\n') for i in range(players_count)]
        except ValueError:
            print('Нужно было вводить целое цисло')
    else:
        players = [my_card, pc_card]
        print('Введён некорректный номер, взяты значения по умолчанию')

    return players

# Создание списка с числами от 0 до 90
def range_list():
    return list(range(1, 91))

# Создание двумерного списка с рандомными числами по возрастанию и пустотами
def card_list():
    rand_lst = random.sample(list(range(1, 91)), 27)
    rand_lst = [sorted(rand_lst[:9]), sorted(rand_lst[9:18]), sorted(rand_lst[18:27])]
    card_lst = []

    for i in rand_lst:
        for j in random.sample([j for j in range(9)], 4):
            i[j] = ''
        card_lst.append(i)

    return card_lst

# Создание словаря с пользователями
players = players_add()
def users_card(players):
    return {i: card_list() for i in players}

users = users_card(players)  # Словарь игроков с карточками
barrel_lst = range_list()  # Оставшиеся бочёнки

# Удаляет элемент списка barrel_lst и возвращает удалённое
def barrel_del():
    return barrel_lst.pop(random.randint(0, len(barrel_lst) - 1))

# Вывод интерфейса
def card_interface(users):
    count_dict = {i: 0 for i in players}  # Словарь количества элементов с '-' у каждого игрока
    bal = True  # Зачёркиваем или продолжаем
    while bal:
        yes_num = False # Угадана ли цифра?
        new_barrel = barrel_del() # Список оставшихся бочёнков
        print(f'Новый бочонок: {new_barrel} (осталось {len(barrel_lst)})') # Для вывода карточек всех пользователей

        # Проход циклом по словарю с карточкой каждого пользователя
        for name, lst in users.items():

            # Для зачёркивания (scratch) угаданного
            new_lst = [] # Инициация новой карточки

            for i in lst:
                if new_barrel in i:
                    yes_num = True
                    scratch_index = i.index(new_barrel)
                    i[scratch_index] = '-'
                    count_dict[name] += 1
                new_lst.append(i)
            users[name] = new_lst

            # Отображение карточек в 3 строки кода во избежание трудночитаемой слишком длинной
            print('-' * (16 - int(0.5 * len(name))), name, '-' * (16 - int(0.5 * len(name))))
            print('\n'.join(['\t'.join(map(str, i)) for i in lst]))
            print('-' * 34)

        # Проверка наличия угаданного числа
        if yes_num:
            print('Есть')

        try:
            yes_no = input('Зачеркнуть цифру? (y/n)\n')
            if (yes_no == 'y' and not yes_num) or (yes_no != 'y' and yes_num):
                print('Игра завершена с проигрышем!')
                break
        except Exception:
            print('Как такое тут вообще могло получиться!?')

        # Проверяем заполнена ли вся карточка штрихом и определяем первого победителя
        for name, num in count_dict.items():
            if num == 15:
                bal = False
                print('Победитель: ', name)
                break

card_interface(users)
