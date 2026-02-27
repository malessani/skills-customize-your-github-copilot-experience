# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI to practice creating endpoints, handling request data, and returning JSON responses. By the end of this assignment, you will understand the core structure of an API service in Python.

## 📝 Tasks

### 🛠️ Create a FastAPI Application

#### Description
Set up a FastAPI project and implement a small API for managing a list of books in memory.

#### Requirements
Completed program should:

- Create a FastAPI app instance and run it locally.
- Implement a `GET /` endpoint that returns a welcome message.
- Implement a `GET /books` endpoint that returns all books.
- Implement a `POST /books` endpoint that adds a new book with fields such as `id`, `title`, and `author`.
- Validate request data using a Pydantic model.


### 🛠️ Add Detail and Deletion Endpoints

#### Description
Expand your API with endpoints to retrieve and remove individual books.

#### Requirements
Completed program should:

- Implement a `GET /books/{book_id}` endpoint that returns one book by ID.
- Implement a `DELETE /books/{book_id}` endpoint that removes one book by ID.
- Return clear error responses when a book ID does not exist.
- Use appropriate HTTP status codes for success and failure.
- Keep endpoint behavior consistent and easy to test using a tool like Swagger UI.
