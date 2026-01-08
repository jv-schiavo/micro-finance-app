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
    
    def create_application(self, customer_id, application_id, applicationDate, income, jobPosition, creditScore, amountRequested, loanPurpose,
                           status, statusUpdateTime, officerNotes, loantermRequested):
        ## Application MUST be created with only existing customers AND products
        query = """
        INSERT INTO application (customer_id, application_id, applicationDate, income, jobPosition, creditScore, amountRequested, loanPurpose,
                           status, statusUpdateTime, officerNotes, loantermRequested)
        VALUES (?,?, DATE('now'), ?,?,?,?,?,'Pending', DATE('now'), ?, ?)
        """
        self.db.execute(query, (customer_id, application_id, applicationDate, income, jobPosition, creditScore, amountRequested, loanPurpose,
                           status, statusUpdateTime, officerNotes, loantermRequested))
        
    def update_application(self, application_id, status, statusUpdateTime):
        query = """
        UPDATE application
        SET status = ?, statusUpdateTime = DATE('now')
        WHERE application_id = ?
        """

        self.db.execute(query, (status, statusUpdateTime, application_id))

    def delete_application(self, application_id):
        query = """
        DELETE FROM application
        WHERE application_id = ?
        """

        self.db.execute(query, application_id)