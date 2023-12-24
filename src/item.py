import csv


class InstantiateCSVError:
    pass


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
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) <= 10:
            self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @staticmethod
    def string_to_number(value: str):
        return int(value)

    @classmethod
    def instantiate_from_csv(cls, filename='../src/items.cvs') -> str:
        """
        класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_
        """
        try:
            with open(filename) as f:
                reader = csv.DictReader(f)
                cls.all.clear()
                for row in reader:
                    name = row['name']
                    price = cls.string_to_number(row['price'])
                    quantity = cls.string_to_number(row['quantity'])
                    cls.all.append(cls(name, price, quantity))  # создаем экзмляры классы и кладем их в список
        except FileNotFoundError:
            return f"Отсутствует файл {filename}"
        except InstantiateCSVError:
            return f"Файл {filename} поврежден"