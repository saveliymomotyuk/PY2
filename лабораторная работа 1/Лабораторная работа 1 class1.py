import doctest
class instagramsubs:
    def __init__(self, subscribers: int, subscribes: int):
        """
        Обьект - ИнстаграммПодписки
        subscrubers = подписчики, subscribes = подписки
        >>>Пример: instagramsubs( 1250, 220)
         """
        if not isinstance(subscribers, int):
            raise TypeError("Подписчики - только цифры")
        if subscribers < 0:
            raise ValueError("Подписчиков не может быть меньше 0")
        self.subscribers = subscribers
        if not isinstance(subscribes, int):
            raise TypeError("Подписки - только цифры")
        if subscribes < 0:
            raise ValueError("Подписок не может быть меньше 0")
        self.subscribes = subscribes

    def subscribersGrow(self, newsub: int) -> None:
        """
        Функция роста подписчиков
        ValyeError когда рост равен 0 и меньше
        >>>Пример: instagramsubs(1250, 220)
        >>>instagramsubs.subscribersGrow(30)
        """
        if newsub < 1:
            raise ValueError("новых подписчиков не может быть меньше 1")

    def subscriberLose(self, sub: int) -> None:
        """Функция отписки подписчиков
              ValyeError когда отписки равены 0 и меньше"""
        if sub < 1:
            raise ValueError("отписок не может быть меньше 1")



if __name__ == "__main__":
    doctest.testmod()
    pass
