import csv
#import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []



    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        #Item.all.append(self)


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        """
        Сложение количества товаров из классов Item и Phone
        (сложение по количеству товара в магазине)
        """
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError()


    def calculate_total_price(self) -> float:
        """
        Общая стоимость товара
        """
        return self.price*self.quantity

    def apply_discount(self) -> float:
        """
        Скидка на товар
        """
        self.price = self.price*self.pay_rate
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, path_items):
        with open(path_items, encoding='utf-8') as f:
            file = csv.DictReader(f)
            for i in file:
                name = i['name']
                price = float(i['price'])
                quantity = int(i['quantity'])
                item = cls(name, price, quantity)
                item.name = name
                item.price = price
                item.quantity = quantity


    @staticmethod
    def string_to_number(number: str) -> int:
        return int(float(number))
