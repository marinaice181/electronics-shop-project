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

    @staticmethod
    def string_to_number(number: str) -> int:
        return int(float(number))

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