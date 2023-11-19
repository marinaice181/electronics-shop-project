import codecs
import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name =  name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            print('Длина наименования товара больше 10 символов')
        else:
            self.__name = new_name[:10]


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename: str):
        """Инициализируем экземпляры класса Item данными из файла src/items.csv"""
        cls.all.clear()  # очистка списка перед загрузкой данных из файла csv

        try:
            with codecs.open(filename, 'r', encoding='utf-8', errors='replace') as f:
                reader = csv.DictReader(f)
                items = []
                for row in reader:
                    if 'name' not in row or 'price' not in row or 'quantity' not in row:
                        raise InstantiateCSVError("Файл items.csv поврежден")
                    name = row['name']
                    price = float(row['price'])
                    quantity = int(row['quantity'])
                    item = cls(name, price, quantity)
                    items.append(item)

                cls.all = items
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv")


    @staticmethod
    def string_to_number(number: str):
            return int(float(number))


    def __add__(self, other):
        """ Сложение количества товаров из классов Item и Phone"""
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return None

