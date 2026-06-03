import pandas as pd
import os

RAW = "data/raw"
PROCESSED = "data/processed"

os.makedirs(PROCESSED, exist_ok=True)

# NAV HISTORY
nav = pd.read_csv(f"{RAW}/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"], errors="coerce")

nav = nav.sort_values(["amfi_code", "date"])

nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv(f"{PROCESSED}/02_nav_history_clean.csv", index=False)

# INVESTOR TRANSACTIONS
txn = pd.read_csv(f"{RAW}/08_investor_transactions.csv")

txn["transaction_type"] = txn["transaction_type"].str.strip().str.upper()

txn["transaction_type"] = txn["transaction_type"].replace({
    "SIP": "SIP",
    "LUMPSUM": "Lumpsum",
    "REDEMPTION": "Redemption"
})

txn["amount_inr"] = pd.to_numeric(txn["amount_inr"], errors="coerce")

txn = txn[txn["amount_inr"] > 0]

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"],
    errors="coerce"
)

valid_kyc = ["Verified", "Pending", "Rejected"]

txn["kyc_valid"] = txn["kyc_status"].isin(valid_kyc)

txn.to_csv(
    f"{PROCESSED}/08_investor_transactions_clean.csv",
    index=False
)

# SCHEME PERFORMANCE
perf = pd.read_csv(f"{RAW}/07_scheme_performance.csv")

return_cols = ["return_1yr_pct", "return_3yr_pct", "return_5yr_pct"]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

perf["anomaly_flag"] = (
    (perf["return_1yr_pct"] > 100) |
    (perf["return_1yr_pct"] < -100)
)

perf["expense_ratio_flag"] = (
    (perf["expense_ratio_pct"] < 0.1) |
    (perf["expense_ratio_pct"] > 2.5)
)

perf.to_csv(
    f"{PROCESSED}/07_scheme_performance_clean.csv",
    index=False
)