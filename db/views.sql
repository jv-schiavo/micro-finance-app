-- Create VIEW for reporting and auditing to each loan 

CREATE VIEW loan_report_view AS
SELECT 
    l.loan_id,
    l.application_id,
    c.name,
    c.phone,
    p.product_name,
    a.applicationDate,
    a.statusUpdateTime AS approval_date,
    l.principalAmount,
    UPPER(l.loanStatus)
FROM loan l
JOIN application a ON l.application_id = a.application_id
JOIN product p ON p.product_id = a.product_id
JOIN customer c ON c.customer_id = a.customer_id;

-- CREATE VIEW for a dashboard 

CREATE VIEW dashboard_view AS
SELECT 
    p.product_name,
    COUNT(l.loan_id) AS total_loans,
    ROUND(SUM(l.principalAmount), 2) AS total_amount_issued,
    ROUND(AVG(l.principalAmount), 2) AS avg_loan_amount
FROM product p
JOIN application a ON p.product_id = a.product_id
JOIN loan l ON l.application_id = a.application_id
WHERE loanStatus = 'Active'
GROUP BY p.product_name;