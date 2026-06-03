-- 1 Top 5 Funds by AUM
SELECT fund_name,
SUM(aum) total_aum
FROM fact_aum
GROUP BY fund_name
ORDER BY total_aum DESC
LIMIT 5;

-- 2 Average NAV Per Month
SELECT strftime('%Y-%m',date) month,
AVG(nav)
FROM fact_nav
GROUP BY month;

-- 3 SIP YoY Growth
SELECT year,
SUM(amount)
FROM fact_transactions
WHERE transaction_type='SIP'
GROUP BY year;

-- 4 Transactions by State
SELECT state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

-- 5 Expense Ratio Below 1%
SELECT *
FROM fact_performance
WHERE expense_ratio < 1;

-- 6 Highest NAV Funds
SELECT fund_name,
MAX(nav)
FROM fact_nav
GROUP BY fund_name;

-- 7 Lowest Expense Ratio
SELECT fund_name,
expense_ratio
FROM fact_performance
ORDER BY expense_ratio;

-- 8 Fund Count by Category
SELECT category,
COUNT(*)
FROM dim_fund
GROUP BY category;

-- 9 Average AUM by Category
SELECT category,
AVG(aum)
FROM fact_aum
GROUP BY category;

-- 10 Top Performing Funds
SELECT fund_name,
return_5y
FROM fact_performance
ORDER BY return_5y DESC
LIMIT 10;