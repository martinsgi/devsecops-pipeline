"""
Unit tests for the DevSecOps Demo Application
Run with: pytest tests/ -v
"""
import pytest
import sys
import os

# Add the app directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_page_returns_200(client):
    """Test that the home page loads successfully"""
    response = client.get('/')
    assert response.status_code == 200


def test_home_page_contains_title(client):
    """Test that the home page contains the expected title"""
    response = client.get('/')
    assert b'Secure DevOps Demo App' in response.data


def test_home_page_contains_search_form(client):
    """Test that the home page has a search form"""
    response = client.get('/')
    assert b'<form action="/search"' in response.data


def test_search_endpoint_returns_200(client):
    """Test that the search endpoint works"""
    response = client.get('/search?query=laptop')
    assert response.status_code == 200


def test_search_with_empty_query(client):
    """Test search with empty query string"""
    response = client.get('/search?query=')
    assert response.status_code == 200


def test_search_results_contain_query(client):
    """Test that search results page shows the query"""
    response = client.get('/search?query=test')
    assert b'Search Results for: test' in response.data


def test_health_endpoint(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'


def test_health_endpoint_returns_json(client):
    """Test that health endpoint returns proper JSON"""
    response = client.get('/health')
    assert response.content_type == 'application/json'
    assert 'status' in response.json
    assert 'app' in response.json


def test_search_finds_laptop(client):
    """Test that search can find items in database"""
    response = client.get('/search?query=Laptop')
    assert response.status_code == 200
    # The response should contain laptop-related content
    assert b'Laptop' in response.data or b'laptop' in response.data
