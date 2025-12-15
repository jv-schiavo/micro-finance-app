--
-- File generated with SQLiteStudio v3.2.1 on Sun Dec 14 17:01:43 2025
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: application
CREATE TABLE application (
    application_id    INTEGER  PRIMARY KEY AUTOINCREMENT,
    customer_id       INTEGER,
    product_id        INTEGER,
    applicationDate   DATETIME NOT NULL,
    income            REAL     NOT NULL,
    jobPosition       TEXT     NOT NULL,
    creditScore       INTEGER  NOT NULL,
    amountRequested   REAL     NOT NULL,
    loanPurpose       TEXT,
    status            TEXT     NOT NULL,
    statusUpdateTime  DATETIME DEFAULT CURRENT_TIMESTAMP,
    officerNotes      TEXT,
    loanTermRequested INT,
    FOREIGN KEY (
        customer_id
    )
    REFERENCES customer (customer_id) ON DELETE RESTRICT,
    FOREIGN KEY (
        product_id
    )
    REFERENCES product (product_id) ON DELETE RESTRICT
);

INSERT INTO application (
                            application_id,
                            customer_id,
                            product_id,
                            applicationDate,
                            income,
                            jobPosition,
                            creditScore,
                            amountRequested,
                            loanPurpose,
                            status,
                            statusUpdateTime,
                            officerNotes,
                            loanTermRequested
                        )
                        VALUES (
                            1,
                            1,
                            1,
                            '2024-04-13',
                            18000.0,
                            'Student',
                            620,
                            9200.0,
                            'Tuition Fees',
                            'Pending',
                            '2025-12-10 19:07:36',
                            'Very likely',
                            180
                        );

INSERT INTO application (
                            application_id,
                            customer_id,
                            product_id,
                            applicationDate,
                            income,
                            jobPosition,
                            creditScore,
                            amountRequested,
                            loanPurpose,
                            status,
                            statusUpdateTime,
                            officerNotes,
                            loanTermRequested
                        )
                        VALUES (
                            2,
                            2,
                            3,
                            '2025-09-09',
                            42000.0,
                            'Engineer',
                            750,
                            15000.0,
                            'Personal Expenses',
                            'Approved',
                            '2025-12-10 19:07:36',
                            'High Income, Stable',
                            84
                        );

INSERT INTO application (
                            application_id,
                            customer_id,
                            product_id,
                            applicationDate,
                            income,
                            jobPosition,
                            creditScore,
                            amountRequested,
                            loanPurpose,
                            status,
                            statusUpdateTime,
                            officerNotes,
                            loanTermRequested
                        )
                        VALUES (
                            3,
                            3,
                            2,
                            '2025-09-12',
                            35000.0,
                            'Accountant',
                            640,
                            36000.0,
                            'New Car',
                            'Rejected',
                            '2025-12-10 19:07:36',
                            'Insufficient affordability',
                            84
                        );

INSERT INTO application (
                            application_id,
                            customer_id,
                            product_id,
                            applicationDate,
                            income,
                            jobPosition,
                            creditScore,
                            amountRequested,
                            loanPurpose,
                            status,
                            statusUpdateTime,
                            officerNotes,
                            loanTermRequested
                        )
                        VALUES (
                            4,
                            4,
                            5,
                            '2025-10-27',
                            28000.0,
                            'Nurse',
                            600,
                            250000.0,
                            'Buy to Let Investment',
                            'Pending',
                            '2025-12-10 19:07:36',
                            'Borderline affordability',
                            348
                        );

INSERT INTO application (
                            application_id,
                            customer_id,
                            product_id,
                            applicationDate,
                            income,
                            jobPosition,
                            creditScore,
                            amountRequested,
                            loanPurpose,
                            status,
                            statusUpdateTime,
                            officerNotes,
                            loanTermRequested
                        )
                        VALUES (
                            5,
                            5,
                            4,
                            '2025-11-19',
                            52000.0,
                            'Director',
                            790,
                            150000.0,
                            'Property Purchase',
                            'Approved',
                            '2025-12-10 19:07:36',
                            'Strong candidate',
                            360
                        );

INSERT INTO application (
                            application_id,
                            customer_id,
                            product_id,
                            applicationDate,
                            income,
                            jobPosition,
                            creditScore,
                            amountRequested,
                            loanPurpose,
                            status,
                            statusUpdateTime,
                            officerNotes,
                            loanTermRequested
                        )
                        VALUES (
                            6,
                            1,
                            2,
                            '2025-12-13',
                            35000.0,
                            'Warehouse Operative',
                            620,
                            35000.0,
                            'Car purchase',
                            'Pending',
                            '2025-12-13 12:26:27',
                            'Test case: amount outside range',
                            24
                        );


-- Table: customer
CREATE TABLE customer (
    customer_id     INTEGER  PRIMARY KEY AUTOINCREMENT,
    name            TEXT     NOT NULL,
    DOB             DATETIME NOT NULL,
    address         TEXT     NOT NULL,
    phone           TEXT     NOT NULL,
    nationalID      TEXT     NOT NULL,
    nationalIDPhoto BLOB     NOT NULL
);

INSERT INTO customer (
                         customer_id,
                         name,
                         DOB,
                         address,
                         phone,
                         nationalID,
                         nationalIDPhoto
                     )
                     VALUES (
                         1,
                         'Joseph Blatter',
                         '1999-02-11',
                         '221 North Street, London',
                         '7342890865',
                         'NI102938A',
                         X'424C4F42'
                     );

INSERT INTO customer (
                         customer_id,
                         name,
                         DOB,
                         address,
                         phone,
                         nationalID,
                         nationalIDPhoto
                     )
                     VALUES (
                         2,
                         'Mary Jane',
                         '1991-07-23',
                         '12 Kensington Road, London',
                         '7712328901',
                         'NI556677B',
                         X'424C4F42'
                     );

INSERT INTO customer (
                         customer_id,
                         name,
                         DOB,
                         address,
                         phone,
                         nationalID,
                         nationalIDPhoto
                     )
                     VALUES (
                         3,
                         'Lionel De Jong',
                         '1995-06-12',
                         '88 Queens Avenue, Birmingham',
                         '7756829384',
                         'NI889900C',
                         X'424C4F42'
                     );

INSERT INTO customer (
                         customer_id,
                         name,
                         DOB,
                         address,
                         phone,
                         nationalID,
                         nationalIDPhoto
                     )
                     VALUES (
                         4,
                         'Gabriel Paul',
                         '2000-01-20',
                         '15 Riverbank Lane, Manchester',
                         '7756432189',
                         'NI778899D',
                         X'424C4F42'
                     );

INSERT INTO customer (
                         customer_id,
                         name,
                         DOB,
                         address,
                         phone,
                         nationalID,
                         nationalIDPhoto
                     )
                     VALUES (
                         5,
                         'Frederich Heinz',
                         '1967-10-14',
                         '12 Chamberlayne Road, Liverpool',
                         'No Phone',
                         'NI667788E',
                         X'424C4F42'
                     );


-- Table: loan
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

INSERT INTO loan (
                     loan_id,
                     application_id,
                     disbursementDate,
                     principalAmount,
                     interestRateApplied,
                     feesApplied,
                     loanTermApplied,
                     outstandingBalance,
                     loanStatus
                 )
                 VALUES (
                     1,
                     2,
                     '2025-12-13',
                     15000.0,
                     15.0,
                     180.0,
                     84,
                     15000.0,
                     'Active'
                 );

INSERT INTO loan (
                     loan_id,
                     application_id,
                     disbursementDate,
                     principalAmount,
                     interestRateApplied,
                     feesApplied,
                     loanTermApplied,
                     outstandingBalance,
                     loanStatus
                 )
                 VALUES (
                     2,
                     5,
                     '2025-12-13',
                     150000.0,
                     9.0,
                     500.0,
                     360,
                     150000.0,
                     'Active'
                 );


-- Table: product
CREATE TABLE product (
    product_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name      TEXT    NOT NULL,
    interestRate      REAL    NOT NULL,
    minAmount         REAL    NOT NULL,
    maxAmount         REAL    NOT NULL,
    loanTermRange     TEXT    NOT NULL,
    fees              REAL    NOT NULL,
    minLoanTermMonths INT,
    maxLoanTermMonths INT
);

INSERT INTO product (
                        product_id,
                        product_name,
                        interestRate,
                        minAmount,
                        maxAmount,
                        loanTermRange,
                        fees,
                        minLoanTermMonths,
                        maxLoanTermMonths
                    )
                    VALUES (
                        1,
                        'Student Loan',
                        9.0,
                        1000.0,
                        20000.0,
                        '10 to 30 years',
                        150.0,
                        120,
                        160
                    );

