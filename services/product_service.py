class ProductService:
    def __init__(self, db):
        self.db = db

    def get_all_products(self):
        query = """
        SELECT product_id, product_name, interestRate, minAmount, maxAmount, loanTermRange, fees, minLoanTermMonths, maxLoanTermMonths
        FROM product;
        """
        return self.db.fetchall(query)
    
    def create_product(self, name, interestRate, minAmount, maxAmount, loanTermRange, fees, minLoanTermMonths, maxLoanTermMonths):
        if not name and interestRate and minAmount and maxAmount and loanTermRange and fees and minLoanTermMonths and maxLoanTermMonths:
            raise ValueError("All fields required")
        query = """
        INSERT INTO product (product_name, interestRate, minAmount, maxAmount, loanTermRange, fees, minLoanTermMonths, maxLoanTermMonths)
        VALUES (?,?,?,?,?,?,?,?)
        """
        self.db.execute(query, (name, interestRate, minAmount, maxAmount, loanTermRange, fees, minLoanTermMonths, maxLoanTermMonths))

    def update_product(self, product_id, name, interestRate, minAmount, maxAmount, loanTermRange, fees, minLoanTermMonths, maxLoanTermMonths):
        query = """
        UPDATE product
        SET product_name = ?, interestRate = ?, minAmount = ?, maxAmount = ?, loanTermRange = ?, fees = ?, minLoanTermMonths = ?, maxLoanTermMonths = ?
        WHERE product_id = ?
        """
        self.db.execute(query, (name, interestRate, minAmount, maxAmount, loanTermRange, fees, minLoanTermMonths, maxLoanTermMonths, product_id))

    def delete_product(self, product_id):
        query = """
        DELETE FROM product WHERE product_id = ?
        """
        self.db.execute(query, product_id)