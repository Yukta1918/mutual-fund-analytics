import requests
import pandas as pd
import os

schemes = {
    "HDFC_Top100":125497,
    "SBI_Bluechip":119551,
    "ICICI_Bluechip":120503,
    "Nippon_LargeCap":118632,
    "Axis_Bluechip":119092,
    "Kotak_Bluechip":120841
}

save_folder = "data/processed"

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(data["data"])

        df.to_csv(
            os.path.join(save_folder, f"{name}.csv"),
            index=False
        )

        print(f"Saved {name}")