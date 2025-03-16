# test_filtering.py
import requests
import json

BASE_URL = "http://localhost:8000/api"

def print_response(response):
    """Pretty print the response"""
    print(f"Status Code: {response.status_code}")
    if response.status_code in [200, 201]:
        try:
            data = response.json()
            print(json.dumps(data, indent=4))
        except:
            print(response.text)
    else:
        print(response.text)
    print("-" * 50)

def test_filtering():
    print("\n===== Testing Filtering =====")
    
    # Test filter by title
    print("\n-- Filter by title containing 'python' --")
    response = requests.get(f"{BASE_URL}/books/?title=python")
    print_response(response)
    
    # Test filter by publication year
    print("\n-- Filter by publication year 2023 --")
    response = requests.get(f"{BASE_URL}/books/?publication_year=2023")
    print_response(response)
    
    # Test filter by year range
    print("\n-- Filter by books published between 2020 and 2023 --")
    response = requests.get(f"{BASE_URL}/books/?min_year=2020&max_year=2023")
    print_response(response)
    
    # Test filter by author name
    print("\n-- Filter by author name containing 'tolkien' --")
    response = requests.get(f"{BASE_URL}/books/?author_name=tolkien")
    print_response(response)

def test_searching():
    print("\n===== Testing Searching =====")
    
    # Test search across title and author
    print("\n-- Search for 'python' in title or author name --")
    response = requests.get(f"{BASE_URL}/books/?search=python")
    print_response(response)

def test_ordering():
    print("\n===== Testing Ordering =====")
    
    # Test ordering by title
    print("\n-- Order by title (ascending) --")
    response = requests.get(f"{BASE_URL}/books/?ordering=title")
    print_response(response)
    
    # Test reverse ordering
    print("\n-- Order by publication year (descending) --")
    response = requests.get(f"{BASE_URL}/books/?ordering=-publication_year")
    print_response(response)
    
    # Test multiple ordering fields
    print("\n-- Order by author name, then publication year --")
    response = requests.get(f"{BASE_URL}/books/?ordering=author__name,publication_year")
    print_response(response)

if __name__ == "__main__":
    test_filtering()
    test_searching()
    test_ordering()