from email_templates.builders.welcome_email_builder import WelcomeEmailBuilder 
from email_templates.builders.reset_password_email_builder import PasswordResetEmailBuilder
from director import EmailDirector
from typing import Dict, Tuple


def generate_welcome_email(user: Dict[str, str]) -> Tuple[str, str]:
    """
    Generates a welcome email for a new user.
    Args:
        user (Dict[str, str]): A dictionary containing user information.
    Returns:
        Tuple[str, str]: A tuple containing the subject and the full email content.
    """
    # Assuming user is a dictionary with keys 'first_name' and 'email'
    if not user:
        raise ValueError("User information is required")
    # Initialize the builder and director
    builder = WelcomeEmailBuilder()
    director = EmailDirector(builder)
    context = {"dashboard_url": "https://app.example.com/dashboard"}
    email = director.build_email(user.first_name, context)

    # Return as formatted string or dict, depending on your mail backend
    full_email = f"""
    {email['greeting']}

    {email['body']}

    {email['footer']}"""

    subject = email['subject']
    return subject, full_email


def generate_password_reset_email(user: Dict[str, str]) -> Tuple[str, str]:
    """
    Generates a password reset email for a user.
    Args:
        user (Dict[str, str]): A dictionary containing user information.
    Returns:
        Tuple[str, str]: A tuple containing the subject and the full email content.
    """
    if not user:
        raise ValueError("User information is required")
    # Initialize the builder and director
    builder = PasswordResetEmailBuilder()
    director = EmailDirector(builder)
    context = {"reset_link": "https://app.example.com/reset-password"}
    email = director.build_email(user.first_name, context)
    full_email = f"""
    {email['greeting']}
    {email['body']}
    {email['footer']}"""
    subject = email['subject']
    return subject, full_email