# qa_python

## tests.py
файл с тестами

_test_add_new_book_negative_name_not_added_book_ - проверка невозможности добавить в словарь книги с негативным именем:
    * в словаре есть книга с указанным именем
    * имя книги не указано
    * имя книги больше 41 символа

_test_set_book_genre_genre_and_book_available_set_genre_ - проверка установки жанра книге, если книга есть в словаре, и есть жанр

_test_get_book_genre_name_book_genre_ - проверка вывода жанра по имени книги 

_test_get_books_with_specific_genre_genre_without_books_empty_ - проверка получения пустого списка при отсутствии книг с указанным жанром в словаре

_test_get_book_genre_dict_book_genre_tru_ - проверка корректности вывода словаря книг с жанром

_test_get_books_for_children_dict_book_genre_without_genre_age_rating_ - проверка отсутствия в списке книг для детей книг с возрастным рейтингом

_test_add_book_in_favorites_double_book_not_duplication_ - проверка невозможности задублировать книгу в избранном

_test_delete_book_from_favorites_book_from_dictionary_book_deleted_ - проверка удаления книги из избранного

_test_get_list_of_favorites_books_list_favorites_true_ - проверка вывода списка избранного

## conftest.py 
файл с фикстурами

_collector_ - создание объекта

_books_genre_ - создание словаря  книга:жанр для объекта

_reference_dictionary_ - создание эталонного словаря книга:жанр

_favorites_ - создание эталонного списка избранного для объекта
