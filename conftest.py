import pytest

# класс BooksCollector, в котором реализован конструктор и методы
from main import BooksCollector

@pytest.fixture # создание объекта
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture # создание словаря  книга:жанр для объекта
def books_genre(collector):
    collector.books_genre = {'Мизери': 'Ужасы',
                             'Король лев': 'Мультфильмы',
                             'Шерлок Холмс и доктор Ватсон': 'Детективы',
                             'Смешарики': 'Мультфильмы',
                             'Десять негритят': 'Детективы',
                             'Понедельник начинается в субботу': 'Фантастика'}
    return collector.books_genre

@pytest.fixture # создание эталонного словаря книга:жанр
def reference_dictionary():
    reference_dictionary = {'Мизери': 'Ужасы',
                            'Король лев': 'Мультфильмы',
                            'Шерлок Холмс и доктор Ватсон': 'Детективы'}
    return reference_dictionary

@pytest.fixture # создание эталонного списка избранного для объекта
def favorites(collector):
    collector.favorites = ['Мизери', 'Шерлок Холмс и доктор Ватсон', 'Десять негритят']
    return collector.favorites