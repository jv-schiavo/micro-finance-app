from datetime import date

class RepaymentService:
    def __init__(self, db):
        self.db = db

    def get_all_repayments(self, loan_id):
        query = """
        SELECT repayment_id, loan_id, repayment_date, repayment_amount, payment_method, source, external_reference, notes, created_at
        FROM repayment
        WHERE loan_id = ?
        ORDER BY repayment_date; 
        """
        return self.db.fetchall(query, (loan_id,))
    
    def create_repayment(self, loan_id, repayment_date, repayment_amount, payment_method, source, external_reference, notes):
        
        now = date.today().isoformat()
        
        query = """
        INSERT INTO repayment (loan_id, repayment_date, repayment_amount, payment_method, source, external_reference, notes, created_at)
        VALUES (?,?,?,?,?,?,?,?)
        """
        repayment_id = self.db.execute_and_return_id(query, (loan_id, repayment_date, repayment_amount, payment_method, source, external_reference, notes, now))
        return repayment_id