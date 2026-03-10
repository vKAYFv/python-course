"""
Автотесты для модуля 01.
Запуск: python -m pytest tasks_test.py -v
"""
import pytest
from tasks import (
    приветствие,
    калькулятор,
    чётное,
    буква_оценки,
    сумма_до,
    количество_чётных,
    fizzbuzz,
)


class TestПриветствие:
    def test_базовый(self):
        assert приветствие("Анна", 23) == "Привет, Анна! Тебе 23 года."

    def test_другое_имя(self):
        assert приветствие("Иван", 30) == "Привет, Иван! Тебе 30 лет."

    def test_один_год(self):
        result = приветствие("Петя", 1)
        assert "Петя" in result and "1" in result


class TestКалькулятор:
    def test_сложение(self):
        assert калькулятор(3, 4, "+") == 7

    def test_вычитание(self):
        assert калькулятор(10, 3, "-") == 7

    def test_умножение(self):
        assert калькулятор(5, 6, "*") == 30

    def test_деление(self):
        assert калькулятор(10, 2, "/") == 5.0

    def test_деление_на_ноль(self):
        assert калькулятор(10, 0, "/") is None

    def test_float(self):
        assert abs(калькулятор(7, 3, "/") - 2.333) < 0.01


class TestЧётное:
    def test_чётные(self):
        for n in [0, 2, 4, 100, -8]:
            assert чётное(n) is True

    def test_нечётные(self):
        for n in [1, 3, 7, 99, -5]:
            assert чётное(n) is False


class TestБукваОценки:
    def test_a(self):
        assert буква_оценки(95) == "A"
        assert буква_оценки(90) == "A"

    def test_b(self):
        assert буква_оценки(85) == "B"
        assert буква_оценки(80) == "B"

    def test_c(self):
        assert буква_оценки(75) == "C"

    def test_d(self):
        assert буква_оценки(65) == "D"

    def test_f(self):
        assert буква_оценки(55) == "F"
        assert буква_оценки(0) == "F"


class TestСуммаДо:
    def test_базовые(self):
        assert сумма_до(1) == 1
        assert сумма_до(5) == 15
        assert сумма_до(10) == 55
        assert сумма_до(100) == 5050


class TestКоличествоЧётных:
    def test_базовые(self):
        assert количество_чётных(1, 10) == 5   # 2,4,6,8,10
        assert количество_чётных(1, 1) == 0
        assert количество_чётных(2, 2) == 1
        assert количество_чётных(0, 10) == 6   # 0,2,4,6,8,10


class TestFizzBuzz:
    def test_первые_15(self):
        result = fizzbuzz(15)
        assert result[0] == 1
        assert result[2] == "Fizz"
        assert result[4] == "Buzz"
        assert result[14] == "FizzBuzz"

    def test_длина(self):
        assert len(fizzbuzz(10)) == 10

    def test_fizz(self):
        result = fizzbuzz(6)
        assert result[5] == "Fizz"   # 6-й элемент (индекс 5) = число 6

    def test_buzz(self):
        result = fizzbuzz(5)
        assert result[4] == "Buzz"   # 5-й элемент = число 5