# test_books_collector.py


class TestBooksCollector:
    
    def test_add_new_book(self, collector):
        collector.add_new_book("Дюна")
        assert "Дюна" in collector.books_genre

    def test_set_book_genre(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.books_genre["Гарри Поттер"] == "Фантастика"

    def test_get_book_genre(self, collector):
        collector.add_new_book("Властелин колец")
        assert collector.get_book_genre("Властелин колец") == ""

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book("Ну, погоди!")
        collector.set_book_genre("Ну, погоди!", "Мультфильмы")
        assert collector.get_books_with_specific_genre("Мультфильмы") == ["Ну, погоди!"]
    
    def test_get_books_genre(self, collector):
        collector.add_new_book("Оно")
        assert collector.get_books_genre() == {"Оно": ""}

    def test_get_books_for_children(self, collector):
        collector.add_new_book("Корпорация монстров")
        collector.set_book_genre("Корпорация монстров", "Мультфильмы")
        assert collector.get_books_for_children() == ["Корпорация монстров"]

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("Хоббит")
        collector.add_book_in_favorites("Хоббит")
        assert collector.get_list_of_favorites_books() == ["Хоббит"]

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Шерлок Холмс")
        collector.add_book_in_favorites("Шерлок Холмс")
        collector.delete_book_from_favorites("Шерлок Холмс")
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book("Мастер и Маргарита")
        collector.add_book_in_favorites("Мастер и Маргарита")
        assert collector.get_list_of_favorites_books() == ["Мастер и Маргарита"]