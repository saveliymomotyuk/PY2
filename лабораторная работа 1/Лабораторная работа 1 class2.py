import doctest
class MoneyInBank:
    def __init__(self, rub: int, dollar: int, euro: int):
        """
        :param rub:
        :param dollar:
        :param euro:
        """
        self.rub = rub
        self.dollar = dollar
        self.euro = euro
        if not isinstance(rub, int):
            raise TypeError("Деньги - это число")
        if rub < 0:
            raise ValueError("Денег не может быть меньше 0")
        if not isinstance(dollar, int):
            raise TypeError("Деньги - это число")
        if dollar < 0:
            raise ValueError("Денег не может быть меньше 0")
        if not isinstance(euro, int):
            raise TypeError("Деньги - это число")
        if euro < 0:
            raise ValueError("Денег не может быть меньше 0")

    def euroGain(self, newEuro: int) -> None:
        """
        >>>MoneyInBank.euroGain(self, newEuro=10)
        :param newEuro:
        :return:
        """
        ...

    def dollarGain(self, newdollar: int) -> None:

        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
