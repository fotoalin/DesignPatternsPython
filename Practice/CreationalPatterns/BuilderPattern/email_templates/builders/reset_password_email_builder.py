from .base import EmailBuilder

class PasswordResetEmailBuilder(EmailBuilder):
    def __init__(self):
        self.email = {}

    def add_subject(self):
        self.email['subject'] = "🔑 Password Reset Request"

    def add_greeting(self, name: str):
        self.email['greeting'] = f"Hi {name},"

    def add_body(self, context: dict):
        self.email['body'] = (
            "We received a request to reset your password.\n"
            "To reset your password, click the link below:\n"
            f"reset_link: {context.get('reset_link')}\n"
        )

    def add_footer(self):
        self.email['footer'] = "If you didn't request this, please ignore this email."

    def get_email(self) -> dict:
        return self.email