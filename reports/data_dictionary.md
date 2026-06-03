# Data Dictionary

## nav_history

| Column | Type | Definition |
|----------|----------|------------|
| amfi_code | INTEGER | Unique scheme code |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

Source: 02_nav_history.csv

---

## investor_transactions

| Column | Type | Definition |
|----------|----------|------------|
| transaction_id | INTEGER | Transaction ID |
| amount | REAL | Investment amount |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| kyc_status | TEXT | KYC verification status |

Source: 08_investor_transactions.csv

---

## scheme_performance

| Column | Type | Definition |
|----------|----------|------------|
| return_1y | REAL | One year return |
| return_3y | REAL | Three year return |
| return_5y | REAL | Five year return |
| expense_ratio | REAL | Fund expense ratio |

Source: 07_scheme_performance.csv