"""
Модуль 01 — Решения
⚠️  Загляни сюда только после того, как попробовал сам!
"""


def greeting(name: str, age: int) -> str:
    return f"Hello, {name}! You are {age} years old."


def calculator(a: float, b: float, operation: str) -> float | None:
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return None  # деление на ноль — возвращаем None
        return a / b


def is_even(n: int) -> bool:
    return n % 2 == 0  # остаток от деления на 2 равен 0 → чётное


def letter_grade(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def sum_to(n: int) -> int:
    # Математическая формула: сумма от 1 до n = n*(n+1)/2
    return n * (n + 1) // 2


def count_even(a: int, b: int) -> int:
    # Считаем числа в диапазоне, которые делятся на 2 без остатка
    return sum(1 for i in range(a, b + 1) if i % 2 == 0)


def triangle(n: int) -> None:
    for i in range(1, n + 1):
        print("*" * i)  # i звёздочек на i-й строке


def fizzbuzz(n: int) -> list:
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:       # делится на 3 и на 5 → проверяем первым
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result