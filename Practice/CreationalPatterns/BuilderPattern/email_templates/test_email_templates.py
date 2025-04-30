from typing import Dict, Tuple
import sys
from pathlib import Path

# Add parent directory to path to enable imports from sibling packages
# This approach works for both direct execution and when running with pytest
parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

from accounts.users import User
# Use a relative import for the email_service
from .email_service import generate_welcome_email, generate_password_reset_email


def test_generate_welcome_email() -> None:
    user = User(first_name="Alice", last_name="Smith", email="alice@example.com", password="securepassword")
    user.is_active = True

    subject, full_email = generate_welcome_email(user)
    print("Subject:", subject)
    print("Email Content:", full_email)
    assert subject == "🎉 Welcome to Our Platform!"
    assert "Hi Alice," in full_email
    assert "Cheers," in full_email
    assert "Thanks for signing up!" in full_email
    assert "https://app.example.com/dashboard" in full_email


def test_generate_password_reset_email() -> None:
    user = User(first_name="Alin", last_name="Morosanu", email="alin@lolascupcakes.co.uk", password="alinsecurepassword")
    user.is_active = True
    user.is_verified = True
    subject, full_email = generate_password_reset_email(user)
    print("Subject:", subject)
    print("Email Content:", full_email)
    assert subject == "🔑 Password Reset Request"
    assert "Hi Alin," in full_email
    assert "Morosanu" not in full_email
    assert "We received a request to reset your password." in full_email
    assert "To reset your password, click the link below:" in full_email
    assert "If you didn't request this, please ignore this email." in full_email
    assert "https://app.example.com/reset-password" in full_email


if __name__ == "__main__":
    test_generate_welcome_email()
    test_generate_password_reset_email()
