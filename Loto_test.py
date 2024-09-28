from Loto_class import Players, MultiPlayers, Card, Barrels, Interface, Game # Импортируем тестируемые классы

class TestPlayer:
    def test_menu(self): # Не число ли и вне пределов?
        main = Players(1) # Создаём экземпляр класса Players
        assert main.menu == 1 # Проверяем переменню menu
        assert len(main.two_players) == 3 # Проверяем число пар в списке

    def test_two_players(self): # Проверяет список с названиями главного меню
        for i in ['1', '2', '3']: # Проверяется эти три предустановленные пункты
            players = Players(menu=i) # Создаём экземпляр класса Players
            assert players.add_players() == players.two_players[int(i)-1] # Сверяем принадлежность пунктов меню к их именам

    def test_players_magic(self): # Корректно ли переопределённые магические методы сравнения работают?
        x = Players(menu='1', two_players='a')
        y = Players(menu='1', two_players='a')
        z = Players(menu='2', two_players='b')
        assert x == y
        assert x != z

class TestMultiPlayers:

    def test_multi_players_zero_more(self): # Для проверки игроков с количеством больше нуля при выборе 4-го пункта
        players = MultiPlayers('2', ['Игрок_1', 'Игрок_2']).multi_players() # Создаём экземпляр модель класса Players
        assert len(players) == 2 # Два ли игрока в итоге возвращает функция multi_players()?
        assert players == ['Игрок_1', 'Игрок_2'] # Именно переданный объекту список возвращает?

    def test_multi_players_invalid_value(self): # Для проверки выбора значения по-умолчанию при вводе некоррентных данных
         for i in ['0', 'a']: # Проверяется эти два неверные значения количества игроков
            players = MultiPlayers(players_count=i).multi_players() # Создаём экземпляр модель класса Players
            assert players == ['Моя карточка', 'Карточка компа'] # Эти ли?

    def test_multi_players_magic(self): # Корректно ли переопределённые магические методы сравнения работают?
        x = MultiPlayers(players_count='1', players='a')
        y = MultiPlayers(players_count='1', players='a')
        z = MultiPlayers(players_count='2', players='b')
        assert x == y
        assert x != z

class TestCard:
    def test_create_card_list(self): # Для проверки генерации карточек
        card_lst = Card()() # Cоздаём экземпляр метода класса
        assert len(card_lst) == 3 # Три ли строчки в карточке?
        for str_lst in card_lst: # Перебираем строчки (вложенные листы) в карточке
            assert len(str_lst) == 9 # 9 ли элементов в строчке (во вложенных листах) карточки?
            assert str_lst.count('') == 4 # Есть ли в них 4 пустые строки?
            assert len(set([str_lst[i] for i in range(len(str_lst))])) > 2 # Рандомно ли перебираются цифры в этих строчках?

    def test_card_magic(self): # Корректно ли переопределённые магические методы сравнения работают?
        x = Card(magic='a')
        y = Card(magic='a')
        z = Card(magic='b')
        assert x == y
        assert x != z

class TestBarrels:
    def test_create_barrels_list(self): # Для проверки создания списка с 90 бочонками
        barrels_lst = Barrels().barrel_lst # Cоздаём экземпляр метода класса
        assert len(barrels_lst) == 90 # В листе 90 элементов (бочонков)?
        assert len(set(barrels_lst)) == len(barrels_lst) # Они разные?

    def test_barrels_magic(self): # Корректно ли переопределённые магические методы сравнения работают?
        x = Barrels(magic='a')
        y = Barrels(magic='a')
        z = Barrels(magic='b')
        assert x == y
        assert x != z

