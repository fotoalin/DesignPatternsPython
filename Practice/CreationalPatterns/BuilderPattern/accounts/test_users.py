from .users import User

def test_user_creation() -> None:
    user = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="securepassword")
    assert user.first_name == "Alice"
    assert user.last_name == "Smith"
    assert user.email == "alice.smith@example.com"