"""
Модуль 02 — Решения
⚠️  Загляни сюда только после того, как попробовал сам!
"""
import random
import string


def reverse_string(s: str) -> str:
    return s[::-1]  # срез с шагом -1 разворачивает строку


def is_palindrome(s: str) -> bool:
    cleaned = s.lower().replace(" ", "")  # убираем регистр и пробелы
    return cleaned == cleaned[::-1]       # сравниваем с перевёрнутой


def count_vowels(s: str) -> int:
    # проверяем каждый символ — входит ли он в строку гласных
    return sum(1 for c in s.lower() if c in "aeiou")


def title_case(s: str) -> str:
    return s.title()  # встроенный метод делает именно это


def remove_spaces(s: str) -> str:
    return s.replace(" ", "")  # заменяем пробел на пустую строку


def unique_words(s: str) -> list:
    seen = set()    # множество для быстрой проверки «уже видели?»
    result = []
    for word in s.lower().split():
        if word not in seen:
            seen.add(word)
            result.append(word)
    return result


def acronym(phrase: str) -> str:
    # берём первую букву каждого слова и делаем заглавной
    return "".join(word[0].upper() for word in phrase.split())


def censor(text: str, banned: list) -> str:
    for word in banned:
        text = text.replace(word, "*" * len(word))  # звёздочки той же длины
    return text


def generate_password(length: int = 12) -> str:
    chars = string.ascii_letters + string.digits + "!@#$"
    # Гарантируем наличие всех типов символов
    password = [
        random.choice(string.ascii_uppercase),  # хотя бы одна заглавная
        random.choice(string.ascii_lowercase),  # хотя бы одна строчная
        random.choice(string.digits),           # хотя бы одна цифра
        random.choice("!@#$"),                  # хотя бы один спецсимвол
    ]
    password += random.choices(chars, k=length - 4)  # остаток длины
    random.shuffle(password)  # перемешиваем чтобы не было паттерна
    return "".join(password)