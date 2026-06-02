import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing = master_codes - nav_codes

print("Total Codes:", len(master_codes))
print("Missing Codes:", len(missing))

if missing:
    print(list(missing)[:20])