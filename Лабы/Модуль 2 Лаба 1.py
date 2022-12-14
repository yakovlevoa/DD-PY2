# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Internet:
    def __init__(self, youtube_downloads: int, facebook_downloads: int):
        """"Класс Internet
        Содержит атрибуты: количество скачиваний youtube и facebook"""
        if not isinstance(youtube_downloads, int):
            raise TypeError
        if not youtube_downloads > 0:
            raise ValueError
        if not isinstance(facebook_downloads, int):
            raise TypeError
        if not facebook_downloads > 0:
            raise ValueError
        self.facebook_downloads = facebook_downloads
        self.youtube_downloads = youtube_downloads

    def is_youtube_more_popular(self) -> bool:
        """Функция проверит больше ли скачиваний у youtube чем у facebook
        пример:
        YOUvsFACE = Internet(10000000, 1000000)
        YOUvsFACE.is_youtube_more_popular()
        return = True or False"""
        ...

    def updating_stats(self, downloads_you: int, downloads_face: int):
        """Обновляет статистику по скачиваниям увеличивая их количество
        пример:
        internet = Internet(10000000, 1000000)
        internet.updating_stats(1000, 900)
        return = обновлённые данные"""
        if not isinstance(downloads_you, int):
            raise TypeError
        if not downloads_you > 0:
            raise ValueError
        if not isinstance(downloads_face, int):
            raise TypeError
        if not downloads_face > 0:
            raise ValueError
        ...


class Lunchbox:
    def __init__(self, sandwich_length: int, sandwich_width: int):
        if not isinstance(sandwich_length, int):
            raise TypeError
        if not sandwich_length > 0:
            raise ValueError
        if not isinstance(sandwich_width, int):
            raise TypeError
        if not sandwich_width > 0:
            raise ValueError
        self.sandwich_width = sandwich_width
        self.sandwich_length = sandwich_length

    def is_length_is_more_than_width(self) -> bool:
        """Функция проверит больше ли длина у сендвича чем ширина
        пример:
        LENvsWID = Lunchbox(15, 8)
        LENvsWID.is_length_is_more_than_width()
        return = True or False"""

        ...

    def biting_the_sandwich(self, bite: int):
        """Функция покажет насколько изменилась длина сендвича помле укуса
        пример:
        sandwich = Lunchbox(15, 8)
        sandwich.biting_the_sandwich(3)
        return = сколько осталось в длину от сендвича"""
        if not isinstance(bite, int):
            raise TypeError
        if not bite > 0:
            raise ValueError
        ...

class Car:
    def __init__(self, horse_powers: int, max_speed: int):
        if not isinstance(horse_powers, int):
            raise TypeError
        if not isinstance(max_speed, int):
            raise TypeError
        if not max_speed > 0:
            raise ValueError
        if not horse_powers > 0:
            raise ValueError
        self.max_speed = max_speed
        self.horse_powers = horse_powers

    def hp_more_than_250(self) -> bool:
        """Функция проверит больше ли мощность в л.с. чем 250 для рассчёта налогов
        пример:
        hp = Car(200, 180)
        hp.hp_more_than_250()
        return = True or False"""
        ...

    def tuning(self, hp_increase: int, speed_increase: int):
        """Функция покажет насколько увеличилась мощность и максимальная скорость после
        тюнинга автомобиля
        пример:
        car = Car(200, 180)
        car.tuning(100, 120)
        return = изменённые значения мощности и скорости
        """
        if not isinstance(hp_increase, int):
            raise TypeError
        if not hp_increase > 0:
            raise ValueError
        if not isinstance(speed_increase, int):
            raise TypeError
        if not speed_increase > 0:
            raise ValueError
if __name__ == "__main__":
    doctest.testmod()
    pass