# Приведённая def setup() в занятии должна была помочь от дублирований, но не работает!!! В итоге код совсем разросся
class TestInterface:
#    def setup(self): # Не работает даже при запуске с pytest -s
#        print("Выполняюсь до теста") # Не работает

    def test_interface(self): # Для проверки инициированных переменных (а нужно ли было его вообще так упорно проверять?)
        card_lst = Card()() # Cоздаём экземпляр метода класса c картами
        barrels_lst = Barrels().barrel_lst # А теперь экземпляр метода класса с бочонками
        interface = Interface(['Игрок_1', 'Игрок_2'], card_lst, barrels_lst) # И объект предитогового класса

        assert interface.players == ['Игрок_1', 'Игрок_2'] # Сохраняет ли неизменно в переменную поданный лист?

        # Ни дескрипторы, ни общий класс почему-то не помогли, пока что оставим дублированными ... на следующий раз
        assert len(card_lst) == 3 # Три ли строчки в переданной карточке?
        for str_lst in card_lst: # Перебираем строчки (вложенные листы) в переданной карточке
            assert len(str_lst) == 9 # 9 ли элементов в строчке (во вложенных листах) этой карточки?
            assert str_lst.count('') == 4 # Есть ли в них 4 пустые строки?
            assert len(set([str_lst[i] for i in range(len(str_lst))])) > 2 # Рандомно ли перебираются цифры в этих строчках?

        assert len(barrels_lst) == 90 # В переданном листе 90 элементов (бочонков)?
        assert len(set(barrels_lst)) == len(barrels_lst) # Они разные?

        assert interface.name_len_lim > 0 # Нужно хотя один символ для имени в выделенном в интерфейсе карточки

        assert len(interface.players) == len(interface.count_dict) # Совпадают ли количество игроков в словаре и списке?
        assert interface.players == [i for i, _ in interface.count_dict.items()] # Одинаковые ли имена игроков в списке и словаре?

    def test_delete_barrel(self): # Правильно ли удаляет бочонок?
        barrels_lst = Barrels().barrel_lst # Создаём экземпляр метода класса с бочонками
        interface = Interface([], [], barrels_lst) # А теперь объект класса
        del_barrel = [interface.delete_barrel() for _ in range(90)] # Удаляем по одиночке случайно все 90 бочонков
        assert len(set(del_barrel)) == 90 # Их было 90 и были разными?

    def test_format_card(self): # Проверка выводимой карточки
        card_lst = Card()() # Cоздаём экземпляр метода класса c картами
        interface = Interface(['Игрок_1'], card_lst, []) # Cоздаём экземпляр класса
        card_format = interface.format_card('Player', [[1, '-', 2], [3, '']])
        assert len(card_format) == 77 # Количество полученных строк ожидаемо?

    def test_print_cards(self): # Ради галочки, мокирование и прочее не проходили, не пишу тут...
        print_cards = Interface([], [], []).print_cards()
        assert print_cards == None # Есть ли что-либо в карточке?

    def test_update_cards(self):# Обновляет ли карточки игроков после вытаскивания нового бочонка
        card = Card()() # Cоздаём экземпляр класса для карт
        card_lst = {'Игрок_1': card, 'Игрок_2': card} # И словарь с картами
        barrels_lst = Barrels().barrel_lst # А теперь экземпляр метода класса с бочонками
        interface = Interface(['Игрок_1', 'Игрок_2'], card_lst, barrels_lst)
        for new_barrel in range(90): # Проходим 90 бочонков
            interface.update_cards(new_barrel) # Будем проверять каждый бочонок
            for player, card in interface.card_lst.items(): # Проход по каждому игроку и карте
                for row in card: # проход по каждому номеру в карте
                    assert new_barrel not in row # Остался ли (зачёркнут ли) номер в итоге?

    def test_check_cards(self): # Правильно ли возвращает True при автонаборе
        interface = Interface([], [], []) # Создаём экземпляр класса
        check_True = interface.check_cards(True, hand=True) # Передаём в созданный метод класса True
        check_False = interface.check_cards(False, hand=True) # Передаём в созданный метод класса False
        assert check_True and check_False == True # Правильно ли их он потом обрабатывает?

    def test_check_winner(self): # Проверка определения победителя (т.е. игрока с 15 зачеркнутыми числами)
        count = Interface([], [], [], count_dict={'Игрок_1': 13, 'Игрок_2': 15}) # У второго игрока победа
        assert count.check_winner() == [False, 'Игрок_2'] # Должен такой список вернуть
        count = Interface([], [], [], count_dict={'Игрок_1': 13, 'Игрок_2': 14})  # Победы нет
        assert count.check_winner() == [True] # Должен такой список вернуть

    def test_card_interface_mark(self): # Зачёркиваются ли числа?
        players = ['Игрок_1', 'Игрок_2'] # Создаём список с игроками
        card_lst = {player: Card()() for player in players} # А также словарь с картами для игроков
        barrel_lst = Barrels().barrel_lst # Ещё и списка вычёркиваемых номеров
        game = Interface(players, card_lst, barrel_lst) # Создаём экземпляр с нашим классом
        for _ in range(len(barrel_lst)): # Проходим по всем бочонкам
            new_barrel = game.delete_barrel() # Удаляем один бочонок
            game.update_cards(new_barrel) # И теперь обновляем карту
            game.check_cards(True, hand=True) # Автоматически зачеркиваем
        for player, card in game.card_lst.items(): # Проверяем, что карточки игроков были обновлены
            assert any('-' in row for row in card) # Есть ли зачеркнутые числа в карточках?

    def test_card_interface_winner(self): # Определяет ли победителей?
        players = ['Игрок_1', 'Игрок_2'] # Создаём список с игроками
        card_lst = {player: Card()() for player in players} # А также словарь с картами для игроков
        barrel_lst = Barrels().barrel_lst # Ещё и списка вычёркиваемых номеров
        game = Interface(players, card_lst, barrel_lst) # Создаём экземпляр с нашим классом
        game.card_interface() # Запускаем процессы интерфейса
        assert game.check_winner()[1] == 'Игрок1' or 'Игрок_2' # Выявила ли какого-либо победителя?

    def test_interface_magic(self): # Корректно ли переопределённые магические методы сравнения работают?
        x = Interface(['Игрок'], {}, [])
        y = Interface(['Игрок'], {}, [])
        z = Interface(['Игрокер'], {}, [])
        assert x == y
        assert x != z

