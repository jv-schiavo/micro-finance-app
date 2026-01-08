class ApplicationService:
    def __init__(self, db):
        self.db = db

    def get_all_applications(self):
        query = """
        SELECT a.application_id, c.name, p.product_name, a.applicationDate, a.income, a.jobPosition, a.creditScore,
        a.amountRequested, a.loanPurpose, a.status, a.officerNotes, a.loanTermRequested
        FROM application a
        JOIN customer c ON a.customer_id = c.customer_id
        JOIN product p ON a.product_id = p.product_id;
        """
        return self.db.fetchall(query)