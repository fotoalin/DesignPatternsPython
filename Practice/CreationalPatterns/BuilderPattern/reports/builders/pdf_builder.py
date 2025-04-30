class PDFReportBuilder(ReportBuilder):
    def __init__(self):
        self.report = []

    def add_title(self, title: str):
        self.report.append(f"[PDF] Title: {title}")

    def add_table(self, data: list):
        self.report.append(f"[PDF] Table: {data}")

    def add_footer(self, footer: str):
        self.report.append(f"[PDF] Footer: {footer}")

    def get_report(self):
        return "\n".join(self.report)