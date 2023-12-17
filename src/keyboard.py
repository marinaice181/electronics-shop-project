
from src.item import Item


class KeyboardMixin:

    def __init__(self):
        self._language = 'EN'

    def change_lang(self):
        if self._language == 'EN':
            self._language = "RU"
        else:
            self._language = "EN"
        return self


class Keyboard(Item, KeyboardMixin):

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self._language = 'EN'

    def __str__(self):
        return self.name

    def change_lang(self):
        if self._language == 'EN':
            self._language = "RU"
        else:
            self._language = "EN"
        return self

    @property
    def language(self) -> str:
        return self._language
