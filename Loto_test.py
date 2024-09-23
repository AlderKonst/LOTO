from Loto_class import Players, MultiPlayers, Card, Barrels, Interface

class TestPlayer:
    def test_menu(self): # Не число ли и вне пределов?
        main = Players(1) # Создаём экземпляр класса Players
        assert main.menu == 1 # Проверяем переменню menu
        assert len(main.two_players) == 3 # Проверяем число пар в списке

    def test_two_players(self): # Проверяет список с названиями главного меню
        for i in ['1', '2', '3']: # Проверяется эти три предустановленные пункты
            players = Players(menu=i) # Создаём экземпляр класса Players
            assert players.add_players() == players.two_players[int(i)-1] # Сверяем принадлежность пунктов меню к их именам

class TestMultiPlayers:

    def test_multi_players_zero_more(self): # Для проверки игроков с количеством больше нуля при выборе 4-го пункта
        players = MultiPlayers('2', ['Игрок_1', 'Игрок_2']).multi_players() # Создаём экземпляр модель класса Players
        assert len(players) == 2 # Два ли игрока в итоге возвращает функция multi_players()?
        assert players == ['Игрок_1', 'Игрок_2'] # Именно переданный объекту список возвращает?

    def test_multi_players_invalid_value(self): # Для проверки выбора значения по-умолчанию при вводе некоррентных данных
         for i in ['0', 'a']: # Проверяется эти два неверные значения количества игроков
            players = MultiPlayers(players_count=i).multi_players() # Создаём экземпляр модель класса Players
            assert players == ['Моя карточка', 'Карточка компа']

class TestCard:
    def test_create_card_list(self): # Для проверки генерации карточек
        card_lst = Card().create_card_list() # Cоздаём экземпляр метода класса
        assert len(card_lst) == 3 # Три ли строчки в карточке?
        for str_lst in card_lst: # Перебираем строчки (вложенные листы) в карточке
            assert len(str_lst) == 9 # 9 ли элементов в строчке (во вложенных листах) карточки?
            assert str_lst.count('') == 4 # Есть ли в них 4 пустые строки?
            assert len(set([str_lst[i] for i in range(len(str_lst))])) > 2 # Рандомно ли перебираются цифры в этих строчках?

class TestBarrels:
    def test_create_barrels_list(self): # Для проверки создания списка с 90 бочонками
        barrels_lst = Barrels().create_barrels_list() # Cоздаём экземпляр метода класса
        assert len(barrels_lst) == 90 # В листе 90 элементов (бочонков)?
        assert len(set(barrels_lst)) == len(barrels_lst) # Они разные?

class TestInterface:
    def test_interface(self): # Для проверки инициированных переменных
        card_lst = Card().create_card_list() # Cоздаём экземпляр метода класса c картами
        barrels_lst = Barrels().create_barrels_list() # А теперь экземпляр метода класса с бочонками
        interface = Interface(['Игрок_1', 'Игрок_2'], card_lst, barrels_lst) # И объект предитогового класса

        assert interface.players == ['Игрок_1', 'Игрок_2'] # Сохраняет ли неизменно в переменную поданный лист?

        # Ни дескрипторы, ни общий класс почему-то не помогли, пока что оставим дублированными ... на следующий раз
        assert len(card_lst) == 3 # Три ли строчки в переданной карточке?
        for str_lst in card_lst: # Перебираем строчки (вложенные листы) в переданной карточке
            assert len(str_lst) == 9 # 9 ли элементов в строчке (во вложенных листах) этой карточки?
            assert str_lst.count('') == 4 # Есть ли в них 4 пустые строки?
            assert len(set([str_lst[i] for i in range(len(str_lst))])) > 2 # Рандомно ли перебираются цифры в этих строчках?

        # Такая же ситуёвина
        assert len(barrels_lst) == 90 # В переданном листе 90 элементов (бочонков)?
        assert len(set(barrels_lst)) == len(barrels_lst) # Они разные?

        assert len(interface.players) == len(interface.count_dict) # Совпадают ли количество игроков в словаре и списке?
        assert interface.players == [i for i, _ in interface.count_dict.items()] # Одинаковые ли имена игроков в списке и словаре?
class TestGame:
    pass