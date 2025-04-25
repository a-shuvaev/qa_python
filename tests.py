from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
   
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_one_book_added(self):
        collector = BooksCollector()
        
        collector.add_new_book('Гордость и предубеждение и зомби')
        
        assert 'Гордость и предубеждение и зомби' in collector.get_books_genre()
        
    @pytest.mark.parametrize('book_name', ['', 'A' * 41])
    def test_add_new_book_invalid_length_not_added(self, book_name):
        collector = BooksCollector()
        
        collector.add_new_book(book_name)
        
        assert book_name not in collector.get_books_genre()
    
    @pytest.mark.parametrize('book_name, genre',[
        ['Гордость и предубеждение и зомби', 'Фантастика'],
        ['Кладбище домашних животных', 'Ужасы'],
        ['Достать ножи', 'Детективы'],
        ['Маша и медведь', 'Мультфильмы'],
        ['Парни со стволами', 'Комедии']
    ])    
    def test_set_book_genre_valid_name_genre_established(self, book_name, genre):
        collector = BooksCollector()
        
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        
        assert collector.get_book_genre(book_name) == genre
    
    def test_set_book_genre_invalid_book_genre_not_established(self):
        collector = BooksCollector()
        
        collector.set_book_genre('Кладбище домашних животных', 'Ужасы')
        
        assert collector.get_book_genre('Кладбище домашних животных') == None
        
    def test_set_book_genre_invalid_genre_not_established(self):
        collector = BooksCollector()
        
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Рофлы')
        
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''
    
    def test_get_book_genre_one_genre_success(self):
        collect = BooksCollector()
        
        collect.add_new_book('Гордость и предубеждение и зомби')
        collect.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        
        assert collect.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'
    
    def test_get_books_genre_add_two_books_and_genre_success(self):
        collect = BooksCollector()
        
        collect.add_new_book('Гордость и предубеждение и зомби')
        collect.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collect.add_new_book('Кладбище домашних животных')
        collect.set_book_genre('Кладбище домашних животных', 'Ужасы')
        
        assert collect.get_books_genre() == {'Гордость и предубеждение и зомби': 'Фантастика',
                                             'Кладбище домашних животных': 'Ужасы'}
    
    def test_get_books_for_children_all_genre_success(self):
        collect = BooksCollector()
        
        collect.add_new_book('Гордость и предубеждение и зомби')
        collect.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collect.add_new_book('Кладбище домашних животных')
        collect.set_book_genre('Кладбище домашних животных', 'Ужасы')
        collect.add_new_book('Достать ножи')
        collect.set_book_genre('Достать ножи', 'Детективы')
        collect.add_new_book('Маша и медведь')
        collect.set_book_genre('Маша и медведь', 'Мультфильмы')
        
        assert collect.get_books_for_children() == ['Гордость и предубеждение и зомби', 'Маша и медведь']
        
    def test_add_book_in_favorites_one_book_success(self):
        collect = BooksCollector()
        
        collect.add_new_book('Гордость и предубеждение и зомби')
        collect.add_book_in_favorites('Гордость и предубеждение и зомби')
        
        assert collect.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']
        
    def test_add_book_in_favorites_not_exist_not_added(self):
        collect = BooksCollector()
        
        collect.add_book_in_favorites('Гордость и предубеждение и зомби')
        
        assert collect.get_list_of_favorites_books() == []
    
    def test_delete_book_from_favorites_delete_one_book_empty(self):
        collect = BooksCollector()
        
        collect.add_new_book('Гордость и предубеждение и зомби')
        collect.add_book_in_favorites('Гордость и предубеждение и зомби')
        collect.delete_book_from_favorites('Гордость и предубеждение и зомби')
        
        assert collect.get_list_of_favorites_books() == []
        
    def test_get_list_of_favorites_books_add_two_books_success(self):
        collect = BooksCollector()
        
        collect.add_new_book('Гордость и предубеждение и зомби')
        collect.add_book_in_favorites('Гордость и предубеждение и зомби')
        collect.add_new_book('Кладбище домашних животных')
        collect.add_book_in_favorites('Кладбище домашних животных')
        
        assert collect.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Кладбище домашних животных']
    
    def test_get_books_with_specific_genre_one_genre_success(self):
        collect = BooksCollector()
        
        collect.add_new_book('Гордость и предубеждение и зомби')
        collect.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collect.add_new_book('Кладбище домашних животных')
        collect.set_book_genre('Кладбище домашних животных', 'Ужасы')
        collect.add_new_book('Задача трех тел')
        collect.set_book_genre('Задача трех тел', 'Фантастика')
        
        assert collect.get_books_with_specific_genre('Фантастика') == ['Гордость и предубеждение и зомби', 'Задача трех тел']

