class CustomerService:
    def __init__(self, db):
        self.db = db

    def get_all_customers(self):
        query = """
        SELECT customer_id, name, DOB, address, phone, nationalID, nationalIDPhoto
        FROM customer;
        """

        return self.db.fetchall(query)
    
    def create_customer(self, name, DOB, address, phone, nationalID, nationalIDPhoto):
        if not name and DOB and address and phone and nationalID and nationalIDPhoto:
            raise ValueError("All fields required")
        
        query = """
        INSERT INTO customer (name, DOB, address, phone, nationalID, nationalIDPhoto)
        VALUES (?,?,?,?,?,?)
        """

        self.db.execute(query,(name, DOB, address, phone, nationalID, nationalIDPhoto))

    def update_customer(self, customer_id, name, address, phone):
        query = """
        UPDATE customer
        SET name = ?, address = ?, phone = ?
        WHERE customer_id = ? 
        """

        self.db.execute(query, (name, address, phone, customer_id))

    def delete_customer(self, customer_id):
        query = """
        DELETE FROM customer WHERE customer_id = ?
        """

        self.db.execute(query, customer_id)

