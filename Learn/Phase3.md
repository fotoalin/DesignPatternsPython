Great! Phase 3 is all about **using design patterns in real Django/Python projects**. The goal is to **internalize** the patterns by applying them in realistic use cases.

---

### 🛠️ Phase 3: Use Patterns in Real Code (4+ weeks)

#### ✅ Strategy
- Take common problems in Django apps.
- Apply one or more patterns to solve them cleanly.
- Build reusable, real-world code snippets or mini-projects.

---

### ✅ Examples with Code

Here are **three practical examples** using popular design patterns in Django:

---

#### 1. **Factory + Strategy Pattern**: Payment System with Multiple Providers

**Use Case:** Choose between PayPal, Stripe, or a local provider dynamically.

```python
# payments/strategies.py
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class StripePayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} via Stripe")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} via PayPal")
```

```python
# payments/factory.py
from .strategies import StripePayment, PayPalPayment

def get_payment_method(method: str):
    if method == "stripe":
        return StripePayment()
    elif method == "paypal":
        return PayPalPayment()
    else:
        raise ValueError("Unknown payment method")
```

```python
# views.py
from payments.factory import get_payment_method

def process_payment(request):
    method = request.GET.get("method")  # "stripe" or "paypal"
    payment = get_payment_method(method)
    payment.pay(100.00)
```

---

#### 2. **Observer Pattern**: Real-Time Notifications

**Use Case:** Send a WebSocket update when a user posts a comment.

```python
# signals.py
from django.dispatch import Signal

comment_posted = Signal()
```

```python
# observers.py
from .signals import comment_posted

def send_websocket_notification(sender, **kwargs):
    comment = kwargs["comment"]
    print(f"New comment: {comment.text}")
    # Send via HTMX WebSocket or Django Channels here

comment_posted.connect(send_websocket_notification)
```

```python
# views.py
from .signals import comment_posted
from .models import Comment

def post_comment(request):
    comment = Comment.objects.create(text="Nice!", user=request.user)
    comment_posted.send(sender=None, comment=comment)
```

---

#### 3. **Decorator Pattern**: Custom Middleware for Request Logging

**Use Case:** Wrap a view function to log user request info.

```python
# middleware/log_decorator.py
from functools import wraps

def log_request(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        print(f"User: {request.user} - Path: {request.path}")
        return view_func(request, *args, **kwargs)
    return _wrapped_view
```

```python
# views.py
from middleware.log_decorator import log_request

@log_request
def dashboard(request):
    return HttpResponse("Welcome to the dashboard.")
```

---

### 💡 Next Steps

Here’s how to go deeper from here:

1. **Pick a pattern** each week and:
   - Use it in a project
   - Write a blog post or video demo explaining it
2. Gradually **refactor old code** to include patterns where they simplify things.
3. Try to **combine patterns** (e.g., Observer + Command for job queues).

Would you like a checklist or tracker to guide your weekly practice in Phase 3?