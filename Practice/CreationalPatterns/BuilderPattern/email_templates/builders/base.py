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
