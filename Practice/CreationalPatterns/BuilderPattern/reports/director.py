class ReportDirector:
    def __init__(self, builder: "ReportBuilder"):
        self.builder = builder

    def build_simple_report(self, title, data, footer):
        self.builder.add_title(title)
        self.builder.add_table(data)
        self.builder.add_footer(footer)
        return self.builder.get_report()