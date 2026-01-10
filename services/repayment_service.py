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
    
    def generate_repayment_xml(self, repayment_id):
        row = self.db.fetchone("""
            SELECT repayment_id, loan_id, repayment_date, repayment_amount, payment_method, external_reference
            FROM repayment r
            WHERE r.repayment_id = ?
        """, (repayment_id,))

        if not row:
            return None

        return f"""<?xml version="1.0" encoding="UTF-8"?>
    <repaymentReceipt>
        <repaymentId>{row["repayment_id"]}</repaymentId>
        <loanId>{row["loan_id"]}</loanId>
        <date>{row["repayment_date"]}</date>
        <amount>{row["repayment_amount"]}</amount>
        <method>{row["payment_method"]}</method>
        <reference>{row["external_reference"]}</reference>
    </repaymentReceipt>
    """
