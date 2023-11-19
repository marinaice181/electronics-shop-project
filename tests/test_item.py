"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

def test_Item_calculate_total_price():
    test_class = Item('Marina', 100.0, 10)
    test_data = test_class.calculate_total_price()
    assert test_data == 1000