CREATE TABLE customer (
    customer_id     INTEGER  PRIMARY KEY AUTOINCREMENT,
    name            TEXT     NOT NULL,
    DOB             DATETIME NOT NULL,
    address         TEXT     NOT NULL,
    phone           TEXT     NOT NULL,
    nationalID      TEXT     NOT NULL,
    nationalIDPhoto BLOB     NOT NULL
);

CREATE TABLE product (
    product_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name  TEXT    NOT NULL,
    interestRate  REAL    NOT NULL,
    minAmount     REAL    NOT NULL,
    maxAmount     REAL    NOT NULL,
    loanTermRange TEXT    NOT NULL,
    fees          REAL    NOT NULL
);

CREATE TABLE application (
    application_id   INTEGER  PRIMARY KEY AUTOINCREMENT,
    customer_id      INTEGER,
    product_id       INTEGER,
    applicationDate  DATETIME NOT NULL,
    income           REAL     NOT NULL,
    jobPosition      TEXT     NOT NULL,
    creditScore      INTEGER  NOT NULL,
    amountRequested  REAL     NOT NULL,
    loanPurpose      TEXT,
    status           TEXT     NOT NULL,
    statusUpdateTime DATETIME DEFAULT CURRENT_TIMESTAMP,
    officerNotes     TEXT,
    FOREIGN KEY (
        customer_id
    )
    REFERENCES customer (customer_id) ON DELETE RESTRICT,
    FOREIGN KEY (
        product_id
    )
    REFERENCES product (product_id) ON DELETE RESTRICT
);

CREATE TABLE loan (
    loan_id             INTEGER  PRIMARY KEY AUTOINCREMENT,
    application_id      INTEGER,
    disbursementDate    DATETIME NOT NULL,
    principalAmount     REAL     NOT NULL,
    interestRateApplied REAL     NOT NULL,
    feesApplied         REAL     NOT NULL,
    loanTermApplied     INTEGER  NOT NULL,
    outstandingBalance  REAL     NOT NULL,
    loanStatus          TEXT     DEFAULT Active
                                 NOT NULL,
    FOREIGN KEY (
        application_id
    )
    REFERENCES application (application_id) ON DELETE RESTRICT
);

CREATE TABLE repayment (
    repayment_id    INTEGER  PRIMARY KEY AUTOINCREMENT,
    loan_id         INTEGER,
    repaymentAmount REAL     NOT NULL,
    repaymentDate   DATETIME NOT NULL,
    paymentMethod   TEXT     NOT NULL,
    reference       TEXT,
    notes           TEXT,
    FOREIGN KEY (
        loan_id
    )
    REFERENCES loan (loan_id) ON DELETE RESTRICT
);-- Use of ON DELETE RESTRICT to avoid deletion in cascade

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at DATETIME NOT NULL
)


INSERT INTO customer (name, DOB, address, phone, nationalID, nationalIDPhoto)
VALUES
('Joseph Blatter', '1999-02-11', '221 North Street, London', '7342890865', 'NI102938A', X'424C4F42'),
('Mary Jane', '1991-07-23', '12 Kensington Road, London', '7712328901', 'NI556677B', X'424C4F42'),
('Lionel De Jong', '1995-06-12', '88 Queens Avenue, Birmingham', '7756829384', 'NI889900C', X'424C4F42'),
('Gabriel Paul', '2000-01-20', '15 Riverbank Lane, Manchester', '7756432189', 'NI778899D', X'424C4F42'),
('Frederich Heinz', '1967-10-14', '12 Chamberlayne Road, Liverpool', 'No Phone', 'NI667788E', X'424C4F42');

INSERT INTO product (product_name, interestRate, minAmount, maxAmount, loanTermRange, fees)
VALUES
('Student Loan', 9.0, 1000, 20000, '10 to 30 years', 150),
('Car Loan', 16.0, 3000, 25000, '3 to 7 years', 250),
('Personal Loan', 15.0, 1000, 50000, '1 to 7 years', 180),
('Mortgage Loan', 9.0, 50000, 500000, '15 to 30 years', 500),
('Business Loan', 11.0, 5000, 150000, '1 to 7 years', 350);

INSERT INTO application 
(customer_id, product_id, applicationDate, income, jobPosition, creditScore, amountRequested, loanPurpose, status, officerNotes)
VALUES
(1, 1, '2024-04-13', 18000, 'Student', 620, 9200, 'Tuition Fees', 'Pending', 'Very likely'),
(2, 3, '2025-09-09', 42000, 'Engineer', 750, 15000, 'Personal Expenses', 'Approved', 'High Income, Stable'),
(3, 2, '2025-09-12', 35000, 'Accountant', 640, 36000, 'New Car', 'Rejected', 'Insufficient affordability'),
(4, 5, '2025-10-27', 28000, 'Nurse', 600, 250000, 'Buy to Let Investment', 'Pending', 'Borderline affordability'),
(5, 4, '2025-11-19', 52000, 'Director', 790, 150000, 'Property Purchase', 'Approved', 'Strong candidate');

