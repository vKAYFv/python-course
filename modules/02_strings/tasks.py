"""
Модуль 02 — Задания по строкам
Запусти тесты: python -m pytest tasks_test.py -v
"""
import random
import string


# Задание 1
# Верни строку задом наперёд.
def reverse_string(s: str) -> str:
    # TODO: твой код здесь
    pass


# Задание 2
# Верни True если строка — палиндром (одинаково читается в обе стороны).
# Игнорируй регистр и пробелы.
# "racecar" -> True, "hello" -> False
def is_palindrome(s: str) -> bool:
    # TODO: твой код здесь
    pass


# Задание 3
# Подсчитай количество гласных букв (a, e, i, o, u).
# Регистр не важен.
def count_vowels(s: str) -> int:
    # TODO: твой код здесь
    pass


# Задание 4
# Верни строку, где каждое слово написано с заглавной буквы.
# "hello world" -> "Hello World"
def title_case(s: str) -> str:
    # TODO: твой код здесь
    pass


# Задание 5
# Удали все пробелы из строки.
# "h e l l o" -> "hello"
def remove_spaces(s: str) -> str:
    # TODO: твой код здесь
    pass


# Задание 6
# Верни список уникальных слов (в нижнем регистре, порядок сохраняется).
# "yes no yes maybe no" -> ["yes", "no", "maybe"]
def unique_words(s: str) -> list:
    # TODO: твой код здесь
    pass


# Задание 7
# Верни акроним из первых букв каждого слова (заглавные).
# "as soon as possible" -> "ASAP"
def acronym(phrase: str) -> str:
    # TODO: твой код здесь
    pass


# Задание 8 ⭐
# Замени все вхождения запрещённых слов звёздочками той же длины.
# censor("bad word here", ["bad"]) -> "*** word here"
def censor(text: str, banned: list) -> str:
    # TODO: твой код здесь
    pass


# Задание 9 ⭐⭐
# Сгенерируй пароль заданной длины.
# Пароль должен содержать: заглавные, строчные, цифры, спецсимволы (!@#$).
# Верни строку — готовый пароль.
def generate_password(length: int = 12) -> str:
    # TODO: твой код здесь
    pass


if __name__ == "__main__":
    print(reverse_string("Python"))
    print(is_palindrome("racecar"))
    print(count_vowels("Hello World"))
    print(title_case("hello world"))
    print(remove_spaces("h e l l o"))
    print(unique_words("yes no yes maybe no"))
    print(acronym("as soon as possible"))
    print(censor("bad word here", ["bad"]))
    print(generate_password(16))