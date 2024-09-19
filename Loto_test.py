# Из-за input() запускать в терминале так: pytest -s
import pytest
from Loto_class import Menu, Players, Card, Barrels, Interface
class TestMenu:
    def test_menu(self): # Не число ли и вне пределов?
        menu = Menu().start_menu()
        assert menu in [1, 2, 3, 4] # Для проверки нужно ввести число от 1 до 4

class TestPlayer:
    def test_two_players(self): # Проверяет количество пар игроков в списке
        players = Players()
        assert len(players.two_players) == 3
    def test_players_list(self): # Список ли получает?
        players = Players().add_players()
        assert type(players) == list
    def multi_players_zero(self): # Срабатывает ли при введении числа игрогов больше нуля
        players = Players().multi_players()
        assert len(players) > 0 # Для проверки нужно ввести число больше нуля

class TestCard:
    pass
class TestBarrels:
    pass
class TestInterface:
    pass
class Game:
    pass
