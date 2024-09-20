import random

class Players:

    def __init__(self, menu=None, two_players=[['Моя карточка_1', 'Моя карточка_2'],
                                               ['Карточка компа_1', 'Карточка компа_2'],
                                               ['Моя карточка', 'Карточка компа']]):
        self.menu = menu or input('1. Игра между двумя людьми\n'
                                  '2. Игра между двумя компами\n'
                                  '3. Игра между человеком и компом\n'
                                  '4. Игра с произвольным количеством игроков\n'
                                  'Введите пункт меню: \n')
        self.two_players = two_players

    def add_players(self): # Код для добавления любого количества игроков
        start_menu = self.menu # Вызов главного меню
        if start_menu == '1':
            return self.two_players[0] # 'Моя карточка_1', 'Моя карточка_2'
        elif start_menu == '2':
            return self.two_players[1] # 'Карточка компа_1', 'Карточка компа_2'
        elif start_menu == '3':
            return self.two_players[2] # 'Моя карточка', 'Карточка компа'
        elif start_menu == '4':
            return MultiPlayers().multi_players() # Вызывается функция для произвольного количества игроков
        else:
            print('Введено не число в пределах от 1 до 4, взяты карточки по умолчанию')
            return self.two_players[2] # 'Моя карточка', 'Карточка компа'

class MultiPlayers(Players):
    def __init__(self, players_count=None, players=None):
        self.players_count = players_count or input("Введите количество игроков: ")
        self.players_count_num = int(self.players_count) if self.players_count.isdigit() else 0 # Для присвоения только чисел
        self.players = players or [input(f"Введите имя {i + 1}-го игрока: ") for i in range(self.players_count_num)]

    def multi_players(self): # Для добавления произвольного количества игроков
        players_count_menu = self.players_count_num # Выбор количества игроков
        if players_count_menu > 0: # Только если введено количество игроков больше нуля
            players_names = self.players # Ввод имён игроков
            return players_names # Возвращаем список игроков
        else:
            print("Введено число ниже нуля или произвольный символ, взяты карточки по умолчанию")
            return ['Моя карточка', 'Карточка компа'] # Чтобы излишне не усложнять инициализатор


class Card:

    def create_card_list(self): # Создание двумерного списка с рандомными числами по возрастанию и пустотами
        rand_lst = random.sample(list(range(1, 91)), 27) # Создаем список из 27 случайных чисел от 1 до 90
        rand_lst = [sorted(rand_lst[:9]), sorted(rand_lst[9:18]), sorted(rand_lst[18:27])]
        card_lst = [] # Создаем пустой список для итоговой карточки

        for i in rand_lst: # Заполняем карточку числами и пустотами
            for j in random.sample([j for j in range(9)], 4): # Выбираем 4 случайных индекса для пустых ячеек
                i[j] = '' # Делаем эту ячейку пустой
            card_lst.append(i) # Добавляем строку в карточку

        return card_lst

class Barrels:

    def create_barrels_list(self):
        return list(range(1, 91)) # Создание списка бочонков с числами от 0 до 90

class Interface:

    def __init__(self, players, card_lst, barrel_lst):
        self.players = players # Список игроков
        self.card_lst = card_lst # Словарь, где ключ - имя игрока, значение - его карточка
        self.barrel_lst = barrel_lst # Список бочонков
        self.count_dict = {i: 0 for i in self.players}

    def delete_barrel(self): # Удаляет элемент списка barrel_lst и возвращает удалённое
        return self.barrel_lst.pop(random.randint(0, len(self.barrel_lst) - 1))

    def print_cards(self):  # Для вывода карточек всех пользователей
        for name, lst in self.card_lst.items():
            # Отображение карточек в 3 строки кода во избежание трудночитаемой слишком длинной
            print('-' * (16 - int(0.5 * len(name))), name, '-' * (16 - int(0.5 * len(name))))
            print('\n'.join(['\t'.join(map(str, i)) for i in lst]))
            print('-' * 34)

    def update_cards(self, new_barrel): # Обновляет карточки игроков после вытаскивания нового бочонка
        yes_num = False # Зачеркнуто ли число хотя бы у одного игрока
        for name, lst in self.card_lst.items(): # Проходим по каждому игроку и его карточке
            new_lst = [] # Создаем новый список для обновленной карточки
            for i in lst: # Проходим по каждой строке карточки
                if new_barrel in i: # Если число есть на карточке
                    yes_num = True # Устанавливаем флаг
                    scratch_index = i.index(new_barrel) # Находим индекс числа в строке
                    i[scratch_index] = '-' # Зачеркиваем число
                    self.count_dict[name] += 1 # Увеличиваем счетчик зачеркнутых чисел для игрока
                new_lst.append(i) # Добавляем обновленную строку в новый список
            self.card_lst[name] = new_lst # Заменяем старую карточку на новую
        return yes_num

    def check_cards(self, yes_num): # Проверяет, правильно ли игрок зачеркнул число
        print('Есть' if yes_num else '') # Сообщаем, есть ли зачеркнутое число у кого-либо

        yes_no = input('Зачеркнуть цифру?\nДа - y, Нет - другие символы\n')
        if (yes_no == 'y' and not yes_num) or (yes_no != 'y' and yes_num): # Проверяем на ошибку
            print('Игра завершена с проигрышем!')
            return False
        return True

    def check_winner(self): # Проверяет, есть ли победитель (т.е. игрок с 15 зачеркнутыми числами)
        for name, num in self.count_dict.items():
            if num == 15: # Если игрок зачеркнул все числа
                print('Победитель: ', name)
                return False
        return True

    def card_interface(self): # Основной игровой цикл
        while True:
            new_barrel = self.delete_barrel() # Вытягиваем новый бочонок
            print(f'Новый бочонок: {new_barrel} (осталось {len(self.barrel_lst)})')
            self.print_cards() # Отображаем карточки
            yes_num = self.update_cards(new_barrel) # Обновляем карточки
            if not self.check_cards(yes_num): # Проверяем, правильно ли зачеркнуто число
                break

            if not self.check_winner(): # Проверяем, есть ли победитель
                break
class Game:

    def gaming(self):
        players = Players().add_players()  # Создание списка игроков
        barrel_lst = Barrels().create_barrels_list()  # Создание списка бочонков

        users = {}  # Создание словаря, где будет ключ - имя игрока, значение - его карточка
        for player in players:  # Создаем новую колоду для каждого игрока
            card_lst = Card().create_card_list()  # Создаем новую колоду
            users[player] = card_lst  # Для каждого игрока

        game = Interface(players, users, barrel_lst)  # Создание экземпляра интерфейса игры, процессов
        game.card_interface()  # Запуск игрового процесса

if __name__ == '__main__':
    gaming = Game() # Экземпляр игры
    gaming.gaming() # Запуск!