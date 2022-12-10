import doctest
class Headphones:
    def __init__(self, chargeleft: int, chargeright: int, lengthOfWire: [int, float]):
        self.chargeleft = chargeleft
        self.chargeright = chargeright
        self.lengthOfWire = lengthOfWire
        Headphones = "Наушники"
        if not isinstance(chargeright, (int, float)):
            raise TypeError("Заряд только цифрой")
        if chargeleft < 0:
            raise ValueError("зарядки не может быть меньше 0")
        if not isinstance(chargeright, (int, float)):
            raise TypeError("Заряд только цифрой")
        if chargeright < 0:
            raise ValueError("зарядки не может быть меньше 0")
        if chargeright > 100:
            raise ValueError("Зарядки не может быть больше 100 процентов")
        if chargeleft > 100:
            raise ValueError("Зарядки не может быть больше 100 процентов")
        if lengthOfWire < 0:
            raise ValueError("Провод не может быть такой короткий")

    def charge(self, charging: int) -> None:

        """
        Зарядка Наушников
        :param charging: проценты заряда
        :return: количество финального заряда
        """

    def musicplay(self, song):
        return "В наушниках играет:", song


if __name__ == "__main__":
    doctest.testmod()
    pass
