# Advanced API Project with Django REST Framework

This project demonstrates the implementation of a RESTful API using Django REST Framework, with a focus on custom serializers, generic views, and advanced query capabilities.

## API Endpoints

### Books API

- **GET /api/books/** - List all books (public)
  - **Filtering Options**:
    - Filter by title: `?title=django`
    - Filter by publication year: `?publication_year=2023`
    - Filter by author ID: `?author=1`
    - Filter by author name: `?author_name=tolkien`
    - Filter by year range: `?min_year=2000&max_year=2023`
  - **Search Options**:
    - Search across title and author name: `?search=python`
  - **Ordering Options**:
    - Order by any field: `?ordering=publication_year`
    - Reverse ordering: `?ordering=-publication_year`
    - Multiple ordering fields: `?ordering=author__name,publication_year`

- **GET /api/books/{id}/** - Get details of a specific book (public)

- **POST /api/books/create/** - Create a new book (authenticated users only)
  - Required fields: `title`, `publication_year`, `author`

- **PUT/PATCH /api/books/update/{id}/** - Update a book (authenticated users only)

- **DELETE /api/books/delete/{id}/** - Delete a book (authenticated users only)

### Authors API

- **GET /api/authors/** - List all authors (public)
  - **Filtering Options**:
    - Filter by name: `?name=tolkien`
  - **Search Options**:
    - Search by name: `?search=tolkien`
  - **Ordering Options**:
    - Order by name: `?ordering=name`
    - Reverse ordering: `?ordering=-name`

- **GET /api/authors/{id}/** - Get details of a specific author (public)
- **POST /api/authors/** - Create a new author (authenticated users only)
- **PUT/PATCH /api/authors/{id}/** - Update an author (authenticated users only)
- **DELETE /api/authors/{id}/** - Delete an author (authenticated users only)

## Examples

### Filtering Examples

Get all books published after 2020: