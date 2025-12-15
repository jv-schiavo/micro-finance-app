-- CREATE TRIGGER TO VALIDATE APPROVAL BASED ON LOAN TERM & AMOUNT REQUESTED
-- BEFORE UPDATE OF STATUS ON APPLICATION
-- CHECK IF: LOAN TERM REQUEST IS INSIDE OF PRODUCT RANGE ALLOWED 
-- AND
-- CHECK IF: AMOUNT REQUEST IS INSIDE OF PRODUCT RANGE ALLOWED
-- IF NOT: BLOCK APPROVAL "Approval denied: requests are outside scope of this product"
-- IF YES: ALLOW TO UPDATE

CREATE TRIGGER check_requests 
BEFORE UPDATE OF status ON application
FOR EACH ROW
WHEN NEW.status = 'Approved'
BEGIN
    SELECT RAISE(ABORT, 'Approval denied, requests are outside scope of product')
    WHERE EXISTS (
        SELECT 1
        FROM product p
        WHERE p.product_id = NEW.product_id
        AND ( NEW.amountRequested < p.minAmount
                 OR NEW.amountRequested > p.maxAmount
                 OR NEW.loanTermRequested < p.minLoanTermMonths
                 OR NEW.loanTermRequested > p.maxLoanTermMonths
         )
    );      
END;


-- CREATE TRIGGER TO CREATE RECORDS ON LOAN TABLE IF STATUS = "Approved"
-- AFTER UPDATE OF STATUS ON APPLICATION
-- IF LOAN EXIST ABORT INSERTION
-- ELSE:
-- INSERT INTO LOAN
-- VALUES ( application_id([application]), disbursementDate = CURRENT_DATE, principalAmount = amountRequested([application]),
-- interestRateApplied(interesRate[product]), feesApplied(fees[product]), loanTermApplied(loanTermRequested([application]),
-- outstadingBalance(amountRequested[application]),loanStatus = 'Active' 
--)

SELECT *
FROM loan;

CREATE TRIGGER creates_loan
AFTER UPDATE OF status ON application
FOR EACH ROW
WHEN NEW.status = 'Approved'
BEGIN
    INSERT INTO loan ( application_id, disbursementDate, principalAmount, interestRateApplied, feesApplied,
    loanTermApplied, outstandingBalance, loanStatus ) 
    SELECT
        NEW.application_id,
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