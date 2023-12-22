from src.keyboard import Keyboard, KeyboardMixin


def test_change_lang():
    kb = Keyboard('Test Keyboard', 900, 1)
    kb.change_lang()
    assert kb.language == 'RU'
    kb.change_lang()
    assert kb.language == 'EN'



def test_str():
    kb = Keyboard('Test Keyboard', 900, 1)
    assert str(kb) == 'Test Keyboard'


def test_KeyboardMixin():
    kb = KeyboardMixin()
    assert kb._language == 'EN'
    kb.change_lang()
    assert kb._language == "RU"
    kb.change_lang()
    assert kb._language == "EN"
