# Micro-Finance Loan Management System

A full-stack loan management desktop app built in Python. It handles everything a small lending operation needs — customer records, loan products, applications, repayments, and reporting — with a normalised SQLite database underneath and a Tkinter GUI on top.

---

## What it does

- Register and manage customers, including identity image storage
- Define loan products with configurable rules and approval criteria
- Process loan applications through an approval workflow, with triggers that enforce business logic automatically
- Track repayments and compute outstanding balances via database views (no redundant stored values)
- Generate operational reports from an in-app dashboard
- Export customer and loan data as XML for audit or compliance use

---

## Stack

| | |
|---|---|
| Language | Python 3 |
| Database | SQLite 3 |
| GUI | Tkinter |
| Data export | XML |

---

## Highlights

**Layered architecture** — the codebase is split into `db/`, `services/`, and `ui/` layers, keeping database logic, business rules, and presentation cleanly separated.

**Schema design** — five core tables (`Customer`, `LoanProduct`, `LoanApplication`, `Loan`, `Repayment`) normalised to 3NF. Referential integrity enforced with foreign keys and UNIQUE constraints throughout.

**Database-level automation** — two SQL triggers handle loan approval validation and automatic loan record creation on approval, keeping business rules at the data layer rather than scattered through application code.

**Security basics** — parameterised queries across all database interactions, with basic encryption on sensitive fields.

---

## Project Structure

```
micro-finance-app/
│
├── db/
│   ├── connection.py           # SQLite connection and config
│   ├── schema.sql              # Tables and constraints
│   ├── triggers.sql            # Business rule triggers
│   └── views.sql               # Reporting views
│
├── services/
│   ├── application_service.py  # Loan application lifecycle
│   ├── auth_service.py         # Auth and access control
│   ├── customer_service.py     # Customer CRUD
│   ├── loan_service.py         # Loan creation and management
│   ├── product_service.py      # Loan product configuration
│   ├── repayment_service.py    # Repayment processing
│   └── report_service.py       # Reporting queries
│
├── ui/
│   ├── login_view.py           # Login screen
│   ├── main_menu_view.py       # Navigation
│   ├── customer_view.py        # Customer management
│   ├── product_view.py         # Loan products
│   ├── application_view.py     # Loan applications
│   ├── loan_view.py            # Loan overview
│   ├── repayment_view.py       # Repayment entry
│   └── report_view.py          # Dashboard
│
├── microfinance.db             # SQLite database
└── app.py                      # Entry point
```

---

## Getting Started

**Prerequisites:** Python 3

```bash
git clone https://github.com/jv-schiavo/micro-finance-app.git
cd micro-finance-app
python app.py
```

The GUI will launch and connect to `microfinance.db` automatically. To inspect or reset the schema, see `db/schema.sql`.
