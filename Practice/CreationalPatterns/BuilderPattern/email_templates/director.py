from builders.base import EmailBuilder

class EmailDirector:
    def __init__(self, builder: EmailBuilder):
        self.builder = builder

    def build_email(self, name: str, context: dict) -> dict:
        self.builder.add_subject()
        self.builder.add_greeting(name)
        self.builder.add_body(context)
        self.builder.add_footer()
        return self.builder.get_email()
