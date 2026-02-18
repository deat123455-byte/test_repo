import sqlite3
from typing import List, Tuple

def create_database():
    """Создает базу данных и таблицу books"""
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    # Создание таблицы books
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER
        )
    ''')
    
    conn.commit()
    conn.close()

def add_book(title: str, author: str, year: int = None) -> int:
    """
    Добавляет новую книгу в базу данных
    
    Args:
        title (str): Название книги
        author (str): Автор книги
        year (int, optional): Год издания
        
    Returns:
        int: ID добавленной книги
    """
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO books (title, author, year)
        VALUES (?, ?, ?)
    ''', (title, author, year))
    
    book_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return book_id

def get_all_books() -> List[Tuple]:
    """
    Получает список всех книг из базы данных
    
    Returns:
        List[Tuple]: Список кортежей с информацией о книгах
    """
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    
    conn.close()
    return books

def update_book(book_id: int, title: str = None, author: str = None, year: int = None):
    """
    Обновляет информацию о книге
    
    Args:
        book_id (int): ID книги для обновления
        title (str, optional): Новое название книги
        author (str, optional): Новый автор книги
        year (int, optional): Новый год издания
    """
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    # Формируем запрос обновления динамически
    updates = []
    params = []
    
    if title is not None:
        updates.append("title = ?")
        params.append(title)
    if author is not None:
        updates.append("author = ?")
        params.append(author)
    if year is not None:
        updates.append("year = ?")
        params.append(year)
    
    if updates:  # Если есть что обновлять
        query = f"UPDATE books SET {', '.join(updates)} WHERE id = ?"
        params.append(book_id)
        cursor.execute(query, params)
        conn.commit()
    
    conn.close()

def delete_book(book_id: int):
    """
    Удаляет книгу по её идентификатору
    
    Args:
        book_id (int): ID книги для удаления
    """
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()

# Тестирование функций
if __name__ == "__main__":
    # Создаем базу данных и таблицу
    create_database()
    
    print("=== Тестирование работы с базой данных ===")
    
    # Добавляем несколько книг
    print("\n1. Добавление книг:")
    book1_id = add_book("Война и мир", "Лев Толстой", 1869)
    book2_id = add_book("Преступление и наказание", "Федор Достоевский", 1866)
    book3_id = add_book("1984", "Джордж Оруэлл", 1948)
    
    print(f"Добавлена книга 1 с ID: {book1_id}")
    print(f"Добавлена книга 2 с ID: {book2_id}")
    print(f"Добавлена книга 3 с ID: {book3_id}")
    
    # Получаем все книги
    print("\n2. Все книги в базе:")
    all_books = get_all_books()
    for book in all_books:
        print(f"ID: {book[0]}, Название: {book[1]}, Автор: {book[2]}, Год: {book[3]}")
    
    # Обновляем информацию о книге
    print("\n3. Обновление информации о книге:")
    update_book(book1_id, year=1870)
    print(f"Обновлен год для книги с ID {book1_id}")
    
    # Проверяем изменения
    updated_books = get_all_books()
    for book in updated_books:
        if book[0] == book1_id:
            print(f"Обновленная книга: ID: {book[0]}, Название: {book[1]}, Автор: {book[2]}, Год: {book[3]}")
    
    # Удаляем книгу
    print("\n4. Удаление книги:")
    print(f"Удаляем книгу с ID {book2_id}")
    delete_book(book2_id)
    
    # Проверяем результат
    print("Книги после удаления:")
    remaining_books = get_all_books()
    for book in remaining_books:
        print(f"ID: {book[0]}, Название: {book[1]}, Автор: {book[2]}, Год: {book[3]}")
    
    print("\n=== Тест завершен ===")