class TestGame: # Сборочный, его вообще непонятно как тестировать

    def test_gaming_add_2_players(self): # Проверяет список c пунктами главного меню с их названиями (как в TestPlayer)
        for i in ['1', '2', '3']: # Проверяется эти три предустановленные пункты
            players = Players(menu=i) # Создаём экземпляр класса Players
            assert players.add_players() == players.two_players[int(i)-1] # Сверяем принадлежность пунктов меню к их именам

    def test_gaming_create_cards(self): # Как хорошо создаются карты?
        card_list = Card()() # Создаём экземпляр класса для карт
        assert len(set(num for row in card_list for num in row if num)) == 15 # Проверка количества чисел
        assert all(1 <= num <= 90 for row in card_list for num in row if num) # Числа в пределах от 0 до 91?
        assert len(card_list) == 3 # Три строки в двумерном списке?
        assert all(len(row) == 9 for row in card_list) # Девять столбцов в двумерном списке?
        for row in card_list: # Проходим по каждой строке списка
            assert sum(num == '' for num in row) == 4 # Пустых ячеек в каждой строке 4?

    def test_gaming_del_barrel(self): # Проверка удаления бочонков
        barrel_list = Barrels().barrel_lst # Cоздаём список вычёркиваемых номеров
        interface = Interface([], [], barrel_list) # И экземпляр с интерфейсом

        initial_length = len(barrel_list) # Берём количество бочонков
        deleted_barrel = interface.delete_barrel() # Проводим удаление бочонка

        assert deleted_barrel in range(1, 91)  # Проверяем, что удаленный бочонок в диапазоне
        assert len(barrel_list) == initial_length - 1  # Проверяем, что длина списка уменьшилась
        assert deleted_barrel not in barrel_list  # Проверяем, что бочонок действительно удален

    def test_game_magic(self): # Корректно ли переопределённые магические методы сравнения работают?
        x = Game(magic='a')
        y = Game(magic='a')
        z = Game(magic='b')
        assert x == y
        assert x != z