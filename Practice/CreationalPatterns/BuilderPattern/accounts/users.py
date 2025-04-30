class User:
    """
    A class representing a user in the system.
    Attributes:
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        email (str): The email address of the user.
        password (str): The password of the user.
    """

    def __init__(self, first_name: str, last_name: str, email: str, password: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_active = True
        self.is_verified = False
        self.is_admin = False
        self.is_superuser = False
        self.is_staff = False
        self.is_authenticated = False
        self.is_anonymous = False

    def __str__(self):
        return f"User({self.first_name}, {self.last_name}, {self.email})"
    def __repr__(self):
        return f"User({self.first_name}, {self.last_name}, {self.email})"
    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return (self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.email == other.email and
                self.password == other.password)
    def __hash__(self):
        return hash((self.first_name, self.last_name, self.email, self.password))
    def __len__(self):
        return len(self.first_name) + len(self.last_name) + len(self.email) + len(self.password)