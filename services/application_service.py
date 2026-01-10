from datetime import date

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
    
    def create_application(self, customer_id, product_id, income, jobPosition, creditScore, amountRequested, loanPurpose,
                            officerNotes, loanTermRequested):
        now = date.today().isoformat()

        query = """
        INSERT INTO application (customer_id, product_id, applicationDate, income, jobPosition, creditScore, amountRequested, loanPurpose,
                           status, statusUpdateTime, officerNotes, loanTermRequested)
        VALUES (?,?,?, ?,?,?,?,?,?,?, ?, ?)
        """
        self.db.execute(query, (customer_id, product_id, now, income, jobPosition, creditScore, amountRequested, loanPurpose,
                           "Pending", now, officerNotes, loanTermRequested))
        
    def update_application(self, application_id, status):
        now = date.today().isoformat()
        query = """
        UPDATE application
        SET status = ?, statusUpdateTime = ?
        WHERE application_id = ?
        """

        self.db.execute(query, (status, now, application_id))

    def delete_application(self, application_id):
        query = """
        DELETE FROM application
        WHERE application_id = ?
        """

        self.db.execute(query, (application_id,))