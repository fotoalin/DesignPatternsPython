Perfect — the **Builder Pattern** fits really well for generating **custom email templates** where parts like subject, body, greeting, and footer vary depending on context (welcome, invoice, password reset, etc).

---

## 📧 Use Case: **Email Template Generator**

Let’s say we’re building transactional emails for a Django app. Instead of mixing logic and string templates everywhere, we’ll use the Builder Pattern to cleanly construct them.

---

### 🧱 Structure

```
email_templates/
├── builders/
│   ├── __init__.py
│   ├── base.py
│   ├── welcome_email_builder.py
│   ├── invoice_email_builder.py
│   └── reset_password_email_builder.py
├── director.py
└── service.py
```

---

### 1. `builders/base.py` — Builder Interface

```python
from abc import ABC, abstractmethod

class EmailBuilder(ABC):
    @abstractmethod
    def add_subject(self): pass

    @abstractmethod
    def add_greeting(self, name: str): pass

    @abstractmethod
    def add_body(self, context: dict): pass

    @abstractmethod
    def add_footer(self): pass

    @abstractmethod
    def get_email(self) -> dict: pass
```

---

### 2. `builders/welcome_email_builder.py` — Concrete Builder

```python
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
            "Thanks for signing up. We're excited to have you on board!\n"
            f"To get started, visit: {context.get('dashboard_url')}"
        )

    def add_footer(self):
        self.email['footer'] = "Cheers,\nThe Team"

    def get_email(self) -> dict:
        return self.email
```

You could similarly create `InvoiceEmailBuilder`, `ResetPasswordEmailBuilder`, etc.

---

### 3. `director.py` — Director

```python
from .builders.base import EmailBuilder

class EmailDirector:
    def __init__(self, builder: EmailBuilder):
        self.builder = builder

    def build_email(self, name: str, context: dict) -> dict:
        self.builder.add_subject()
        self.builder.add_greeting(name)
        self.builder.add_body(context)
        self.builder.add_footer()
        return self.builder.get_email()
```

---

### 4. `service.py` — Client Code

```python
from email_templates.builders.welcome_email_builder import WelcomeEmailBuilder
from email_templates.director import EmailDirector

def generate_welcome_email(user):
    builder = WelcomeEmailBuilder()
    director = EmailDirector(builder)
    context = {"dashboard_url": "https://app.example.com/dashboard"}
    email = director.build_email(user.first_name, context)

    # Return as formatted string or dict, depending on your mail backend
    full_email = f"""{email['greeting']}

{email['body']}

{email['footer']}"""

    subject = email['subject']
    return subject, full_email
```

---

## 📬 Output Example

```text
Subject: 🎉 Welcome to Our Platform!

Hi Alice,

Thanks for signing up. We're excited to have you on board!
To get started, visit: https://app.example.com/dashboard

Cheers,
The Team
```

---

## ✅ SOLID Principles

| Principle | How It's Applied |
|----------|------------------|
| **S**    | Each builder builds one kind of email only. |
| **O**    | You can add new email types without touching existing builders. |
| **L**    | Director works with any `EmailBuilder`. |
| **I**    | Interface is tailored for email generation only. |
| **D**    | `Director` depends on abstraction, not on specific builders. |

---

Would you like this extended into a **Django email-sending service** using `send_mail()` or integrated with an email provider like SendGrid or Mailgun?