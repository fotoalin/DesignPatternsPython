from .base import EmailBuilder

class WelcomeEmailBuilder(EmailBuilder):
    def __init__(self):
        self.email = {}

    def add_subject(self):
        self.email['subject'] = "🎉 Welcome to Our Platform!"

    def add_greeting(self, name: str):
        self.email['greeting'] = f"Hi {name},"

    def add_body(self, context: dict):
        self.email['body'] = (
            "Thanks for signing up! We're excited to have you on board!\n"
            f"To get started, visit: {context.get('dashboard_url')}"
        )

    def add_footer(self):
        self.email['footer'] = "Cheers,\nThe Team"

    def get_email(self) -> dict:
        return self.email
