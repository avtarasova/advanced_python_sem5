from dataclasses import dataclass
from inspect import get_annotations
from datetime import datetime, timedelta

import sqlite3


@dataclass
class Readers:
    name: str
    id: int = 0

    def __init__(self, name):
        self.name = name


@dataclass
class Books:
    author: str
    title: str
    publish_year: int | None = None
    id: int = 0

    def __init__(self, author, title, publish_year=None):
        self.author = author
        self.title = title
        self.publish__year = publish_year


@dataclass
class Records:
    book_id: int
    reader_id: int
    taking_date: str = str(datetime.today().date())
    returning_date: str = str(datetime.today().date() + timedelta(days=7))
    id: int = 0

    def __init__(self, reader_id, book_id):
        self.book_id = book_id
        self.reader_id = reader_id


def add(obj):
    cls = type(obj)
    table = cls.__name__
    fields = get_annotations(cls)
    fields.pop('id')
    names = ', '.join(fields.keys())
    placeholders = ', '.join('?' * len(fields))
    values = [getattr(obj, i) for i in fields]
    with sqlite3.connect('library.db') as con:
        cur = con.cursor()
        cur.execute('PRAGMA foreign_keys = ON')
        cur.execute(f'INSERT INTO {table} ({names}) '
                    f'VALUES ({placeholders})', values)
        con.commit()
        obj.id = cur.lastrowid
    con.close()
    return obj.id


def get(table, pk):
    with sqlite3.connect('library.db') as con:
        cur = con.cursor()
        res = cur.execute(f'SELECT * FROM {table} WHERE id = {pk}')
        temp = res.fetchone()
    con.close()
    return temp


def get_all(table):
    with sqlite3.connect('library.db') as con:
        cur = con.cursor()
        res = cur.execute(f'SELECT * FROM {table}')
    return res.fetchall()


def delete(book_id, reader_id):
    pk = 0
    recs = get_all('Records')
    for i in recs:
        if i[1] == reader_id and i[2] == book_id:
            pk = i[0]
    if pk != 0:
        with sqlite3.connect('library.db') as con:
            cur = con.cursor()
            cur.execute(f'DELETE FROM \'Records\' WHERE id = {pk}')
            con.commit()
        con.close()


def test():
    add(Records(1, 1))
    rec = get_all("Records")
    print(rec)
    delete(1, 1)
    books = get_all('Records')
    print(books)


def execute():
    while True:
        try:
            cmd = input('$> ')
        except EOFError:
            break
        if not cmd:
            continue
        if cmd == 'Вывести список книг':
            books = get_all('Books')
            for book in books:
                print(f"Название - {book[2]}, автор - {book[1]}, год публикации - {book[3]}")
        if cmd == 'Вывести список читателей':
            readers = get_all('Readers')
            for reader in readers:
                print(reader[1])
        if cmd == 'Добавить книгу':
            title = input("Введите название книги:\n")
            author = input("Введите автора:\n")
            publish_year = input("Введите год публикации (опционально):\n")
            inp = [title, author, publish_year]
            if publish_year == '':
                book = Books(inp[1], inp[0])
            else:
                book = Books(author=inp[1], title=inp[0], publish_year=inp[2])
            add(book)
        if cmd == 'Добавить читателя':
            inp = input("Введите имя:\n")
            reader = Readers(name=inp)
            add(reader)
        if cmd == 'Выдать книгу читателю' or cmd == 'Принять книгу':
            book_id, reader_id = 0, 0
            name = input("Введите имя читателя:\n")
            title = input("Введите название книги:\n")
            author = input("Введите автора:\n")
            inp = [name, title, author]
            readers = get_all('Readers')
            books = get_all('Books')
            for book in books:
                if book[2] == inp[1] and book[1] == inp[2]:
                    book_id = book[0]
            for reader in readers:
                if reader[1] == inp[0]:
                    reader_id = reader[0]
            if book_id != 0 and reader_id != 0:
                if cmd[0] == 'В':
                    record = Records(book_id=book_id, reader_id=reader_id)
                    add(record)
                else:
                    delete(book_id=book_id, reader_id=reader_id)
            elif reader_id == 0:
                print('Мы не знаем этого читателя')
                continue
            elif book_id == 0:
                print('У нас нет и не было такой книжки')
                continue
        if cmd == 'Посмотреть выданные книги':
            recs = get_all('Records')
            for rec in recs:
                reader = get('Readers', rec[1])
                book = get('Books', rec[2])
                print(f'{book[2]} ({book[1]}) выдана читателю {reader[1]} {rec[3]}. Вернуть нужно {rec[4]}.')


if __name__ == '__main__':
    execute()
