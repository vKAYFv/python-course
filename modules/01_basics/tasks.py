"""
Модуль 01 — Задания
Заполни тело каждой функции.
Запусти тесты: python -m pytest tasks_test.py -v
"""


# Задание 1
# Верни строку приветствия вида: "Hello, Anna! You are 23 years old."
def greeting(name: str, age: int) -> str:
    # TODO: твой код здесь
    pass


# Задание 2
# Принимает два числа и операцию ('+', '-', '*', '/').
# Верни результат. При делении на 0 верни None.
def calculator(a: float, b: float, operation: str) -> float | None:
    # TODO: твой код здесь
    pass


# Задание 3
# Верни True если число чётное, False если нечётное.
def is_even(n: int) -> bool:
    # TODO: твой код здесь
    pass


# Задание 4
# Принимает оценку (0–100) и возвращает букву:
# 90-100 → "A", 80-89 → "B", 70-79 → "C", 60-69 → "D", ниже 60 → "F"
def letter_grade(score: int) -> str:
    # TODO: твой код здесь
    pass


# Задание 5
# Верни сумму всех чисел от 1 до n включительно.
# Пример: sum_to(5) → 15  (1+2+3+4+5)
def sum_to(n: int) -> int:
    # TODO: твой код здесь
    pass


# Задание 6
# Верни количество чётных чисел в диапазоне [a, b] включительно.
def count_even(a: int, b: int) -> int:
    # TODO: твой код здесь
    pass


# Задание 7 ⭐
# Напечатай треугольник из символов '*' высотой n строк.
# Функция ничего не возвращает, только печатает.
#
# Пример для n=4:
# *
# **
# ***
# ****
def triangle(n: int) -> None:
    # TODO: твой код здесь
    pass


# Задание 8 ⭐⭐
# FizzBuzz: пройди числа от 1 до n.
# - Делится на 3 → добавь "Fizz"
# - Делится на 5 → добавь "Buzz"
# - Делится на 3 и 5 → добавь "FizzBuzz"
# - Иначе → добавь само число (int)
# Верни список.
def fizzbuzz(n: int) -> list:
    # TODO: твой код здесь
    pass


if __name__ == "__main__":
    print(greeting("Anna", 23))
    print(calculator(10, 3, "+"))
    print(calculator(10, 0, "/"))
    print(is_even(4))
    print(letter_grade(85))
    print(sum_to(5))
    triangle(4)
    print(fizzbuzz(15))