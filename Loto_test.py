import pytest
from Loto_class import Players, Card, Barrels, Interface
class TestPlayer:
    def test_players(self):
        players = Players(['Первый игрок', 'Второй игрок'])
        assert len(players.players) == 2 and players.players == ['Первый игрок', 'Второй игрок']

class TestCard:
    pass
class TestBarrels:
    pass
class TestInterface:
    pass
class Game:
    pass
