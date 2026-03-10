"""
Модуль 01 — Основы Python
Запусти: python theory.py
Читай код + комментарии, меняй значения, экспериментируй!
"""

# ─────────────────────────────────────────────
# 1. Вывод на экран
# ─────────────────────────────────────────────
print("=" * 40)
print("1. Print")
print("=" * 40)

print("Hello, World!")
print("Python", "is", "great")           # несколько аргументов через запятую
print("one", "two", "three", sep="-")    # свой разделитель между аргументами
print("no newline", end=" ")             # end="" — без переноса строки
print("continues here")


# ─────────────────────────────────────────────
# 2. Переменные и типы данных
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("2. Variables and types")
print("=" * 40)

name = "Alexander"       # str — строка
age = 28                 # int — целое число
height = 1.78            # float — число с точкой
is_student = True        # bool — булево (True/False)

print(f"Name:       {name}        ({type(name).__name__})")
print(f"Age:        {age}          ({type(age).__name__})")
print(f"Height:     {height}       ({type(height).__name__})")
print(f"Student:    {is_student}      ({type(is_student).__name__})")


# ─────────────────────────────────────────────
# 3. Арифметика
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("3. Arithmetic")
print("=" * 40)

a, b = 17, 5

print(f"{a} + {b}  = {a + b}")
print(f"{a} - {b}  = {a - b}")
print(f"{a} * {b}  = {a * b}")
print(f"{a} / {b}  = {a / b:.2f}")    # деление — всегда float
print(f"{a} // {b} = {a // b}")       # целочисленное деление (без остатка)
print(f"{a} % {b}  = {a % b}")        # остаток от деления
print(f"{a} ** {b} = {a ** b}")       # возведение в степень

x = 10
x += 5   # то же что x = x + 5
x -= 2   # то же что x = x - 2
x *= 3   # то же что x = x * 3
print(f"\nx после операций: {x}")


# ─────────────────────────────────────────────
# 4. Условия
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("4. Conditionals")
print("=" * 40)

temperature = 22

if temperature > 30:
    print("Hot!")
elif temperature > 20:
    print("Warm and comfortable")  # выполнится это — 22 > 20
elif temperature > 10:
    print("Cool, grab a jacket")
else:
    print("Cold!")

# Тернарный оператор — краткая запись if/else в одну строку
status = "adult" if age >= 18 else "minor"
print(f"{name} is an {status}")


# ─────────────────────────────────────────────
# 5. Циклы
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("5. Loops")
print("=" * 40)

# for + range — перебор по диапазону
print("Таблица умножения на 3:")
for i in range(1, 11):
    print(f"3 x {i:2} = {3 * i}")

# while с break — выходим когда нашли что искали
print("\nПервое число, делящееся и на 7, и на 11:")
n = 1
while True:
    if n % 7 == 0 and n % 11 == 0:
        print(f"Нашли: {n}")
        break  # выходим из цикла
    n += 1

# continue — пропускаем итерацию и идём к следующей
print("\nЧётные числа от 1 до 20:")
for i in range(1, 21):
    if i % 2 != 0:
        continue  # нечётное — пропускаем
    print(i, end=" ")
print()  # перевод строки в конце


# ─────────────────────────────────────────────
# 6. Вложенные циклы
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("6. Nested loops — таблица умножения")
print("=" * 40)

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:3}", end="")  # :3 — ширина поля 3 символа
    print()  # перевод строки после каждой строки таблицы