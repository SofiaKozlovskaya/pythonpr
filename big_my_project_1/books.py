from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class Book:
    title: str                # Название
    author: str               # Автор
    genre: str                # Жанр
    year: date                # Год издания
    pages: int                # Количество страниц
    rating: float             # Рейтинг (0-5)
    id: int | None = None

@dataclass(slots=True)
class ReaderBook:
    book_id: int              # ID книги из каталога
    user: str                 # Имя читателя
    status: str               # Статус: хочу прочитать, читаю, прочитано, брошено
    personal_rating: float | None = None  # Личная оценка (0-5)
    review: str | None = None            # Отзыв (текст)
    id: int | None = None
