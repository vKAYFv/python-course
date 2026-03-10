"""
Решения к модулю 01.
⚠️  Загляни сюда только после того, как попробовал сам!
"""


def приветствие(имя: str, возраст: int) -> str:
    # Определяем правильное окончание
    if возраст % 100 in range(11, 20):
        окончание = "лет"
    elif возраст % 10 == 1:
        окончание = "год"
    elif возраст % 10 in [2, 3, 4]:
        окончание = "года"
    else:
        окончание = "лет"
    return f"Привет, {имя}! Тебе {возраст} {окончание}."


def калькулятор(a: float, b: float, операция: str) -> float | None:
    if операция == "+":
        return a + b
    elif операция == "-":
        return a - b
    elif операция == "*":
        return a * b
    elif операция == "/":
        if b == 0:
            return None
        return a / b


def чётное(n: int) -> bool:
    return n % 2 == 0


def буква_оценки(оценка: int) -> str:
    if оценка >= 90:
        return "A"
    elif оценка >= 80:
        return "B"
    elif оценка >= 70:
        return "C"
    elif оценка >= 60:
        return "D"
    else:
        return "F"


def сумма_до(n: int) -> int:
    return sum(range(1, n + 1))
    # Или математически: return n * (n + 1) // 2


def количество_чётных(a: int, b: int) -> int:
    count = 0
    for i in range(a, b + 1):
        if i % 2 == 0:
            count += 1
    return count


def треугольник(n: int) -> None:
    for i in range(1, n + 1):
        print("*" * i)


def fizzbuzz(n: int) -> list:
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result