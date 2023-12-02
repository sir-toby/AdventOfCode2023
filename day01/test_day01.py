import pytest

from day01 import day01

searchterms = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def test_firstDigit():
    assert day01.firstDigit("123") == 1
    assert day01.firstDigit("abc98") == 9
    assert day01.firstDigit("abc") == None
    assert day01.firstDigit("bc6") == 6


def test_lastDigit():
    assert day01.lastDigit("123") == 3
    assert day01.lastDigit("abc98") == 8
    assert day01.lastDigit("abc") == None
    assert day01.lastDigit("6bc") == 6


def test_part1():
    assert day01.part1(["ab12", "b6c"]) == 78


def test_findleft():
    assert day01.findLeft("one", searchterms) == 1
    assert day01.findLeft("asdf1three", searchterms) == 1
    assert day01.findLeft("sevenine", searchterms) == 7


def test_findRight():
    assert day01.findRight("one", searchterms) == 1
    assert day01.findRight("asdfone3", searchterms) == 3
    assert day01.findRight("sevenine", searchterms) == 9


def test_part2():
    assert day01.part2(["ab12", "b6c", "onetwothree", "arnfionefl5"]) == 106
