from sqlalchemy import create_engine
import pandas as pd
import os

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

processed = "data/processed"

for file in os.listdir(processed):

    if file.endswith(".csv"):

        table_name = file.replace(".csv", "")

        df = pd.read_csv(
            os.path.join(processed, file)
        )

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(
            f"{table_name}: {len(df)} rows loaded"
        )