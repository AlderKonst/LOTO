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
    pass
class TestBarrels:
    pass
class TestInterface:
    pass
class TestGame:
    pass