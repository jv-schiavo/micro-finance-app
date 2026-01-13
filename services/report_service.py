class ReportService:
    def __init__(self, db):
        self.db = db

    def get_loan_report(self):
        query = """
        SELECT *
        FROM loan_report_view;
        """
        return self.db.fetchall(query)
    
    def get_dashboard_data(self):
        query = """
        SELECT *
        FROM dashboard_view
        """
        return self.db.fetchall(query)