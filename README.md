# Micro-Finance Loan Management System

## Project Overview

This project is a proof-of-concept **Micro-Finance Loan Management System** developed as part of the *Advanced Database Systems (QHO541)* module. The system demonstrates the design, implementation, and testing of a relational database solution aligned with real-world lending operations, supported by a Python Tkinter graphical user interface and XML data handling.

The solution replaces a legacy flat-file approach with a **normalised SQLite database (3NF)** that enforces business rules at database level and supports operational workflows such as customer registration, loan applications, loan issuance, repayments, reporting, and regulatory data export.

---

## Business Context

The system is designed for a small-to-medium micro-finance organisation that issues personal loans. The primary objectives are:

* Maintain accurate and traceable customer records
* Standardise loan products and approval rules
* Track loan lifecycles from application to repayment
* Support operational reporting and auditing
* Enable structured XML exports for regulatory compliance

The database design and application features are driven by seven defined business requirements, documented in the accompanying report.

---

## Technologies Used

* **Database:** SQLite 3
* **Programming Language:** Python 3
* **GUI Framework:** Tkinter
* **Data Exchange Format:** XML
* **Development Environment:** Any Python-compatible IDE (e.g. VS Code, PyCharm)

---

## Project Structure

```
MICRO_FINANCE_APP
│
├── db/
│   ├── connection.py        # SQLite connection and configuration
│   ├── schema.sql           # Database tables and constraints
│   ├── triggers.sql         # Business rule enforcement triggers
│   └── views.sql            # Reporting and aggregation views
│
├── services/
│   ├── application_service.py  # Loan application lifecycle logic
│   ├── auth_service.py         # Authentication and access control
│   ├── customer_service.py     # Customer CRUD operations
│   ├── loan_service.py         # Loan creation and management logic
│   ├── product_service.py      # Loan product governance
│   ├── repayment_service.py    # Repayment processing and balance logic
│   └── report_service.py       # Reporting and dashboard queries
│
├── ui/
│   ├── application_view.py     # Loan application GUI
│   ├── customer_view.py        # Customer management GUI
│   ├── loan_view.py            # Loan overview and details GUI
│   ├── login_view.py           # Login and authentication screen
│   ├── main_menu_view.py       # Main navigation menu
│   ├── product_view.py         # Loan product management GUI
│   ├── repayment_view.py       # Repayment entry and review GUI
│   └── report_view.py          # Reporting and dashboard GUI
│
├── microfinance.db          # SQLite database file
├── app.py                   # Application entry point
├── .gitignore
└── README.md

---

## Database Design Summary

- Fully normalised relational schema compliant with **Third Normal Form (3NF)**
- Minimum of five substantial tables, including:
  - Customer
  - LoanProduct
  - LoanApplication
  - Loan
  - Repayment
- Referential integrity enforced using primary keys, foreign keys, and UNIQUE constraints
- Derived financial values (e.g. outstanding balance) calculated via **views**, not stored redundantly

---

## Key Database Features

### Triggers

- **Loan Approval Validation Trigger**: Ensures loan applications meet product rules before approval
- **Loan Creation Trigger**: Automatically creates a loan record when an application is approved, preventing duplicates

### Views

- Operational reporting views for active loans, customer summaries, and portfolio oversight
- Aggregated data using SQLite functions such as `COUNT`, `SUM`, `AVG`, and `ROUND`

### Functions

- Reusable SQL functions embedded within views to support consistent reporting and analysis

---

## Application Features (Python Tkinter GUI)

- Create, update, delete, and view records via a graphical interface
- Structured input forms with validation to prevent invalid data entry
- Secure communication with SQLite using parameterised queries
- Report generation via database views

---

## Validation and Security

- Input validation implemented at application level
- Parameterised SQL queries used to mitigate SQL injection risks
- Basic encryption and decryption applied to sensitive data fields

---

## Image Storage

- Customer identity images are stored in the database using the **BLOB (Binary Large Object)** data type
- Images are retrieved and displayed via the application where required

---

## XML Functionality

- Customer and loan data can be exported in **XML format** for regulatory and audit purposes
- XML elements are derived from relational fields
- XML data can be read, queried, and modified within the application

---

## How to Run the Application

1. Ensure **Python 3** is installed on your system
2. Clone or extract the project ZIP file
3. Navigate to the project root directory
4. (Optional) Review or initialise the database using `schema.sql`
5. Run the application:

```bash
python app/main.py
````

6. The Tkinter GUI will launch, allowing interaction with the database

---

## Testing

The system was tested using:

* Manual test cases for insert, update, and delete operations
* Trigger validation tests for loan approval and creation
* Referential integrity tests to confirm constraint enforcement
* GUI interaction testing for data validation and error handling
* XML export verification

---

## Known Limitations

* SQLite mathematical function support is limited; complex interest calculations are handled at application level
* The system is a proof-of-concept and not intended for production deployment without further hardening

---

## Author Note

This project was developed as an academic submission to demonstrate database design, implementation, and integration skills in line with the Advanced Database Systems (QHO541) module requirements.
