from abc import ABC, abstractmethod

class ReportBuilder(ABC):
    @abstractmethod
    def add_title(self, title: str): pass

    @abstractmethod
    def add_table(self, data: list): pass

    @abstractmethod
    def add_footer(self, footer: str): pass

    @abstractmethod
    def get_report(self): pass