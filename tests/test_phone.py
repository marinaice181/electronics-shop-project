"""Тесты с использованием pytest для модуля phone"""

import pytest
from src.phone import Phone


def test___init__():
    """
    Тест инициализации
    """
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'


def test_number_of_sim():
    """
    Тест количества сим-карт
    """
    phone1 = Phone("iPhone 10", 20_000, 5, 2)
    phone1.number_of_sim = 2
    assert phone1.number_of_sim == 2


def test_number_of_sim__value_error():
    """
    Тест с проверкой ошибки малого или отрицательного количества сим-карт
    """
    with pytest.raises(ValueError):
        phone2 = Phone("iPhone 20", 120_000, 5, 0)
        phone2.number_of_sim = 0
        phone2.number_of_sim


def test___repr__():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"