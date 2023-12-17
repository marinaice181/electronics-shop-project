"""Тесты с использованием pytest для модуля phone"""

from src.phone import Phone
from src.item import Item


def test_phone():
    """
    Проверка всех данных
    """
    phone = Phone("test1", 120000, 5, 2)
    assert phone.name == "test1"
    assert phone.price == 120000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2


def test_number_of_sim_setter():
    """
    Проверка на изменение количества сим карт
    """
    phone = Phone("test1", 120000, 5, 2)
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2


def test_phone__error_number_of_sim():
    """
    Проверка на отрицательное и float количество сим карт
    """
    with pytest.raises(ValueError):
        phone = Phone("test1", 699.99, 10, -2)
        phone1 = Phone("test2", 699.99, 10, 2.7)