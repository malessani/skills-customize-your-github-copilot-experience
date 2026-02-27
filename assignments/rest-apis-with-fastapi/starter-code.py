from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books API")


class Book(BaseModel):
    id: int
    title: str
    author: str


books: List[Book] = [
    Book(id=1, title="Clean Code", author="Robert C. Martin"),
    Book(id=2, title="The Pragmatic Programmer", author="Andrew Hunt")
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Books API"}


@app.get("/books", response_model=List[Book])
def get_books():
    return books


@app.post("/books", response_model=Book, status_code=201)
def create_book(book: Book):
    if any(existing_book.id == book.id for existing_book in books):
        raise HTTPException(status_code=400, detail="Book ID already exists")
    books.append(book)
    return book


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            del books[index]
            return
    raise HTTPException(status_code=404, detail="Book not found")
