"""
Модуль 02 — Тесты по строкам
Запусти: python -m pytest tasks_test.py -v
"""
import pytest
from tasks import (
    reverse_string, is_palindrome, count_vowels,
    title_case, remove_spaces, unique_words,
    acronym, censor, generate_password
)


class TestReverseString:
    def test_regular_word(self):
        assert reverse_string("Python") == "nohtyP"

    def test_short(self):
        assert reverse_string("abc") == "cba"

    def test_empty(self):
        # пустая строка остаётся пустой
        assert reverse_string("") == ""

    def test_single_char(self):
        assert reverse_string("a") == "a"

    def test_palindrome_unchanged(self):
        # палиндром после разворота совпадает с оригиналом
        assert reverse_string("racecar") == "racecar"


class TestIsPalindrome:
    def test_simple_palindrome(self):
        assert is_palindrome("racecar") is True
        assert is_palindrome("level") is True
        assert is_palindrome("madam") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False
        assert is_palindrome("Python") is False

    def test_case_insensitive(self):
        # регистр не должен влиять
        assert is_palindrome("Racecar") is True
        assert is_palindrome("Level") is True

    def test_with_spaces(self):
        # пробелы игнорируются
        assert is_palindrome("a man a plan a canal panama") is True

    def test_single_char(self):
        assert is_palindrome("x") is True


class TestCountVowels:
    def test_basic(self):
        assert count_vowels("hello") == 2       # e, o

    def test_case_insensitive(self):
        assert count_vowels("HELLO") == 2       # регистр не важен

    def test_no_vowels(self):
        assert count_vowels("bcdf") == 0

    def test_all_vowels(self):
        assert count_vowels("aeiou") == 5

    def test_mixed(self):
        assert count_vowels("Hello World") == 3  # e, o, o


class TestTitleCase:
    def test_two_words(self):
        assert title_case("hello world") == "Hello World"

    def test_three_words(self):
        assert title_case("python is great") == "Python Is Great"

    def test_single_word(self):
        assert title_case("python") == "Python"

    def test_already_title(self):
        assert title_case("Hello World") == "Hello World"


class TestRemoveSpaces:
    def test_spaces_between_chars(self):
        assert remove_spaces("h e l l o") == "hello"

    def test_spaces_in_word(self):
        assert remove_spaces("no spaces") == "nospaces"

    def test_only_spaces(self):
        assert remove_spaces("   ") == ""

    def test_no_spaces(self):
        # строка без пробелов не меняется
        assert remove_spaces("hello") == "hello"


class TestUniqueWords:
    def test_basic(self):
        assert unique_words("yes no yes maybe no") == ["yes", "no", "maybe"]

    def test_case_insensitive(self):
        # все варианты регистра — одно слово
        assert unique_words("Yes yes YES") == ["yes"]

    def test_no_duplicates(self):
        result = unique_words("one two three")
        assert result == ["one", "two", "three"]

    def test_order_preserved(self):
        # порядок первого появления должен сохраняться
        result = unique_words("c b a c b a")
        assert result == ["c", "b", "a"]


class TestAcronym:
    def test_common_phrase(self):
        assert acronym("as soon as possible") == "ASAP"

    def test_three_words(self):
        assert acronym("Python Is Great") == "PIG"

    def test_single_word(self):
        assert acronym("hello") == "H"

    def test_uppercase_result(self):
        # результат всегда в верхнем регистре
        result = acronym("hello world")
        assert result == result.upper()


class TestCensor:
    def test_single_word(self):
        assert censor("bad word here", ["bad"]) == "*** word here"

    def test_replace_preserves_length(self):
        # звёздочки той же длины что и слово
        result = censor("hello world", ["world"])
        assert result == "hello *****"

    def test_multiple_banned_words(self):
        result = censor("foo and bar", ["foo", "bar"])
        assert result == "*** and ***"

    def test_no_banned_words(self):
        # если запрещённых слов нет — строка не меняется
        assert censor("hello world", []) == "hello world"


class TestGeneratePassword:
    def test_correct_length(self):
        # длина должна совпадать с заданной
        for length in [8, 12, 16, 20]:
            assert len(generate_password(length)) == length

    def test_default_length(self):
        assert len(generate_password()) == 12

    def test_has_uppercase(self):
        password = generate_password(20)
        assert any(c.isupper() for c in password), "Нет заглавных букв"

    def test_has_lowercase(self):
        password = generate_password(20)
        assert any(c.islower() for c in password), "Нет строчных букв"

    def test_has_digit(self):
        password = generate_password(20)
        assert any(c.isdigit() for c in password), "Нет цифр"

    def test_has_special(self):
        password = generate_password(20)
        assert any(c in "!@#$" for c in password), "Нет спецсимволов"

    def test_unique_each_time(self):
        # два пароля не должны совпадать (с высокой вероятностью)
        p1 = generate_password(16)
        p2 = generate_password(16)
        assert p1 != p2