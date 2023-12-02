import pytest
from pytest_mock import mocker

from day02 import day02

def test_Draw_isValid_False():
    assert day02.Draw(13,0,2).isValid() == False

def test_Draw_isValid_True():
    assert day02.Draw(12,13,14).isValid() == True

def test_Game_isValid_True(mocker): 
    mocker.patch('day02.day02.Draw.isValid', return_value=True)
    assert day02.Game(1, [mocker.MagicMock()]).isValid() == True

def test_Game_isValid_False(mocker):
    mocker.patch('day02.day02.Draw.isValid', return_value=False)
    assert day02.Game(1, [mocker.MagicMock()]).isValid() == False

def test_Game_calculate_Power(): 
    day02.Game(1, [{'red': 1, 'blue': 2, 'green': 3}]).calculatePower() == 6
    day02.Game(1, [{'red': 1, 'blue': 2, 'green': 3}, {'red': 6, 'blue': 2, 'green': 1}]).calculatePower() == 36

def test_import_line():
    game = day02.importLine('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')
    assert isinstance(game, day02.Game)
    assert game.id == 1
    assert game.draws[0].blue == 3
    assert game.draws[0].green == 0
    assert game.draws[0].red == 4
    assert game.draws[2].green == 2

def test_importFile():
    gameList = day02.importFile('./day02/input/test1.txt')
    assert len(gameList) == 5
    assert (isinstance(game, day02.Game) for game in gameList)


