import pytest

# файл с тестовыми данными
import data

# класс BooksCollector, в котором реализован конструктор и методы
from main import BooksCollector

@pytest.fixture # создание объекта
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture # создание словаря  книга:жанр для объекта
def books_genre(collector):
    collector.books_genre = data.dict_books_genre
    return collector.books_genre

@pytest.fixture # создание эталонного списка избранного для объекта
def favorites(collector):
    collector.favorites = data.ls_favorites
    return collector.favorites