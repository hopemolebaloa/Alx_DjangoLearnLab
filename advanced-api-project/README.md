# Advanced API Project with Django REST Framework

This project demonstrates the implementation of a RESTful API using Django REST Framework, with a focus on custom serializers and generic views.

## API Endpoints

### Books API

- **GET /api/books/** - List all books (public)
  - Supports filtering with query parameters:
    - `?title=searchterm`
    - `?year=2023`

- **GET /api/books/{id}/** - Get details of a specific book (public)

- **POST /api/books/create/** - Create a new book (authenticated users only)
  - Required fields: `title`, `publication_year`, `author`

- **PUT/PATCH /api/books/update/{id}/** - Update a book (authenticated users only)

- **DELETE /api/books/delete/{id}/** - Delete a book (authenticated users only)

### Authors API

- **GET /api/authors/** - List all authors (public)
- **GET /api/authors/{id}/** - Get details of a specific author (public)
- **POST /api/authors/** - Create a new author (authenticated users only)
- **PUT/PATCH /api/authors/{id}/** - Update an author (authenticated users only)
- **DELETE /api/authors/{id}/** - Delete an author (authenticated users only)

## Authentication

- This API uses token authentication for protected endpoints
- To obtain a token, send a POST request to `/api-token-auth/` with username and password
- Include the token in the Authorization header: `Authorization: Token <your_token>`

## Data Models

### Author
- `name` (string): The author's name

### Book
- `title` (string): The book's title
- `publication_year` (integer): Year when the book was published
- `author` (foreign key): Reference to an Author object

## Custom Validations

### Book Model Validation
- Publication year cannot be in the future
- Publication year cannot be before 1700
- Title must be at least 3 characters
- Title cannot contain inappropriate words
- Books published before 1900 cannot have "Modern" in the title

### Author Model Validation
- Name must be at least 2 characters long
- Name cannot contain numbers

## Running the Project

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Start the server: `python manage.py runserver`
6. Access the API at http://localhost:8000/api/