INSERT INTO product (
                        product_id,
                        product_name,
                        interestRate,
                        minAmount,
                        maxAmount,
                        loanTermRange,
                        fees,
                        minLoanTermMonths,
                        maxLoanTermMonths
                    )
                    VALUES (
                        2,
                        'Car Loan',
                        16.0,
                        3000.0,
                        25000.0,
                        '3 to 7 years',
                        250.0,
                        36,
                        84
                    );

INSERT INTO product (
                        product_id,
                        product_name,
                        interestRate,
                        minAmount,
                        maxAmount,
                        loanTermRange,
                        fees,
                        minLoanTermMonths,
                        maxLoanTermMonths
                    )
                    VALUES (
                        3,
                        'Personal Loan',
                        15.0,
                        1000.0,
                        50000.0,
                        '1 to 7 years',
                        180.0,
                        12,
                        84
                    );

INSERT INTO product (
                        product_id,
                        product_name,
                        interestRate,
                        minAmount,
                        maxAmount,
                        loanTermRange,
                        fees,
                        minLoanTermMonths,
                        maxLoanTermMonths
                    )
                    VALUES (
                        4,
                        'Mortgage Loan',
                        9.0,
                        50000.0,
                        500000.0,
                        '15 to 30 years',
                        500.0,
                        180,
                        360
                    );

INSERT INTO product (
                        product_id,
                        product_name,
                        interestRate,
                        minAmount,
                        maxAmount,
                        loanTermRange,
                        fees,
                        minLoanTermMonths,
                        maxLoanTermMonths
                    )
                    VALUES (
                        5,
                        'Business Loan',
                        11.0,
                        5000.0,
                        150000.0,
                        '1 to 7 years',
                        350.0,
                        12,
                        84
                    );


-- Table: repayment
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
);


-- Table: users
CREATE TABLE users (
    user_id       INTEGER  PRIMARY KEY AUTOINCREMENT,
    username      TEXT     NOT NULL
                           UNIQUE,
    password_hash TEXT     NOT NULL,
    created_at    DATETIME NOT NULL
);


-- Index: idx_loan_application_unique
CREATE UNIQUE INDEX idx_loan_application_unique ON loan (
    application_id
);


-- Trigger: check_requests
CREATE TRIGGER check_requests
        BEFORE UPDATE OF status
            ON application
      FOR EACH ROW
          WHEN NEW.status = 'Approved'
BEGIN
    SELECT RAISE(ABORT, "Approval denied, requests are outside scope of product") 
     WHERE EXISTS (
               SELECT 1
                 FROM product p
                WHERE p.product_id = NEW.product_id AND 
                      (NEW.amountRequested < p.minAmount OR 
                       NEW.amountRequested > p.maxAmount OR 
                       NEW.loanTermRequested < p.minLoanTermMonths OR 
                       NEW.loanTermRequested > p.maxLoanTermMonths) 
           );
END;


-- Trigger: creates_loan
CREATE TRIGGER creates_loan
         AFTER UPDATE OF status
            ON application
      FOR EACH ROW
          WHEN NEW.status = 'Approved'
BEGIN
    INSERT INTO loan (
                         application_id,
                         disbursementDate,
                         principalAmount,
                         interestRateApplied,
                         feesApplied,
                         loanTermApplied,
                         outstandingBalance,
                         loanStatus
                     )
                     SELECT NEW.application_id,
                            CURRENT_DATE,
                            NEW.amountRequested,
                            p.interestRate,
                            p.fees,
                            NEW.loanTermRequested,
                            NEW.amountRequested,
                            'Active'
                       FROM product p
                      WHERE p.product_id = NEW.product_id;
END;


-- View: dashboard_view
CREATE VIEW dashboard_view AS
    SELECT p.product_name,
           COUNT(l.loan_id) AS total_loans,
           ROUND(SUM(l.principalAmount), 2) AS total_amount_issued,
           ROUND(AVG(l.principalAmount), 2) AS avg_loan_amount
      FROM product p
           JOIN
           application a ON p.product_id = a.product_id
           JOIN
           loan l ON l.application_id = a.application_id
     WHERE loanStatus = 'Active'
     GROUP BY p.product_name;


-- View: loan_report_view
CREATE VIEW loan_report_view AS
    SELECT l.loan_id,
           l.application_id,
           c.name,
           c.phone,
           p.product_name,
           a.applicationDate,
           a.statusUpdateTime AS approval_date,
           l.principalAmount,
           UPPER(l.loanStatus) 
      FROM loan l
           JOIN
           application a ON l.application_id = a.application_id
           JOIN
           product p ON p.product_id = a.product_id
           JOIN
           customer c ON c.customer_id = a.customer_id;


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
