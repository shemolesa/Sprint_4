import pytest

import data

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

    # проверяем, что в словарь не добавляются книги с негативным именем: такая книга уже есть в словаре, имя книги не указано, имя книги больше 41 символа
    @pytest.mark.parametrize('name', ['', '4 1  s y m b o l                         !'])
    def test_add_new_book_negative_name_not_added_book(self, collector, name, books_genre):
        len_books_genre = len(collector.books_genre) # вычисляем исходную длину словаря
        collector.add_new_book(name) # добавляем книгу с негативным именем
        assert len(collector.books_genre) == len_books_genre #проверяем, что длина словаря не изменилась

    # проверяем, что книге из словаря установлен жанр
    def test_set_book_genre_genre_and_book_available_set_genre(self, collector):
        collector.books_genre = {'Король лев': ''} # заполняем словарь книгой без жанра
        collector.set_book_genre('Король лев','Мультфильмы')  # устанавливаем жанр книге
        assert collector.books_genre == {'Король лев': 'Мультфильмы'} #проверяем, что жанр установлен книге

    # проверяем вывод жанра по имени книги из словаря книг с жанром
    def test_get_book_genre_name_book_genre(self, collector, books_genre):
        assert collector.get_book_genre('Король лев') == 'Мультфильмы' # проверяем, что жанр верный

    # проверяем, что список книг с указанным жанром пустой, если такие книги отсутствуют в словаре
    def test_get_books_with_specific_genre_genre_without_books_empty(self, collector, books_genre):
        assert collector.get_books_with_specific_genre('Комедия') == [] #проверяем, что список пустой

    # проверяем корректность вывода словаря книг с жанром
    def test_get_books_genre_dict_book_genre_true(self, collector):
        collector.books_genre = data.dict_books_genre  # заполняем словарь
        assert collector.get_books_genre() == data.dict_books_genre #reference_dictionary # сравниваем полученный словарь с эталоном

    #проверяем отсутствие в списке книг для детей книг с возрастным рейтингом
    def test_get_books_for_children_dict_book_genre_without_genre_age_rating(self, collector, books_genre):
        books_age_rating = ['Мизери', 'Шерлок Холмс и доктор Ватсон', 'Десять негритят']
        assert books_age_rating not in collector.get_books_for_children() # проверяем, что в сформированный список не попали книги  с возрастным рейтингом

    # проверка невозможности задублировать книгу в избранном
    def test_add_book_in_favorites_double_book_not_duplication(self, collector, books_genre, favorites):
        len_collector_favorites = len(collector.favorites) #сохраняем первоначальную длину списка избранного
        collector.add_book_in_favorites('Десять негритят') #добавляем книгу в избранное
        assert len(collector.favorites) == len_collector_favorites # проверяем, что длина списка избранного не изменилась

    # проверка удаления книги из избранного
    def test_delete_book_from_favorites_book_from_dictionary_book_deleted(self, collector, favorites):
        collector.delete_book_from_favorites('Десять негритят') # удаляем книгу из избранного
        assert 'Десять негритят' not in collector.favorites # проверяем отсутствие книги в избранном

    # проверка вывода списка избранного
    def test_get_list_of_favorites_books_list_favorites_true(self, collector):
        reference_favorites = ['Мизери', 'Колобок', 'Шерлок Холмс и доктор Ватсон', 'Десять негритят'] #эталонный список избранного
        collector.favorites = reference_favorites # заполняем список фаворитов
        assert collector.get_list_of_favorites_books() == reference_favorites # сравниваем полученный список с эталоном

