from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_same_book(self):
        collector = BooksCollector()
        collector.add_new_book("Зомби захочет убить вас")
        collector.add_new_book("Зомби захочет убить вас")
        assert len(collector.get_books_rating()) != 2

    def test_set_book_rating_not_in_list(self):
        collector = BooksCollector()
        collector.set_book_rating("Кошка зомби", 1)
        assert collector.get_book_rating("Кошка зомби") != 1

    def test_set_book_rating_zero(self):
        collector = BooksCollector()
        collector.add_new_book("Zombie Dog")
        collector.set_book_rating("Zombie Dog", 0)
        assert collector.get_book_rating("Zombie Dog") != 0

    def test_set_book_rating_above_ten(self):
        collector = BooksCollector()
        collector.add_new_book("Marmot zombie")
        collector.set_book_rating("Marmot zombie", 15)
        assert collector.get_book_rating("Marmot zombie") != 15

    def test_get_book_rating_by_name(self):
        collector = BooksCollector()
        collector.add_new_book("One")
        assert collector.get_book_rating("One") == 1

    def test_get_books_with_specific_rating(self):
        collector = BooksCollector()
        collector.add_new_book("Two")
        collector.add_new_book("Three")
        collector.set_book_rating("Three", 8)
        assert "Three" in collector.get_books_with_specific_rating(8)

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Python for dummies")
        collector.add_book_in_favorites("Python for dummies")
        assert collector.get_list_of_favorites_books().__contains__("Python for dummies")

    def test_add_book_in_favorites_if_not_in_books_rating(self):
        collector = BooksCollector()
        collector.add_book_in_favorites("111")
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("AQA chapter_1")
        collector.add_new_book("AQA chapter_2")
        collector.add_book_in_favorites("AQA chapter_1")
        collector.add_book_in_favorites("AQA chapter_2")
        collector.delete_book_from_favorites("AQA chapter_1")
        assert "AQA chapter_1" not in collector.get_list_of_favorites_books()
