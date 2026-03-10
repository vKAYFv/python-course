"""
Модуль 01 — Тесты
Запусти: python -m pytest tasks_test.py -v
"""
import pytest
from tasks import greeting, calculator, is_even, letter_grade, sum_to, count_even, fizzbuzz


class TestGreeting:
    def test_basic(self):
        # базовый случай
        assert greeting("Anna", 23) == "Hello, Anna! You are 23 years old."

    def test_other_name(self):
        assert greeting("Ivan", 30) == "Hello, Ivan! You are 30 years old."

    def test_contains_name_and_age(self):
        # имя и возраст должны присутствовать в строке
        result = greeting("Pete", 1)
        assert "Pete" in result
        assert "1" in result


class TestCalculator:
    def test_addition(self):
        assert calculator(3, 4, "+") == 7

    def test_subtraction(self):
        assert calculator(10, 3, "-") == 7

    def test_multiplication(self):
        assert calculator(5, 6, "*") == 30

    def test_division(self):
        assert calculator(10, 2, "/") == 5.0

    def test_division_by_zero(self):
        # деление на ноль — ожидаем None
        assert calculator(10, 0, "/") is None

    def test_float_result(self):
        # проверяем точность до 3 знаков
        assert abs(calculator(7, 3, "/") - 2.333) < 0.01

    def test_negative_numbers(self):
        assert calculator(-5, 3, "+") == -2
        assert calculator(-4, -2, "*") == 8


class TestIsEven:
    def test_even_numbers(self):
        # все эти числа должны вернуть True
        for n in [0, 2, 4, 100, -8]:
            assert is_even(n) is True, f"{n} должно быть чётным"

    def test_odd_numbers(self):
        # все эти числа должны вернуть False
        for n in [1, 3, 7, 99, -5]:
            assert is_even(n) is False, f"{n} должно быть нечётным"


class TestLetterGrade:
    def test_a_grade(self):
        assert letter_grade(100) == "A"
        assert letter_grade(95) == "A"
        assert letter_grade(90) == "A"   # граница A

    def test_b_grade(self):
        assert letter_grade(89) == "B"   # граница B
        assert letter_grade(85) == "B"
        assert letter_grade(80) == "B"   # граница B

    def test_c_grade(self):
        assert letter_grade(79) == "C"   # граница C
        assert letter_grade(75) == "C"
        assert letter_grade(70) == "C"

    def test_d_grade(self):
        assert letter_grade(69) == "D"
        assert letter_grade(65) == "D"
        assert letter_grade(60) == "D"

    def test_f_grade(self):
        assert letter_grade(59) == "F"
        assert letter_grade(30) == "F"
        assert letter_grade(0) == "F"


class TestSumTo:
    def test_one(self):
        assert sum_to(1) == 1

    def test_five(self):
        assert sum_to(5) == 15           # 1+2+3+4+5

    def test_ten(self):
        assert sum_to(10) == 55

    def test_hundred(self):
        assert sum_to(100) == 5050       # классическая формула Гаусса


class TestCountEven:
    def test_one_to_ten(self):
        assert count_even(1, 10) == 5    # 2,4,6,8,10

    def test_no_even(self):
        assert count_even(1, 1) == 0     # нет чётных

    def test_single_even(self):
        assert count_even(2, 2) == 1     # само число чётное

    def test_includes_zero(self):
        assert count_even(0, 10) == 6    # 0,2,4,6,8,10

    def test_large_range(self):
        assert count_even(1, 100) == 50


class TestFizzBuzz:
    def test_first_element_is_one(self):
        assert fizzbuzz(15)[0] == 1      # первый элемент — число 1

    def test_fizz(self):
        result = fizzbuzz(15)
        assert result[2] == "Fizz"       # число 3
        assert result[5] == "Fizz"       # число 6
        assert result[8] == "Fizz"       # число 9

    def test_buzz(self):
        result = fizzbuzz(15)
        assert result[4] == "Buzz"       # число 5
        assert result[9] == "Buzz"       # число 10

    def test_fizzbuzz(self):
        result = fizzbuzz(15)
        assert result[14] == "FizzBuzz"  # число 15

    def test_length(self):
        assert len(fizzbuzz(10)) == 10
        assert len(fizzbuzz(1)) == 1

    def test_plain_number(self):
        result = fizzbuzz(7)
        assert result[6] == 7            # число 7 — просто число