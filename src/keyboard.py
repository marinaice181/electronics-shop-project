from src.item import Item


class MixinLang:
    def __init__(self):
        """
        Инициализация
        """
        language = "EN"
        self.language = language

    def change_lang(self):
        """
        Меняет язык клавиатуры
        """
        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"

    def save_lang(self):
        print(f'Язык клавиатуры - {self.language}')


class Keyboard(Item, MixinLang):
    """
    Класс клавиатуры
    """
    def __init__(self, name: str, price: float, quantity: int):
        """
        Инициализыция товара - клавиатуры со взятием функцианала от класса Item и Миксина
        :param name: Имя
        :param price: Цена
        :param quantity: Количество
        """
        super().__init__(name, price, quantity)