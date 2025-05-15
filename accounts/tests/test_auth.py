import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from accounts.models import User

@pytest.mark.django_db
def test_signup_success():
    client = APIClient()
    response = client.post("/signup", {
        "username": "testuser",
        "password": "testpass123",
        "nickname": "Tester"
    })
    assert response.status_code == 201
    assert response.data["username"] == "testuser"

@pytest.mark.django_db
def test_signup_existing_user():
    User.objects.create_user(username="testuser", password="testpass123", nickname="Tester")
    client = APIClient()
    response = client.post("/signup", {
        "username": "testuser",
        "password": "testpass123",
        "nickname": "Tester"
    })
    assert response.status_code == 400
    assert response.data["error"]["code"] == "USER_ALREADY_EXISTS"

@pytest.mark.django_db
def test_login_success():
    User.objects.create_user(username="testuser", password="testpass123", nickname="Tester")
    client = APIClient()
    response = client.post("/login", {
        "username": "testuser",
        "password": "testpass123",
    })
    assert response.status_code == 200
    assert "token" in response.data
