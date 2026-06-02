import pandas as pd
import os

folder_path = "data/raw"

csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv") and (f.startswith("0") or f.startswith("1"))]

for file in csv_files:
    print("\n" + "="*60)
    print("Dataset:", file)

    df = pd.read_csv(os.path.join(folder_path, file))

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    # print("\nMissing Values:")
    # print(df.isnull().sum())

    # print("Duplicates:", df.duplicated().sum())


#Any anomalies
#1. 12 Missing values found 04_monthly_sip_inflows in yoy_growth_pct column.