# test_api.py
import os
import django
import json
import requests

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_api_project.settings')
django.setup()

# Constants
BASE_URL = "http://localhost:8000/api"

def test_book_endpoints():
    print("\n===== Testing Book Endpoints =====")
    
    # 1. Test listing books (public access)
    print("\n-- Testing GET /books/ (List) --")
    response = requests.get(f"{BASE_URL}/books/")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json() if response.status_code == 200 else response.text}")
    
    # 2. Test creating a book (unauthenticated - should fail)
    print("\n-- Testing POST /books/create/ without authentication (should fail) --")
    book_data = {
        "title": "Test Book",
        "publication_year": 2020,
        "author": 1  # Assumes author with ID 1 exists
    }
    response = requests.post(f"{BASE_URL}/books/create/", json=book_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json() if response.status_code in [200, 201, 400] else response.text}")
    
    # 3. Rest of the tests would require authentication tokens
    print("\nFor complete testing including authenticated requests, you would need to:")
    print("1. Get an authentication token")
    print("2. Use the token in subsequent requests")
    print("3. Test the protected endpoints with proper authentication")

if __name__ == "__main__":
    test_book_endpoints()
    print("\nNote: Some tests may fail if the server is not running.")
    print("Start the server with 'python manage.py runserver' before running this script.")