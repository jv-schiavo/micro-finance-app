from datetime import date

class LoanService:
    def __init__(self, db):
        self.db = db
        
    def create_loan_from_application(self, application_id):

        existing = self.db.fetchone(
            "SELECT loan_id FROM loan WHERE application_id = ?",
            (application_id,)
        )

        if existing:
            return existing["loan_id"]
        
        row = self.db.fetchall("""
            SELECT
                a.application_id,
                a.amountRequested AS principal,
                p.interestRate AS rate,
                p.fees AS fees
            FROM application a
            JOIN product p ON p.product_id = a.product_id
            WHERE a.application_id = ?
        """, (application_id,))[0]

        principal = float(row["principal"])
        rate = float(row["rate"])
        fees = float(row["fees"])

        interest_amount = principal * (rate / 100)
        total_payable = principal + interest_amount + fees

        today = date.today().isoformat()

        self.db.execute("""
            INSERT INTO loan (
                application_id,
                disbursementDate,
                principalAmount,
                interestRateApplied,
                feesApplied,
                total_payable,
                outstandingBalance,
                loanStatus,
                total_payable
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            application_id,
            today,
            principal,
            rate,
            fees,
            row["loanTermRequested"],
            total_payable,       
            "Active",
            total_payable
        ))

    def get_all_loans(self):
        query = """
        SELECT
            l.loan_id,
            c.name,
            l.disbursementDate,
            l.outstandingBalance,
            l.total_payable
        FROM loan l
        JOIN application a ON l.application_id = a.application_id
        JOIN customer c ON a.customer_id = c.customer_id;
        """
        return self.db.fetchall(query)